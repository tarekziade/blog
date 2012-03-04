Title: How to add rotatezlogs in your buildout
Date: 2008-03-02 20:43
Category: plone, python, zope

[iw.rotatezlogs][] is a very useful package made by Gilles Lenfant to
rotate log file in Zope. This is quite useful to make sure they don't
get huge.   
  
I have made the necessary changes in [plone.recipe.zope2instance][] and
[plone.recipe.zope2zeoserver][] to make it available in a buildout
environment. Since those changes are now released, here's the way to add
the log rotator in your buildout if you wish to use it:   
   [buildout]



    ...



    [instance]



    ...



    event-log-custom =

        %import iw.rotatezlogs

        <rotatelogfile>

            path ${buildout:folder}/var/log/event.log

            max-bytes 1MB

            backup-count 5

        </rotatelogfile>



    access-log-custom =

        %import iw.rotatezlogs

        <rotatelogfile>

            path ${buildout:folder}/var/log/instance-Z2.log

            max-bytes 1MB

            backup-count 5

        </rotatelogfile>



    eggs =

        ...

        iw.rotatezlogs



    [zeo]



    ...



    zeo-log-custom =

        %import iw.rotatezlogs

        <rotatelogfile>

            path ${buildout:folder}/var/log/zeoserver.log

            max-bytes 1MB

            backup-count 5

        </rotatelogfile>



    eggs =

        ...

        iw.rotatezlogs

  
The package is added in the eggs section to make sure the recipes adds
it in the Python path when the script (zope or zeo) is loaded.   
  
Gilles told us that the rotator will be integrated in ZConfig itself
sometimes, so it will be even simpler to use.

  [iw.rotatezlogs]: http://pypi.python.org/pypi/iw.rotatezlogs
  [plone.recipe.zope2instance]: http://pypi.python.org/pypi/plone.recipe.zope2instance/
  [plone.recipe.zope2zeoserver]: http://pypi.python.org/pypi/plone.recipe.zope2zeoserver/
