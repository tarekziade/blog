Title: Do not upload dev releases at PyPI
Date: 2011-02-15 17:15
Category: python

The [discussion we had][] on the SQLAlchemy mailing list, triggered by
the release of *0.7.1b*, made me realize that we need a heads-up on this
problem. *EDIT: a [similar problem occurred][] for psycopg2 today.*   
  
**Until our packaging ecosystem knows how to handle properly
*development releases*, the best practice for *mature* projects is to
avoid publishing anything that is not a *final release* at PyPI (or any
download link that points to a development release)   
**   
  
By development releases, as opposed to final releases, I include:   
-   any release that is a snapshot of the trunk or tip of the project
-   any alpha, beta, or release candidate

  
And by *mature* project, I mean any project that already published one
stable release at PyPI.   
  
The reason is that our current set of packaging tools do not know how
to make a difference between a final release and a development release.
  
  
Setuptools' *easy\_install* script will scan the simple index page,
order the releases number via its version sorting algorithm, then take
the "latest" version.   
  
So calling:   
   $ easy_install Foo

  
will install the latest uploaded release for the *Foo* project, even if
it's a development version. If you use Setuptools' *install\_requires*
option in your setup.py, the same thing will happen.   
  
To prevent it, you can tell the tool which version you want, and even
provide a complex condition, like:   
   $ easy_install SQLAlchemy >=0.5, <0.7

  
But there's no way to tell it to get the latest final.   
  
zc.buildout is the only tool in my knowledge that prevents this, with
[the prefer-final option][].   
### How Distutils2 and PEP 386 fixes the problem

  
But uploading release candidates is a great way to get feedback from
the community, and it's currently frustrating not to be able to push
development versions at PyPI. Because depending on the installers our
users will use, they might be unable to control if they want to opt in
using non final releases.   
  
And, well, what's a final release ? what's a beta ? Are we sure all
tools agree on the versionning schemes ?   
  
How can I make sure my beta version will be recognized as a beta
release by all tools out there ?   
  
[PEP 386 solves this][] by defining a version scheme.   
  
And guess what:   
-   The new [Metadata 1.2 - PEP 345][], implemented in Distutils2,
    recognizes only PEP 386 versions
-   PyPI will reject any project that uploads metadata 1.2 with a
    non-PEP 386 version. And this is already activated at PyPI.
-   The Distutils2 installer recognizes development releases and let you
    decide which one to pick.

  
Granted, it's going to take a while before all installers use the new
standards, and all projects out there make the jump to Metadata 1.2, but
at least we know the problem and implemented the solution..   
  
And[Pycon should be an important milestone][] since the first beta of
Distutils2 will be released at... PyPI and will be usable by any
project.

  [discussion we had]: http://groups.google.com/group/sqlalchemy/t/c831f7fe7268c51f
  [similar problem occurred]: http://mail.python.org/pipermail/distutils-sig/2011-February/017355.html
  [the prefer-final option]: http://pypi.python.org/pypi/zc.buildout#preferring-final-releases
  [PEP 386 solves this]: http://www.python.org/dev/peps/pep-0386/
  [Metadata 1.2 - PEP 345]: http://www.python.org/dev/peps/pep-0345/
  [Pycon should be an important milestone]: http://us.pycon.org/2011/schedule/presentations/81/
