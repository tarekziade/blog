Title: Distutils state
Date: 2009-05-10 15:30
Category: distutils, python

Since Pycon, a lot of discussion and work has been going on.

  
During the summit, we made a few decisions (see
[http://mail.python.org/pipermail/python-dev/2009-March/087834.html][])
but this topic is **so wide and so complex** that a lot of discussion
still needs to be done to have a clear and complete picture of where we
want to go and how we are going to do it

  
But we have made significant progress and reached consensus on some key
points. This entry is a short list of these key points.

  
### Being able to compare project versions

  
If you take a look in Distutils code, there's a *version* and a
*versionpredicate* module that provides a way to compare versions. This
feature is barely used by Distutils itself, and a very few number of
projects out there are using it (If you do so, please let me know).

  
This is probably because Distutils provides two different ways to
compare versions: a "strict" one and a "loose" one. In other words
Distutils clearly states that it is unable to provide a unique version
comparison algorithm that can be used by anyone out there. Anyone means
here : Python developers, OS packagers, etc.

  
Setuptools did a better job by providing an algorithm that covers most
cases, but suffers from this universality: it's too heuristic.

  
So one of the main topic during Pycon was to try to find a version
comparison algorithm that would just work for everyone and in the
meantime would be strict enough to be useful. That's a pretty tough
task, but I think we have reached something that is "good enough" for
everybody. We had the chance to have people from Ubuntu, RedHat during
Pycon to work on this task, and Trent Mick took the lead during the
sprints to come up with a prototype.

  
It's described here :
[http://wiki.python.org/moin/Distutils/VersionComparison][] and I have
put the code here [http://bitbucket.org/tarek/distutilsversion][].

  
Two more things to take care of:

  
-   Philip Eby came up with an edge-case : being able to do a*
    development version of a post release*.
-   Jean-Paul Calderone proposed to add a constructor that would take
    explicit arguments to describe the version, rather than a string
    representation

  
There's a branch (tarek-postdev) on bitbucket to work on these two
cases. But basically, it seems that we have a consensus on a unique way
to compare versions in Python ! This is a great step forward.

  
Another point that* Toshio* Kuratomi raised during a hall discussion was
the fact that some Python developers are not having good practices when
versioning their releases. So we agreed that a good *"How to properly
use version numbers for your projects releases"* document will have to
be delivered in Distutils documentation, besides the new algorithm. I am
pretty confident that people will eventually follow it.

  
### APIs to access installed project metadata, and an egg-info standard

  
Once a project is installed in Python, you don't have a way to get its
metadata and to answer to basic questions like:

  
-   what are the installed packages ?
-   what is the version ?
-   how is the author ?

  
Of course you can dig in your installation and get back most of these,
but depending how you installed your package (manual, easy\_install,
pip) it might be located in different places.

  
So we agreed on a standard for this, described in PEP 376 :
[http://www.python.org/dev/peps/pep-0376][]

  
An API will be introduced to be able to get the info for a installed
package, as long as it was installed using PEP 376 standard.

  
### An uninstall feature !

  
A feature that is claimed for a long time now should be introduced in
Distutils : uninstallation !

  
Distutils will provide a basic, reference *uninstall* feature that will
remove all files that where previously installed for a project. This
will be doable as long as this list of files is recorded at installation
time, and not used by another project.

  
See the details in PEP 376.

  
### Standardize PKG-INFO

  
New fields will be added in the metadata of a project. The most
important one is** install\_requires** from setuptools, which let you
list the projects your project depend on and their versions.

  
This is for informational purpose, and Distutils will not provide an
install feature that will fetch and install dependencies. This can be
done by third-party tools like easy\_install as long as they use the
installation standard described earlier.

  
We started this work with Jim Fulton at Pycon, and Tres Seaver took the
lead on this task since then. The plan is to update PEP 345 . The work
is done in a branch here :
[http://svn.python.org/view/peps/branches/jim-update-345/pep-0345.txt?view=markup][]

  
But the remaining work is focusing on practical details. Just remember
that PKG-INFO will evolve and install\_requires will be integrated
amongst other changes.

  
### Distutils code cleanup, test coverage

  
The test coverage is starting to look good and most modules are covered
around 80%. I guess this is the average in most Test-Driven Development
projects out there. So Distutils is becoming a good citizen of the
standard library ;)

  
The remaining work for a good test coverage is mostly on compilers side
and os specific commands.

  
My black list of untested (or nearly untested) modules :

  
-   bcppcompiler
-   cygwinccompiler
-   emxccompiler
-   msvc9compiler
-   msvccompiler
-   command.bdist\_msi
-   command.bdist\_rpm

  
I need to figure out how to properly test them. Last, I need to set up a
buildbot that will try out Distutils trunk on a list of projects out
there, like numpy for example.

  
### Other topics

  
Check this ! [http://wiki.python.org/moin/Distutils][]

  

  [http://mail.python.org/pipermail/python-dev/2009-March/087834.html]: http://mail.python.org/pipermail/python-dev/2009-March/087834.html
  [http://wiki.python.org/moin/Distutils/VersionComparison]: http://wiki.python.org/moin/Distutils/VersionComparison
  [http://bitbucket.org/tarek/distutilsversion]: http://bitbucket.org/tarek/distutilsversion
  [http://www.python.org/dev/peps/pep-0376]: http://www.python.org/dev/peps/pep-0376
  [http://svn.python.org/view/peps/branches/jim-update-345/pep-0345.txt?view=markup]:
    http://svn.python.org/view/peps/branches/jim-update-345/pep-0345.txt?view=markup
  [http://wiki.python.org/moin/Distutils]: http://wiki.python.org/moin/Distutils
