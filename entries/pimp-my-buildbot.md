Title: Pimp my buildbot !
Date: 2008-04-01 12:00
Category: plone, python, quality, sprint, zope

**Edit : this post is a bit deprecated, the project is now called
collective.buildbot. See:
[http://pypi.python.org/pypi/collective.buildbot][]**   
  
When a project team use Test-Driven Development to build the code
(everyone should), the next step is to set up automate builds, as
explained in [continous integration][].   
  
This is where [Buildbot][] is great. It is easy and flexible to
install, even more since [Twisted][] has been eggified. A few
easy\_install steps are now sufficient to create a buildbot waterfall.
Configuring a buildbot requires writing a few Python scripts though, and
this has to be done everytime a project starts.   
  
In my work, I need to be able to set buildbots in a matter of minutes,
and they are always similar. They just need a buildmaster, a buildslave,
and a few rules.   
  
A first attempt to make things easier is to write a [Python Paste][]
script that generates default files. This is not very flexible though,
as upgrades are still a bit tedious.   
  
A more interesting solution is to provide [zc.buildout][] recipes that
take care of buildmaster and buildslave generation, through a very
simple configuration file.   
  
We have started this project, in order to be able to launch buildbot
within a buildout.   
  
The project has three parts:   
-   [**iw.buildbot**:][] a thin layer on the top of Buildbot that allows
    to drive it with configuration files, instead of Python code. In
    other words, it makes buildbot configuration based on declarative
    configuration file and dynamic Python code, instead of declarative
    Python code.
-   [**iw.recipe.buildmaster**][]: a zc.buildout recipe that creates a
    buildbot instance together with configuration files.

  
-   [**iw.recipe.buildslave**][]: a zc.buildout recipe that creates a
    buildslave

  
The result is that creating a buildbot is done in a few lines in the
buildout.cfg file:   
   [buildout]

    parts =

      buildmaster

      linux_debian



    [buildmaster]

    recipe = iw.recipe.buildmaster

    project-name = Ingeniweb Public buildbot

    project-url = http://ingeniweb.com

    port = 8999

    wport = 9000

    url = http://buildbot.ingeniweb.com

    slaves =

      linux_debian    xxxxx

    projects =

      iw.recipes 



    [linux_debian]

    recipe = iw.recipe.buildslave

    host = localhost

    port = ${buildmaster:port}

    password = xxxx 



    [iw.recipes]

    slave-name=linux_debian

    base-url=http://ingeniweb.svn.sourceforge.net

    repository=/svnroot/ingeniweb/projects/iw.recipes/

    branch=buildout

    build-sequence =

        python bootstrap.py

        bin/buildout 



    test-sequence =

        bin/test -v --exit-with-status

  
-   **buildmaster** defines the project name and url, the buildbot web
    port, slave port and url, and a list of slaves and projects.
-   each project has his own section, where the Subversion path is
    defined, as well as the build sequence and the test sequence.
-   each slave is defined in its section

  
From there other buildouts can be created to group packages to be
tested, and to define a script that can be used for tests. For Zope
applications, that would be *zopectl* of course, as long as it is used
with *--exit-with-status*.   
  
This is the case for [iw.recipes][]: it grabs all iw.recipes.\* eggs to
hook them to a testrunner.   
  
The result can be see here: [http://buildbot.ingeniweb.com][]   
  
The next steps are to make sure everything works fine under Windows,
and see how things goes in various projects, then make it work with all
kinds of VCS and schedulers.   
  
I will probably propose a sprint task on this in [Paris sprint][] and
see if the package meets interest.

  [http://pypi.python.org/pypi/collective.buildbot]: http://pypi.python.org/pypi/collective.buildbot
  [continous integration]: http://en.wikipedia.org/wiki/Continuous_integration
  [Buildbot]: http://buildbot.net/trac
  [Twisted]: http://twistedmatrix.com/trac/
  [Python Paste]: http://pythonpaste.org/
  [zc.buildout]: http://pypi.python.org/pypi/zc.buildout
  [**iw.buildbot**:]: https://ingeniweb.svn.sourceforge.net/svnroot/ingeniweb/iw.buildbot/trunk/
  [**iw.recipe.buildmaster**]: https://ingeniweb.svn.sourceforge.net/svnroot/ingeniweb/iw.recipe.buildmaster/trunk/
  [**iw.recipe.buildslave**]: https://ingeniweb.svn.sourceforge.net/svnroot/ingeniweb/iw.recipe.buildbslave/trunk/
  [iw.recipes]: https://ingeniweb.svn.sourceforge.net/svnroot/ingeniweb/projects/iw.recipes/buildout/buildout.cfg
  [http://buildbot.ingeniweb.com]: http://buildbot.ingeniweb.com/
  [Paris sprint]: http://www.openplans.org/projects/plone-3-paris-sprint/project-home
