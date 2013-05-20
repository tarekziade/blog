A step-by-step introduction to Circus
#####################################


:date: 2013-05-20 18:30
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

.. note::

   Circus is a process & socket manager. See https://circus.readthedocs.org


.. figure:: https://farm9.staticflickr.com/8420/8751753401_0760d37279.jpg
   :target: https://secure.flickr.com/photos/kennethreitz/8751753401/in/pool-2174519@N25/

   Photo by kennethreitz

During Django Con, I was asked how to use Circus to run & monitor a Python
web application. The documentation has no single page step-by-step tutorial
yet, so here goes... this blog post will be integrated into the documentation
for the next release.


Installation
------------

Circus is tested under Mac OS X and Linux, on the latest Python 2.6 and 2.7.
To run a full Circus, you will also need **libzmq**, **libevent** &
**virtualenv**.

Under Debuntu::

    $ sudo apt-get install libzmq-dev libevent python-virtualenv

Create a virtualenv and install *circus*, *circus-web* and *chaussette*
in it ::

    $ virtualenv /tmp/circus
    $ cd /tmp/circus
    $ bin/pip install circus
    $ bin/pip install circus-web
    $ bin/pip install chaussette

Once this is done, you'll find a plethora of commands in the local bin dir.

Usage
-----

*Chaussette* comes with a default Hello world app, try to run it::

    $ bin/chaussette

You should be able to visit http://localhost:8080 and see *hello world*.

Stop Chaussette and add a circus.ini file in the directory containing::

    [circus]
    stats_endpoint = tcp://127.0.0.1:5557
    httpd = 1

    [watcher:webapp]
    cmd = bin/chaussette --fd $(circus.sockets.web)
    numprocesses = 3
    use_sockets = True

    [socket:web]
    host = 127.0.0.1
    port = 9999


This config file tells Circus to bind a socket on port *9999* and run
3 chaussettes workers against it. It also activates the Circus web
dashboard and the statistics module.

Save it & run it using **circusd**::

    $ bin/circusd --daemon circus.ini

Now visit http://127.0.0.1:9999, you should see the hello world app.

You can also visit http://localhost:8080/ and enjoy the Circus web dashboard.


Interaction
-----------

Let's use the circusctl shell while the system is running::

    $ bin/circusctl
    circusctl 0.7.1
    circusd-stats: active
    circushttpd: active
    webapp: active
    (circusctl)

You get into an interactive shell. Type **help** to get all commands::

    (circusctl) help

    Documented commands (type help <topic>):
    ========================================
    add     get            list         numprocesses  quit     rm      start   stop
    decr    globaloptions  listen       numwatchers   reload   set     stats
    dstats  incr           listsockets  options       restart  signal  status

    Undocumented commands:
    ======================
    EOF  help


Let's try basic things. Let's list the web workers processes and add a
new one::

    (circusctl) list webapp
    13712,13713,13714
    (circusctl) incr webapp
    4
    (circusctl) list webapp
    13712,13713,13714,13973


Congrats, you've interacted with your Circus! Get off the shell
with Ctrl+D and now run circus-top::

    $ bin/circus-top

This is a top-like command to watch all your processes' memory and CPU
usage in real time.

Hit Ctrl+C and now let's quit Circus completely via circus-ctl::

    $ bin/circusctl quit
    ok


Next steps
----------

You can plug your own WSGI application instead of Chaussette's hello
world simply by pointing the application callable.

Chaussette also comes with many backends like Gevent or Meinheld.

Read https://chaussette.readthedocs.org/ for all options.

