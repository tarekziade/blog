Circus 0.3 released
###################

:date: 2012-04-17 21:29
:tags: python, mozilla
:category: python
:author: Tarek Ziade

.. image:: http://circus.readthedocs.org/en/latest/_images/circus-medium.png

.. note::

   Circus is a program that will let you run and watch multiple processes.
   Like Supervisord, BluePill and Daemontools.

The third release of Circus is here. It wanted to hightlight three new features
we've added since 0.1:

1. rlimit support
2. stderr and stdout streaming
3. flapping detection


rlimit support
--------------

Circus comes now with `rlimit <http://docs.python.org/library/resource.html#resource-limits>`_
support. For example, if you want a specific process to have a limited number of open files
to 100, you can use in your Circus configuration file the **rlimit_nofile** option::

    [circus]
    check_delay = 5
    endpoint = tcp://127.0.0.1:5555

    [watcher:myprogram]
    cmd = myprogram
    rlimit_nofile = 500

This feature is built-in in the Python standard library, in the *resource* module so that
was easy to add. The next step here would be to see how Circus could interact with tools
like `cgroups <https://en.wikipedia.org/wiki/Cgroups>`_.


stderr and stdout streaming
---------------------------

That feature is a must have, and we worked quite a bit on it to make sure it's fast
even with hundreds of processes being watched : the ability to stream the standard
output and standard error streams of all processes back into Circus.

For example, if you want **all** processes to write their stdout continously
into a file, you can write::

    [watcher:myprogram]
    cmd = myprogram
    numprocesses = 100

    # will push in test.log the stream every 300 ms
    stdout_stream.class = FileStream
    stdout_stream.filename = myprogram.log
    stdout_stream.refresh_time = 0.3

The core of this feature is a call to the **select()** function from the
standard library on the PIPEs opened on each process.

The gist of this code is::

    import fcntl

    for pipe in pipes:
        fcntl.fcntl(pipe, fcntl.F_SETFL, os.O_NONBLOCK)

    while True:
        rlist, __, __ = select(pipes, [], [])
        for pipe in rlist:
            try:
                data = pipe.read(self.buffer)
                redirect_to_circus(data)
            except IOError, ex:
                if ex[0] != errno.EAGAIN:
                    raise


**redirect_to_circus** basically redirects the stream to
whatever class you've configured in **stdout_stream.class**.
You can provide your own class if you want to implement
a specific stream handler.

We've implemented this stream redirector with one thread per
watcher that operates the select() calls, but also have a Gevent
implementation that uses greenlets instead of threads and
Gevent's own select() implementation.

The threaded version is the default one, but you can pick the
gevent backend with the **stream_backend** option.

Flapping
--------

Yet another important feature to have: the ability to detect
that a process that's launched constantly dies. That happens
when the process command line is wrong or when a resource the
program uses is not reachable for example.

Tools like daemontools will simply try again and again to run
the service, eating in the process the whole CPU of your server.

With this feature built-in and enabled by default, Circus detects
the flapping of processes, and try again *later* then eventually
quit trying.

Of course, the flapping dance is published in the PUB/SUB
channel so it's easy to build a script that will send you
an alert when it happens.


What's next
===========

We've been doing extensive load testing for a Mozilla project that's
going in production next week, and Circus seems to be quite stable so
far. It's handling around 150 processes per server right now, and
everything's working like a charm.

I think Circus has reached a level now where it could replace tools
like Daemontools in some of our set ups.

The next major step is to refactor a bit the tool to make it more
pluggable.

For example, the flapping detection is built-in, but could be
factored out as a plug-in since it subscribes to the PUB/SUB channel
to get notified when a process is restarted, and could control
everything as a client like circusctl.

In other words, it would be nice to provide a base class that gets
notifications and acts upon. The auto-grow feature I want
to add --a feature where Circus adds automatically workers depending
on the load-- could be a plugin based on that class.

Links:

- the doc: http://circus.readthedocs.org/en/latest/index.html
- the release: http://pypi.python.org/pypi/circus/0.3.1
- the repo: https://github.com/mozilla-services/circus

Please let us know what you think !
