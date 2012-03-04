Title: Mozilla Services - Year 1 !
Date: 2011-06-21 16:13
Category: mozilla, python

What’s this ? read [this post][].   
### What happened

  
Time flies... This is a special entry because today it's been exactly
one year since I've joined Mozilla. So I'll try to summarize what I've
done during the past year, what worked well, what needs more work.   
  
I was the first *"Python guy"* hired in the Services team. Since the
plan was (and still is) to do all future server-side work in Python,
this gave me the opportunity to set up the basis for our eco-system.
Since then, more Python devs have joined the team and others have gained
some experience in the language, and we're now all Python guys ;)   
  
I** created a micro-framework** for all our server-side applications.
It's a thin layer on the top of WebOb + Routes, with some specific
features we need (like a hearbeat page for all our apps). Nothing fancy
but it makes it easy for someone to start a Server application sharing a
common standard.   
  
I** re-wrote all the PHP code** that is needed to run a Sync server
(Registration + Storage) in Python, using the micro-framework. This was
done months ago, and both the core and the apps have evolved since then,
following the changes that were made in the PHP parts. Pushing the work
in production was the hardest part because it supposes a lot of
coordination between Devs and Ops. And Ops had zillions of stuff to do
for the Firefox 4 launch, so we missed that launch. Since then, the
Registration part was pushed, and we're about to push the Storage part.
  
  
I wrote the **Easy Setup server**, that is used for example when you
set up your Android phone's Sync account by transferring your desktop
Sync profile. This was really fun because it was the first project I did
from scratch. I worked on the design with Phillip and Stefan and I
really enjoyed it. A small, fun and interesting project.   
  
I added a **IP blacklisting middleware** into the Easy Setup server,
that rejects calls from an IP if it has done too many attempts in a
short time window. This work led to a new project that is currently
under development by Ryan: a blacklisting server that can work across
several applications.   
  
I've set up a **documentation center** at
[http://docs.services.mozilla.com/][]that is built using Sphinx. The
sweet thing about it is that its content lives in a [Mercurial
repository][], so developers can change the documentation directly. The
goal of this website is to provide a single place for all our APIs
specifications, and our development guidelines, with a minimal overlap
with sites like MDN etc.   
  
I've created [pypi2rpm][] and we worked with Richard S. on deploying
our Python applications using it. The tool is built on the new packaging
tool I am working on for Python and let you create RPMs files for our
projects. It's a mix of a PyPI crawler, a version sorter and a RPM
creator. We've created a release process based on this:
[http://docs.services.mozilla.com/server-devguide/release.html][]   
  
I've set up a **Jenkins server** for our server projects. Can't link it
because it currently leaves in our intranet. The Jenkins server does the
following for every server application:   
-   builds it
-   runs its tests
-   build all its RPMs under Centos5 and Rhel6
-   Install all the RPMs under a Centos5 chroot and check that there's
    no dependency error

  
I've set up a **PyPI Mirror** in our intranet so Jenkins (or someone
creating RPMs) does not rely on any external resource.   
  
Also: we're having regular MoPy meetings now at Mozilla \\o/   
### What's next

  
During the next months we will do a lot of work in the Sync
application(s) to support new features and optimize existing ones. We'll
also start new projects.   
  
For the tooling/framework parts, here are a few paths where I'd like to
see us going.   
  
**Continuous load testing**: one goal I have is to make it possible for
anyone to run a load test on one of our applications via Jenkins, on a
given stage or dev server. Then see the results, compare them with some
previous runs etc. The second goal is to make load tests an easy thing
for developers to add early in a project. Writing load tests makes your
application faster, just because you focus on it, that's a fact.   
  
I've made good progress in this topic and some stuff are going to land
into Funkload itself to make it easier to automate load tests and
reports generation. The next task I have is to work with other teams
involved with Services, and make sure their use cases in this area are
provided by the tools.   
  
**A standard for our API specifications**. This is a personal project I
have, but it is directly inspired by our work at Services. I want to
reduce the path from a server API specification to its implementation.
For this [I am working on a DSL][] that can be used to describe some
APIs, produce their documentation and eventually, be used to run a
server. If my experiment goes well, I'll introduce it.   
  
**Cross-team code review**. Inspired by Jeff and some other people
during a MoPy meeting, I started to write a small web site that could be
used by a dev to ask for code reviews from people outside its team. The
idea is that the website tries to find automatically someone that has
the required skill to do the review. A review will cost you some credits
and by doing a review you'll earn some.   
### On working remotely

  
I am a big fan of remote working. I am doing it for years. It works
quite well within the Services team, and half of the team is doing it.
The one thing that's hard to manage is the timezones: I am the only guy
in Europe and I am 9 hours in front of Mountain View.   
  
This means that if I need to work & chat with my colleagues, I have to
do it on the evenings. Also, some events have to be scheduled on the PDT
timezone. For instance, production pushes are starting at midnight for
me. I had to adapt a bit my schedule for this, it was hard at first but
now it's working well.   
  
But... I would really love to see some more people in my team hired in
Europe, so I can speak with them on daytime.   
  
As a conclusion for year 1, I love my job at Mozilla. I'm working with
a lot of smart guys and we get things done, mostly because everyone in
this team is passionate. I a looking forward for year 2.

  [this post]: http://tarekziade.wordpress.com/2010/11/30/rsync-mozillaservices-community-week-47/
  [http://docs.services.mozilla.com/]: http://docs.services.mozilla.com/
  [Mercurial repository]: https://hg.mozilla.org/services/docs
  [pypi2rpm]: http://pypi.python.org/pypi/pypi2rpm
  [http://docs.services.mozilla.com/server-devguide/release.html]: http://docs.services.mozilla.com/server-devguide/release.html
  [I am working on a DSL]: https://tarekziade.wordpress.com/2011/06/17/anatomy-of-a-web-service-part-2-redbarrel/
