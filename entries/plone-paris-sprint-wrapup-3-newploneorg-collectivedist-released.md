Title: Plone Paris Sprint wrapup #3, new.plone.org, collective.dist released !
Date: 2008-05-06 12:49
Category: plone, python, sprint, zope

The main task I worked on during the sprint with Alex and Matthew was
making PloneSoftwareCenter ready for the new version of Plone.org. These
guys rock. We did tons of things and the new plone.org website is coming
up. Alex worked for quite a while on migrating plone.org to plone 3, but
let me focus on the software center part.   
  
First of all, let me explain what is the final goal of the work done in
the software center.   
### The future of Plonistas: a 100 % egg-based world and what is means
for production

  
Since a few years, Zope code base was moved into a set of namespaced
packages. Plone is following closely. From there zc.buildout is
providing a simple way to pick up the right set of packages to build an
application. This set is automatically chosen by recipes at Zope and
Plone level. Then developers add their own packages and dependencies to
provide custom features in their applications.   
  
This mechanism means that each team has to:   
-   make distributions of packages (tarball, eggs, ..)
-   build the application with buildout, then release a source
    distribution
-   and provide a way for other developers to build the application on
    their own, by:   
   -   publishing the buildout configuration files
    -   pushing the packages the buildout uses into to a server that is
        reachable by developers
    -   make sure Plone and Zope packages are also reachable

      

  
This means that each team is responsible at least to release packages.
  
#### Distutils and Cheeseshop

  
Distutils provides two commands to publish packages to the world:
**register** and **upload**. These commands were intended to provide to
the developer a way to push packages to any server that supports the
protocol, by using the *--repository* option.   
  
But in reality, the only server that is publicly available is the
Cheeseshop ([pypi.python.org][]). Furthermore Distutils is not providing
everything needed to work with another server than the Cheeseshop, like
I will explain later in this post. So all Plone and Zope packages are
uploaded there.   
  
Therefore, pypi.python.org became a single point of failure when you
need to build a Plone or Zope application. With the growth of the
community, this means that the repository will get bigger and have to
deal with more and more request. PyPI weight around 4 gigas at this
time, of zip files and tarballs.   
  
While the actual server is really fast, it makes it a bit hard to work
when it is down. It didn't happen often. Twice as far as I remember. But
when it happens, the crowd that uses zc.buildout is frozen because they
run buildouts several time per day. They can use cache of course, as
long as those are up-to-date.   
  
Some mirrors emerged, like
[http://release.ingeniweb.com/pypi.python.org-mirror][]. Some enhanced
indexes were created as well, like [http://download.zope.org/simple][],
which is still referring to pypi.python.org but performs a bit of
crawling to speed things up when a buildout uses it through
easy\_install.   
  
But all of these are just enhancement to a cheeseshop-centric model.   
  
Furthermore, in case of a private application, **you do not want to see
packages in the Cheeseshop but you might also want to provide developers
a similar way to manage and use them.**   
#### Plone.org software center is dying !

  
For public applications, given the fact that Distutils provides a
simple way to push a package to a public location (one shell command),
people have started to stop updating the [*Products*][] section of
Plone.org. This happens because updating it means doing a whole lot more
than the simple register+upload call. You need to login into the
website, then manually upload the packages, then change the front page
of the product if needed etc..   
  
So being able to push packages to plone.org with the same set of
commands, is the right solution for developers.   
  
Pushing a package means uploading a public archive but it also means
updating the front page for the given package, with the register
command.   
  
That what I worked on, at PloneSoftwareCenter level, continuing
Sidnei's work: making it act like Cheeseshop. Now the feature is ready
and being alpha-tested at [new.plone.org][]   
#### Toward a distributed model

  
![Playing with several egg-based servers][]   
  
What we will be able to do from there, is to distribute packages (in
blue) to the Cheeseshop (2) as usual, but also to Plone.org (1). Having
such a tool also allows people to run other cheeseshop-like servers,
wether they are public (3) or private (4). This is useful when you are
working on customer projects and do not wish to make their packages
available to the world, or even if it is a public project, you do not
want to push them to PyPi.   
  
Furthermore, it allows having a bit of redundancy : your packages
become available in several places, which is better. Think about the
mirrors at Sourceforge, same thing here...   
  
This distributed model is used at Ingeniweb, and in other companies I
am starting to list (If you do please let me know, this is important to
promote the tool).   
### The new Plone Software Center (PSC)

  
If you are extensively working with packages and buildouts, you should
consider trying the new PSC, read
[http://tarekziade.wordpress.com/2008/03/20/how-to-run-your-own-private-pypi-cheeseshop-server/][]
for this. Each project now in the software center can hold several eggs,
and it makes it possible to provide a nice deployment model for your
teams: developer push packages releases in such a server **with the
distutils standards**, while customers or deployers can build their
applications by picking them up through their buildouts.   
  
And it is in Plone, so you can provide extensive features, like a bug
tracker, and all the sweet things Plonecan provide.   
  
The work left to be done in PSC is :   
-   making the storage for archives (tgz, egg) pluggable so new storing
    strategies can be provided in separate packages, under the
    collective.psc namespace, I started this work in a branch.
-   finish the collective.psc.mirroring package, that will be used in
    plone.org to fill a system folder, in order to provide an Apache
    direct view over the archives stored. This will make zc.buildout /
    easy\_install use this stream rather than hitting the Plone
    instance. Although the final goal will be to transform it into a
    storage strategy, but time is running and this is useful **now** for
    plone.org.
-   extensive tests on new.plone.org

  
### collective.dist

  
To be able to deal with several servers, I have released
[collective.dist][] after the sprint (previously iw.dist). This package
provides two new distutils commands: **mupload** and **mregister**,
together with a new **pypirc** format.   
  
Follow the documentation, and you will be set in a matter of minutes.
This package is already used by many developers to make their life
easier, and will help you when the new plone.org goes live.   
### disutils evolution

  
collective.dist is an evolution of distutils I have been working at
Python level for months. It is available as a Python patch here :
[http://bugs.python.org/issue1858][]. mregister and mupload are just
modified register and upload commands that makes it possible to interact
with several PyPi-like servers, that's it. PSC uses Distutils standards
in any case, so it is possible to use the regular register and upload
commands with it of course. It is just not convenient because you will
need to have the same username and password on both CheeseShop and the
third-party egg server (or change your pypirc file everytime :D)   
  
So the patch, basically, just makes the -r option of distutils commands
a 100% operational.   
  
Now my job is to convince Python core developers it should be
integrated into Python 2.6, and I am working on this. It is a logical
evolution, but it sounds overkill to some people that does not have this
kind of need: "Why changing that ? we have only one package server,
which is the cheeseshop".   
  
It can also sound to some of them like I am (together with the team of
20 developers we have ;) ) the only person on earth that wishes it, but
as soon as the new Plone.org will be online, a lot of people will start
needing such a feature. But having it in 2.6 will make it available as a
standard in Plone/Zope world in... a few years.   
  
In any case, most of them agree in the fact that this change is logical
and that the current pypirc format is not to be kept. So I guess it is
just a matter of time and patience.

  [pypi.python.org]: http://pypi.python.org
  [http://release.ingeniweb.com/pypi.python.org-mirror]: http://release.ingeniweb.com/pypi.python.org-mirror
  [http://download.zope.org/simple]: http://download.zope.org/simple
  [*Products*]: http://plone.org/products
  [new.plone.org]: http://www.aclark.net/Members/aclark/plone-org-upgrade-update
  [Playing with several egg-based servers]: http://tarekziade.files.wordpress.com/2008/05/collective-dist.png
  [http://tarekziade.wordpress.com/2008/03/20/how-to-run-your-own-private-pypi-cheeseshop-server/]:
    http://tarekziade.wordpress.com/2008/03/20/how-to-run-your-own-private-pypi-cheeseshop-server/
  [collective.dist]: http://pypi.python.org/pypi/collective.dist
  [http://bugs.python.org/issue1858]: http://bugs.python.org/issue1858
