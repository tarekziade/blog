Title: Distutils2 vs Pip
Date: 2010-05-31 12:21
Category: gsoc, python

*Note: if you are not familiar with [PEP 345][], you might want to read
it to understand this entry.* *It adds for instance "Requires-Dist" that
is similar to setuptools' install\_requires and provides a standard for
dependencies description.*   
  
The GSOC has started and we are already working on a lot of tasks about
packaging. The main difficulty is to make sure each student works
without overlapping with others, and never get blocked. That's why we
will have weekly meetings with (almost) everyone. In parallel, the nice
posse from the Montreal user group is organizing Distutils sprints quite
often now. That means that we now have an important manpower for
Distutils and things are starting to speed up.   
  
There's one controversial topic though, that we need to straighten up :
do we want to add an installer in Distutils2 ? And since Distutils2 goal
is to be back in the stdlib for Python 3.2, that means: do we want to
add an installer in the stdlib ?   
  
My answer so far is **Yes**. And that's what I'll be working on unless
someone is able to change my mind :)   
### What is Distutils2 ?

  
Let me explain first what is the Distutils2 project, and what we want
it to provide. Like its predecessor, Distutils2 wants to provide two
things:   
1.  **a toolbox for third packaging tools**, whether they are *simple*
    installers or full featured package managers (PyPM, Pip, Enthought
    Installer etc..). This toolbox will include (if not already)
    reference implementation of PEP 345, PEP 376, PEP 386. In other
    words, if you want to create the next killer packaging system, you
    can use modules like *distutils2.version* (PEP 386) or
    *distutils2.metadata* (PEP 345) to build it, without depending on
    the "everything is a command" philosophy of Distutils.
2.  **a standalone tool that can be used to install or remove
    distributions**. That's what Distutils is and that's what we want to
    provide in the future in Distutils2. The ability to install projects
    (and therefore its dependencies since this is a new metadata field
    we added in PEP 345).

  
The controversy is about 2. It's controversial to provide a script that
installs dependencies via PyPI into distutils2 because some projects
like Pip already provides this feature.   
### Our current packaging ecosystem explained

  
A few years ago, before Setuptools added the ability to install
dependencies via ***easy\_install***, installing a distribution of a
given project was as simple as running a ***python setup.py install***.
This was installing the distribution in the target system, in proper
locations defined by the ***install*** command. That's it.   
  
Setuptools grew organically on the top of Distutils to provide new
metadata like the "install\_requires" field, that lists dependencies.
Setuptools provided two things:   
-   A new** install command** that triggers the installation of
    dependencies, by reading the setuptools-specific "install\_requires"
    metadata, and fetching dependencies at PyPI and installing them
    recursively.
-   An **easy\_instal**l script that can be used to install a
    distribution located at PyPI. That's just a bootstrap on the top of
    the new install command. In other words, it grabs the archive at
    PyPI, unpack it, and run "python setup.py install" on it.

  
In other words, **your Python project setup.py is the installer
itself** because when you use setuptools, it calls its specific install
command and triggers the installation chain.   
  
That's when the mess started: people that didn't have setuptools
installed couldn't install projects that was using it of course. So the
solution that was provided was to propose an **ez\_setup.py** script
that you have to include in your project and to run when setup.py is
used, to be able to run your installation. In other words, your setup.py
is bootstrapping the utilization/installation of setuptools. And that
turned out to be really messy since Setuptools has its own way for
installing things. I hope I don't sound harsh here, Setuptools is the
best thing that happened to packaging in years. And a lot of our current
work is to bring back its features into the "main stream".   
  
The result is that you, as a end user, do not control what installer is
going to be used, and you end up with a site-packages that has projects
installed differently, and that uses different installers.   
  
I am strongly against this behavior because of the mess it creates.
**In my opinion a python source distribution should not embed an
installer and force its usage like this**. We need to separate concerns:
a python source project should be a dumb container with the code, and
with some metadata.   
  
Then Pip showed up.   
  
Pip is an installer script that grabs the project you want to install
and run "python setup.py install" on it. That's all it does when the
project is a plain Distutils one. When it encounter Setuptools projects,
it blocks the installation of the project's dependencies I have
described earlier, and installs it like a simple Distutils project.
Then, it analyzes its dependencies and installs each one of them
separately.   
  
That's really the way to go because it breaks what setuptools is
enforcing: projects are not installing other projects in the process
anymore. And in the long term, it will allow us to get rid of setup.py
(but that's another blog post). And I hope Pip will soon be able to
install Distutils2 projects because it is providing unifi ed metadata
(distutils+setuptools -\> PEP 345).   
### Distutils2 vs Pip

  
So as I said before: it's controversial to provide a script that
installs dependencies via PyPI into distutils2 because Pip already
provides this feature.   
  
But one Distutils2 goal (like Distutils) is to provide a command to
install a Distribution of your system so it works. And the concept of
"Distribution" has evolved, thanks to PEP 345. this means that it needs
to install dependencies now, exactly the way Pip does.   
  
We could just tell people to install Pip on the top of the stdlib. But
the goal is to provide in the stdlib a working packaging environment,
that provides a minimum set of features. The goal is to have something
that works when you install Python 3.2, like what was provided when
distutils was brought in (eg *batteries included*).   
  
Mac OS X includes easy\_install, I don't see any good reason not to
include a package installer in the Python stdlib itself. At least, we
will be able to have a control on what script gets installed by default
with Python.   
  
That's why I have proposed to include Pip in Distutils2 but Ian and
Carl seems a bit reluctant for various reasons. One of them is that
having Pip included in the stdlib will slow down their work. I don't
think this is true as long as it's included carefully. If Distutils2
allows its installer to be replaced through configuration by another
one, then Pip can have new releases independently from the version
included in the stdlib and people can upgrade their system without
having to wait for the next Python release.   
  
In any case, we are working on the various bits that are composing an
installer in Distutils2 during GSOC since one of the goal of the project
as I said earlier, is to provide a toolbox. So if the merge does not
occur, it's likely that we will start a installer/uninstaller script in
Distutils2, and it will look a lot like Pip I guess.   
  
*EDIT: to make things clearer, when I am saying that both projects
should merge, I am only referring to the raw "install with dependencies"
features in Pip, and not all the other features.*

  [PEP 345]: http://www.python.org/dev/peps/pep-0345/
