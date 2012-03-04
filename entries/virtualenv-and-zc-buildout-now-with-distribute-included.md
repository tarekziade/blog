Title: virtualenv and zc.buildout now with Distribute included
Date: 2009-11-07 01:36
Category: distribute, distutils, python, zc.buildout

We are still actively working in fixing all the remaining bugs in
[Distribute][] (our Setuptools fork).   
  
But we have reached an important milestone this week: both
[virtualenv][] and [zc.buildout][] now comes with an option to switch to
Distribute.   
  
In virtualenv:   
   $ virtualenv --distribute ENV

  
In zc.buildout, using its bootstrap.py file:   
   $ python bootstrap.py --distribute

  
Enjoy !   
  
For those who may wonder why they should switch to Distribute over
Setuptools, it's quite simple:   
-   Distribute 0.6.x is a drop-in replacement for Setuptools
-   Distribute is actively maintained, and has over 10 commiters
-   Distribute 0.6.x offers Python 3 support !

  
And if you still struggle with packaging issues, the place to hang
around to get some help is the \#distutils IRC channel on Freenode.

  [Distribute]: http://pypi.python.org/pypi/distribute
  [virtualenv]: http://pypi.python.org/pypi/virtualenv/1.4
  [zc.buildout]: http://pypi.python.org/pypi/zc.buildout
