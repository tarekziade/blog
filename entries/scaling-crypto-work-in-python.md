Title: Scaling Crypto work in Python
Date: 2012-02-06 09:03
Category: mozilla, python

We're building a new service at [Services][] called the ***Token
Server*** - The idea is simple : give us a [Browser ID][] assertion and
a service name, and the Token Server will send you back a token that's
good for 30 minutes to use for the specific service.   
  
That indirection makes our live easier to manage user authentication
and resource allocation for our services . A few examples:   
-   when a new user wants to use Firefox Sync, we can check which server
    has the smallest number of allocated users, and tell the user to go
    there
-   we can manage a user from a central place
-   we can manage a user we've never heard about before without asking
    her to register specifically to each service -- that's the whole
    point of Browser ID

  
I won't get into more details because that's not the intent of this
blog post. But if you are curious the full draft spec is here
-[https://wiki.mozilla.org/Services/Sagrada/TokenServer][]   
  
What's this post is really about is how to build this token server.   
  
The server is a single web service that gets a Browser ID assertion and
does the following:   
1.  verify the assertion
2.  create a token, which is a simple JSON mapping
3.  encrypt and sign the token

  
### The GIL, Gevent, greenlet and the likes

  
Implementing this using [Cornice][] and a crypto lib is quite simple,
but has one major issue : the crypto work is CPU intensive, and even if
the libraries we can use have C code under the hood, it seems that the
GIL is not released enough to let your threads really use several cores.
For example, we benched M2Crypto and it was obvious that a
multi-threaded app was locked by the GIL.   
  
But we don't use threads in our Python servers -- we use Gevent
workers, which are based on greenlets. But while greenlets help on I/O
bound calls, it won't help on CPU bound work : you're tied into a single
thread in this case and each greenlet that does some CPU work blocks the
other ones.   
  
It's easy to demonstrate -- see
[http://tarek.pastebin.mozilla.org/1476644][] If I run it on my Mac Book
Air, the pure Python synchronous version is always faster (huh, the
gevent version is \*much\* slower, not sure why..)   
  
So the sanest option is to use separate processes and set up a
messaging queue between the web service that needs some crypto work to
be done and specialized crypto workers.   
  
We're back in that case to our beloved 100% I/O bound model we know how
to scale using NGinx + GUnicorn + GEvent   
  
For the crypto workers, we want it to be as fast as possible, so we
started to look at [Crypto++][] which seems promising because it uses
CPU-specific calls in ASM. There's the [pycryptopp][] binding that's
available to work with Crypto++ but we happen to need to do some tasks
that are not available in that lib yet -- like [HKDF][].   
  
Yeah, at that point it became obvious we'd use pure C++ for that part,
and drive it from Python.   
### Message passing

  
Back to our Token server -- we need to send crypto work to our workers
and get back the result. The first option that comes in mind is to use
[multiprocessing][] to spawn our C++ workers and to feed them with work.
  
  
The model is quite simple, but now that we have one piece in C++, it's
getting harder to use the built-in tools in multiprocessing to
communicate with our workers -- we need to be lower level and start to
work with signals or sockets. And well, I am not sure what would be left
of multiprocessing then.   
  
This is doable but a bit of a pain to do correctly (and in a portable
way.) Moreover, if we want to have a robust system, we need to have
things like a hearbeat, which requires more inter-process message
passing. And now I need to code it in Python ***and*** C++   
  
Hold on -- Let me summarize my requirements:   
-   inter-process communication
-   something less painful than signals or sockets
-   very very very fast

  
I got tempted by [Memory Mapped Files][], but the drawbacks I've read
here and there scared me.   
### ZeroMQ

  
It turns out [zeromq][] is perfect for this job - there are clients in
Python and C++, and defining a protocol to exchange data from the Python
web server to the crypto workers is quite simple.   
  
In fact, this can be done as a reusable library that takes care of
passing messages to workers and getting back results. It has been done
hundreds of times, there are many examples in the zmq website, but I
have failed to find any Python packaged library that would let me push
some work to workers transparently, via a simple *execute()* call -- if
you know one tell me!.   
  
So I am building one since it's quite short and simple -- The project
is called ***PowerHose*** and is located here
:[https://github.com/mozilla-services/powerhose][].   
  
Here is its descriptions/limitations:   
-   Powerhose is based on a single master and multiple workers protocol
-   The Master opens a socket and waits for workers to register
    themselves into it
-   The worker registers itself to the master, provides the path to its
    own socket, and wait for some work on it.
-   Workers are performing the work synchronously and send back the
    result immediatly.
-   The master load-balances on available workers, and if all are busy
    waits a bit before it times out.
-   The worker pings the master on a regular basis and exits if it's
    unable to reach it. It attempts several time to reconnect to give a
    chance to the master to come back.
-   Workers are language agnostic and a master could run heterogeneous
    workers (one in C, one in Python etc..)
-   Powerhose is not serializing/deserializing the data - it sends plain
    strings. This is the responsibility of the program that uses it.
-   Powerhose is not responsible to respawn a master or a worker that
    dies. I plan to use [daemontools][] for this, and maybe provide a
    script that runs all workers at once.
-   Powerhose do not queue works and just rely on zeromq sockets.

  
The library implements this protocol and gives two tools to use it:   
-   A JobRunner class in Python, you can use to send some work to be
    done
-   A Worker class in Python **and** C++, you can use as a base class to
    implement workers

  
Here's an example of using Powerhose:   
-   The Server -
    [https://github.com/mozilla-services/powerhose/blob/master/examples/square\_master.py][]
-   The Python worker -
    [https://github.com/mozilla-services/powerhose/blob/master/examples/square\_worker.py][]
-   The C++ worker (don't look at the code :) -
    [https://github.com/mozilla-services/powerhose/blob/master/examples/square\_worker.cpp][]

  
For the Token server, we'll have:   
-   A JobRunner in our Cornice application
-   A C++ worker that uses Crypto++

  
The first benches look fantastic -- probably faster that anything I'd
have implemented myself using plain sockets :)   
  
I'll try to package Powerhose so other projects at Mozilla can use it.
I am wondering if this could be useful to more people, since I failed to
find that kind of tool. How do *you* scale your CPU-bound web apps ?

  [Services]: https://wiki.mozilla.org/Services/
  [Browser ID]: https://browserid.org/
  [https://wiki.mozilla.org/Services/Sagrada/TokenServer]: https://wiki.mozilla.org/Services/Sagrada/TokenServer
  [Cornice]: http://packages.python.org/cornice/
  [http://tarek.pastebin.mozilla.org/1476644]: http://tarek.pastebin.mozilla.org/1476644
  [Crypto++]: http://cryptopp.com/
  [pycryptopp]: https://tahoe-lafs.org/trac/pycryptopp
  [HKDF]: http://en.wikipedia.org/wiki/HKDF
  [multiprocessing]: http://docs.python.org/library/multiprocessing.html
  [Memory Mapped Files]: http://en.wikipedia.org/wiki/Memory-mapped_file
  [zeromq]: http://www.zeromq.org/
  [https://github.com/mozilla-services/powerhose]: https://github.com/mozilla-services/powerhose
  [daemontools]: http://cr.yp.to/daemontools.html
  [https://github.com/mozilla-services/powerhose/blob/master/examples/square\_master.py]:
    https://github.com/mozilla-services/powerhose/blob/master/examples/square_master.py
  [https://github.com/mozilla-services/powerhose/blob/master/examples/square\_worker.py]:
    https://github.com/mozilla-services/powerhose/blob/master/examples/square_worker.py
  [https://github.com/mozilla-services/powerhose/blob/master/examples/square\_worker.cpp]:
    https://github.com/mozilla-services/powerhose/blob/master/examples/square_worker.cpp
