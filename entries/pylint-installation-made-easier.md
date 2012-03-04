Title: Pylint installation made easier 
Date: 2008-02-20 17:12
Category: plone, python, quality, zope

**EDIT: logilab.pylininstaller is now deprecated, since Logilab made
Pylint easy\_installable now.**   
  
**So, just call : easy\_install pylint.**   
  
I love [Pylint][].   
  
Correctly configured, it is really useful to raise your code quality.
But it can be really painful to install if you are not under a
Debian-like or OpenSuse-like system, because of its dependencies that
are not namespaced packages (logilab-common and logilab-astng).   
  
In other words, don't try to easy\_install the packages that are on
PyPI, it will not work.   
  
That's why I have created an egg, called [logilab.pylintinstaller][],
that will let you install it as easy as:   
   $  easy_install logilab.pylintinstaller

  
It bundles all dependencies and grabs pylint 0.14, then installs
everything.   
  
Thanks to Sylvain Thénault from Logilab for his help on this.

  [Pylint]: http://www.logilab.org/project/name/pylint
  [logilab.pylintinstaller]: http://pypi.python.org/pypi/logilab.pylintinstaller
