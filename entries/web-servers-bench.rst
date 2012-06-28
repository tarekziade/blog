WGSI Web Servers Bench
######################

:date: 2012-06-28 14:50
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade
:status: draft

.. image:: http://funkload.nuxeo.org/_static/funkload-logo-small.png


Circus is now able to `bind and manage sockets <http://circus.readthedocs.org/en/latest/sockets/#sockets>`_,
and in cunjunction with `Chaussette <http://chaussette.readthedocs.org>`_ you can run a full web stack.

In other words, Circus can spawn as many Chaussette processes as you want, each one will act as
a *web worker*: they'll all accept requests on the same socket.

Why would you want to do this ? Because it's much more ergonomic to manage your web workers in
the same tool than the other processes you might have in your Web stack. (Redis, memcached. etc).

From the `Web UI <http://circus.readthedocs.org/en/latest/circushttpd/#circushttpd>`_ or from the
command line, you can drive your stack at your finger tips. Adding or removing workers live,
seeing the load of each involved process, getting a real time graph of socket hits. etc.

But of course all of this would be meaningless if Circus was making things slower than our
current Web Stack -- Gunicorn behind Nginx.

So I did a few benches and this blog post is the results of my benches.

**tl;dr: Circus + Chaussette + [gevent.pywsgi | meinheld] is fast and stable, we
will gain a very slight speed bump by moving away from Gunicorn, and gain a lot of features.
Good to go !**

.. note::

    Publishing a bench often leads to a flamewar because it's super
    hard to do it in a fair and proper way. I tried my best in the amount of
    time I wanted to spend on this. So if you see anything that seems wrong, let me know !

    I'd be happy to rework things.


The benched app
---------------

I did not want to bench an *Hello World* because this is meanlingless. If your server
is great at Hello Worlds, maybe it will collapse on a real application because it can keep
up with requests filling the backlog.

I did not want either to have variations because of a third party application I'd call
from the benched app, like a database.

So what I did is create an application that does three things:

- do some maths to eat the CPU a little bit
- sleep for 100 ms
- write some data in a file

The whole response is back in about 200 ms, and I guess that makes the benched app
*realistic* enough. It does a bit of I/O and a (smaller) bit of CPU.

The code::

    import os, time, tempfile

    def bench_app(environ, start_response):
        start = time.time()
        status = '200 OK'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)

        for i in range(10000):
            10 * 1000 * 1000
        time.sleep(.1)
        fd, path = tempfile.mkstemp()
        for i in range(10000):
            os.write(fd, str(i))
        os.close(fd)
        os.remove(path)
        return ['%.4f' % (time.time() - start)]

The code is located at https://github.com/tarekziade/chaussette/blob/master/chaussette/util.py

And if you install Chaussette, you can use that app in your favorite WSGI server by plugging
**chaussette.util.bench_app**.

This app is executed with Chaussette 0.1 and the trunk of Circus, using this config::

    [circus]
    check_delay = 5
    endpoint = tcp://127.0.0.1:4555
    pubsub_endpoint = tcp://127.0.0.1:4556
    stats_endpoint = tcp://127.0.0.1:4557

    [watcher:dummy]
    cmd = bin/chaussette --fd $(circus.sockets.foo) --backend fastgevent chaussette.util.bench_app

    use_sockets = True
    warmup_delay = 0
    numprocesses = 50

    [socket:foo]
    host = 0.0.0.0
    port = 8080


Here, Circus bind the port **8080** port and runs **50** workers using the **fastgevent**
backend.

The backends I am trying during these benches:

* gevent - based on Gevent's pywsgi server
* fastgevent - based on Gevent's wsgi server - supposedly faster but does not
  support streaming.
* meinheld - based on Meinheld's C-based server

On Gunicorn side, I am using only the **gevent** backend, since this is the one we currently
use for all our apps and run the app like this::

    $ gunicorn -w 50 -k gevent -t 120 chaussette.util:bench_app


Notice that I had to bump the workers timeout a bit otherwise I was starting to
get errrors on high loads.

Also: Circus and Gunicorn both have a socket backlog of 2048.


The Test
--------

I used `Funkload <http://funkload.nuxeo.org>`_ because it's the best tool I know to do
these things. It spits cool graphs, so I don't have to worry about plotting my data
after the test.

The test is dead simple::

    from funkload.FunkLoadTestCase import FunkLoadTestCase


    class Bench(FunkLoadTestCase):
        def setUp(self):
            self.root = self.conf_get('main', 'url')

        def test_simple(self):
            res = self.get(self.root)
            self.assertEquals(res.code, 200)


Yeah, that's all. I am hammering the server root URL and make sure I get a 200 back.

The full code is at https://github.com/tarekziade/wsgi-bench/blob/master/loadtest.py

The test was done with 50, 100, 150, 200, 250, 300 and 400 virtual users and each time
during 120 seconds. In Funkload, virtual users are concurrent threads the tool launches
to do the benching.

The hardware
------------

Hahaha. That's the sweet part. Don't ask me how/who/where but I did my bench on two
24-cores boxes with a indecent amount of RAM.

.. image:: http://blog.ziade.org/yunocores.jpg

I am not event going to talk about tweaking the system, or mention the RAM - Just that
I made sure the web server had enough FDs to be happy, and that I used a single
Funkload node to send the load.

So, each test is about running 50 workers in Circus, or in Gunicorn, with a various
amount of concurrent requests and see how things go.

The results
-----------

For each run, I am getting two graphs:

- The number of Requests Per Second (RPS) successful or not over Concurrent Users (CUs).
- The Duration of each request (Duration) over Concurrent Users (CUs).

The first graph gives the raw RPS evolving over the load, and the second one has
more interesting information:

- avg: Average response time for a page or request.
- med: Median or 50th percentile, response time where half of pages or requests are delivered.
- p90/p95
  - 90th percentile, response time where 90 percent of pages or requests are delivered.
  - 95th percentile, response time where 95 percent of pages or requests are delivered
- min/p10
  - Minimum response time for a page or request.
  - 10th percentile, response time where 10 percent of pages or requests are delivered.


Gunicorn + gevent
:::::::::::::::::

.. image:: http://blog.ziade.org/gunicorn_rps.png

The RPS seems cahotic, but not really, that's just a graph scaling effect. For every step,
the system did a RPS between **14** and **14.25**, which is very stable.

.. image:: http://blog.ziade.org/gunicorn_requests.png

The Duration is growing steadily, but we can see that the delta is also growing bigger.

At 400 CUs, the fastest response remains almost unchanged, but the slowest one is like
almost a minute.

Two things:

- the benched application does not use any socket, so Gevent is not really going any
  async work. But that's very realistic for our apps. We always use this backend
  even if the call does not do any network I/O
- upping the backlog did not really impact things - but having a smaller backlog led
  to errors.


Chaussette + gevent
:::::::::::::::::::


.. image:: http://blog.ziade.org/gevent_rps.png


Same than Gunicorn, but *slightly* faster. And well, things seem to go up, not down
like in Gunicorn case.


.. image:: http://blog.ziade.org/gevent_requests.png

Same as Gunicorn, very very slighlty faster at 400 CUs but almost no differences.

Chaussette + fastgevent
:::::::::::::::::::::::

*gevent.wsgi* is supposedly faster. From Gevent `doc <http://www.gevent.org/servers.html>`_::

    wsgi.WSGIServer is very fast as it uses libevent's http server implementation
    but it shares the issues that libevent-http has.

    In particular:

    - does not support streaming: the responses are fully buffered in memory before sending; likewise, the incoming requests are loaded in memory in full;
    - pipelining does not work: the server uses "Connection: close" by default;
    - does not support SSL.


So I am not sure why yet but things started to crash after 150+ users. See below

.. image:: http://blog.ziade.org/fastgevent_rps.png

Of course that impacted the other graph by lowering the average response time.

.. image:: http://blog.ziade.org/fastgevent_requests.png

A connection refused error is very fast to come back ! :)

Chaussette + meinheld
:::::::::::::::::::::

Wooo meinheld is awesome !

The RPS is is *slightly* better :

.. image:: http://blog.ziade.org/meinheld_rps.png

But more interesting, see how tight the delta is for the fastest to the slowest requests
on each run, and see how "fast" is the slowest request -- we are far from the 60 seconds
we had earlier:

.. image:: http://blog.ziade.org/meinheld_requests.png

Everything is packed under 30 seconds, *always*.


Conclusion
----------

So far Circus + Chaussette + Meinheld is the winner. I am amazed by the difference on
the slowest responses on high loads.

That makes me confident that we can switch to this stack in the future. We'd still want
the *gevent* back end for I/O bound apps, but Meinheld also do some socket monkey patching
so that is a potential replacer, or at least can be used in apps that don't need gevent's
monkey pacthing.

I also need to investigate on why fastgevent failed that way. There's a high probability
I screwed things up when I embed it in Chaussette.

Btw, did I mention Chaussette can now be `used with Django <http://chaussette.readthedocs.org/en/latest/index.html#running-a-django-application>`_ ?
