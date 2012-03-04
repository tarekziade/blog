Title: Distutils: introducing the check command (reStructuredText control)
Date: 2009-04-10 14:11
Category: distutils, python, quality

I am introducing the **check** command in Distutils. This command will
check your package metadata, like the **sdist** and the **register**
command already do (they display warnings).   
  
But the new thing is that it will also allow you to check if
*long\_description* is reStructuredText compliant.   
  
Its usage will be:   
   $ python setup.py check --restructuredtext

    running check

    warning: check: Title underline too short. (line 32)

    warning: check: Title underline too short. (line 32)

    warning: check: Could finish the parsing. (line None)

  
And there's also a *strict* mode, that raises an error in case
something is wrong   
   $ python setup.py check --restructuredtext --strict

    running check

    warning: check: Title underline too short. (line 32)

    warning: check: Title underline too short. (line 32)

    warning: check: Could finish the parsing. (line None)

    error: Please correct your package.

  
Last, this command will be used by **register**, and **sdist**, so you
can stop the process in case the metadata are not correct. This is
useful to make sure your PyPI home page is not broken for example, since
it parses *long\_description* to build it. So a good practice will be to
use *strict* when registering a package:   
   $ python setup.py register --strict

    running register

    running check

    warning: check: Title underline too short. (line 32)

    warning: check: Title underline too short. (line 32)

    warning: check: Could finish the parsing. (line None)

    error: Please correct your package.

  
This feature will land in Python 2.7 (I am working on it and it should
be commited this week end). Of course, it will not introduce a hard
dependency on docutils in Python, neither it will change the current
default behavior.   
  
Until then, you can use [collective.dist 0.2.3][], that provides this
feature for Python 2.4 to 2.6

  [collective.dist 0.2.3]: http://pypi.python.org/pypi/collective.dist
