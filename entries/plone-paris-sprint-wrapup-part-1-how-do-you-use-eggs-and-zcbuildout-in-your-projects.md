Title: Plone Paris Sprint wrapup, part #1: How do you use eggs and zc.buildout in your projects ? 
Date: 2008-04-29 13:02
Category: parissprint2008, plone, python, quality, sprint, zope

This is the first post of the wrapups I want to do about the sprint that
we had in Paris last week-end. We had a Bird of Feather about how people
use eggs and zc.buildout in their projects, how they release and deploy
them.   
  
There were some people from Headnet (Anton, Mustapha) and Infrae (Kit,
Sylvain) and Ingeniweb (Me), and we compared a bit how we are working
with eggs, zc.buildout etc.   
  
That is what I love in our community: companies can share their
knowledge and grow up all together, technically speaking.   
  
We all have internal recipes, command-line scripts, and are all
relatively happy with zc.buildout. This discussion was very instructive.
  
  
From there, I thaught it would be a good idea to launch a new project
in the community, on the top of zc.buildout (and maybe
zc.sourcerelease), that would provide a common set of tools and
deploying best practices, for people that works with the buildout, no
matter which framework they use (Silva, Plone, etc.)   
  
The first step for this project is to find the common needs and see if
we can join forces to build common tools. To start it up, I decided to
wrap up and release our internal set of tools into a single package
called [iw.releaser][] and publish it. This is the work I have done
during the last months with the help of Gael, to help our team to work
with zc.buildout in Plone Projects. It is Subversion dependent at this
time.   
  
I am expecting some feedback from Anton and Sylvain to see if we can
make it a collective tool.   
  
This package provides:   
-   a skeleton to build a project structure (buildout, packages; docs,
    etc.) so all projects have a standardized structure
-   a 'release' distutils command that releases a package, upload it to
    the Cheeseshop or other servers, and send a shout out mail
-   a set of command line tools, that can be used to deploy a buildout.
    These commands are doing many things besides launching a buildout
    building (which is a bit different from zc.sourcerelease)

  
This package is used at Ingeniweb for a few months now, and I tried to
summarize how it is used in the [docs][iw.releaser]. I bet a lot of bugs
will be found if you try it, so consider this package as a non-mature
package yet.   
  
Join us all ! So you will be able to release and deploy your
buildout-based apps with a few command-line calls, :D

  [iw.releaser]: http://pypi.python.org/pypi/iw.releaser/
