Shared Sockets in Circus
########################

:date: 2012-06-12 08:00
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziadé

.. image:: https://farm2.staticflickr.com/1011/1354246617_cbb4c6072f.jpg
   :target: https://secure.flickr.com/photos/vero-b/1354246617/sizes/m/in/photostream/


Mongrel2 vs Gunicorn
====================

The last time I blogged I was looking as Mongrel2 as a potential replacement for
Gunicorn.

The Goal is : being able to use Circus to manage independently each web
worker - read my previous `entry <http://blog.ziade.org/2012/05/31/mongrel2-amp-circus-full-control-of-your-web-stack/>`_

It turns out that after some detailed benchmarks using Funkload and a classical
web application that's doing some I/O, the Gunicorn stack was 20% faster than the
Mongrel2 stack. I won't publish this benchmark, the important thing is just
that for *my* app which processes requests really fast,
on the same hardware, Mongrel2 was 20% slower.

That still makes Mongrel2 very appealing, because this overhead is
almost unnoticed for many apps where most of the time is spent querying
databases.

I suspect Gunicorn is faster because workers are receiving the request directly
into the socket, then parse it once and go ahead and build the response.

In Mongrel2 case, the request is parsed then serialized in Json to go through
the ZeroMQ socket, then unserialized by m2wsgi in the worker, then the
response is sent back.


Going lower level ala einhorn
=============================

After more thoughts, and a `tweet from Whit <https://twitter.com/whitmo/status/208250435176374272>`_,
I realized Mongrel2 was adding yet another indirection with its own
potential issues. Sure it solves the issue I have, which is to be able
to treat each web worker as an independent process in Circus, but the
extra communication layer can be an extra worry. For instance, we currently
have a lot of tweaking work going on so the ZMQ parts of our apps work
smoothly.

There's one important property when you work with socket. And that
property is used by Gunicorn, Unicorn, Apache, etc.: when you fork a
process, the child can accept connection in a socket that was
created and bound in the parent process.

In other words, if **circusd** *-- the Circus process that runs all the
processes --* creates a socket and starts listening to it, any child
process will be able to accept new connections from it.

So if Circus itself manage sockets, it can send to its child processes
one way or another the file descriptor number of the sockets it created.

It's easy from there to recreate a socket in the child process and
work with. In Python that's done with the **fromfd** function::

    import socket

    socket.fromfd(my_fd, socket.AF_INET, socket.SOCK_STREAM)


In C or C++ it's even simpler since most socket operations are
done directly with the FD value.

Delegating sockets management to the parent process and have child
process work with already bound sockets is a little bit in the
spirit of `einhorn <https://stripe.com/blog/meet-einhorn>`_

In Circus, managing sockets could be done really simply, by
declaring new sections in the configuration file, that list
the sockets it should bind on startup

An example where Circus would open a socket on port 8080 and another one
on 8081, with a specific type::

    [circus]
    endpoint = tcp://127.0.0.1:5555

    [socket:web]
    host = localhost
    port = 8080

    [socket:another]
    host = localhost
    port = 8081
    type = AF_INET6


Check out `this issue <https://github.com/mozilla-services/circus/issues/142>`_
for more details about adding this socket support in Circus.


Meet Chaussette
===============

Once Circus binds and listens to some sockets, we just need to
spawn workers that get the file descriptor number and
run a web server out of it.

I have started a prototype based on **wsgiref** that does exactly this:
it's a WGSI server that can be run with a file descriptor instead
of a host and port values.

Chaussette lives here : https://github.com/tarekziade/chaussette

Everything else is similar to wsgiref. The only issue I had was
that everything in the standard library is making the assumption that
when you want to create a server, you want to bind the socket.

I have found no server out there that was abstracting this enough
for me to simply reuse it. All WSGI web servers out there can be launched
against a host or a unix socket, not an existing file descriptor.

.. note::

   **Follow-up** After a few mail exchanges on WEB-SIG and with
   the maintainer of Meinheld, I am happy to say that both uWsgi
   and Meinheld now offer an option to run with an fd.

   For example in uWsgi::

        uwsgi --http-socket fd://12 -w module:app

   This should be part of their next release.


Since we have the **unix:** prefix convention for Unix Sockets,
maybe a **fd:** prefix convention could be a nice addition.

Anyways, **chaussette** can be run against a WSGI application the
classical way, using --host and --port, or can be run using
the --fd option. And the latter will only work if chaussette was
launched as a child process and the parent has created the socket.

The final Circus configuration could look like this::

    [circus]
    endpoint = tcp://127.0.0.1:5555

    [socket:web]
    host = localhost
    port = 8080

    [watcher:web_worker]
    use_sockets = true
    cmd = chaussette --fd {SOCKET:web} mywsgi.app


*{SOCKET:web}* would be in that case replaced by the real integer value
of the bound socket.

Ohai! I have my Circus-based stack and I can manage each process
separately !


What's next
===========

Chaussette is based on wsgiref so is not going to perform that well.
I have started another prototype based on `Meinheld <http://pypi.python.org/pypi/meinheld>`_
but I have to change the C code.

I have also done a prototype using `Diesel <https://github.com/jamwt/diesel>`_, that
works, but this project is a full framework, where I want a minimal worker process
that just runs a WSGI app.

Maybe I should talk about the *fd:XXX* standard idea on WEB-SIG. It's easy to
implement in every web server, and would make it possible for people to use
any server they want, and take care of the process management themselves.
