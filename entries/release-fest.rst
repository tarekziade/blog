Mozilla Services Release Fest
#############################

:date: 2012-12-18 18:00
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

.. image:: https://farm4.staticflickr.com/3243/3139510688_04e21acfc9_n.jpg
   :align: right
   :target: https://secure.flickr.com/photos/86886338@N00/3139510688/


Christmas is almost there, so we decided to make a few releases for some of
our tools.


Circus 0.6
::::::::::

Circus is a process/sockets manager on steroids.

It's been a long while since we wanted to release Circus 0.6 -- this is
a big release that bring in a **lot** of fixes and some exciting new features:

- `Hooks <http://circus.readthedocs.org/en/0.6/hooks/>`_ -- Now you can call some
  code during the watchers start/stop process. One use case is to verify that a
  process you start is *really* up. For example a Redis server.

- More **plugins** were contributed: *RedisObserver*, *HTTPObserver*,
  *ResourceWatcher* and more -- see http://circus.readthedocs.org/en/0.6/plugins

- Now with Chaussette 0.6, fully supports unix sockets.

- *circusctl* now has autocompletion and inline help for commands.

- It's getting easier to configure Circus, in particular
  `environment variable <https://circus.readthedocs.org/en/0.6/configuration/#env-watchers-as-many-sections-as-you-want>`_

- We improved documentation about `installing <http://circus.readthedocs.org/en/0.6/installation/>`_
  Circus and deploying its `web dashboard <http://circus.readthedocs.org/en/0.6/circushttpd/>`_.

Links:

* Get it at http://pypi.python.org/pypi/circus/0.6.0
* Get the docs at http://circus.io


Vaurien 1.5
::::::::::::

Vaurien is a TCP proxy you can use between a web app and a backend (like a database),
to slow down or break the connection.

We're currently using Vaurien to see how the Marketplace app reacts when something goes
wrong in the backends.

Vaurien is now organized in **protocol** and **behaviors**. A *protocol* is a plugin
used to process a request sent to a specific backend- like *mysql*, *redis* etc..
A *behavior* is a class that degrades how the proxy works, like adding a *delay*.

This new version fixes some bugs and adds `more protocols <http://vaurien.readthedocs.org/en/1.5/protocols.html>`_.

Links:

* Get it at http://pypi.python.org/pypi/vaurien/1.5
* Get the docs at https://vaurien.readthedocs.org/en/1.5/


Chaussette 0.6
::::::::::::::

Chaussette is a WSGI server with many backends like Gevent or Waitress.
It can be used in conjunction with Circus Sockets.

This release has 2 new features:

* a gevent-websocket backend
* now supports unix sockets

Links:

* Get it at http://pypi.python.org/pypi/chaussette/0.6
* Get the docs at http://chaussette.readthedocs.org/en/0.6


Boom! 0.3
:::::::::

Boom! is your Apache Bench replacement. It's based on Gevent so you can spawn a fair
amount of load.


Links:

* Get it & read about it at http://pypi.python.org/pypi/boom/0.2

