Title: Firefox Sync Server in Python -- Take 1
Date: 2010-08-10 15:07
Category: firefox, python, sync

I have been working for a bit more than a month now on the next
generation of the Firefox Sync server in Python and while the project is
still in its early stages and subject to a lot of changes, I think it's
a good idea to share now about what we are building here at Mozilla.
Maybe that'll attract contributors !   
### About Sync

  
[Firefox Sync][] (formerly Weave) let you synchronize your Firefox
bookmarks, history, passwords, opened tabs etc. so you can have them on
any computer, or even use them from your iPhone [by using Firefox
Home][].   
  
Clients that are syncing work with our servers at Mozilla by using the
Sync and the User APIs defined in these documents:   
-   [https://wiki.mozilla.org/Labs/Weave/User/1.0/API][]
-   [https://wiki.mozilla.org/Labs/Weave/Sync/1.0/API][]

  
The User APIs manage the users accounts and tell the client which
server holds the data of a given user. In other words, each user is
tightly coupled to a single server when reading or writing data. This
natural sharding is great for scaling Sync, and is possible because
users don't share data (yet... ;))   
  
Another important point is that the data are encrypted on client side
before they are sent over. That's because one of the key concept of Sync
is that your data should not be known by our servers, to protect your
privacy. Well, we could probably still know *how many* bookmarks you
have by counting the number of entries in the DB, or *how often* you use
your browser. But as soon as you use a service like that you have to
give away these kind of information, most of the time just because they
are useful to make the service faster or understand any potential
problem. [Read our privacy policy here][].   
  
And the good news is that you can set up your *own* Sync server and
even implement it yourself if you want.   
  
So, a Sync server a pretty passive storage server, that is quite easy
to scale while keeping [data consistency][] across clients.   
### About the code

  
The current implementation uses Apache, PHP, LDAP, MySQL and Memcached.
For various reasons I won't detail in this post --that might be another
post-- , it has been decided to switch the Sync server to Python   
#### Python libraries

  
The Sync server is composed of web services and a few screens used for
the password reset process, so using a web framework would have been
overkill. Although, writing a wsgi-enabled server made a lot of sense
since it allows people to run our implementation on their laptop, or on
any wsgi-compatible web server they wish to use.   
  
So, I've picked :   
-   [Routes][], to dispatch requests to a few classes (controllers)
-   [WebOb][] to process incoming requests and build responses
-   [Paste. PasteScript, PasteDeploy][], to group the configuration in
    an ini file and make it easy to run the application with a built-in
    server.

  
There are alternative routing systems, but **Routes** really fits my
brain and make the dispatching quite simple. I really like the fact that
you can *optionally* use regular expressions to validate URLs.   
  
**WebOb** is quite a standard library and make our life simple to read
requests and write responses. The code in our controllers stays KISS
with WebOb when you have to read incoming data: they're all available in
simple mappings. The response is also built by WebOb and you can forget
about all the wsgi protocol details. We mainly return JSON dumps that
WebOb wraps into responses.   
  
Last, **Paste** is very handy to run the server locally, to initialize
data, and handle multiple configurations. I should also say that my
colleague[Ian Bicking][] is behind the Paste and WebOb libs, and
involved in the Sync project. So those were quite natural choices.   
  
The authentication process is a custom function that reads a basic
authentication header and checks it using an authentication plugin (more
on plugins later in this post.)   
  
For the storage, I've picked **SQLAlchemy** and **python-ldap**. I
don't really use the ORM part of SQLAlchemy and write pretty raw SQL
queries to avoid any extra overhead. The benefit of the ORM was null
here anyways, since all storage I/O are contained in a storage class
that outputs simple mappings. I have created the mappers though, as they
are useful to initialize a DB on a first run.   
  
But when the server runs, SQLAlchemy is mainly used for:   
-   its connection pooling abilities.
-   the nice parameters binding
-   the ability to switch to any DB system via configuration (as long as
    the SQL is compatible of course)

  
As for** python-ldap** (I didn't implement the LDAP part yet), it's the
standard connector I have always used with various flavors of LDAP
servers (OpenLDAP, ActiveDirectories, etc.). I don't think there is any
competitor for this anyways.   
#### Caching

  
The caching is currently done using Memcached. For instance, when
clients are often asking for specific collection items, they end up in
memcached to lower the number of queries made to MySQL. For the Python
implementation though, I've decided to use [**Redis**][] instead.   
  
In terms of speed, Redis and Memcached are quite similar. Redis though
has interesting extras:   
-   The data is saved to the disk, so you don't lose your cache. The
    speed stays almost the same as memcached since the disk syncs are
    done asynchronously from time to time. Since a Sync user is tightly
    coupled to a storage server, that's an interesting feature to have.
    And, hey, you can move data from a Redis DB to another, so migrating
    the cache to another server is even possible.
-   Redis provides built-in APIs to work with sets and lists, which
    authorizes more complex caching without extra code. This will allow
    us to do more caching in the future.

  
#### Storage

  
The storage itself will stay on MySQL but we will probably explore
alternative storages systems in the future. One requirement of Sync is
to be able to *write* data as fast as possible so all clients can have
access to them as soon as possible. Right now, Sync provides [immediate
consistency][], since all writes are done synchronously on a single
server.   
#### Plugins

  
The PHP application was built with extensibility in mind: the way
Mozilla stores the data and authenticates users (a mix of LDAP and
MySQL) might not work if the code is used by someone else. That's why
the code was built using abstractions for the storage and the
authentication part, and the Python version took back this good idea.   
  
Basically, you can write a new authentication or storage class, and
configure Sync to use it. See the documentation I am building on this:
[http://sync.ziade.org/doc/storage.html][] (temporary location)   
#### Web server

  
The web server that runs the Python application will stay Apache (with
[mod\_wsgi][]) since it has proven to work very well with the current
implementation. I might bench other servers in the future though, like
[Gunicorn][] + nGninx or [uWSGI][] + nGninx. We now have a nice
[Grinder][] script that realistically mimics Sync users, so..   
### Doc and Code

  
I've started a documentation, the temporary location is at
[http://sync.ziade.org/doc][] and you can grab the code we are building
at [http://hg.mozilla.org/users/telliott\_mozilla.com/sync-server][].
You can already use the server with your Firefox / Firefox Home, but
this is still at development stage, so use at your own risks.   
  
I would love to get some feedback on that work !

  [Firefox Sync]: https://www.mozilla.com/en-US/firefox/sync/
  [by using Firefox Home]: http://www.mozilla.com/en-US/mobile/home/
  [https://wiki.mozilla.org/Labs/Weave/User/1.0/API]: https://wiki.mozilla.org/Labs/Weave/User/1.0/API
  [https://wiki.mozilla.org/Labs/Weave/Sync/1.0/API]: https://wiki.mozilla.org/Labs/Weave/Sync/1.0/API
  [Read our privacy policy here]: https://services.mozilla.com/privacy-policy/Privacy_Policy.pdf
  [data consistency]: http://en.wikipedia.org/wiki/Data_consistency
  [Routes]: http://routes.groovie.org
  [WebOb]: http://pythonpaste.org/webob/
  [Paste. PasteScript, PasteDeploy]: http://pythonpaste.org/
  [Ian Bicking]: http://blog.ianbicking.org/
  [**Redis**]: http://code.google.com/p/redis/
  [immediate consistency]: http://en.wikipedia.org/wiki/Immediate_consistency
  [http://sync.ziade.org/doc/storage.html]: http://sync.ziade.org/doc/storage.html
  [mod\_wsgi]: http://code.google.com/p/modwsgi/
  [Gunicorn]: http://www.google.com/url?sa=t&source=web&cd=1&ved=0CBgQFjAA&url=http://gunicorn.org/&ei=ojlhTNSzG9W6jAfVweiwCQ&usg=AFQjCNH4886vZhhVrpKRkAak1Ja0k68d3g
  [uWSGI]: http://projects.unbit.it/uwsgi/
  [Grinder]: http://grinder.sourceforge.net/
  [http://sync.ziade.org/doc]: http://sync.ziade.org/doc
  [http://hg.mozilla.org/users/telliott\_mozilla.com/sync-server]: http://hg.mozilla.org/users/telliott_mozilla.com/sync-server
