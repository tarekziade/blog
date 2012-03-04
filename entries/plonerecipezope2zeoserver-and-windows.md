Title: plone.recipe.zope2zeoserver and Windows
Date: 2008-02-21 09:27
Category: plone, python, zope

The [0.11][] release of plone.recipe.zope2zeoserver is out. If you are
under Windows you will probably enjoy this upgrade. The *zeoctl*
starting script was not working under win32 because it is based on
zdaemon, which is Linux-specific.   
  
I have added two scripts in the recipe, to be able to launch Zeo:   
-   at the command line, with bin\\zeo.bat
-   as a service, with bin\\zeoservice.exe install/start/stop/remove

  [0.11]: http://pypi.python.org/pypi/plone.recipe.zope2zeoserver/0.11
