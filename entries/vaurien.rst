Put some chaos in your tests
#############################

:date: 2012-10-20 10:50
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

.. image:: http://www.codinghorror.com/.a/6a0120a85dcdae970b014e880f778e970d-800wi
   :align: right
   :target: http://www.youtube.com/watch?v=WgjcvxQjpKA


Ever heard of the `Chaos Monkey <http://www.codinghorror.com/blog/2011/04/working-with-the-chaos-monkey.html>`_?

It's a project at Netflix to enhance the infrastructure tolerance. The Chaos Monkey
will randomly shut down some servers or block some network connections, and the system
is supposed to survive to these events. It's a way to verify the high availability
and tolerance of the system.

Besides a redundant infrastructure, if you think about reliability at the level
of your web applications there are many questions that often remain unanswered
until you get the issue in production:

- What happens if the MYSQL server is restarted? Are your connectors able
  to survive this event and continue to work properly afterwards?

- Is your web application still working in degraded mode when Membase is
  down?

- Are you sending back the right 503s when postgresql times out ?

Of course you can -- and should -- try out all these scenarios on stage while
sending to your application a realistic load.

But testing these scenarios while you are building your code is also a good
practice, and having automated functional tests for this is preferable.

That's where **Vaurien** is useful.

Vaurien is basically a Chaos Monkey for your TCP connections, we've started
at Mozilla. It's fresh but it's already something people can hack with.

Vaurien is a TCP proxy between your application and any backend.

You can use it in your functional tests or even on a real deployment
through the command-line.


Vaurien in your tests
---------------------

If you want to run and drive a Vaurien proxy from your code, the project
provides a simple class for this.

Here's an example:

.. code-block:: python

    import unittest
    from vaurien import Client, start_proxy, stop_proxy


    class MyTest(unittest.TestCase):

        def setUp(self):
            self.proxy_pid = start_proxy(port=8080)

        def tearDown(self):
            stop_proxy(self.proxy_pid)

        def test_one(self):
            client = Client()

            with client.with_handler('errors'):
                # do something...
                pass

            # we're back to normal here


In this test, the proxy is started and stopped before and after the
test, and the *Client* class will let you drive its behavior.

The class interacts with the proxy through a special HTTP api, to
tell it how to behave on TCP calls.

Within the **with** block, the proxy will error out any call by using
the *errors* handler, so you can verify that your application is
behaving as expected when it happens.

A **handler** is a piece of code that is called by the proxy and does
whatever it wants with the incoming request. In our case it errors
out :)

Vaurien provides a collections of handlers:

- **normal**: A transparent proxy, which doesn't modify at all the requests and
  responses
- **delay**: Adds a delay *before* the backend is called
- **errors**: Reads the packets that have been sent, then throws errors on
  the socket.
- **hang**: Reads the packets that have been sent, then hangs.
- **blackout**: Don't do anything -- the sockets get closed


Extending Vaurien
------------------

Vaurien comes with a few handlers, but you can create your own
handlers and plug them in a configuration file.

In fact that's the best way to create realistic issues: imagine that you
have a very specific type of error on your LDAP server everytime your
infrastructure is under heavy load. You can reproduce this issue in your
handler and make sure your web application behaves as it should.

Creating new handlers is done by implementing a callable with the
following signature::

    def super_callable(source, dest, to_backend, name, settings, server):
        pass


Where:

- **source** and **dest** are the source and destination sockets.
- **to_backend** is a boolean that tels you if this is the communication to
  the proxied server or from it.
- **name** is the name of the callable.
- **settings** the settings for *this* callable
- **server** the server instance - it can be useful to look at the global
  settings for instance, and other utilities.

*to_backend* will let you impact the behavior of the proxy when data is coming
in **or** out of the proxy.

Here is how the `delay` handler is specified, for instance:

.. code-block:: python

    def delay(source, dest, to_backend, name, settings, proxy):
        if to_backend:
            # a bit of delay before calling the backend
            gevent.sleep(settings.get('sleep', 1))

        dest.sendall(proxy.get_data(source))


You can then simply use it in your calls as you would use another handler,
by pointing the callable name.


Running Vaurien as a standalone proxy
-------------------------------------

Vaurien also comes as a command-line tool.

Let's say you want to add a delay for 20% of the requests done on google.com.

You can use the **vaurien** script and just run::

    $ vaurien --local localhost:8000 --distant google.com:80 --behavior 20:delay

Vaurien will stream all the traffic to google.com but will add delays 20% of the
time.

You can also create a *ini* file for this and pass it to the script:

.. code-block:: ini

    [vaurien]
    distant = google.com:80
    local = localhost:8000
    behavior = 20:delay

    [handler:delay]
    sleep = 2

And of course you can tweak the behavior of the proxy. Here, we're defining
that the delay will last for 2 seconds.


What' next
-----------

I am starting to use Vaurien in some of my functional tests, and I'd love to see
if this can be a useful tool to others -- and eventually release a first version
at PyPI.

Useful Links:

- The doc is at http://vaurien.readthedocs.org
- The repository and issue tracker is at GitHub : https://github.com/mozilla-services/vaurien

