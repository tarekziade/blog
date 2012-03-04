Title: Fixing packaging terminology confusion 
Date: 2010-01-07 21:30
Category: python

*Edit: the discussion is still going on, so I've probably blogged that a
little bit early (I was excited about it ;)). Stay tuned for the final
output.*   
  
Brad Allen launched a thread in [Distutils-SIG][] about packaging
terminology confusion. In particular the usage of the word "**package**"
in our community. Part of the confusion is because of the meaning of
this word in Python (that is, a directory containing one of several
Python modules, with a special one named \_\_init\_\_.py) and in some
systems like Debian (there, a package is a distribution file for a
library or an application).   
  
This confusion was present in PEP 345 (which was started years ago, so
that explains it) - and is present in Distutils documentation and also
in PyPI (That is: Python **Package** Index).   
  
I really like Tres Seaver's definitions, because they match prefectly
the reality:   
-   **package** means a Python package, (directory intended to be on
    sys.path, with an \_\_init\_\_.py. We \*never\* mean a distributable
    or installable archive, except when "impedance matching" with folks
    who think in terms of operating system distributions.
-   **distribution** is such a distributable / installable archive:
    either in source form (an 'sdist'), or one of the binary forms
    (egg., etc.). Any distribution may contain multiple packages (or
    even no packages, in the case of standalone scripts).
-   **project** is the process / community which produces releases of a
    given set of software, identified by a name unique within PyPI's
    namespace. PyPI manages metadata about projects (names, owners) and
    their releases. Every real project has at least one release.
-   **release** is a set of one or more distributions of a project, each
    sharing the same version. Some PyPI metadata is specific to a
    release, rather than a project. Every release has at least one
    distribution.

  
And I really like Martin's proposal in the thread (in Catalog-SIG since
it was cross-posted): "PyPI would then be the **Python Project Index**."
  
  
I'll fix Distutils documentation on my side accordingly, as well as the
[guide][] we are building. Let's promote these definitions :)

  [Distutils-SIG]: http://mail.python.org/pipermail/distutils-sig/2010-January/015232.html
  [guide]: http://guide.python-distribute.org
