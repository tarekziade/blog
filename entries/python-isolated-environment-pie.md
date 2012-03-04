Title: Python Isolated Environment (PIE)
Date: 2008-12-15 10:24
Category: python, zc.buildout, zope

Here's a proposal I will send to the python-dev. What do you think ?   
  
*(Disclaimer : this proposal is highly inspired from the work done by
people in various tools, it does not reinvent anything)*   
### The problem

  
Python developers distribute and deploy their packages using myriads of
dependencies. Some of them are not yet available as official OS python
packages. Even sometimes one package conflicts with the *official*
version of a package installed in a given OS.   
  
In any case, the cycle of development of most Python applications is
shorter than the release cycle of Linux distributions, so it is
impossible for application Foo to wait that Bar 5.6 is officialy
available in Debian 4.x.   
  
Therefore, there's a need to provide or describe a specific list of
dependencies for their application to work.   
  
And this list of dependency might conflict with the existing list of
packages installed in Python. In other words, even if this is not a
wanted behavior from an os packager point of view, an application might
need to provide its own execution context.   
  
Right now, when Python is loaded, it uses the site module to browse the
site-packages directory to populate the path with packages it find
there. *.pth* files are also parsed to provide extra paths.   
  
Python 2.6 has introduced per-user *site-packages* directory, where you
can define an extra directory, which is added in the path like the
central one.   
  
But both will append new paths to the environment without any rule of
exclusion or version checking.   
### The workarounds

  
A few workarounds exist to be able to express what packages (and
version) an application needs to run, or to set up an isolated
environment for it:   
-   [*setuptools*][] provides the *install\_requires* mechanism where
    you can define dependencies directly inside the package, as a new
    metadata. It also provides a way to install two different versions
    of one package and let you pick by code or when the program starts,
    which one you want to activate.
-   [*virtualenv*][] will let you create an isolated Python environment,
    where you can define your own site-packages. This allows you to make
    sure you are not conflicting with a incompatible version of a given
    package.
-   [*zc.buildout*][] relies on setuptools and provides an isolated
    environment a bit similar in some aspects to virtualenv.
-   [pip][] provides a way to describe requirements in a file, which can
    be used to define *bundles*, which are very similar to what
    zc.buildout provides.

  
But they all aim at the same goal : define a specific execution context
for a specific application, and declare dependencies with no respect to
other applications or to the OS environment.   
  
This proposal describes a solution that can be added to Python to
provide that feature.   
### The solution

  
A *isolated environment* file that describes dependencies is added.
This file can be tweaked by the application packager, or later by the OS
packager if something goes wrong.   
#### The isolated environment file

  
A new file called a *Python Isolated Environment* file (PIE file) can
be provided by any application to define the list of dependencies and
their versions.   
  
It is a simple text file with a first line that provides :   
-   a list of paths, separated by ':', on line 1
-   then one package per line, starting at line 2. each package can be
    prefixed by a \`!\`

  
For example:   
   /var/myapp/myenv

    lxml

    sqlite

    sqlalchemy

    !sqlobject

  
This list of packages might or might not be installed in Python.   
  
Versions can be provided as well in this file :   
   /var/myapp/myenv:/var/myapp/myenv2

    lxml >= 0.9

    sqlite > 1.8

    sqlalchemy == 0.7

    !sqlobject == 0.6

  
The file is saved with the *pie* extension,   
#### Loading an isolated environment file

  
A new function called *load\_isolated\_environment* is added in
*site.py*, that let you load a PIE file.   
  
Loading a PIE file means:   
-   for each package defined, starting at line 2,
    *load\_isolated\_environment* will look into the environment if the
    package with the particular version exists. The version is given by
    the *package.\_\_version\_\_* value or the *PKG-INFO* one when
    available. If the package exists but the version is not available,
    the version 0.0 is used.
-   for packages without the ! prefix:   
   -   if the package is not found, it will scan each path provided on
        line 1 of the file, using the *site-packages* method, looking
        for that package.
    -   if the package is found, it is added in the path.
    -   if the package is not found, a *PackageMissing* error is raised.

      
-   for packages starting with the ! prefix:   
   -   if the package is found, it is removed from the path

      

  
This function can be called by code like this:   
   >>> from site import load_isolated_environment

    >>> load_isolated_environment('/path/to/context.pie')

  
From there, *sys.path* meets the requirements and the code that is
executed after this call will benefit from this context.   
Another context can be loaded in the same process :   
   >>> load_isolated_environment('/path/to/another_context.pie')

  
Limitations:   
-   if the new context brakes other programs in the process. It's up to
    the application packager to fix the context file.
-   it's not the job of *load\_isolated\_environment* to resolve
    dependencies issues : if the *foo* package needs the *bar* package,
    it won't complain.
-   it is not the job of *load\_isolated\_environment* to get missing
    dependencies.

  
#### Using an isolated environment file

  
Typically, an isolated environment file can be used into high-level
Python scripts. For example, any script an application provides to be
launched :   
   # this script runs zope

    from site import load_isolated_environment

    load_isolated_environment('zope-3.4.pie')



    import zope



    if __name__ == '__main__':

        zope.run()

  [*setuptools*]: http://pypi.python.org/pypi/setuptools/
  [*virtualenv*]: http://pypi.python.org/pypi/virtualenv
  [*zc.buildout*]: http://pypi.python.org/pypi/zc.buildout
  [pip]: http://pypi.python.org/pypi/pip
