Pycon WebDev Summit Report - Python Application Packages
########################################################

:date: 2012-03-10 08:00
:tags: python, mozilla
:category: python
:author: Tarek Ziade

.. image:: http://awesomeness.openphoto.me/custom/201203/1331302621-pyweb5_600x950.jpg

We had a web summit at Pycon last Thursday and a few discussions next on
that **Python application package** idea. I had conversations myself with 
a bunch of different people, trying to understand what they were at
and what were their goal in this.

If you want to know what it is all about, read Ian blog's here:
http://blog.ianbicking.org/2012/02/29/python-application-package

He describes one possible solution to create *Python application packages*.

The final goal is to be able to make it easier for cloud providers to run 
our apps. I should mention that they don't really have an issue here, they
already run Python apps (Mozilla too ;)).  But they use their own standards
-- so  the idea is to see if a common standard is possible.

During the summit, and right after, I suggested we would work together on 
defining what we wanted to achieve
and to start a draft of a standard in a PEP during the Pycon sprint.

It's interesting to see how saying the word *PEP* can scare some people out
by the way. When related to packaging, that word induce to some people 
things like *long process*,  *consensus hard to achieve*, 
*fights on mailing list* and so on. Some people want to solve their problems
**right now**, which is awesome, but...

But if their ambition is to see their solution
adopted by the community at large, they might fall into the trap we went in 
with **setuptools** a few years ago, which is to create and push a new
de-facto standard on the top of an existing, official standard in a way
that creates chaos in the packaging eco-system -- because of two competing 
standards. So while it's great to build tools, I think that kind of
standard should be discussed together from the beginning to see where are 
the common grounds.

So I would like to step back a little bit and clarify a few things:

1. **A Standard is not an implementation** -- and this is in particular important
   when we're thinking about building something to describe a Python application
   standard -- so let's drop any bit of code for now imo.

2. **Solving this problem is not specific to a Web application** -- defining 
   a Python application *that can be launched* is not specific to a web app.
   In fact, as Kenneth put it, we're talking about defining a *service* here.

3. **A deployment format is not a standard** -- I think some people were 
   confusing formats and standards. We were talking about how Java WAR files were cool 
   because you could just deploy that file and have the server *run it*, like the
   Python eggs a few years ago I guess.

4. **This standard is not here to compete with other packaging system** -- whathever
   we build should not be a way to "avoid having to deal with system libraries".
   It should be possible to deploy an application using virtualenv and a local directory,
   but again, this is orthogonal to having a standard. As a RPM packager I want to 
   be able to deploy your *service* in my own fashion, and that standard should help me too.

5. **A Python web app is also a Python package** -- this is important to note because a 
   package already has metadata information see PEP 345 - 
   http://www.python.org/dev/peps/pep-0345. And in fact, many things I see in Ian
   proposal are already solved by that PEP.

Based on these remarks, I would like during the sprint to work in two directions:

- thinking about extending to PEP 345 to introduce fields specific to the notion
  of *running a service* and describe how it would look like in 
  packaging/distutils2's *setup.cfg*

- thinking about how to introduce this standard in the existing eco-system for
  people to use immediatly on existing projects.


So far my thinking is that we should provide a field called **Application** that 
points a script to run an application -- like what you would point with the **script**
option in distutils or in distribute/setuptools **console entry point**.

I am not sure yet about the environment and the config files.

Next episode during the sprints !
