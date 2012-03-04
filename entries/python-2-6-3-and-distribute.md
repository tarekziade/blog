Title: Python 2.6.3 and Distribute.
Date: 2009-10-03 14:20
Category: distribute, distutils, python

[Python 2.6.3][] is out, will a lot of bugs fixed. I had my share with
Distutils and fixed quite a few, and 2.6.3 is looking very good so far !
  
  
Just a quick note for Setuptools users: you might bump into a problem
if you provide a C extension. The setuptools code makes some assumptions
on *how* and in *which order* the Distutils *build\_ext* API are called.
It also overrides some of these API to do some internal extra work. In
other words, the way Setuptools patches Distutils makes it very
sensitive to any internal Distutils code changes. In this particulare
case you might have this bug:   
   File "...setuptools/command/build_ext.py", line 85, in get_ext_filename   KeyError: 'xxx'

  
The fix is quite simple, it can be done by the end-user or in your
package (which is better of course).   
-   In your package : use "[Distribute][] \>= 0.6.3" distribution
    instead of the usual "Setuptools == 0.6c9" distribution in you
    dependencies list. The code remain unchanged and you can still
    "import setuptools" and have it working fine.
-   As an end-user: just do a Distribute installation and your fine
    "(sudo) easy\_install Distribute"

  
Hang in *\#distutils* on Freenode, or drop a mail in [distutils-SIG][]
in case you have a problem.   
  
Just to make things clear: The Distribute 0.6.x series is a mirror of
Setuptools 0.6c9 code, with bug fixes.

  [Python 2.6.3]: http://python.org/download/
  [Distribute]: http://ttp://pypi.python.org/pypi/distribute
  [distutils-SIG]: http://mail.python.org/mailman/listinfo/distutils-sig
