Circus 0.5 released
###################

:date: 2012-07-06 23:50
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

.. image:: http://cdn.memegenerator.net/instances/400x/23069364.jpg
   :align: right


2 weeks and 180 commits after Circus 0.4, we've just released Circus 0.5

This release puts Circus in a whole new dimension because, amongst many
small features and fixes, we have added **socket support**.

What are Circus Sockets ?
-------------------------

Circus can bind network sockets and manage them as it does for processes.

The main idea is that a child process that's created by Circus to run
a command, can inherit from all the opened file descriptors.

That's how Apache or Unicorn works, and many other tools out there.

Why would you do this ? To manage all the processes that compose
your full web stack in a single tool for example.


Circus web stack v.s. a classical web stack
-------------------------------------------

Let's take an example with a Python `WSGI web stack <http://wsgi.readthedocs.org/en/latest/what.html>`_
-- but that would work with a Ruby or Java stack.

In a classical WSGI stack, you have a server like Gunicorn that serves on a port
or an unix socket and is usually deployed behind a web server like Nginx:

.. image:: http://circus.readthedocs.org/en/0.5/_images/classical-stack.png


Clients call Nginx, which reverse proxies all the calls to Gunicorn.

If you want to make sure the Gunicorn process stays up and running, you have to use
a program like Supervisord or upstart.

Gunicorn in turn watches for its processes ("workers").

In other words you are using two levels of process management. One that you manage
and control (supervisord), and a second one that you have to manage in a different UI,
with a different philosophy and less control over what's going on (the wsgi server's one)

This is true for Gunicorn and most multi-processes WSGI servers out there
I know about. uWsgi is a bit different as it offers plethoras of options.

But if you want to add a Redis server in your stack, you *will* end up with
managing your stack processes in two different places.


Circus' approach on this is to manage processes *and* sockets.

A Circus stack can look like this:

.. image:: http://circus.readthedocs.org/en/0.5/_images/circus-stack.png


So, like Gunicorn,
Circus is able to bind a socket that will be proxied by Nginx. Circus don't
deal with the requests but simply binds the socket. It's then up to a web worker
process to accept connections on the socket and do the work.

It provides equivalent features than Supervisord but will also let you
manage all processes at the same level, whether they are web workers or Redis or
whatever. Adding a new web worker is done exactly like adding a new Redis
process.

And it has a cool real-time web UI were you are even getting the
number of hits your sockets are getting:


.. image:: http://blog.ziade.org/circus-graph.png



Real-world example
------------------

But enough theory, let's see how you can run a stack. For this
you need Circus *and* a process that accept connections on a
socket Circus binds.

`Chaussette <http://chaussette.rtfd.org>`_ is exactly that
kind of program.

Once it's installed, running 5 web workers can be done by creating a
socket and calling the **chaussette** command in a worker, like this:

.. code-block:: ini

    [circus]
    httpd = 1

    [watcher:web]
    cmd = chaussette --fd $(circus.sockets.web) mycool.app
    use_sockets = True
    numprocesses = 5

    [socket:web]
    host = 0.0.0.0
    port = 8000


*$(circus.sockets.web)* will be replaced by the FD value once the socket is
created and bound on the 8000 *port*.

Run this file with **circusd** and manage your stack at *http://localhost:8080*

**You can also run Django apps in Circus using Chaussette**

More info on all of this at http://circus.readthedocs.org/en/0.5/usecases/


What's next
-----------

For 0.6, we're focusing on adding security and clustering.

If you want to participate see `Contributing <http://circus.readthedocs.org/en/0.5/contributing/#contribs>`_

Useful Links:

- There's a mailing list for any feedback or question: http://tech.groups.yahoo.com/group/circus-dev/
- The repository and issue tracker is at GitHub : https://github.com/mozilla-services/circus
- Join us on the IRC : Freenode, channel #mozilla-circus

