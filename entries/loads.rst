Loads 0.1 released
##################

:date: 2013-08-13 15:19
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade


We're currently focusing on `Loads <https://github.com/mozilla-services/loads>`_
with Alexis and I have just released the first `version at PyPI <https://pypi.python.org/pypi/loads>`_.

It's a distributed load testing tool.

It's still at a very early stage but I think it's worth releasing it to share
it with people that might be interested in doing heavy distributed load testing.

From a user's perspective, the key concepts of Loads are:

1. Write functional tests in any language using the tools you love.
   Currently we support Python using WebTest, Requests and/or ws4py for web sockets,
   and Javascript using Mocha (the JS support is still experimental).
2. Use Loads to load test a server using those functional tests
3. Get the results in real-time

If you want to give it a shot, `install it <http://loads.readthedocs.org/en/latest/installation/>`_ ,
then follow the guide here: http://loads.readthedocs.org/en/latest/guide and let us
know what you think.

Beware that it's an early prototype, probably still full of bugs.


Design
------

From a design point of view, this is how Loads is organized when you run a load test
across several servers:

.. figure:: http://loads.readthedocs.org/en/latest/_images/loads.png

Loads uses a ZeroMQ **Broker** that drives several **Agents** to run tests.
Tests results are sent in real time into a publisher.

In detail:

1. The Loads program sends a message to the broker, asking it to run the
   tests on N agents.

2. The broker selects available agents and send them the tests to run.

3. Each agent run the tests

4. When a test is done, whether it has failed or succeeded, the agent sends
   back to the broker information about what happened.


Next steps
----------

Right now, we've deployed Loads on AWS on several boxes, and started
to use it to load test a few of our applications we're currently
building at Mozilla Services.

The long term goal is to offer a load testing service to our team,
so anyone can send huge loads on a staging or dev application with
a simple command line call.

I hope that we will have something that works well by the
end of the summer and be useful to more people than our own team.

If you're interested, please join the fun at https://github.com/mozilla-services/loads

