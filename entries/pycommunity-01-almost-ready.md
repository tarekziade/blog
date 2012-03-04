Title: PyCommunity 0.1 almost ready
Date: 2007-02-11 22:53
Category: documentation, pycommunity, pycon, python, quality, zope

I've been working a lot on PyCommunity packaging lately, so it can be
ready for my PyCon tutorial. Version 0.1 will be released by then and
will autogenerate html pages for a Python project that bases its
documentation on reST files.   
  
There are a few mandatory files that have to be present in the project
for the tool to work, but it is not really restrictive. I tried a few
runs on Zope codebase and it works fine, besides a few problems with
epydoc (some Zope files are breaking epydoc, I need to dig on this) and
a few failures on some malformed reST files.   
  
PyCommunity is based on [Cheetah templates][], that can be customized
to smoothly integrate generated pages into an existing website.   
  
Features to complete for 0.1:   
-   [Cheesecake][] index report for each package
-   test coverage report for each package, using [trace2html][]
-   [Crunchy frog][] integration
-   [Pygments][] integration
-   SVN hook dameon with a queue, so the generation can be done smoothly
-   Folder and file skipping to avoid the process of unwanted content

  
The source code is in a Mercurial repository, right here:
[http://hg.programmation-python.org/repositories/public][]   
  
If you [follow this link][], you will see a generated site based on a
fake project used in PyCommunity unit tests.

  [Cheetah templates]: http://www.cheetahtemplate.org/ "chetah"
  [Cheesecake]: http://sourceforge.net/projects/cheesecake/ "Cheesecake"
  [trace2html]: http://cheeseshop.python.org/pypi/trace2html/
    "Trace2html"
  [Crunchy frog]: http://crunchy.sourceforge.net/ "Crunchy"
  [Pygments]: http://pygments.pocoo.org/ "Pygments"
  [http://hg.programmation-python.org/repositories/public]: http://hg.programmation-python.org/repositories/public
  [follow this link]: http://programmation-python.org/pycommunity/
