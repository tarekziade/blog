Mongrel2 & Circus = Full control of your web stack
##################################################

:date: 2012-05-31 17:00
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziadé

.. image:: https://upload.wikimedia.org/wikipedia/en/0/0b/Mongrel_2_logo.png

.. role:: strike
    :class: strike

Gunicorn frustrations
=====================

I like Gunicorn but as `Circus <http://circus.readthedocs.org/en/latest/index.html>`_  grows
I am getting frustrated of the lack of control I have over the web worker it manages.

Basically, Gunicorn does the same work than Circus on the processes it manages: it
spawns them and manage their lives.

But Circus gives us much more control over the processes
it runs. We can:

- get a continuous feedback on the CPU / Memory usage, per process
- :strike:`add or remove more processes`
- basically do any maintenance operation on a live stack

Also, features like the flapping control, or the `Web Console <http://circus.readthedocs.org/en/latest/circushttpd/>`_
coming in the 0.4 version, makes Circus much more appealing to use.

What I want to have is a simple Python process that gets HTTP requests
and send back responses. From there I can drive my little workers in Circus
as I would do for any other processes.

I can't do this with Gunicorn because it uses a prefork model and deal itself with
its processes.

:strike:`If I run a Gunicorn server with a single worker for instance, I can't add
more workers once it's live.`

:strike:`The socket Gunicorn binds belong to its main process and you can't run another process on it.`

**edited** - *as Philip said in the comments, Gunicorn let you add/remove workers
with the TTIN and TTOU signals, but Circus have much more control, see* :
http://circus.readthedocs.org/en/latest/commands/#circus-ctl-commands

ZeroMQ sockets are a bit different here, as you can connect as many processes as
you want on a single socket, and have load-balancing for free.

I guess one solution would be to rewrite a WSGI server that interprets the HTTP
request then pushes it to a ZMQ socket for a worker to pick it up.

But wait, it exists..


Mongrel2
========

`Mongrel2 <http://mongrel2.org/>`_ is exactly what I am looking for, because it
basically forwards HTTP requests into a ZMQ socket, where I can connect as
many workers as I want.

`m2wsgi <https://github.com/rfk/m2wsgi>`_ is a WSGI handler that can be used
to get the ZMQ requests from Mongrel2 and send back the response.

It's simple to create a script that runs your Python WSGI app using m2wsgi::

    from m2wsgi.io.standard import WSGIHandler
    from mysuperapp import wsgiapp

    zmq_port =  "tcp://127.0.0.1:9999"
    handler = WSGIHandler(wsgiapp, zmq_port)
    handler.serve()

Then to have Mongrel2 send stuff on that port. Something like::

    wsgi_handler = Handler(send_spec='tcp://127.0.0.1:9999',
                        send_ident='be4ee7d-6a47-42dd-9acd-1707add81835',
                        recv_spec='tcp://127.0.0.1:9998',.
                        recv_ident='')

    routes={ '/': wsgi_handler }

    localhost = Host(name='localhost', routes=routes)
    localip = Host(name='127.0.0.1', routes=routes)

    main = Server(
        uuid='31bf6b07-a147-466c-87b5-961481b99201',
        access_log='/logs/access.log',
        error_log='/logs/error.log',
        chroot='/var/www/mongrel2/',
        pid_file='/run/mongrel2.pid',
        default_host='localhost',
        name='main',
        port=6767,
        hosts=[localhost, localip]
    )

    settings = {'zeromq.threads': 1}
    servers = [main]


(Inspired from http://server.dzone.com/articles/deploying-graphite-mongrel2)


And finally, have Mongrel and m2wsgi processes managed by Circus::

    [circus]
    check_delay = 5
    endpoint = tcp://127.0.0.1:5555
    pubsub_endpoint = tcp://127.0.0.1:5556
    stats_endpoint = tcp://127.0.0.1:5557

    [watcher:mongrel2]
    cmd = mongrel2 tests/config.sqlite 31bf6b07-a147-466c-87b5-961481b99201
    warmup_delay = 0
    numprocesses = 1
    working_dir = /Users/tarek/Dev/github.com/circus-wsgi
    stdout_stream.class = StdoutStream
    stderr_stream.class = StdoutStream

    [watcher:m2wsgi]
    cmd = bin/python server.py
    numprocesses = 2


Then. circusctl, circus-top and circushttpd give me a full control on my stack,
live::

    $ circusctl list
    circusd-stats,m2wsgi,mongrel2

    $ circusctl list m2wsgi
    1

    $ circusctl incr m2wsgi
    2

    $ circusctl stats m2wsgi
    m2wsgi:
    1: 10936  python tarek 0 N/A N/A N/A N/A N/A
    2: 10946  python tarek 0 N/A N/A N/A N/A N/A


What's next
===========

I'll bench a Mongrel2-Circus stack to see how it performs compared to our current
Gunicorn stack.

If the results are good, I might try to write a small *circus-wsgi* integration
package to make it easier to setup and configure everything together.
