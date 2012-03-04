Title: Distutils and Distribute status (part #1)
Date: 2009-11-18 09:36
Category: python

Someone told me on IRC that it's currently hard to follow what's going
on in the packaging front. The truth is that it's almost impossible if
you don't read **all** mails posted in Distutils-SIG.   
  
So here's a quick wrap-up that can save you some time if you are not
reading Distutils-SIG.   
### PEP 345 - Metadata 1.2

  
We are almost done with the update of [PEP 345][]. This PEP is
describing the Metadata fields for a distribution, that get added in the
file named PKG-INFO. This file is inserted in all your distribution and
also published at PyPI. It's the ID card of your project.   
  
We are adding these fields in the metadata:   
-   Maintainer : the maintainer's name
-   Maintainer-email : the maintainer's email
-   Requires-Python : What Python versions are compatible with this
    distribution
-   Requires-External : A list of external dependencies, like "libpng",
    "libxslt"
-   Requires-Dist : A list of Python dependencies, from the names
    founded at PyPI. like "zope.interface"
-   Provides-Dist : A list of additional distribution names this
    distribution provides (as a complement to the one provided in
    "Name")
-   Obsoletes-Dist : A list of Python dependencies that are incompatible
    with the current distribution

  
Another important change is **environment markers**. An **environment
marker** is a marker that can be added at the end of a field after a
semi-colon (';'), to add a condition about the execution environment.   
  
Examples:   
   Requires-Dist: pywin32, bar > 1.0; sys.platform == 'win32'

    Obsoletes-Dist: pywin31; sys.platform == 'win32'

    Requires-Dist: foo; os.machine == 'i386'

    Requires-Dist: bar; python_version == '2.4' or python_version == '2.5'

    Requires-External: libxslt; 'linux' in sys.platform

  
This will allow developers to define different conditions depending on
the target platform. Moreover, this will allow tools like Pip to get a
list of all dependencies for a given project and a given platform just
by querying PyPI, and with no downloads or build required !   
  
Last, for all the fields that manipulates versions, PEP 345 will use
the version scheme described in PEP 386.   
### PEP 386 - Version scheme

  
We've designed in [PEP 386][] a version scheme that works with most
Python software we know about. This version scheme comes with a new
version comparison algorithm that will be provided by Distutils.   
  
The scheme is in pseudo-regexpr (read the PEP for more details):   
   N.N[.N]+[abc]N[.N]+[.postN+][.devN+]

  
Don't be afraid ! It looks complex but it's not. The apparent
complexity is due to the fact that we need to be able to work with
development versions and post-release versions.   
  
There are good chances that your project already works with this
version scheme. If you want to give it a shot, there's a prototype you
can play with in an external repo here:
[http://bitbucket.org/tarek/distutilsversion/][]   
### PEP 376 - Installation standard

  
[PEP 376][] is quite completed now. We have our "standard" for
site-packages, we know how to query installed projects, and how to
remove them.   
  
The discussions are now focusing on the "data" problem. Which is : how
to describe in Distutils, in a more elegant way, the data files you are
using, such as images, man files etc.   
  
This is required to provide to developers more control on how their
data files are installed on the target system, and to the packagers more
tools to re-package a Python distribution.   
  
Wolodja Wentland has been doing a lot of work in this area and leads
this "data" effort. You can follow the discussion on this work in the
Python wiki, starting at:
[http://wiki.python.org/moin/Distutils/DiscussionOverview][].   
### PEP 382 -Namespaces packages

  
Distribute comes with a namespace package system, that allows you to
have packages under the same namespace, spread into several
distributions.   
  
That's what Plone and Zope use to be able to release all those plone.\*
and zope.\* distributions.   
  
Martin von Loewis proposed to implement it in Python, and this is
described in [PEP 382][].   
  
We are now waiting for Martin to implement it, and are ready to drop in
Distribute 0.7.x the namespace feature in favor of supporting the PEP
382 one.   
### Distutils redesign discussions

  
One thing that makes Distutils a bit hard to work with, is how commands
are designed. David Cournapeau (from the Numpy project) gave us an
example of a use case that makes it hard. He basically needs to run the
"build" command knowing the finalized options from the "install"
command.   
  
In other words, when you call something like :   
   $ python setup.py install --prefix=/some/place

  
The install command will use the prefix option to cook some other
options. The build command that needs all the options needs in that case
to look over the install command to get the values.   
  
This is not optimal because it means that a **build** command depends
on an **install** command to run. It also makes options redundants from
one command to the other.   
  
The solution we are going to try is to create a new command, called
**configure**, that will be in charge of building a file with all the
options that are required by the build command and the install command.
  
  
This is not new. It has been implemented years ago in 4suite, and it's
the philosophy behind tools like scons, etc: a configure/make/make
install principle applied to a Python project.   
  
This redesign is going to occur in Distribute 0.7. Once it's ready, if
the community has tried it and gave us positive feedback, I'll push it
in Distutils.   
  
It might happen before Python 2.7 is out, it might not.   
### Other topics

  
There are many other topics, like PyPI mirroring ([PEP 381][]) etc.
I'll write a blog entry later for these.

  [PEP 345]: http://www.python.org/dev/peps/pep-0345
  [PEP 386]: http://www.python.org/dev/peps/pep-0386/
  [http://bitbucket.org/tarek/distutilsversion/]: http://bitbucket.org/tarek/distutilsversion/
  [PEP 376]: http://www.python.org/dev/peps/pep-0376/
  [http://wiki.python.org/moin/Distutils/DiscussionOverview]: http://wiki.python.org/moin/Distutils/DiscussionOverview
  [PEP 382]: http://www.python.org/dev/peps/pep-0382/
  [PEP 381]: http://www.python.org/dev/peps/pep-0381/
