Title: RedBarrel is now socket.io compatible
Date: 2011-08-03 18:18
Category: mozilla, python

I got really excited by web sockets the other week-end, so I decided
that [RedBarrel][] should support them out of the box and provide a very
easy way to work with them, like what socket.io can provide on the
server-side.   
### The usual "Chat" application

  
I have a first version of sockets support in RedBarrel. Most web socket
demos include a chat application. I ripped the one I found here:
[https://bitbucket.org/denis/websocket/src/tip/examples][] and changed
it until it worked in RedBarrel.   
  
The whole application is composed of the RBR file, a python module an
an html page with its JS libs.   
  
Here's the relevant parts of the RBR file:   
   # hooks the chat() function as a socket.io service

    path socket (

        method SOCKETIO,

        use python:redbarrel.demos.sockets.chat

    );



    # that's the html file that displays the chat room

    path chat_html (

        method GET,

        url /,

        use file:chat.html

    );

  
And the whole app is contained in one module:   
   import json

    _BUFFER = []

    _D = json.dumps



    def add(msg):

        _BUFFER.append(msg)

        if len(_BUFFER) > 30:

            del _BUFFER[0]



    def chat(globs, request):

        """A Chat room using web sockets"""

        socketio = request.socketio

        sid = socketio.session.session_id



        def announce(message):

            socketio.broadcast(_D({'announcement': message}))



        if socketio.on_connect():

            announce(sid + ' connected')

            socketio.send(_D({'buffer': _BUFFER}))



        while True:

            message = socketio.recv()

            if len(message) == 1:

                message = {'message': [sid, message[0]]}

                add(message)

                socketio.broadcast(_D(message))

            else:

                if not socketio.connected():

                    announce(sid + ' disconnected')

  
Nothing fancy here, gevent.socketio does all the magic. But I am very
glad that I was able to integrate this in RedBarrel with the
no-boiler-code-at-all philosophy I want to keep. That is 1/ define a RBR
file 2/ do the coding   
### How the feature was added

  
The problem with web sockets is that their implementations may vary or
may be nonexistent under some browser flavors. I've hacked something
that worked, then looked at how I could make the thing work under
Firefox, IE and Chrome and started to feel like back in the old days
when we had to work out our Javascript code for all the different
browsers. This may be still true but at least they are some decent
libraries now that make most of the JS code cross-compatible.   
### socket.io

  
[socket.io][] seems to do a very good job in this area for web sockets
by providing a lot of different *transports* implementations for
applications that want to have "websocket-like" features. A Transport
here is just one way to send and receive data between the client and the
server. It may be the shiny web sockets, it may be something else.   
  
socket.io has a websocket implementation -- sorry I am not following
the RFCs on this, but I know there are at least 2 versions -- **but
also** some fallbacks in case the browser does not seem to be compatible
with web sockets. That includes a flash component and various other
techniques based on async calls, like [XHR polling][]. And it works
really well -- I don't know how the fallback algorithm works internally,
but I was able to have a socket.io app running against the latest
Firefox, an old one and Chrome.   
### gevent.socketio

  
On the server side, I wanted to implement in RedBarrel something that
looked as simple as what socket.io offers. So I needed to:   
-   implement every transport protocol socket.io supports
-   provide an async layer for all the broadcasting work

  
But.. it turns out that the [gevent.socketio][] project already offers
all of this -- it implements requests handlers for all the transports
and a socket object with what we need. It uses [GEvent][] in the
background.   
  
So basically all I had to do was to :   
1.  extend the RedBarrel DSL so we can define "sockets" in applications
2.  make the RedBarrel wsgi application use gevent.socketio to handle
    incoming requests
3.  expose the socket object in the WebOb request object on the fly
4.  let the code do whatever it wants with the request and the socket,
    hopefully something useful

  
1. was easy -- you can now define one path that has **SOCKETIO** as its
*method*. That tells RedBarrel that the application will use socket.io
and calls should be transmitted to the code pointed. The syntax might
evolve since "path socket" (see the example at the beginning of this
post) is not really needed. I might change it to something more straight
forward.   
  
2. was done by switching to gevent.socketio own wsgi handlers + gevent
runner. Once gevent.socketio has done its prep work like the web socket
handsake, it goes back to the wsgi application -- so in our case the
generic RedBarrel application that runs the DSL.   
  
3. When RedBarrel is called, it looks for the environ, where
gevent.socketio adds a socket object and simply stick it to the WebOb
request object.   
  
4. the code that is called receives, like for classical calls, a WebOb
object and can use the attached socket.   
### What's next

  
I am going to add a sexy demo -- I asked people on G+ what demo I
should add and it looks like I'll add a real-time server monitoring demo
(using [Flot][]) with these features:   
-   people can look in real-time what's going on (CPU, Memory) via
    constantly updated diagrams
-   people can talk to each other on the page ("Hey bob, the server is
    melting down, don't you think?")

  
If you have a small websocket app in Python and would be interested to
see how it could fit in RedBarrel, please let me know, I'd be happy to
give it a shot

  [RedBarrel]: http://redbarrel.readthedocs.org/en/latest/
  [https://bitbucket.org/denis/websocket/src/tip/examples]: https://bitbucket.org/denis/websocket/src/tip/examples
  [socket.io]: http://socket.io
  [XHR polling]: http://en.wikipedia.org/wiki/Comet_(programming)#XMLHttpRequest_long_polling
  [gevent.socketio]: http://pypi.python.org/pypi/gevent-socketio/
  [GEvent]: http://gevent.org/
  [Flot]: http://code.google.com/p/flot/
