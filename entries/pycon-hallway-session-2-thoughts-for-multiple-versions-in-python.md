Title: Pycon hallway session #2: thoughts for multiple versions in Python
Date: 2009-03-30 07:16
Category: distutils, pycon, python

We had an excellent brainstorming session today in the hall, with
Toshio, Georg, Martin, Thomas, etc.. (sorry we were so many I don't have
the full list) with some insights from Guido and Brett. We tried to
think about a way to handle multiple versions of a same package.   
  
Here's the two most important concepts :   
-   **Unicity: **There should be one and only one instance of a Python
    package at a given version on a system
-   **Combination:** One Python application combines several packages to
    run

  
## About unicity

  
A Python package is a component that can be installed on a system. If
you use the standard Distutils approach, it will end up in the Python
site-packages directory and be importable by the interpreter. This
package comes with a version number and is unique.   
  
This unicity is important for security and maintainability. For
instance, if there's a security hole in a package, the fix is applied in
one place and the system maintainer knows it can't be present elsewhere
on the system.   
  
*This is the system administrator point of view*   
## About Combination

  
What defines a Python application is the fact that is selects a list of
packages it needs to run. And this varies for every application. So two
Python applications might need a different version of a given package
and that is normal.   
  
What's important is to have the right list of packages when an
application loads. Tools like zc.buildout or virtualenv are perfect for
this need : they create an isolated environment for your application to
run with the right set of packages.   
  
So the simplest way to release an application is to ship it with
everything required, regardless the unicity.   
  
*This is the application developer point of view*   
## The idea

  
zc.buildout and virtualenv are a blast for developers, and another
thing system packagers might dislike. This is because they break the
unicity by allowing developers to ship their applications as black
boxes. Of course one may say that this is perfectly fine since what's
inside an application is not the problem of the system packager. But
since this application is made of packages that may be shared on the
system by other applications, that is redondant.   
  
Forget *site-packages* for a moment. And let's think about a new
loading system for packages. This approach is similar in some ways to
setuptools' multiple version system.   
### Storing multiple versions

  
First of all, let's store the packages in a directory, and for each
version of the package, under a sub-directory which name is the version.
  
  
For example:   
-   SQLAlchemy   
   -   0.4   
       -   package code is here
        -   package egg-info here

          
   -   0.5   
       -   package code is here
        -   package egg-info here

          

      
-   jsonlib   
   -   1.2.6   
       -   package code is here
        -   package egg-info here

          
   -   1.3.10   
       -   package code is here
        -   package egg-info here

          

      

  
Given this structure, some mechanism can provide to the interpreter the
latest available version of a package, as long as Distutils knows how to
handle version comparisons correctly ([which will be the case in a near
future][])   
### Choosing specific versions

  
Back to our application. Let's call it MyApp, version 1.0.   
  
It needs specific versions for some packages. Forget *zc.buildout* and
*pip* for a moment. And let's think about a different way to express the
packages (and versions) its needs.   
  
Let's make a Python package for this application and let's make a few
assumptions on some features in Distutils:   
-   setuptools' install\_requires has made it into Distutils, as part of
    metadata.
-   metadata are defined **statically** in a package, apart from
    setup.py.

  
So basically, the application is mainly a static list of dependencies
defined into *install\_requires*. For example:   
-   SQLAlchemy \> 0.4
-   jsonlib == 1.2.6

  
When MyApp will get installed by Distutils, it will be added in the
packages tree.   
  
When it is used, it will need to load the versions of SQLAlchemy and
jsonlib it needs. The ones that are inside its metadata.   
  
To make it possible, the script that launches the application calls a
built-in function called read\_deps, that takes the metadata and reads
them to know which versions fit:   
   # the script

    read_deps('PKG-INFO')



    import SQLAlchemy

    import jsonlib

    ...

  
This call will load the right versions in the packages tree:   
-   SQLAlchemy   
   -   0.4
    -   0.5

      
-   jsonlib   
   -   1.2.6
    -   1.3.10

      
-   MyApp   
   -   1.0

      

  
### What's next

  
I just dropped here the rough idea, and a lot of details are missing.
But I think it's a good thing to share this idea here in its early
stage.   
  
We have decided we would try to write a prototype using *importlib* and
*sys.meta\_path*. Maybe Georg will start it during the Pycon sprint, and
start to digg into the details. He was working on this when I left the
open session at Pycon.   
  
Stay tuned

  [which will be the case in a near future]: http://wiki.python.org/moin/DistutilsVersionFight
