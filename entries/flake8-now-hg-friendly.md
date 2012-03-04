Title: Flake8 now Hg friendly
Date: 2011-02-12 13:40
Category: mozilla, python

I apologize in advance to the authors of [pep8][] and [Pyflakes][], as
[Flake8][] is a horrible hack on the top of those two tools. But it's
really what we needed at Mozilla Services to check that anything that
lands into our Python repositories follow these simple rules:   
-   PEP 8 compliant
-   No unused imports
-   No undefined names

  
So Flake8 is a simple script that calls pep8 and pyflakes and merges
the output, so you get all warnings grouped by files, instead of having
to run both tools one after the other. I've stripped all options for now
and you just call the script over a single Python file, over a directory
or by using a \*.py glob-style pattern.   
  
I added a few features on the top of it:   
-   Python files that starts with this header are skipped: ***\# flake8:
    noqa***
-   Lines that contains a ***\# NOQA*** comment at the end will be
    skipped

  
In the 0.4 version I have added a Mercurial hook you can use to
automatically control your code when you call the ***push*** or the
***qrefresh*** command.   
  
Here's how you configure it in your* .hgrc* once Flake8 is installed:   
   [hooks]

    commit = python:flake8.hg_hook

    qrefresh = python:flake8.hg_hook



    [flake8]

    strict = 0

  
If *strict* option is set to **1**, any warning will block the commit.
When *strict* is set to **0**, warnings are just displayed in the
standard output. I use it in non-strict mode, so I just get a display of
the issues my code has.   
  
Stuff I might add in the future:   
-   A cleaner merge of pep8 and PyFlakes options
-   ***EDIT: Added in 0.5*** ~~A[cyclomatic complexity metric][] so I
    can print out "Hey what's up with all those loops ? flat is better
    than nested!"~~

  
A more ambitious feature would be to detect similar code patterns and
warn the developer that the function he's adding looks a lot like
function Foo in module Boo. This implies using a tool like
[CloneDigger][], but also keeping in a local, centralized database, some
kind of index of every piece of code that gets committed. This is
mandatory to speed up the comparison work and avoid introducing huge
lags as the code base grows. Mmmm that would be a good GSOC topic !

  [pep8]: http://pypi.python.org/pypi/pep8
  [Pyflakes]: http://pypi.python.org/pypi/pyflakes
  [Flake8]: http://pypi.python.org/pypi/flake8/
  [cyclomatic complexity metric]: http://en.wikipedia.org/wiki/Cyclomatic_complexity
  [CloneDigger]: http://clonedigger.sourceforge.net/
