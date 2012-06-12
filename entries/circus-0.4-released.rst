Circus 0.4 released
###################

:date: 2012-06-12 23:50
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziadé & Alexis Métaireau


.. image:: http://docs.circus.io/en/latest/_images/circus-architecture.png

.. note::

   Circus is a program that will let you run and watch multiple processes.
   Like Supervisord, BluePill and Daemontools.

We've just released Circus 0.4, after a final hacking day with Alexis at my
house.

I have already talked about most things we've added in this release
last month -- see http://blog.ziade.org/2012/05/12/circus-04-coming-soon

We'll just talk about the new things that have happened since then.

This is a blog post we are writing together with Alexis

circushttpd
-----------

The Circus web UI now uses socket.io, a javascript toolkit which uses
websockets on recent browsers and degrades gracefully on older browsers,
using for example XHR polling.

This allows us to have websockets to stream the statistics from Circus to
the web and have real-time graphs in our web console, without doing polling over HTTP
when not needed, which means without bugging too much the server. Some minor
refactorings took place on the web ui (more to come): it's now nicer to
implement new features / plugging in new commands etc.


Plugins
-------

We've added a plugin system that's documented here: http://docs.circus.io/en/latest/plugins

A Plugin is a process that listens to Circus events and let you act upon
those events. That's how the *flapping* feature or the *statsd* feature are
implemented.

Creating and adding your own plugin is as simple as using the base *CircusPlugin*
class and adding your code to the configuration file::

    [circus]
    ...

    [plugin:logger]
    use = myproject.plugins.MySuperPlugin
    option1 = foo
    option2 = bar


Circus will instanciate the plugin in a process, and treat it exactly like the usual
**watchers** sections.


circusd-stats performance fix
-----------------------------

We hacked on the 0.4 release at my house today, and fixed a performance
problem we had in **circusd-stats**. The part that was calling
**psutil** to collect stats about each process was also collecting
the process children stats.

It turns out psutil is a bit suboptimal here: everytime it tries
to get a process parent pid, it opens under Linux the */proc/PID/status*
file and iterates on each line until it gets the information. This
read operation is never cached.

The effect is that on high load, **circusd-stats** was doing a bunch
of I/O to get back an information that could be cached. 1 call
against our *circus.util.get_info()* API was doing an average of
240 calls on that file !!

I have added a bug in the psutil tracker, and I am pretty sure this
will be fixed soon. Until then, and since we don't need the children
info when we stream stats about a process, we've just changed
*get_info()* so it does not get the children info if you don't
need it.

No more call to psutil's *get_process_ppid()* and a huge boost
in our performances -- **circusd-stats** is now *way* faster and does
not consume the CPU at all, even on high loads.


Another change we did was to get rid of threads when we didn't needed them. The
motivation behind this being us having hard time debugging Circus when both
threads and gevent where into play.

The *circus.stats* streamer does not use threads anymore. Rather, it uses
pyzmq's *ioloop* `periodic callbacks <http://zeromq.github.com/pyzmq/api/generated/zmq.eventloop.ioloop.html#periodiccallback>`_

The previous implementation was using some threads and a queue to stream
messages. Removing all this extra code allows to have a cleaner overview
of what's going on and simplifies the implementation.

Now, the *StatsStreamer* class subscribes to all Circus events and maintains
periodic callbacks for each of the Circus watchers. The callbacks are gathering
statistics for each of the managed processes and publish information to the
stats endpoint, which can then be used by either the webui or circus-top to
display them.

What's next
-----------

The next big thing for Circus 0.5 is the socket feature, explained
here -- http://blog.ziade.org/2012/06/12/shared-sockets-in-circus
