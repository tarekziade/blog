Circus 0.4 coming soon
######################

:date: 2012-05-12 15:00
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziadé

.. image:: http://circus.readthedocs.org/en/latest/_images/circus-medium.png

.. note::

   Circus is a program that will let you run and watch multiple processes.
   Like Supervisord, BluePill and Daemontools.

The next release of Circus, that should be happening soon, has some
new features I want to hilight in this post:

1. **circusd-stats**, a process that streams statistics on Circus.
2. **circus-top**, a top-like console
3. **circushttpd**, a Web Managment interface

circusd-stats
=============

In Circus 0.3, if you want to know how much CPU and Memory each process takes,
you can use circusctl::

    $ bin/circusctl stats dummy
    dummy:
    1: 91238  python root 0 3M 2G 62.6 0.1 0:04.80
    3: 91240  python root 0 3M 2G 63.2 0.1 0:04.80
    2: 91239  python root 0 3M 2G 63.1 0.1 0:04.80
    5: 91242  python root 0 3M 2G 62.8 0.1 0:04.82
    4: 91241  python root 0 3M 2G 62.6 0.1 0:04.76

I was a bit amazed by the inaccuracy of our CPU stats when I compared them to
a simple call to ps or top.

The problem was that **psutil**, the library we use to build the stats, has
two ways of calculating the CPU usage:

- a blocking call, that calculates the usage of the CPU for a bit of time,
  like 500ms.
- a non-blocking call, that just returns the value since the last call,
  that will be accurate as long as you wait at least 100ms between two calls.

The problem with any of these techniques is that, when you have hundreds of
processes running, you can't really do this calculation on the fly without
making the client wait for a long time. And Circus naively used the
non-blocking calls, meaning that the CPU usage values was relying on the
frequency of client calls.

**circusd-stats** solves this problem by constantly calculating in a
separate process all the stats for all the processes. It has a dedicated
thread per watcher, and simply listens to Circus pub/sub socket to know
when a process is added or removed.

**circusd-stats** itself publishes at a constant pace in a new,
dedicated ZMQ pub/sub channel the stats for each process, and also
aggregated stats for each watcher.

From there, any feature that needs accurate stats can register to
that pub/sub channel to receive the stats. Stats can be filtered by
watcher name, by PID, or the client can get all of them.

**circusd-stats** CPU usage can be quite important, so we've added
configurable intervals between two stats calls.

circus-top
==========

The first stats client we've added into Circus is **circus-top**, a
console script that uses **curses** to display a console dashboard
where every process CPU and memory usage is constantly refreshed.

.. image:: http://ziade.org/circus-top.png

It's a read-only console, so you can't do anything like killing
a process, but it is a good way to check if there's any issue
with your system

circushttpd
===========

I have already talked about the Web Admin tool we were building
here : http://blog.ziade.org/2012/04/23/a-web-admin-for-circus/

And well, thanks to Adnane, it now look really great. Check out
the new screencast: https://plus.google.com/106436370949746015255/posts/U6yKgbLn4a4

circushttpd is a heavy user of stats, and instead of using
the stats command **circusd** provides, it now uses the **circusd-stats**
stream.

What's next
===========

We're currently changing **circusdhttp** so it uses **socket.io** instead
of the current polling. **socket.io** will use web sockets when the browser
is compatible, and fallback to XHR-polling.

Once this integration is ready, we'll cut a 0.4

An exciting feature is planned for 0.5 : **circus-cluster**, a tool
to drive several instances of **circus** we'll call **Circus Nodes**.

This new feature will allow you to run and manage a whole cluster.
**circus-top** and **circushttpd** will be adapted to work with
**circus-cluster** as well.
