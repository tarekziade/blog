Title: A co-server for Zope
Date: 2007-09-28 08:13
Category: plone, python, zope

  

  
  
# Zasync

  
A few years ago, when we hit with CPS on some big customers intranet
scalability problems, we started to use [ZAsync][] in order to perform
some tasks in the background. That improved a lot the application
overall performance. What ZAsync does is recording in BTrees within the
ZODB tasks to perform, let's say Python scripts to simplify. Then a
twisted client that runs independantly opens the ZODB to read the BTree
and find the task to perform. It acts like another Zope thread in some
ways. But there's something I never understood:   
  
**Why the job queue is stored in the ZODB database ?**   
  
When we talk about scalability, most of time, the infrastructure is
more complex than a simple ZEO. It has Apaches, smtps, load balancers
all over the place. It has cron tasks to perform a variety of things,
link sending mails, creating images, or anything that can be done in the
background. It has most of the time other piece of software that perform
other things. Having a co-server that gives Zope code the ability to
perform background tasks is good.   
  
**Having a co-server that gives any software the ability to program a
task is better**   
  
Many applications, many different Zope instances, can benefit from a
centralized task manager.   

  
  
# Quartz

  
In Java world, I have used a server called [Quartz.][] It is an
independant task manager, where you can register tasks and perform jobs,
given a timing. It's like a smart cron. Using the beans technology, it
can run code independantly, or run it within a Java Server application's
context.   
  
**Why don't we have such a software in Python ?**   
  
Maybe we do, but I have never found it, so i ported part of the idea to
Python in a tool called TaskManager, that I use for example on
[fr.luvdit.com][] which is a Django application. It sends mails,
calculates neighbourhoods, etc.. Maybe I should release it but that's a
packaging work I didn't find the time to do. Any piece of Python
software can register itself as a task, in order to provide a service.
The jobs are stored into a SQL Database, that is opened through an API
by all the clients that want to perform a task, and by the co-server
that reads the queue and actually perform the tasks. It has three queue
in fact, for different priorities. The client-side APIs are really
simple and are nothing but SQL queries.   

  
  
# [lovely.remotetask][]

  
Back to Zope. Lovely systems works on a Zope 3 tool, which seems to be
working a bit like ZAsync: it stills stores the tasks in the ZODB, but
dedicates a Zope application to work as a web service provider if I
understood well. It's the way to go in term of infrastructure but I
think that it's overkill to use a Zope instance for that.   
  
**Why do we need to deploy a whole Zope stack to have a co-server ?**   
  
A dedicated, pure Python application, using a SQL database, fits better
because several task runners can work in the same queue, to create a
real producer-consumers queue. In their need to perform tasks on various
platforms, having a centralized job queue and several executors is more
scalable because the producer doesn't deal with several co-servers.   
  
Furthermore, the XML-RPC layer is not a necessity, and not as robust as
SQL: if the co-server is down, the Zope server cannot send jobs anymore,
or check for job states and get them. Working with a SQL table prevent
from this. You might argue that this is the worst scenario, but by
experience, the more application servers an infrastructure has, the more
potential point of failure you get. You might argue that the SQL server
might go down as well, but it's not a code stack, and just holds data to
be processed: all the functionalities, thus the weaknesses, are on the
co-server side. You might also argue that it makes the solution
Python-dependant, but it would be deadly simple to provide a client for
another language.   
  
Anyway, using the ZODB to store such things and a Zope to play with
them is a small mistake in my humble opinion, even if it's based on
PersistentQueue, which looks pretty robust. Let's keep this kind of
database do what it was meant for: storing persistent objects that are
publishable.   

  
  
# What I would love to have

  
The perfect co-server that I can think of, would be an independant
Python software, like TaskManager that would look like this:   
             -------        -------  <-> co-server instance 1 / win32

             | zope  | <->  | sqldb | <-> co-server instance 2 / linux

              -------        -------  <-> co-server instance 3 / linux

                               ^

     ----------------          |

    | another server |<--------

     ----------------

  
-   sqldb is a database that store jobs;
-   each arrow is provided by a python API, that knows how to interact
    with the database;
-   a co-server is an independant, pure Python runner, that picks up
    some work into the DB;
-   each co-server instance is able to perform tasks, that are provided
    through a plugin system.
-   for zope-dependant tasks, a generic task provides an entry point to
    execute code through XML-RPC calls *or* through a direct ZODB
    opening to avoid eating a thread (eg à la ZAsync);

  
OK, this is exactly Quartz :)   
  
In the last five years, most of the scalability problems I bumped into,
were resolved by a good practice: **let's be less Zope-centric when we
talk about infrastructure**.   
  
I would be pleased to have a few comments from Lovely guys on this
topic, and I thank them for their latest post, that helps a lot the
community to think about scalable solutions for Zope.

  [ZAsync]: http://www.zope.org/Members/poster/zasync
  [Quartz.]: http://www.opensymphony.com/quartz/
  [fr.luvdit.com]: http://fr.luvdit.com/
  [lovely.remotetask]: https://launchpad.net/lovely.remotetask
    "lovely-remotetask"
