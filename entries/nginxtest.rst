NGinxTest
#########

:date: 2014-06-29 11:40
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

I've been playing with Lua and Nginx lately, using the `OpenResty <http://openresty.org/>`_
bundle.

This bundle is an Nginx distribution on steroids, that includes some extensions and in
particular the `HTTPLuaModule <http://wiki.nginx.org/HttpLuaModule>`_ which let you script
Nginx using the Lua programming language.

Coming from a Python background, I was quite pleased with the Lua syntax, which feels
like a *cleaner Javascript inspired from Pascal and Python* - if that even
makes any sense :)

Here's how a Lua function look like::

    -- rate limiting
    function rate_limit(remote_ip, stats)
        local hits = stats:get(remote_ip)
        if hits == nil then
            stats:set(remote_ip, 1, throttle_time)
            return false
        end

        hits = hits + 1
        stats:set(remote_ip, hits, throttle_time)
        return hits >= max_hits
    end


Peformance-wise, interacting with incoming web requests in Lua co-routines in
Nginx is blazing fast. And there are a lot of work that can be done there to
spare your proxied Python/Node.js/Go/Whatever application some cycles
and complexity.

It can also help you standardize and reuse good practices across all your web
apps no matter what language/framework they use.

Some things that can be done there:

- web application firewalling
- caching
- dynamic routing
- logging, load balancing
- a ton of other pre-work...

To put it simply:

*Nginx become very easy to extend with Lua scripting
without having to re-compile it all the time, and Lua lowers the barrier
for ops and developers to implement new server behaviors.*


Testing with Test::Nginx
------------------------

When you start to add some Lua scripting in your Nginx environment, testing
soon become mandatory. Pure unit testing Lua scripts in that context is
quite hard because you are interacting with Nginx variables and functions.

The other approach is doing only pure functional tests by launching Nginx
with the Lua script loaded, and interacting with the server using an HTTP
client.

OpenResty offers a Perl tool to do this, called `Test::Nginx <https://github.com/openresty/test-nginx>`_
where you can describe in a light DSL an interaction with the NGinx server.

Example from the documentation::

    # foo.t
    use Test::Nginx::Socket;
    repeat_each(1);
    plan tests => 2 * repeat_each() * blocks();
    $ENV{TEST_NGINX_MEMCACHED_PORT} ||= 11211;  # make this env take a default value
    run_tests();

    __DATA__

    === TEST 1: sanity
    --- config
    location /foo {
        set $memc_cmd set;
        set $memc_key foo;
        set $memc_value bar;
        memc_pass 127.0.0.1:$TEST_NGINX_MEMCACHED_PORT;
    }
    --- request
        GET /foo
    --- response_body_like: STORED
    --- error_code: 201


The data section of the Perl script describes the Nginx configuration, the request made
and the expected response body and status code.

For simple tests it's quite handy, but as soon as you want to do more complex
tests it becomes hard to use the DSL. In my case I needed to run a series of requests
in a precise timing to test my rate limiting script.

I missed my usual tools like `WebTest <http://webtest.readthedocs.org/en/latest/>`_, where
you can write plain Python to interact with a web server.


Testing with NginxTest
----------------------

Starting and stopping an Nginx server with a specific configuration loaded is not
hard, so I started a small project in Python in order to be able to write my tests using WebTest.

It's called `NGinxTest <https://github.com/tarekziade/NginxTest>`_ and has no ambitions
to provide all the features the Perl tool provides, but is good enough to write complex
scenarios in WebTest or whatever Python HTTP client you want in a Python unit test class.

The project provides a **NginxServer** class that takes care of driving an Nginx server.

Here's a full example of a test using it::

    import os
    import unittest
    import time

    from webtest import TestApp
    from nginxtest.server import NginxServer

    LIBDIR = os.path.normpath(os.path.join(os.path.dirname(__file__),
                            '..', 'lib'))
    LUA_SCRIPT = os.path.join(LIBDIR, 'rate_limit.lua')

    _HTTP_OPTIONS = """\
    lua_package_path "%s/?.lua;;";
    lua_shared_dict stats 100k;
    """ % LIBDIR


    _SERVER_OPTIONS = """\
    set $max_hits 4;
    set $throttle_time 0.3;
    access_by_lua_file '%s/rate_limit.lua';
    """ % LIBDIR


    class TestMyNginx(unittest.TestCase):

        def setUp(self):
            hello = {'path': '/hello', 'definition': 'echo "hello";'}
            self.nginx = NginxServer(locations=[hello],
                                    http_options=_HTTP_OPTIONS,
                                    server_options=_SERVER_OPTIONS)
            self.nginx.start()
            self.app = TestApp(self.nginx.root_url, lint=True)

        def tearDown(self):
            self.nginx.stop()

        def test_rate(self):
            # the 3rd call should be returning a 429
            self.app.get('/hello', status=200)
            self.app.get('/hello', status=200)
            self.app.get('/hello', status=404)

        def test_rate2(self):
            # the 3rd call should be returning a 200
            # because the blacklist is ttled
            self.app.get('/hello', status=200)
            self.app.get('/hello', status=200)
            time.sleep(.4)
            self.app.get('/hello', status=200)


Like the Perl script, you provide bits of configuration for your Nginx
server -- in this case pointing the Lua script to test and some general
configuration.

Then I test my rate limiting feature using Nose::


    $ bin/nosetests -sv tests/test_rate_limit.py
    test_rate (test_rate_limit.TestMyNginx) ... ok
    test_rate2 (test_rate_limit.TestMyNginx) ... ok

    ----------------------------------------------------------------------
    Ran 2 tests in 1.196s

    OK


Out of the 1.2 seconds, the test sleeps half a second, and the class starts
and stops a full Nginx server twice. Not too bad!


I have not released that project at PyPI - but if you think it's useful to you
and if you want some more features in it, let me know!
