django-memcached-pool  and Ultramemcache released
#################################################

:date: 2012-09-24 13:00
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

Background
==========

One thing we had to fix on the Marketplace server was an issue with Membase
where we were busting the Moxi server on high loads.

The Moxi server is a proxy the Membase server runs so the Membase server
becomes compatible with any Memcache client.

Moxi is provided in Membase and runs by default on every node.

What is does is query all the Membase nodes, build a graph and decide
depending on the key, which node should be called.

It follows the `vbucket algorithm <http://dustin.github.com/2010/06/29/memcached-vbuckets.html>`_
that provides consistency when you add or remove nodes. Read: your data
is not lost if a new Membase node is added, unlike Memcached.

Moxi is mandatory in the Python eco-system because there is no
vbucket-compatible membase clients out there AFAIK.

It's not hard to do since it's just a matter of downloading a file from one of the membase nodes
to get a graph and calculate where the item is located, given a key.

But hey, it's not the sexiest task and Moxi is there, so...

The only issue with this is that with the default Django memcached backend, which
creates a new socket everytime you use it, the Moxi server will just pile
up connections and start to refuse new ones.

You can tweak it to get more, but a smarter strategy is just to keep
a persistent connection on the Django side so we don't open that many connections.

And it will be faster !

So I've created **django-memcached-pool** for this.


django-memcached-pool
=====================

`django-memcached-pool <https://github.com/mozilla/django-memcached-pool>`_ is a pool of
connectors that will keep opened connections against Membase node(s).

It has the following features:

- configurable list of Membase nodes
- configurable pool size
- configurable timeout when connecting on a node - when it times out the node is blacklisted
- a node stays in the blacklist for 4 seconds, but you can change that value

If you run your Django app with a classical sync worker -- like with the gunicorn default
worker, keeping more than one connection is not really useful. But as soon as
you switch to an async worker using Gevent or whatever, you'll need to be able to have
several connections at the same time so it does not become a bottleneck.

I've also decided to use `umemcache <http://pypi.python.org/pypi/umemcache>`_
in **django-memcached-pool** for these reasons:

- it's pretty damn fast
- it uses plain CPython sockets, so if you run it with Gevent and call its monkey
  patching functions, the socket calls won't block

There were a few things that needed to get fixed though, for umemcache to be a good
replacement for *python-memcached*


ultramemcache
=============

When we switched to ultramemcache, it started to throw errors on some set() calls.

Turned out umemcache limits the size of the Memcache items to around 1MB. Also turns
out we had some bugs on our side, because we were pushing full objects in Memcache
instead of their ids -- so we had items with 5mb of pickled data  :)

Anyways, this 1000*1000 (so a bit less than 1MB) is not something that's really
relevant these days, as you can configure Membase to do more (or less)

The other issue was that umemcache did not let me configure the socket timeout
when I was creating a new Client instance. The socket object was not *published*
as an attribute in the CPython Client class.

So I've contributed those small features and Jonas nicely merged them and pushed
a 1.5 on PyPI. yay OSS \\o/

**umemcache** is now a good replacement for **python-memcache**

The only feature it misses to be a full drop-in replacement is the client-side
sharding strategies most clients provide, so your code picks a server out of a list,
given a storage key.

But since we're using Membase, we don't care anymore - It's up to Moxi to
do this sharding job.

The only thing I've added on the client-side in django-memcached-pool is a
round-robin-like load balancer so the client can be configured to run against several
Membase nodes. If one goes down it's blacklisted for a while and the next connector
will pick another server.



What's next ?
=============

I don't know. You try it and tell me ?

