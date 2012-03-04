Title: Buildout: plone.org and pypi.python.org are acting like SPOF
Date: 2008-01-30 09:20
Category: plone, python, windows, zope

Yesterday, plone.org was moved on another server. It was an horrible day
for our people here that didn't have a local cache of eggs to build
their instances. So plone.org was acting like a Single Point Of
Failure(SPOF) for some packages.   
  
A few developers, that are under windows, were even having permission
denied errors on their buildout because when a package is badly
downloaded is not correctly crushed before a new attempt (I need to add
a ticket about this in setuptools tracker I guess).   
  
Anyway, we decided to create a mirror here, (I am buiding it at
http://release.ingeniweb.com/ this morning hopefully) to avoid such
problems.   
  
This makes me think that zc.buildout should introduce a high-level
mirror mechanism in the find-links variable, that would let someone
explicitely provide a list of mirror. It could look like this:   

    find-links =

      http://pypi.python.org/simple |  http://release.ingeniweb.com/pypi-mirror

      http://dist.plone.org |  http://release.ingeniweb.com/plone-dist-mirror

  
It could be used to switch the find-links values sent to setuptools
when the primary url is down by attempting a simple call with a timeout.
