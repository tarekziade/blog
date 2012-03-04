Title: distutils: multiple servers in .pypirc 
Date: 2008-01-17 11:06
Category: plone, python, zope

Since I am working on PloneSoftwareCenter to make it PyPI-compatible, I
have worked on distutils side to make the *register* and *upload*
command more friendly when an egg has to be registered to several
servers.   
  
The problem with the actual .pypirc file is that it won't let you
define many username/password for many servers: it is dedicated for one
server. In the meantime, you can specify in a command line option which
server you want to deal with:   
   $ python setup.py register -r http://my.server/pypi

  
But this will take the username/password in .pypirc. So if your
username differs from one server to another, it won't work.   
  
I have worked on an enhanced version for this, described here:
[http://wiki.python.org/moin/EnhancedPyPI][]   
  
The patch is ready, and comes with new unit tests *register* and
*upload* commands didn't have yet. The new .pypirc format was shaped
with the help and feedback of catalog-sig people, thanks to Martin v.
Loewis and Fred Drake and others. I am going to submit it for inclusion
today. If it is accepted and integrated we will be able to deal with our
eggs like this:   
   $ python setup.py register sdist upload    # goes to PyPI

  
   $ python setup.py register sdist upload -r plone.org   # goes to plone.org ;)

  
The next step is to provide a patch for a permissive trove classifier
in PyPI. Then all PyPI-like servers will be able to provide the same
service for egg developers, no matter how they deal with classifiers.

  [http://wiki.python.org/moin/EnhancedPyPI]: http://wiki.python.org/moin/EnhancedPyPI
