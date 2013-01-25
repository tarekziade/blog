A new development era (essay)
#############################

:date: 2013-01-25 19:00
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

I `posted a G+
<https://plus.google.com/106436370949746015255/posts/CqxZKt3zoEm>`_ yesterday
where I was basically saying: all clients apps will be HTML5/JS at some point
on mobile/tablets/desktop, and what we call "web applications" on server side,
are just becoming a bunch of specialized web services, or proxies that route
calls to backends.

The post had a **lot** of feedback and that was pretty cool to have the
experience of many developers. Most of them agreed with the general idea, and I
thought it would be interesting to blog it here - refined with all the
feedback.


2000 - 2012
===========

.. image:: http://blog.ziade.org/2000-2012.png

When I think about my first years of developement, we were doing
*heavy clients* using tools like *Borland Delphi* and the server
was just the SQL Database. That was before 2000. Doing an application
UI in the web was inconceivable. The only applications we had in the
browser were desktop applications hidden in ActiveX components - and
some Java ones for the brave. We had **rich clients** made with some
desktop GUI toolkits, and some ugly looking web apps. BB forums
anyone?

But if you are a developer of that generation, you've witnessed
the growth of the web ecosystem like I did.

We built **feature-loaded web frameworks** and started
to create *amazing* web apps, backed by new HTML/JS technologies
like the 2004 buzzword **ajax**. They were so amazing compared
to what we had before in the browser, that they just killed
some of their desktop applications counterparts.

Think about mail clients: the first web mails we had, had
a poor UX - and then GMail changed the game. Nowadays,
I guess it's easy to predict that desktop mail apps are
going to disappear at some point.


So until the last few years, the typical ecosystem was an
amazing set of tools on the server-side, that included zillions
of template engines, to produce rich web pages.

Of course, we started to include more and more display
logic on the client side, using jQuery and async calls
over the server.

But the server was still where everything was happening,
from the DB calls to the HTML page rendering.

**And right now we are shifting**


2013 - ?
========

We're moving away from the model I've described earlier.
That move is obvious to many developers, but the big
crowd of devs out there (that includes me) is still doing
the classical server-side MVC development, when sometimes
they should ponder what could be pushed on the client
side - for instance everything related to rendering a
display.

And the HTML/JS ecosystem is gaining a lot of maturity.
So much that the server-side web frameworks role
are starting to change slowly: it's not that big
framework that's responsible to render HTML pages anymore,
doing all the heavy-lifting of calling backends
and databases.

It's becoming just a proxy in front of database systems,
or specialized web services, that sends back JSON
responses to the web browser, and let it handle all
the templating and all the display work.

Micro-frameworks are getting a lot of traction for that
reason: the web app become either that thin link
between a smart JS app and a solid database systeme,
either that specialized web service that provides
some business logic.


.. image:: http://blog.ziade.org/2013-.png


`Web sockets <https://developer.mozilla.org/en-US/docs/WebSockets>`_
offer real-time capabilities that are quite
amazing. You can potentially offer interactions between
users within the browser with a very simple server that
just keeps track of sockets. (that introduces other
scalability issues though)

With `CORS <http://www.w3.org/TR/cors/>`_, it gets even
further: a Javascript application
can now connect directly to various web services located
on different servers.

For instance, if there are no complex security/permissions
needs, you can probably call directly servers like Elastic
Search to provide a search feature.

You can build diagrams by doing queries to a DB
backend, with a minimal server layer that just routes
your calls.

And soon enough, local storages will be a standard
thing in Javascript applications.

Last but not least, all the responsive design techniques
let people build interfaces that will work on different screen
sizes.

The boundaries between your mobile, your tablet and your
desktop computer are getting fuzzier. They're becoming
devices with different screen sizes now, with different storages
and CPU powers, that are just powering a web browser.

You get the idea: an HTML page with some Javascript
can do a whole lot of things that used to be done on the
server side.

I would not be surprised if one day
`Firefox OS <https://www.mozilla.org/en-US/firefoxos/>`_ is used on
the desktop :)

To quote someone on G+:

    This is exactly my experience. My server side has evolved to basically a
    simple REST layer plus a zeromq/protobuf -> Websockets/JSON translation and
    routing layer. With backbone/knockout/angular etc on the front end, there's
    not really much else I can see needing to do in the backend.

So I believe we're going to a world where any connected
device, including your desktop, is made of HTML/JS apps, and that
the complexity of our applications are moving around, towards a
much cleaner layout: everything related to display on the client-side,
and everything related to business logic, data etc, on specialized
backends or databases systems - but moved out of those
big web frameworks we still all use a bit.

If you are a server-side guy like me, you ought to love all those
micro frameworks, and to build a bunch of small, specialized web services
that all together, can power-up a Javascript app.

In fact, I think **Python is becoming the secret weapon behind every
good Javascript application** ;)

Or... maybe we're just cycling again and again, as
JR states it:


    I always think that there is some imaginary pendulum that swings between
    extremes. At first, everything was done on the server, then PCs were
    introduced and people moved complexity there with the server holding data.
    Then the web was born and complexity once again shifted back to the server,
    and now that browsers are more capable, the focus is again shifting to the
    client.


If you want to comment, I'd suggest doing it in the G+ thread
since it started there.



