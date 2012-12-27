How to improve your web app backends connections
################################################

:date: 2012-12-27 23:50
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

I've talked about this previously, but let me state it
again before I introduce the tools.

One of the most common issue I witness in web applications out there
is their inability to cope with backend issues.

For example, if you are using a MySQL database, a simple test to do
to see how your web app behaves is to shutdown your MySQL cluster or
server and play with the app.

Of course it'll be all broken. But how broken ? can I still browse
pages that are not doing SQL Queries ?

What happens when you restart MySQL ? Is your web application
back on its feet or do you have broken connectors ?

How a simple MySQL restart impacts your app ?

You get the idea: we should test these scenarios, before
they happen in production -- because they *will* happen.

This topic is basically what I've been working on at Mozilla
for the last month, and we built a tool to help us
testing this: `Vaurien <https://vaurien.readthedocs.org>`_


Setting up the proxy
====================

Shutting down MySQL is a good test to do, but you should
also ask yourself how your application behaves when MySQL
works but is *very* slow.

Vaurien is a TCP proxy that can simulate these kind of behaviors.

To set it up, just run::

    $ pip install vaurien

Since Vaurien uses Gevent, you will need libevent. Under
Windows I preconise to use Gevent's binary distributions.

Now let's run a proxy in front of your MySQL server. Vaurien
supports several protocols including MySQL.

To launch the proxy, open a shell and run::


    $ vaurien --protocol mysql --proxy 0.0.0.0:3307 --backend 192.168.1.123:3306 --http


This line will open the 3307 socket on your local host and relay all calls
to *192.168.1.123*, supposing your MySQL server runs there.


The **--http** flag opens a web service to drive the proxy from the command line
or from some APIs calls.

From there, change your application settings so it uses 0.0.0.0:3307 as the
MySQL server, and double check that the proxy works as expected.

.. note::

   By default Vaurien runs its web service on port 8080. In case
   you already use that port, change it with --http-port.



Breaking things
===============

The first test you can do is to fake a *shut down*. Open another shell and
just call the *vaurienctl* command line::

    $ vaurienctl set-behavior blackout

By default, *vaurienctl* knows the proxy can be reached on the local host
on port **8080**. If you ran it on another port, be sure to adapt the call
with the --http-port option.

Once the call has been made, play with your application and see how it behaves :)

Make sure you put the proxy back to being a transparent proxy with::

    $ vaurienctl set-behavior dummy

And see if you application is back to normal.

Another thing you can try is to make MySQL just hangs on any call.
It's different from a black out because it just keeps the socket
open and hang there. Usually, if your application does not handle
timeouts correctly, it will hang too - and that's something to fix.

::

    $ vaurienctl set-behavior hang


More breaking
=============

With Vaurien, you can also simulare errors and delays.

The full list of behaviors is here: https://vaurien.readthedocs.org/en/latest/behaviors.html

It also support a good range of protocols: https://vaurien.readthedocs.org/en/latest/protocols.html
and the *TCP* one should work out of the box with any protocol we did not specifically implement.

Instead of using the **vaurienctl** command line (or even Curl), you can also use the API we
provide.

For example you could write functional tests that launch the proxy and drive it::


    import unittest
    from vaurien import Client, start_proxy, stop_proxy


    class MyTest(unittest.TestCase):

        def setUp(self):
            self.proxy_pid = start_proxy(port=8080)

        def tearDown(self):
            stop_proxy(self.proxy_pid)

        def test_one(self):
            client = Client()
            options = {'inject': True}

            with client.with_behavior('error', **options):
                # do something...
                pass

            # we're back to normal here


The real fun is to start writing your own protocols and behaviors,
since Vaurien is based on a plugins system.

Feedback
========

The code repository & bug tracker are located at https://github.com/mozilla-services/vaurien
Don’t hesitate to send us pull requests or open issues.


