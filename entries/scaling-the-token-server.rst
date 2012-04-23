Scaling the Mozilla Token Server
################################

:date: 2012-04-12 00:00
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziadé & Alexis Métaireau & Pete Fritchman
:status: draft

This blog post gives a high level overview of the work we did
to scale the Mozilla Token Server. I worked with Alexis on this project
on the coding side, and Pete is our "op" guy.

The *Mozilla Token Server* is going to become an important piece of our
server-side infrastructure are Mozilla in the upcoming months, because
it will be called by *all* clients that want to interact with our online
services.

The *Apps In The Cloud* project is the first service that implements this
and the next generation of *Firefox Sync* will probably be the second service
using it, followed by more.


What's the Token Server ?
=========================

The Token Server is a service which aims to centralize authentication for
all the services we provide -- it's basically a CaS. (xxx)

The core idea is:

1 - You provide credentials to the Token Server, it's able to verify,
    and ask for an access on a specific service.
2 - The Token Server allocates you to a specific node for that service,
    e.g. a unique URL to call to interact with the service.
3 - The Token Server then emits a unique token for you, that is signed
    using a secret shared between the Token Server and the service node.
4 - You use this token to authenticate to the service.

Tokens are limited in time and the client calls back the Token Server
from time to time to get a fresh token.

For us, this centralization is great for several reasons:
- in case a node gets compromised, we can revoke instantly the validity
  of all tokens that were issued, forcing the clients to issue a fresh
  token.
- we can have a single users database for all our services ala LDAP
- it's easy to migrate users around, by reallocating them to new nodes
  and forcing them to get a new token.
- it's potentially possible to support multiple authentication schemes
  in the Token Server without impacting services.

See XXX for more info in this.

The token server could support any kind of authentication scheme, but
v1 will only support Browser-ID assertions.


Implementation challenges
=========================

Building this kind of service is a bit of a challenge because it
slightly differs from the usual web application that does database
calls and issue results as HTML or JSON response.

The main difference is that the server is doing a lot of CPU
intensive work to verify the Browser-ID assertions and to create
tokens. And, as I explained in a previous blog post <XXX>
that's not the best use case for Python.

We needed to convert all the CPU-bound calls into I/O-bound calls
since our gevent-based stack is very easy to scale for I/O bound web
apps.

That's why we've
created `Powerhose <http://github.com/mozilla-services/powerhose>`_, a
tool that transmits crypto jobs from the web application to a pool of
specialized workers.

This was done using a ZMQ broker <xxx> and the overhead is minimal as
long as all workers are located on the same server. ZMQ has several
available transports and we're using the IPC transport. But since
this is just a configuration option, we could imagine deploying
Powerhose clusters and use a TCP transport, as long as the round-trip
overhead worth the pain.

But it turns out that even with a slight transport overhead, the
magic of Gevent can operate on the application now that everything's
back to a pure I/O stack : instead of blocking on the CPU-intensive
calls, the server is now able to make good usage of the Gevent
cooperative sockets XXX and accepts more connections while the
Powerhose workers do their duties.

So, the average response time is probably slightly bigger but
the server is able to respond to a large number of simultaneous
requests.

I should also mention that these architectural choices were made
because we're deploying boxes with a lot of processor cores.
XXX

Load testing
------------

As said, the tokenserver is a key part of our new infrastructure and will be
called a lot. We indeed have unit and functional tests, but we also needed to
ensure the fact that it's handling the load well.

This means testing the real stack. To do the load tests, we used the incredibly
easy and powerful Funkload <XXX>. Writing load tests is just a matter of
describing, in python, the requests you want to do. You can then configure
where to send the requests and how many of them you want. From this, you can
get nice graphs telling you how much time the requests took, if some of them
failed, etc.

Creating valid browserid assertions can be done quite simply: you need to ask
browserid.org (or any browserid provider). The problem with this is that we
would add some extra load to browserid.org without any other good reason than
load testing. Rather than doing this, we introduced a backdoor in our system to
bypass browserid.org.

WHAT? A BACKDOOR?

If you happen to set the `loadtest_mode` flag to `True` in your configuration,
we will use a local certificate to verify the signature of the assertions you
send in to the tokenserver. And we can use the matching private certificate to
sign the assertions in the first place.

When I first started, I just sent a bunch of valid assertions to the
tokenserver, verifying that they were considered as valid ones and 
happily returning 200 with a token. Wow. Incredible performances.

Of course, this was wrong. What we are doing here is only to assign an user to a
node and then read again and again the node information from the database.
Because databases are smart, they end up storing this in memory and not reading
anything at all.

To understand why, we need to recall what we want to test: that the load is
correctly handled by the tokenserver. What is this so-called "load", then? The
tokenserver is doing basically three things: checking the browserid assertion,
assigning users to nodes (if they are not already) and retrieving this
information.

Two different kind of tasks: node assignment and node retrieval. Testing node
assignment can be done by sending assertions with email addresses unknown to
the tokenserver. This can be done fairly easily by generating email addresses
in the form of `<uuid>@loadtest.local`.

Testing node retrieval is a bit more tricky: we need to first create the
records in the database and then send the rights assertions there, mesuring the
number of requests we could handle and watching some metrics on the database.

Handling errors
---------------

Obviously, we are doing code here. And code always fail. So we were in need to
handle those errors, especially in the crypto workers. There are a bunch of
things that could possibly go wrong:

* We are unavailable to retrieve some certificate from the network
* The assertion the users sent us is wrong, we are unable to parse it.
* The assertion is no longer valid (expired)
* The signature doesn't match with the retrieved certificate

Ops challenges
==============

XXX

