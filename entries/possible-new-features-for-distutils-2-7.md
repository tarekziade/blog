Title: Possible new features for Distutils 2.7
Date: 2010-01-07 06:46
Category: python

While PEP 345 and PEP 386 are waiting for [the final approval][], I am
back at work on Distutils code work, PEP 376, Distribute, and the
HitchHicker guide to Packaging. The latter is growing faster than I have
expected, thanks to the contributions of John Gabriele. [It has quite
some content already][]. I think the guide is an important task, and
I'll try to focus on it in this first trimester.   
### Distutils 2.7 new features

  
Python 2.7 first beta version is [around the corner][], and once it's
reached we can't add new features. So, besides the code that will be
changed if the PEPs we worked on at Distutils-SIG are accepted, here's a
list of small features I'd like to introduce in Distutils:   
-   **a test command**, that just uses the new [unittest discovery
    script][] to run unittest-compatible tests.
-   **a new option for sdist called 'extra\_files'**, that will allow to
    list extra files to be included in the distribution. These files
    will not be installed by 'install', just be part of the
    distribution. This will allow including files like CHANGELOG, etc..
    without having to use a MANIFEST template.
-   **a very basic pre/post commit hook for the install command**. These
    hooks will be deactivated when any bdist\_\* command runs install to
    create the binary tree. Now for bdist\_rpm own hooks, I guess the
    best way would be to make install consumes the same two options than
    bdist\_rpm (pre-install, post-install) so a project will be able to
    define a hook that is used by RPM and/or *python setup.py install*

  
If you think about something that should be added in 2.7, speak up !

  [the final approval]: http://mail.python.org/pipermail/python-dev/2010-January/094771.html
  [It has quite some content already]: http://guide.python-distribute.org
  [around the corner]: http://www.python.org/dev/peps/pep-0373/#release-schedule
  [unittest discovery script]: http://docs.python.org/dev/library/unittest.html#test-discovery
