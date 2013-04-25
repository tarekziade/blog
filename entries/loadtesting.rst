Thoughts on Load Testing
########################

:date: 2013-04-25 23:50
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

We are `Funkload <http://funkload.nuxeo.org/>`_ fans at Mozilla Services. Writing a
load test against one of our web service is dead easy using that tool.

It boils down to writing a functional test in Python, that calls the service,
then ask Funkload to run it in parallel, accross many threads and boxes.

We've written a web app on the top of Funkload called Marteau -
`initial blog post about it <http://blog.ziade.org/2012/08/22/marteau-distributed-load-tests/>`_
that now allows us to provision slaves on demand on Amazon WS and run
distributed load tests.

You can watch this hangout to better understand what Marteau & Funkload are https://plus.google.com/106436370949746015255/posts/Lq7t4jkiwNR

Marteau is already useful to us but I am now facing some difficulties to
improve the tool and add some features we want, like:

- realtime JS charts of the ongoing load test
- web socket load testing
- the ability to run load tests written in other languages or frameworks, like node.js

Funkload is a project that was started 10 years ago, and is very robust. But it
has evolved from a tool that runs on a single box to a distributed load testing
tool by using SSH. In other words, a distributed load test in Funkload is just
several load tests running in parallel, then a merge of all the results files
that are copied back to a single box through SSH.

It means that there is no specific client/server protocol and no way
to interact live with the slaves that are running in the distributed mode.
You can kill them of course, or just wait for them to return.

I started to add some `communication channel <https://github.com/nuxeo/FunkLoad/blob/master/src/funkload/rtfeedback.py>`_
in the tool but the core itself was not built with this in mind.

I have found the `locust.io <http://locust.io>`_ project, which has this
approach and which looks very promising, but does not exactly provide
what I am looking for.

For example, I don't really want developers to have to write load tests
using yet another set of APIs. The concept of writing Python unit tests is
fabulous and I don't want to lose it.


Starting Loads
==============

I am experimenting on something new, based on what we've learned from our experience
with Funkload and what we need in Marteau.

It's called **Loads** and it's a client/server architecture based on ZMQ
that will use a very simple protocol based on Message Pack or maybe BJson
- we will see.

It's quite similar to locust.io in the principles, but instead of introducing
new APIS, it's going to rely on a set of API people know & like :
`Requests <http://docs.python-requests.org>`_.

So, how will a load test with **Loads** look like ?

.. code-block:: python

    import unittest
    from loads import Session


    class TestWebSite(unittest.TestCase):

        def setUp(self):
            self.session = Session()

        def test_something(self):
            res = self.session.get('http://blog.ziade.org')
            self.assertTrue('Tarek' in res.content)


That's it. A unittest class that uses a *Session* class. The Session object
is `the same one you find in Requests <http://docs.python-requests.org/en/latest/user/advanced/#session-objects>`_.

I am not sure yet how I will extend the API so it can work with web sockets.
That'll come later.

This test can then be executed using the **loads** command. Example for 10 concurrent users
and 10 runs each:

.. code-block:: python

  $ bin/loads test_blog.TestWebSite.test_something -c 10 -n 10
  [====================================================================================================]  100%


Like locust.io, Loads uses `greenlets <http://sdiehl.github.com/gevent-tutorial/#greenlets>`_
here, so you can already push quite some load from a single box.

Everytime a request is done, the status code returned by the server and the time it took
are pushed in a stream. The stream can be the standard output or a ZMQ stream.

And I will be using the ZMQ stream to actually drive distributed tests.

Each **agent** will connect to a master through ZMQ. The master will be able to drive
them through a dedicated ROUTE socket and will ask agents to run some load tests.

Results will be sent back via ZMQ in real-time using a dedicated channel.

The master will then publish all results in a merged stream - a ZMQ pub socket.

From there, the Marteau web app will be able to register to that stream of result to
display some real time charts and allow any kind of interaction.
Or any app that whishes to do something with the results.

And since there are some ZMQ bindings in most languages, it's possible to
implement a node.js client for example, so the system can have agents able
to run Javascript-based tests and report back results to the master like
the built-in Python agent.


That's the plan. I have started the prototype here: https://github.com/tarekziade/loads
and I am very excited about this project.

