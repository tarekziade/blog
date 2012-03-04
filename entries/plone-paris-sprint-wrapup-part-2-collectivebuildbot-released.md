Title: Plone Paris Sprint wrapup, part #2: collective.buildbot released !
Date: 2008-05-02 09:24
Category: plone, python, quality, sprint, zope

The [Pimp my Buildbot][] project that was started here at Ingeniweb some
time ago, to be able to set up a buildbot in a matter of minutes with
zc.buildout, was continued during the sprint, and the guys did a great
job on it.   
  
It will be used here in customer projects with a Paster that adds
buildbot support when a project starts, because it is a waste of time
for the developers to set everything everytime.   
  
Jean-Francois Roche, Kai Lautaportti and Gael Pasgrimaud added
extensive configuration options (mail, scheduling), and made the SVN
Poller works. This feature allows for instance to make the buildbot
watch a SVN repository without having to add a hook in the server
(post-commit hook for instance), when you don't own it (SourceForge,
collective, etc)   
  
The tool is released in the [collective][], and available at the
[Cheeseshop][] in one single package !   
  
If you want to set a buildbot   
-   provide for each one of your project a buildout that has a test
    script
-   make sure the test script returns exit code (--with-exit-status with
    zope.testing)
-   create a buildout cfg file using collective.buildbot
-   run buildout, that's it !
-   run the master, slaves scripts, and go to the /waterfall page

  
Just try out our own [buildbot][] by running this sequence:   
   $ cd /tmp/

    $ mkdir my_bot

    $ cd my_bot/

    $ svn co https://ingeniweb.svn.sourceforge.net/svnroot/ingeniweb/buildbot/trunk .

    $ python bootstrap.py

    $ bin/buildout

    $ bin/master start

    $ bin/linux_debian start   (that's our slave)

  
You should have a buildbot running then at
http://localhost:9000/waterfall   
  
The tool, without the polling stuff, also works with Mercurial and Bzr,
but probably needs more tests with these repositories. We also need to
make sure the slaves works fine under Windows, and add a nice front page
to the buildbot.   
  
If you use it let us know !

  [Pimp my Buildbot]: http://tarekziade.wordpress.com/2008/04/01/pimp-my-buildbot/
  [collective]: http://svn.plone.org/svn/collective/collective.buildbot/trunk/
  [Cheeseshop]: http://pypi.python.org/pypi/collective.buildbot
  [buildbot]: http://buildbot.ingeniweb.com/waterfall
