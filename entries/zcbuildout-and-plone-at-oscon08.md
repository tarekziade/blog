Title: zc.buildout and Plone at OSCON&#039;08
Date: 2008-03-21 18:51
Category: plone, python, zope

Cool, my proposal for [OSCON 2008][] has been accepted, and will be
about Plone 3, zc.buildout and the work on creating private PyPI servers
using PloneSoftwareCenter.   
  
It will present how we work at Ingeniweb with both public and private
packages, to deliver Plone applications to customers, using eggs and
buildout.   
  
It's funny because since a few days, there are a lot of discussions
around distutils, PyPI and setuptools, and about making things better at
Python level on how to distribute packages and applications. So it seems
to be a hot topic.   
  
From my point of view, PyPI brought a lot in the past years in this
area, and being able to deploy a pypi-compatible software center in a
company helps a lot in using the same set of command line tool.
(distutils/setuptools)   
  
So, I am pretty happy nowadays with zc.buildout and setuptools (thanks
to Mr Fulton, Eby and al), despite all the critical that has been made
about setuptools in the last few days, and despite the fact that it is
\*so hard\* to make a tiny little change make it to distutils trunk :'(
...   
  
Anyways, if you do Plone or Zope dev, and if you are interested about
software delivery, I'd be glad to exchange about it, to see how you work
and deliver Zope apps, to get other point of views before OSCON.   
  
Here's the abstract of my talk:   
Software delivery for complex systems in Python/Zope used to be a little
bit homemade: people usually used custom scripts to deploy their
systems, or relied on generic installation tools. For Plone
applications, most of the time a complex installation guide was provided
to the customer, with a list of dependencies to install and system
changes to take care of.
  
  
The Python Package Index (PyPI), formerly the **Cheeseshop**, brought a
few years ago a new way to distribute Python applications, together with
**setuptools**. It made it possible to install a Python library the same
way package systems like *apt* or *yum* does. From there people started
to deliver their software in separated components, called **eggs**.
Since most applications in Plone are now egg-based, it is possible to
install a software with a list of eggs.
  
  
  
zc.buildout provides a descriptive language to list all eggs needed for
a software to run and a plugin system that allows to customize each
steps.This talk will present a case study of a Plone application life
cycle:
  
  
-   environment building - creating the buildout and its recipes
-   continuous integration with buildbot – running the buildout on
    target systems
-   deploying – preparing and packaging the buildout for an offline
    installation
-   updating – preparing and releasing an update

  
And will present a set of extra tool we have built on the top of
zc.buildout to standardize our projects developments and help the
developers:   
-   a set of templates to start a buildout-based project in subversion
-   a tool to create buildbot slaves automatically, given a buildout
-   a diff tool to ease the upgrade of a buildout that is in production.

  

  [OSCON 2008]: http://en.oreilly.com/oscon2008/public/content/home
