Title: a small Distutils2 foretaste
Date: 2010-04-08 10:52
Category: python

*Notice: If you didn't follow what's going on in the packaging world,
you can read [this][].*   
  
The first public version of Distutils2 will be **1.0a1**, and is
scheduled for **April 30th**.   
  
We are working on implementing the various PEPs, removing the bad bits
inherited from Distutils, keeping the good ones, and adding the work
that was done in Distribute, like the Python 3 work (and grabbing the
good bits of Setuptools as well, like the *test* command.) I have also
proposed a GSOC project, and I hope it will be picked by the PSF, to
boost the work.   
  
In any case, lots of tasks will not be ready for **1.0a1**, and will be
shipped later. But I think its important to release what we currently
have since it's *also* a result of over 1 year of work I have been doing
within the stdlib. As a reminder: I reverted this work in Python, making
Distutils there pretty similar to 2.6's, and I've forked this work to
create distutils2.   
  
Anyways, this blog entry is focusing on describing some of the features
you will find in Distutils2 *today*.   
  
The code is located in the new Python Mercurial repository
([http://hg.python.org/distutils2][]).   
### Distutils2 philosophy

  
One of the key point of Distutils2 is to try to provide tools for
third-party projects like Pip, PyPM, etc. without forcing them to adopt
the *everything-is-a-distutils-command* philosophy. People have suffered
from this in the past, and this problem was probably one of the reason
the Setuptools project has to patch Distutils' code all over the place.
  
  
I am therefore trying to think about Distutils2 as two distinct things:
  
1.  a python packaging framework with tools anyone can use
2.  a python package manager based on CLI commands people can use to
    build, upload, install packages.

  
The way 2. is working today in Distutils has been very controversial,
and they are other tools out there based on other philosophies. I'll
focus on making 1. as useful as possible for all tools, without forcing
them to adopt 2. But also to enhance/fix 2.   
  
There are key features to add in Distutils2 to make the CLI command
system more useful. For instance, adding a ***configure*** command that
will take all compiling options and generate a configuration file that
can be consumed by other commands (build or install for instance) will
probably make people life easier. This has been done by 4Suite, and this
will be done in Distutils2.   
  
In the Framework part, we already have two interesting modules you can
already use:   
### The version module

  
The ***version*** module is the implementation of PEP 376. It provides
among other things:   
-   The **NormalizedVersion** class you can use to work with PEP 376
    version
-   The **suggest\_normalized\_version()** function you can use to try
    to transform any version into a PEP 376-compatible version. This
    function is based on what we have learned by looking at the projects
    released at PyPI.

  
So, if you need to compare versions, you can create instances of
**NormalizedVersion** using the string representation of the version,
and use any comparison operator.   
   >>> from distutils2.version import NormalizedVersion

    >>> NormalizedVersion('1.2a1') < NormalizedVersion('1.2')

    True

  
In case the version is not PEP 376 compatible, the class will throw an
exception   
   >>> NormalizedVersion('1.2-a1')

    Traceback (most recent call last):

    ...

    distutils2.errors.IrrationalVersionError: 1.2-a1

  
And for these "irrational versions" ;), you can use
**suggest\_normalized\_version** to try to convert them:   
   >>> from distutils2.version import suggest_normalized_version

    >>> suggest_normalized_version('1.2-a1')

    '1.2a1'

    >>> NormalizedVersion(suggest_normalized_version('1.2-a1'))

    NormalizedVersion('1.2a1')

  
### The metadata module

  
The ***metadata*** module implements PEP 345 (the new metadata) but
also works with old metadata versions. It provides a
**DistributionMetadata** class you can use to read or write metadata
files (those PKG-INFO file you can find in any release). This class is
compatible with all versions of Metadata:   
-   1.0 : PEP 241
-   1.1 : PEP 314
-   1.2 : PEP 345

  
The PEP 345 implementation supports the micro-language for the
environment markers, and displays warnings when versions that are
supposed to be PEP 386 are violating the scheme.   
#### Reading metadata

  
The **DistributionMetadata** class can be instanciated with the path of
the metadata file, and provides a dict-like interface to the values:   
    >>> from distutils2.metadata import DistributionMetadata

     >>> metadata = DistributionMetadata('PKG-INFO')

     >>> metadata.keys()[:5]

     ('Metadata-Version', 'Name', 'Version', 'Platform', 'Supported-Platform')

     >>> metadata['Name']

     'CLVault'

     >>> metadata['Version']

     '0.5'

     >>> metadata['Requires-Dist']

     ["pywin32; sys.platform == 'win32'", "Sphinx"]

  
The fields that supports environment markers can be automatically
ignored if the object is instanciated using the
***platform\_dependant*** option. **DistributionMetadata** will
interpret in the case the markers and willautomatically remove the
fields that are not compliant with the running environment.   
  
Here's an example under Mac OS X. The win32 dependency we saw earlier
is ignored:   
    >>> from distutils2.metadata import DistributionMetadata

     >>> metadata = DistributionMetadata('PKG-INFO', platform_dependant=True)

     >>> metadata['Requires-Dist']

     ['Sphinx']

  
If you want to provide your own execution context, let's say to test
the Metadata under a particular environment that is not the current
environment, you can provide your own values in the
**execution\_context** option, which   
is the dict that may contain one or more keys of the context the
micro-language expects.   
  
Here's an example, simulating a win32 environment:   
    >>> from distutils2.metadata import DistributionMetadata

     >>> context = {'sys.platform': 'win32'}

     >>> metadata = DistributionMetadata('PKG-INFO', platform_dependant=True,

     ...                                 execution_context=context)

     ...

     >>> metadata['Requires-Dist'] = ["pywin32; sys.platform == 'win32'",

     ...                              "Sphinx"]

     ...

     >>> metadata['Requires-Dist']

     ['pywin32', 'Sphinx']

  
#### Writing metadata

  
Writing metadata can be done using the **write** method:   
   >>> metadata.write('/to/my/PKG-INFO')

  
The class will pick the best version for the metadata, depending on the
values provided. If all the values provided exists in all versions, the
class will used ***metadata.PKG\_INFO\_PREFERRED\_VERSION***. It is set
by default to **"1.0"**.   
#### Conflict checking and best version

  
Some fields in PEP 345 have to follow a version scheme in their
versions predicate. When the scheme is violated, a warning is emited:   
   >>> from distutils2.metadata import DistributionMetadata

    >>> metadata = DistributionMetadata()

    >>> metadata['Requires-Dist'] = ['Funky (Groovie)']

    "Funky (Groovie)" is not a valid predicate

    >>> metadata['Requires-Dist'] = ['Funky (1.2)']

  
Stay tuned for some more fortastes of Distutils2 !   
  
And if you want to contribute, join us in \#distutils (freenode)

  [this]: http://guide.python-distribute.org/introduction.html#current-state-of-packaging
  [http://hg.python.org/distutils2]: http://hg.python.org/distutils2
