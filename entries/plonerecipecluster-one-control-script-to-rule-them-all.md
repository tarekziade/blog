Title: plone.recipe.cluster, one control script to rule them all
Date: 2008-03-06 22:29
Category: plone, python, zope

There is something that is a bit missing in a buildout environment to be
able to drive it with no pain : a gobal script that allows starting,
stopping or restarting every software that is bundled in it.   
  
For instance, a buildout often has a Zeo server, a Zope instance and
some other servers like Pound, Apache or Squid (just control scripts and
sometimes a whole build. A global script can handle this by running a
suite of commands for each action: start, stop, restart.)   
  
Let's take an example: we want to run a Zeo server, a Zope client, and
a pound load balancer. These actions can be listed in a buildout section
like this:   

    [buildout] ...



    [cluster]



    recipe = plone.recipe.cluster

    poundctl = ${buildout:bin-directory}/pound -f ${buildout:directory}/parts/pound/etc/pound.cfg -c ${buildout:directory}/var/pound.pid



    start =

        ${buildout:bin-directory}/zeoserver start

        ${buildout:bin-directory}/instance start

        ${cluster:poundctl}



    stop =

        ${buildout:bin-directory}/zeoserver stop

        ${buildout:bin-directory}/instance stop

        pid:${buildout:directory}/var/pound.pid



    restart =

        ${buildout:bin-directory}/zeoserver restart

        ${buildout:bin-directory}/instance restart

        ${cluster:poundctl}

  
The zeoserver and instance scripts are daemons that just need to be
called, and the pound script which is also running as a daemon, do not
have any option to be stopped, but will let the user define a pid file.
So having a way to kill the pid defined by this file is enough in this
case.   
  
The recipe can therefore build a control script that launches the set
of commands for each action:   

    $ bin/cluster start

    Starting Cluster...

    $ bin/cluster stop

    Stopping cluster...

  
Let's take another example: a buildout that runs a simple script that
is not daemonized. In other words, it needs to be run in the background
and its pid saved, so the cluster recipe will know how to stop it:   

    [cluster]



    recipe = plone.recipe.cluster

    start =

        background:${buildout:directory}/bin/script

        ${buildout:bin-directory}/instance start



    stop =

        ${buildout:bin-directory}/instance stop



    restart =

        background:${buildout:directory}/bin/script

        ${buildout:bin-directory}/instance restart

  
In this case, the *background:* prefix will indicated the recipe to
execute the command in the background, and to keep its PID in a file.
When the stop command will be called, it will be stopped automatically.
  
  
I think that all cases are covered by this recipe, and I have a
prototype working for Linux/Mac here:   

[http://svn.plone.org/svn/collective/buildout/plone.recipe.cluster/trunk][]
. I took back and adapted some work done by Blue Dynamics
([bda.daemon][]). System programming is a bit over my head so it needs
some more work in the coming days, but it is working already.   
  
Then, the next step will be to make it win32 compliant, using NT
Services for this, and hopefully releasing a first 0.1.0 version.   
  
If you feel that there's some missing use cases, let me know ! (the
full README is [here][])

  [http://svn.plone.org/svn/collective/buildout/plone.recipe.cluster/trunk]:
    http://svn.plone.org/svn/collective/buildout/plone.recipe.cluster/trunk
  [bda.daemon]: http://svn.plone.org/svn/collective/bda.daemon/trunk/bda/daemon/
  [here]: http://svn.plone.org/svn/collective/buildout/plone.recipe.cluster/trunk/plone/recipe/cluster/README.txt
