Title: PEP 345 and 386 accepted -- Summary of changes
Date: 2010-02-10 10:24
Category: python

Several PEPs were accepted this month by Guido, and among them PEP 345
and PEP 386, which are about Python packaging. I am summarizing in this
entry the main changes we've made.   
## PEP 345 - Metadata v1.2

  
This PEP is about the Metadata that gets added in your project when you
build a distribution using Distutils or a Distutils-based tool. Those
are fields like "name" or "version" you pass as options in your setup.py
file. They eventually land in a PKG-INFO file then at PyPI and in each
Python's site-packages where the project is installed. They are also
useful when your project gets repackaged by an OS packager.   
### New fields

  
PEP 345 adds some new fields :   
-   **Maintainer** : a string containing the maintainer's name
-   **Maintainer-email** : a string containing the maintainer's e-mail
-   **Requires-Python** : Python version(s) that the distribution is
    guaranteed to be compatible with.
-   **Requires-External** : Describes some dependencies in the system
    that the distribution is to be used
-   **Requires-Dist** : String naming some other distutils project
    required by this distribution.
-   **Provides-Dist** : String naming a Distutils project which is
    contained within this distribution.
-   **Obsoletes-Dist** : String describing a distutils project's
    distribution which this distribution renders obsolete
-   **Project-URL** : String containing a browsable URL for the project
    and a label for it, separated by a comma.

  
***Maintainer*** and ***Maintainer-email*** were added because people
were confused about the *maintainer* and *maintainer\_email* options
they have in Distutils. Before PEP 345, if you used the *author*
***and*** the *maintainer* fields, one was dropped and one was kept to
fill the *Author* metadata field.   
  
***Requires-Python*** was added so people could list the Python
versions their project is compatible with. We do have classifiers
already for that in the Trove classifier, but this new field is more
than a simple field : the version string that is used supports a syntax
that makes it possible to describe any set of Python versions. See the
[version specifier][] of the PEP.   
  
Remember the *requires.txt* metadata Setuptools introduced together
with the *install\_requires* option ? ***Requires-Dist*** is comparable
to this and will let you define dependencies on other Python projects.
Distutils had the ***Requires*** field, but it was defining dependencies
at the **module** level and this was never really used by the community.
So ***Requires*** is gone in 1.2. Last, ***Requires-Dist*** is using a
version comparison scheme described in details in [the version specifier
section][version specifier].   
  
***Provides-Dist*** gives you the ability among other things to
reorganize your project names or to distribute a subproject in several
projects. For instance, the project called *ZODB* used to include the
project *transaction* that is also distributed as a standalone project
now. If *ZODB* is installed, and if you need *transaction*, you won't
have to install it again.   
  
***Obsoletes-Dist*** will let you make sure a project that is
incompatible with your project is not installed at the same time.   
  
***Project-URL*** is useful to provide a list of URLs for your project
like a browsable repository or a tracker. The goal will be to add a
small box on PyPI project pages for these URLs, so developers can
emphasize them. This will hopefully address the complaints PyPI had in
these past months when the comment system was added.   
  
Some small changes were made on existing fields. One important change
is on the ***Description*** field (*long\_description* in setup.py).
Before PEP 345, once this value was written in the metadata file, its
empty lines and spaces at the beginning of lines were truncated. In
other words, if a tool was reading back this value, its reSTrucured
syntax was broken. This is no longer the case.   
  
Once I've finished implementing PEP 345, you will be able to read back
a project's metadata usig the *DistributionMetadata* class. See an
[example][].   
### Environment Markers

  
When Pip wants to install all the dependencies a project requires, it
has to follow these steps:   
1.  download the project from PyPI
2.  execute a Distutils command on setup.py, like egg\_info, to get the
    metadata. And in particular the list of requirements

  
This is mandatory because the metadata are not statically defined and
the developer might need to run some code in his setup.py to know what
dependencies are required, depending on the target platform.   
  
For example:   
       if sys.platform == 'win32':

            install_requires = ['pywin32']

        else:

            install_requires = []

  
In other words, there's no way to get the metadata without running
third-party code. Environment markers fix this issue in most cases by
providing a micro-language that can be used at the field level. At the
end, you can write things like that in the metadata:   
       Requires-Dist: pywin32 (>1.0); sys.platform == 'win32'

  
And Distutils will provide a tool to parse and execute this expression,
so you know if your target platform have to use this metadata field.
Meaning that Pip or other tools will be able to read metadata of a
project without running any third party code. For example to get all the
dependencies of a project depending on the target platform just by
querying PyPI.   
  
See all the details [in the section in the PEP][].   
## PEP 386

  
Throughout all the PEP 345, we had to compare versions. To be able to
perform this, we need to have a common standard for versions numbers.
That's what PEP 386 was written for.   
  
The idea is not to force people to version their project using this
version scheme, but rather to provide a scheme that is good enough for
interoperability and that is human readable.   
  
PEP 386 provides this scheme (in pseudo-format) :   
     N.N[.N]+[{a|b|c|rc}N[.N]+][.postN][.devN]

  
The corresponding regular expression is:   
       expr = r"""^

        (?P<version>\d+\.\d+)         # minimum 'N.N'

        (?P<extraversion>(?:\.\d+)*)  # any number of extra '.N' segments

        (?:

            (?P<prerel>[abc]|rc)         # 'a' = alpha, 'b' = beta

                                         # 'c' or 'rc' = release candidate

            (?P<prerelversion>\d+(?:\.\d+)*)

        )?

        (?P<postdev>(\.post(?P<post>\d+))?(\.dev(?P<dev>\d+))?)?

        $"""

  
The scheme handles these cases:   
-   pre-releases
-   development versions
-   final versions
-   post-release versions
-   development versions of post-release versions

  
Here are some examples:   
   >>> from verlib import NormalizedVersion as V

    >>> (V('1.0a1')

    ...  < V('1.0a2.dev456')

    ...  < V('1.0a2')

    ...  < V('1.0a2.1.dev456')

    ...  < V('1.0a2.1')

    ...  < V('1.0b1.dev456')

    ...  < V('1.0b2')

    ...  < V('1.0b2.post345')

    ...  < V('1.0c1.dev456')

    ...  < V('1.0c1')

    ...  < V('1.0.dev456')

    ...  < V('1.0')

    ...  < V('1.0.post456.dev34')

    ...  < V('1.0.post456'))

    True

  
This can look utterly complex to you, but in fact there are good
chances that your version scheme is already compatible with this one.
We've tested in on PyPI, and 88 % of the projects' distributions were
recognized.   
### The suggest\_rational\_version function

  
Let's face it: there are hundreds of valid versionning schemes that are
not compatible with what we've done. So we are adding a function called
*suggest\_rational\_version* that can be used to transform a version
that is not "PEP-386" compliant into one that is compliant.   
  
This does a number of simple normalizations to the given string, based
on an observation of versions currently in use on PyPI.   
  
Given a dump of those versions on February 10th 2010, the function has
given those results out of the 9066 distributions PyPI had:   
-   8058 (88.88%) already match `NormalizedVersion` without any change
-   795 (8.77%) match when using this suggestion method
-   213 (2.35%) don't match at all.

  
And here's an extract of the 2.35% unrecognized scheme:   
-   0.2-grigoropoulos
-   0.1-alphadev
-   working proof of concept
-   bzr14
-   1 (first draft)

  
In other words, they are unusable anyways. If you want to try this on
your own versions, grab the code at
[http://bitbucket.org/tarek/distutilsversion/][]. And if you version
doesn't match at all and you think its a mistake, let me know so we can
work your case.   
## Conclusion + my rant on packaging

  
I have started working seriously on packaging issues a year ago. And I
kept on hearing complaints on how packaging sucks hard. That was
frustrating since some folks and I were working hard to change things
(and we still do). I kept seeing the same people ranting about
packaging, and most of the time they were not willing to help around. I
guess that's just me being naive, but let me say it one more time :)   
  
**If you don't like how packaging works in Python, stop complaining and
come in the Distutils mailing list, or in \#distutils on freenode and
help us !**   
  
I am now really glad that these PEPs were accepted by Guido because
they are the first milestone we had to reach to improve things for real
in packaging. Python 2.7 is going to make a big jump forward in this
area !   
  
Next milestone we are trying to reach for 2.7 is to finish PEP 376
(uninstall feature, querying installed packages, etc)

  [version specifier]: http://www.python.org/dev/peps/pep-0345/#version-specifiers
  [example]: http://docs.python.org/dev/distutils/examples.html#reading-the-metadata
  [in the section in the PEP]: http://www.python.org/dev/peps/pep-0345/#environment-markers
  [http://bitbucket.org/tarek/distutilsversion/]: http://bitbucket.org/tarek/distutilsversion/
