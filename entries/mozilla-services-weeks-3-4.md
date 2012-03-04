Title: Mozilla Services - Weeks 3-4
Date: 2011-02-04 10:13
Category: mozilla, python

What's this ? Read [this post][].   
### What happened

  
The two last weeks where more about fixing small issues here and there
and thinking about the tools we need to build good server-side
applications. We finalized with Stefan the work on the [Easy Setup
protocol][](Pake). The protocol is now able to work under flaky wifi
condition. Typically, if your device is in a wifi environment that drops
the connection often, instead of starting the transaction back again
every time it drops. we've added a way to resume it.   
  
The latest Firefox Home release includes this change, and the server is
compatible with the hardened protocol as well as the previous one. That
way it still works with older clients and with Firefox 4 itself, which
do not have this improvement yet (yeah, Richard & Phillip are quite busy
on fixing blockers, so they'll come to it later).   
  
This flaky wifi issue, a few bugs we had with the Sync server when the
LDAP or the MySQL server dropped, and the blog post about the [Netflix
Chaos Monkey][] gave me a idea of a project we should do at some point
at Mozilla:   
  
We need to make sure all our apps are robust when a back-end server
(==ldap, memcached, mysql, etc) gets down, and in particular make sure:
  
-   all requests to our server return 503 and logs errors correctly, and
    nothing bad happens on client-side
-   once the back-end is back, the server should return to a normal
    behavior
-   the whole system should stay stable during the back-end blackout,
    and after

  
I've started to write down some ideas about this. Basically, I want
each piece of our dev and stage servers infrastructure to get very slow
or entirely down for a bit, at random times. Then, I want to observe how
the application reacts during and **after** the event.   
### The Seism Project

  
There are many low-level tools that allow injecting delays and errors
at the TCP level. Some of them can require BSD systems, like dummynet.
Since Linux 2.4 TC can be used to do traffic shaping. But using those
tools requires setting up a dedicated infrastructure/configuration every
time we want to use such a tool for an app.   
  
Since all our server pieces are TCP-based, another way of doing it is
to write a TCP proxy that is able to manage the delays, shutdowns and
errors, and to some extent simulate HTTP, LDAP or SQL specific issues
when it makes sense.   
  
I call this project **"Seism"**   
  
The front server that is being tested can run one proxy per back-end
and be configured to use them with no extra work.   
  
One important feature is to log the behavior of the infrastructure when
a perturbation happens, to see if the application behaves as expected.   
  
One idea to perform this is to create yet another specialized proxy in
front of the application to be tested to record what happens when a
perturbation is simulated. The* "back proxy"* can send a signal to the
*"front proxy"*, describing what kind of perturbation it just did, and
the front proxy can record how the application reacted by logging the
response it sent (or the lack of response if the app dies).   
  
The final log will tell us how the app is behaving depending on the
perturbations. One nice feature would be a dashboard to display this.
e.g. all green if the client receives 503s and 200s, red if it receives
a 500 etc.   
  
The behavior logger should also log the next N requests to check that
the server is behaving normally after the perturbation. It can also log
the CPU and Memory to check for stability.   
  
I think this can be really useful to bullet-proof automatically every
Server application we're building, in cunjunction with Hudson. A
continuous integration system can run in a hostile, Seism-enabled
infrastructure, and report failures.   
### Docs & Templates

  
Another thing I've been doing is starting to build a "Developer Guide"
for the server-side, that would make it easy for people to get started
in building server applications that are using our tools and
environment.   
  
We have this awesome tool in the Python community called [Sphinx][].
It's used to document Python itself, but also tons of projects out
there. It's based on a light text format ([reStructuredText][]) and
allow you to treat documents like code. In other words, everything you
write is pushed in a repository, has an history, patches etc.. And
Sphinx is able to generate a static HTML site out of it or a PDF.   
  
So, the dev guide code is here:
[http://hg.mozilla.org/services/server-devguide/][] and an HMTL
rendering, update hourly, lives here: [http://sync.ziade.org/doc/][]   
  
It's an early draft, full of *TODO* and *XXX*. But you get the idea: I
am trying to document everything a developer that wants to work with our
code should know.   
  
And one important thing I have started there is to build [Applications
Templates][], so people that want to build a new app on the top of our
tools, an app that follows our standards, can get started in seconds.   
### What's planned

  
So, the focus in the upcoming weeks for me is to make sure the Python
Sync server gets into production, and second level tasks include writing
more doc and polishing our server-side tools.

  [this post]: http://tarekziade.wordpress.com/2010/11/30/rsync-mozillaservices-community-week-47/
  [Easy Setup protocol]: https://wiki.mozilla.org/Services/Sync/SyncKey/J-PAKE
  [Netflix Chaos Monkey]: http://techblog.netflix.com/2010/12/5-lessons-weve-learned-using-aws.html
  [Sphinx]: http://sphinx.pocoo.org/
  [reStructuredText]: http://sphinx.pocoo.org/rest.html
  [http://hg.mozilla.org/services/server-devguide/]: http://hg.mozilla.org/services/server-devguide/
  [http://sync.ziade.org/doc/]: http://sync.ziade.org/doc/
  [Applications Templates]: http://sync.ziade.org/doc/code.html#paster-template
