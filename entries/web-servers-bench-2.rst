WSGI Web Servers Bench Part 2
#############################

:date: 2012-07-03 14:50
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade


Last week I published `a bench on Circus <http://blog.ziade.org/2012/06/28/wgsi-web-servers-bench/>`_
and I had some good feedback in the comments.

We ended up saying that the app I was benching was hammering the disk too much to provide
results that were accurate.

Following *AdamSkutt* suggestions, I've modified the benched app so it would do
I/O-bound tasks without hitting the disk, by exchanging data with a thread
through a pipe.

The new app does the following:

1. a loop that does *10 \* 1000 \* 1000* 10000 times. (CPU)
2. a *time.sleep(N)* where N is between 75 to 100 ms  (just piling up)
3. 100 bytes sent to the *DB thread* using the pipe (I/O)
4. a small HTML page sent by the *DB thread* and redirected by the main
   thread to the client (I/O)

See https://github.com/tarekziade/chaussette/blob/master/chaussette/util.py#L144

A *DB thread* is a Thread that opens a pipe to get data from the main thread,
and another pipe to send back data.

See https://github.com/tarekziade/chaussette/blob/master/chaussette/util.py#L72

To have a realistic simulation, the app runs 10 of those DB threads in a queue
and each incoming requests picks one and interacts with it.

That's basically what you would have when you use a pool of DB connectors
in your application.

An interesting thing to notice is that with this application, we are doing
some socket I/O, thus the gevent and meinheld workers should be *slightly*
faster than with the previous app.

But the percentage of socket I/O work involved in the call is quite small
compared to the rest -- around 10%.  I did not want to make it too unfair
for other workers that don't automagically patch the socket module.

To summarize, the new application:

- is twice faster -- around 100 ms per call
- does not hammer the disk anymore.
- still does some CPU and I/O work

Now to the results !

Gunicorn + gevent
-----------------

.. image:: http://blog.ziade.org/new_gunicorn_rps.png

.. image:: http://blog.ziade.org/new_guicorn_requests.png


The web server is ten times faster than the previous run, which is much
better since the app is only 2 times slower. Not hitting the hard disk
helps here of course.

Doing a higher RPS also makes the RPS graph much more readable -- with
a bigger scale, we can see it steadily decreasing starting at 100 CUs.

Overall I would not say that things look that different for the duration,
as it's similar to the previous run except the scale.


Chaussette + waitress
---------------------

.. image:: http://blog.ziade.org/new_waitress_rps.png

.. image:: http://blog.ziade.org/new_waitress_requests.png


I tried the waitress backend as well this time, and was really surprised by
how well it performed -- it's *slightly* slower than Gunicorn + Gevent
but by not much. They look very similar, which was a surprise for me.

I was also happy to see that the RPS graph had a similar trend, making me
think this bench is more accurate.


Chaussette + meinheld
---------------------

.. image:: http://blog.ziade.org/new_meinheld_rps.png

.. image:: http://blog.ziade.org/new_meinheld_requests.png


Circus + Meinheld is slightly faster than Circus + Waitress (expected) and
Gunicorn + Gevent. We're seeing the same tendency on high load.


Chaussette + gevent
-------------------

.. image:: http://blog.ziade.org/new_gevent_rps.png

.. image:: http://blog.ziade.org/new_gevent_requests.png


Circus + Gevent is in turn slightly faster.


Chaussette + fastgevent
-----------------------

.. image:: http://blog.ziade.org/new_fastgevent_rps.png

.. image:: http://blog.ziade.org/new_fastegevent_requests.png


Circus + fastgevent is the fastest one unlike the previous run.
We don't have the errors anymore on this run.


Conclusion
----------

This new bench seems to be more accurate, and the results are a bit different
for meinheld and fastgevent.

Fastest to slowest:

1. Circus + fastgevent
2. Circus + gevent
3. Circus + meinheld
4. Gunicorn + gevent
5. Circus + waitress

Overall, my conclusion is similar to the previous one: that makes me
confident we can switch to Circus in the future.

I still need to investigate on why fastgevent failed in the previous run.

Thanks *AdamSkutt* and al for the feedback.
