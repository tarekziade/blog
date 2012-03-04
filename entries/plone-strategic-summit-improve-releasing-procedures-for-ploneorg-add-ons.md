Title: Plone Strategic Summit: Improve releasing procedures for plone.org add-ons
Date: 2008-02-13 17:51
Category: plone, python, zope

I have been suggested as a "champion" at the Plone Strategic Summit on
this task:   
  
*\# Improve release procedures for add-ons on plone.org: document a
release process, and create release tools for packaging and uploading
products from the command line.*   
  
This is great, because I have been working a lot in this area in the
past month and I think I have a precise idea on what should be done in
the Plone community to improve add-ons products visibility and releasing
process. I am going to expose here the steps I think we should take, and
how to do them, so people can give some feedbacks. Most of them were
already explained on this blog on several entries.   
### PyPI vs Plone.org

  
The Cheeseshop (PyPI) is now playing an important role in Plone
development. Everytime a Plone 3 application is built somewhere in the
world, the Cheeseshop is serving hundreds of tarballs and eggs. Since
Zope and Plone has been eggified, and since zc.buildout has been used as
the standard way to build a Plone application, Plone developers are
releasing all their eggs at PyPI.   
  
This releasing process is really convenient, as a package can be
uploaded, and shout out in just one command:   
   $ python setup.py register sdist bdist_egg upload

  
And an alias can make it even simpler:   
   $ python setup.py release

  
The problem is that many Plone.org add-on products pages that used to
be up-to-date are not upgraded anymore. So Basically, Plone.org Software
Center is dying because of the actual releasing process of eggs..   
#### The SPOF problem

  
Another issue with the PyPI-centralized development process is that it
becomes a Single Point of Failure. In other words, if PyPI is down, all
the buildouts out there are stocked, unless you have a up-to date egg
cache on your side.   
  
PyPI though, together with distutils, was thaught as a distributed
system: you can theorically call register and upload commands to any
server that implements the PyPI Apis. But there are no other PyPI-like
server yet in the community. The PyPI code is open source for sure, and
anyone could take it and run his own PyPI...   
#### PloneSoftwareCenter features

  
Another risk we have with a PyPI-centric approach is loosing the
features that PSC provides at Plone.org. Those are great, and should be
used by all add-ons out there. Milestones, bug tracker, etc.. Everything
is provided at plone.org for someone to promote and work with his
product.   
#### The solution we should take

  
To avoid the problems mentioned, we need to:   
-   make PloneSoftwareCenter, therefore Plone.org, PyPI-compatible
-   make distutils command-line tools able to interact with several
    PyPI-compatible servers, besides the official one
-   provide a simple guideline for the Plone community to work with
    these tools

  
#### The steps

  
##### PSC

  
Sidnei has created 2 years ago a branch for PSC with an experimental
PyPI support. I have taken this work and continued it on a branch that
is almost finished. My goal is to finish it at [the Paris Sprint][], so
PSC will be fully PyPI-compliant. I will soon blog on this to describe
the work.   
##### .pypirc and distutils

  
In order to be able to interact with several PyPI-like server, the
.pypirc file need to evolve. I made a patch and a proposal (see:
[http://wiki.python.org/moin/EnhancedPyPI][]) I will try to push in the
next Python Bug Day in two weeks, so it is integrated in Python 2.6. If
it is accepted, I will release a library that implements the same patch,
but for Python 2.4 and 2.5, through specific setuptools commands.   
##### guideline

  
From there, I guess a guideline can be written, explaining :   
-   how to create a Plone 3 package (through skeletons)
-   how to release it to both PyPI and plone.org

  
Another point of interest will be to explain how to deal with several
egg servers in a buildout.   
#### Proposed calendar

  
-   *Mid-March* : provide a package to handle the new .pypirc format
-   *End of March* : submit the guideline, based on the PSC current
    branch, and a public instance of the new PSC so people can try it.
-   *End of April *: finalize PSC PyPI support at the Paris Sprint,
    together with Alex Clark, so it is available to Plone.org when it
    goes Plone 3
-   After that: submit a guideline on how Plone companies can use PSC to
    create a private PSC, and work together with PyPI, plone.org and
    their own PSC, in a buildout environment

  
I have also proposed an OSCON topic on this, in Portland, in July. So
if my talk is accepted, this can be a good place to promote Plone.org's
Plone Software Center.

  [the Paris Sprint]: http://www.openplans.org/projects/plone-3-paris-sprint/project-home
  [http://wiki.python.org/moin/EnhancedPyPI]: http://wiki.python.org/moin/EnhancedPyPI
