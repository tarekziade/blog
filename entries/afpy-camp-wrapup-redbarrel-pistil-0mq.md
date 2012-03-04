Title: Afpy Camp Wrapup -- RedBarrel + Pistil + 0mq
Date: 2011-08-08 18:12
Category: mozilla, python

![image][]   
  
We had a lot of fun at the Afpy Computer Camp this year. Some people
worked on RedBarrel with me and some others on various topics, including
Pyti -- A GSOC project.   
  
In RedBarrel, besides fixing a lot of bugs we did the following:   
  
We've finished two socket.io based demos
  
-   a [monitoring page][] that displays in real-time using [Flot][] the
    CPU and memory usage of the server
-   an [url shortener][] that provides a monitoring page where you can
    see on a google map a live stream of the location of the URL
    visitors.

  
We've integrated [Pistil][] into Redbarrel
  
We started to integrate scaling features
  
  
Pistil is Benoit's new project. It's a project very similar to
[Gunicorn][] that allows you to define how a web server behaves via
"workers" and "arbiters". Pistil is basically replacing all Gunicorn
components except the command line script. One nice feature Benoit added
to Pistil this week-end is the ability to define different kind of
workers.   
  
That's because in Redbarrel we need:   
-   some RedBarrel workers, each one running a RedBarrel wsgi server to
    build the responses -- [see this code][]
-   One Flash server policy worker for the flash fallback in socket.io
    -- [see this code][1]
-   A Broadcast server -- I'll explain why later

  
Once you've integrated Pistil, you just need to add a custom
command-line script in your app and call*** arbiter.run()***[-- see this
code][]   
  
From now on, RedBarrel doesn't need GUnicorn anymore to run and manage
several processes. yay.   
### Scaling RedBarrel

  
The goal of integrating Pistil into Redbarrel was to make it possible
to run several processes (==workers) to handle more requests.   
  
RedBarrel is using Gevent underneath via gevent.socketio, so that gives
a single worker the ability to run a lot of concurrent requests already.
But still, if you're doing database accesses in your application, you
will need to run several workers if you want to handle several hundreds
of concurrent requests.   
  
And that leads to another issue : if the application uses the socket.io
features, we need the ability to broadcast messages to **all** connected
clients no matter which process they're in. gevent.socketio implements
this feature using Gevent queues in memory, so **it's constrained to a
single process**.   
  
If you have several processes, you need to be able to broadcast
messages to all the workers in order to reach all connected clients. A
inter-process communication protocol needs to be set up for this.   
  
[zeromq][] to the rescue !   
### zeromq integration

  
zeromq seems to be the best tool for this, because it hides all the
complexity when you need to set up a simple communication protocol
between several processes and servers. zeromq also allows you to use
different transports, whether they are local to the same server (ipc) or
between servers (tcp).   
  
zeromq provides several behaviors to exchange messages : PUSH/PULL,
PUB/SUB etc. see [its nice doc][].   
  
For our use case, we need to be able to broadcast messages from any
worker to all other workers. Instead of linking all workers to each
other, a simpler pattern is to have a single server that is responsible
for all the broadcasting. Workers subscribe to it to receive messages,
but also can send messages to broadcast to the server.   
  
Setting this up with zeromq is done by using a bi-directional
communication through 2 channels:   
  
A **publisher/subscribers** channel.
  
-   the publisher is a single zeromq server that is able to broadcast
    messages to several subscribers.
-   each worker becomes a subscriber and receives messages from the
    publisher.

  
A **push/pull** channel.
  
-   each worker may push messages to be broadcasted to the publisher
-   the publisher pulls messages and broadcasts them to all subscribers

  
  
That sounds like a complex setup, but is not at all ! In my first load
tests it seems very efficient.   
  
To implement this in RedBarrel, we used [pymzq][]. We also needed to
use[gevent\_zmq][]. This small library simply makes pymzq green, so it's
compatible with Gevent. The code I added is composed of a Broadcaster
class and a Client class. It's very straightforward. [You can read the
code here][].   
  
Now when RedBarrel is launched, one Broadcaster is launched and every
worker has one zmq Client, allowing inter-worker
broadcasting.![image][2]   
### Next steps

  
The next steps are:   
-   make gevent.socketio use our zeromq system. gevent.socketio
    currently uses Queues to push and pull messages to be broadcasted.
    We can keep these queues and just feed them via zeromq. What I need
    to do here is to hook the worker's broadcasting feature into the
    code that interacts with the queue.
-   allow inter-servers communication. this will simply be done by
    allowing a broadcaster to become a subscriber of other servers
    broadcasters, so it can broadcast locally to its own subscriber what
    was broadcasted in the other server. What I am unsure about yet is
    how the whole thing will scale under a very heavy message load.

  
Some other features ideas we had:   
-   provide a key/value storage using redis and a pure-python fallback
    and allow its definition via the DSL.
-   add an event system based on the zeromq integration. one event that
    comes in mind: broadcast to all workers an event everytime a key is
    changed in the storage.

  
And, yeah, we ate and drunk a lot..

  [image]: https://lh4.googleusercontent.com/-ov7H4MpuS88/Tj7fpDpA7hI/AAAAAAAABMI/zBIp62HBJL0/s288/11+-+1
    "Dinner at the Afpy Camp"
  [monitoring page]: https://bitbucket.org/tarek/redbarrel/src/tip/redbarrel/demos/rtmonitor/
  [Flot]: https://code.google.com/p/flot/
  [url shortener]: https://bitbucket.org/tarek/redbarrel/src/tip/redbarrel/demos/shortener/
  [Pistil]: https://github.com/meebo/pistil
  [Gunicorn]: http://gunicorn.org/
  [see this code]: https://bitbucket.org/tarek/redbarrel/src/43dfbce63b29/redbarrel/server.py#cl-92
  [1]: https://bitbucket.org/tarek/redbarrel/src/43dfbce63b29/redbarrel/server.py#cl-150
  [-- see this code]: https://bitbucket.org/tarek/redbarrel/src/43dfbce63b29/redbarrel/util.py#cl-56
  [zeromq]: http://www.zeromq.org/
  [its nice doc]: http://zguide.zeromq.org/chapter:all
  [pymzq]: http://zeromq.github.com/pyzmq/
  [gevent\_zmq]: https://github.com/traviscline/gevent-zeromq
  [You can read the code here]: https://bitbucket.org/tarek/redbarrel/src/43dfbce63b29/redbarrel/broadcast.py
  [2]: http://tarekziade.files.wordpress.com/2011/08/biere-e1312794381879.jpg?w=768
    "biere"
