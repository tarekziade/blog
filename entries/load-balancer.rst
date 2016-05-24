Consistent Load Balancing
#########################

:date: 2016-05-16 19:50
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade


This is an interesting problem to look at. Let's say you have 1 million users
and 5 storage servers. You are building an application that needs to pick one
of the 5 storage servers depending on the user id.

You want your app to do it as consistently as possible. e.g. a given
user should always land on the same backend.

When a request comes in:

- each request is identified by a unique user id.
- the app should always call the same storage server given that id.
- you want all your users to be distributed equally across your storage
  servers.
- when a storage server is removed from the list, you want users
  to stick with the servers they initially got. For users on the
  removed server, they should be dispatched equally on other servers.
- when a server is added, you want the minimal numbers of users to
  be moved around.
- The application is stateless about this, so when I deploy
  a new node and give it the list of the storage servers,
  it should be able to start distributing users among them
  without prior knowledge.


Point 4 and 6 discards a simple round-robin solution.

The solution to that problem is to build a deterministic function
that projects a user id into the space composed of the servers.
(yeah well, clustering I guess.)

There are two known algorithms to do that. The consistent hashing
algorithm and the rendezvous hashing.


Consistent Hashing
==================

`Consistent Hashing <https://en.wikipedia.org/wiki/Consistent_hashing>`_
is a hashing that can be used to minimize the shuffling of users
when a server is removed or added.

This is how it's implemented:

- each server name is converted into a unique number
- that number is projected on an modulo interval (a circle)
- every user is also converted into a unique number and projected on the circle
- the server that's the closest to the user is picked

If you want nice drawing go `here <http://michaelnielsen.org/blog/consistent-hashing/>`_.

This is an elegant solution because removing a server keeps the rest
stable, and adding one server shuffles a minimal number of users.

The conversion from a name to a integer is key here: you have to
be deterministic but in the same time try to have the numbers randomly
and kind-of-evenly distributed on the circle.

Here's how you can do it using MD5::

    import hashlib

    def hash(key):
        return long(hashlib.md5(key).hexdigest(), 16)


Using a classical hash like MD5 gives us the random part, but
depending on the server name you might well end up with two servers
that are very close to each other on the circle

And the result will be that when the users are converted into
numbers, a very small amount of users will go to some servers.

One solution to fix that is to add replicas: for each server,
instead of projecting a single number on the circle, we'll project
100. For example, "server1" becomes "server1:1", "server1:2", ..,
"server1:100" and those values are transformed into numbers.

Using replicas is very efficient to make sure users are
spread evenly.



RendezVous
==========


The other algorithm is called `RendezVous <https://en.wikipedia.org/wiki/Rendezvous_hashing>`_
and is based on a similar idea where servers are converted into numbers with a hash.

The difference is that instead of projecting servers and their replicas on a circle,
the algorithm uses weights. To find which server a user should use, for each
combination of server and user, a number is created with a classical hash function.

The server that's picked is the one with the highest number.

The Python code looks like this::

        def get_server(user):
            high_score = -1
            winner = None

            for server in server:
                score = hash(server + user)
                if score > high_score:
                    high_score, winner = score, ip
                elif score == high_score:
                    high_score, winner = score, max(server, winner)

            return winner


The advantage of this method is that you don't have to create replicas
to worry about distribution. In fact, according to my tests, RendezVous is
doing a better job than Consistent Hashing for distributing users.

One key decision is to decide which hashing algorithm you want to use.


It's all about the hashing!
===========================

Both RendezVous and Consistent hashing are using a classical hashing
function to convert the servers and users into numbers - and picking
one was not obvious.

I came across this amazing `stackexchange post <http://programmers.stackexchange.com/questions/49550/which-hashing-algorithm-is-best-for-uniqueness-and-speed/145633#145633>`_ that shed some light on different hashing, their strengths
and weaknesses. You should read it, you will learn a lot.

The take away for my experiment was that some hashing functions
are doing a better job at randomizing values in the hash space.
Some very simple functions are also colliding quite often, which
can be a problem.

So I tried a bunch of them and benchmarked them.

It's interesting to note that I had much better results for my use
case using RendezVous & sha256 than RendezVous & Murmur, when the
latter is usually what people use with RendezVous.

I ended up removing Murmur from my tests, the results where
too bad.


Anyways, here's the full implementation I did, based on
snippets I found here and there, and the result:

`The gist <https://gist.github.com/tarekziade/efa320ee463d9675db6f55f2ffaa7f86>`_

**And the winnner is : RendezVous and sha256**

Of course, that entirely depends on how many servers & users you have.
