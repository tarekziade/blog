zmq and gevent debugging nightmares
###################################

:date: 2012-05-25 13:29
:tags: python, mozilla
:category: python
:author: Tarek Ziade

.. image:: http://powerhose.readthedocs.org/en/latest/_images/medium-powerhose.png

.. note::

   Powerhose turns your CPU-bound tasks into I/O-bound tasks so your Python applications
   are easier to scale.


I've released Powerhose 0.4 at PyPI - http://pypi.python.org/pypi/powerhose/0.4, and this
new version has a few changes that are worth speaking of.


pyzmq + gevent = ?
------------------

The biggest issue I faced with Powerhose was related to gevent. We have a powerhose set up
here at Mozilla with 175 workers and each one of them is performing crypto work.

A Powerhose worker is just a call to **powerhose-worker** pointing to a callable.

What I did not realize was that the module that was imported was also used by our main
application, and was calling gevent and gevent_zmq monkey patching.

**gevent_zmq** is a library that patches pyzmq so it interacts well with gevent. It's
going to die eventually since *pyzmq* is including a *green* module that will provide
gevent compatibility. But this module does not provide a Poller yet.

So, in other words, any project that has pyzmq & gevent will **block** unless you
use gevent_zmq. And if you use the Poller you need my fork: https://github.com/tarekziade/gevent-zeromq

Back to my workers. Having them patched by gevent/gevent_zmq is not an issue per se.
It can even speed up very slightly things since the workers are fetching certificates on
the web sometimes.

But at some point -- or more precisely, around every 24 hours, the workers were simply
locking themselve and hanging there.

After a lot of work, I found out that gevent had its own dns resolver which was used
when calling **socket.getaddrinfo**, and for some reason -- a bad interaction between zmq
and gevent I suspect, a greenlet was locked.

Maybe that's a bug in gevent_zmq, maybe that's an issue in gevent itself..

I failed to find the real reason because the lock happened in various places in the
gevent socket code. I did not spend more time on this since the bug seems to have gone
away once I removed gevent altogether from the workers as we don't use gevent there
and the workers are **sync** beasts.

The one thing I was able to do though was to write a little piece of code to
dump all running threads and greenlets to understand what's going on::

    import traceback, sys, gc

    def dump_stacks():
        dump = []

        # threads
        threads = dict([(th.ident, th.name)
                            for th in threading.enumerate()])

        for thread, frame in sys._current_frames().items():
            dump.append('Thread 0x%x (%s)\n' % (thread, threads[thread]))
            dump.append(''.join(traceback.format_stack(frame)))
            dump.append('\n')

        # greenlets
        try:
            from greenlet import greenlet
        except ImportError:
            return dump

        # if greenlet is present, let's dump each greenlet stack
        for ob in gc.get_objects():
            if not isinstance(ob, greenlet):
                continue
            if not ob:
                continue   # not running anymore or not started
            dump.append('Greenlet\n')
            dump.append(''.join(traceback.format_stack(ob.gr_frame)))
            dump.append('\n')

        return dump


That should be useful in the future.

Bottom line:

- gevent does not have good debugging tools - I guess the function I wrote is
  useful, it can be even injected live on a running process using Pyrasite.

  But gevent should provide this kind of utility imho - I'll propose something

- I am looking forward for pyzmq.green with the Poll class. We've opened a ticket
  on this, and it will eventually land I guess.


zmq_bind() bug ?
----------------

The other issue I had was with the ZMQ bind() API. Powerhose's Broker binds a
socket, but it turns out you can bind as many broker as you want on the
same IPC or TPC adress !

You end up with one active broker and a lot of *zombies brokers*...

See this bug to reproduce the issue:
https://github.com/zeromq/pyzmq/issues/209 (the past
scripts will be online for a month)


And that's the thread I started in the zmq mailing list:
http://lists.zeromq.org/pipermail/zeromq-dev/2012-May/017249.html

So until this is solved, what I did is add a health feature in Powerhose.
You can now call the broker, but instead of passing a job, you can pass
a **PING** and the broker will directly return its PID instead of
passing your call to a worker.

That's good enough to make sure the broker is up and running, and
the **powerhose-broker** command line has gained two options::

    $ powerhose-broker --check
    .. checks if the broker is alive and running, prints its pids...

    $ powerhose-broker --purge-ghosts
    .. kill any "ghost" broker...

The broker itself does a --check when it starts and exits if it finds
a running broker on the same endpoint.

This will be useful for a Nagios checker. But... zmq should just error out
when you try to bind twice.


What's next
===========

I am wondering at this point, besides those small fixes, if Powerhose
should gain more features... Circus itself provides all the stats and
maintenances feature we need to manage powerhose workers..

Links:

- the doc: http://powerhose.readthedocs.org/en/latest/index.html
- the release: http://pypi.python.org/pypi/powerhose/0.4
- the repo: https://github.com/mozilla-services/powerhose

Please let us know what you think !
