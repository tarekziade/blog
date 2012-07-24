Mozilla Services Python Tools And Libraries
###########################################

:date: 2012-07-24 09:32
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

.. image:: https://farm8.staticflickr.com/7278/7126147125_fdc4643ed9.jpg
   :align: right
   :target: https://secure.flickr.com/photos/75905404@N00/7126147125/


One of the biggest advantage of contributing to Mozilla is that
*everything* we're writing is open-sourced, so I wanted to take
a bit of time to present some of the tools and libs we're working on.

Maybe some of them could be useful to other projects.

Kazoo
=====

`kazoo` simplifies communication with Apache Zookeeper from Python making it
easier to write code that's less error-prone than using the basic Python
Zookeeper library. It implements patterns from Netflix Curator, in a more
Pythonic manner, and is compatible with async environments like gevent.

- Documentation: http://kazoo.readthedocs.org
- Source: https://github.com/python-zk/kazoo


Metlog
======

Metlog is a service for applications to capture and inject arbitrary data into
a back end storage suitable for out-of-band analytics and processing.

It's a client-server system that has almost no impact on your application
performances. You can use it to send stats to `Logstash <http://logstash.net>`_
for instance, using various transports like UDP and ZeroMQ.

- Documentation of the Python client: http://metlog-py.readthedocs.org
- Source: https://github.com/mozilla-services/metlog-py


Cornice
=======

Cornice provides helpers to build & document REST-ish Web Services with
`Pyramid <http://docs.pylonsproject.org/projects/pyramid>`_,
with decent default behaviors. It has validation features, and can be
integrated with tools like Colander for complex validations.

Cornice can automatically generate Sphinx-based documentation for your
APIs.

- Documentation: http://cornice.readthedocs.org
- Source: https://github.com/mozilla-services/cornice


Circus
======

Circus is a process & socket manager. It can be used to monitor and control
processes and sockets.

With Circus you can control a whole stack from the command-line or a web
interface, and have real-time statistics.

- Documentation: http://docs.circus.io
- Source: https://github.com/mozilla-services/circus


Queuey
======

Wat? Another message queue?

Given the proliferation of message queue's, one could be inclined to believe
that inventing more is not the answer. Using an existing solution was attempted
multiple times with most every existing message queue product.

The others failed (for our use-cases).

Queuey is meant to handle some unqiue conditions that most other message queue
solutions either don't handle, or handle very poorly. Many of them for example
are written for queues or pub/sub situations that don't require possibly longer
term (multiple days) storage of not just many messages but huge quantities of
queues.

- Documentation: http://queuey.readthedocs.org
- Source: https://github.com/mozilla-services/queuey


Powerhose
=========

Powerhose turns your CPU-bound tasks into I/O-bound tasks so your Python
applications are easier to scale.

Powerhose is an implementation of the Request-Reply Broker pattern in ZMQ,
with some extra features around.

- Documentation: http://powerhose.readthedocs.org
- Source: https://github.com/mozilla-services/powerhose



