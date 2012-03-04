Title: bdist_rpm is dead, long life to Py2RPM
Date: 2011-03-25 16:39
Category: mozilla, python

One thing I've learned along the way while working on Python packaging
matters is that it's quite impossible to maintain in the stdlib scope
tools like bdist\_rpm, which builds RPMs using Distutils' enabled
projects.   
  
I've asked around, and it turns out 9 out of 10 of the packagers are
not using it for their daily RPM packaging work, unless they are also
the developers of the projects to package. They use their own tools.   
  
There are several reasons:   
-   bdist\_rpm makes a lot of assumptions when creating the spec files.
-   there are no way to customize some sections in the spec file that
    will be generated.
-   the spec file is most of the time edited by packagers before it's
    actually used, so the automatic full translation from Python
    metadata to RPM metadata is a false good idea. And while packagers
    have templates, they eventually end up working manually in the spec.
-   What's good for RedHat 5 is not for the latest Fedora
-   Python sdtlib cycle does not match the distro cycles. So even if we
    update it, it would be soon deprecated again

  
So, when it was suggested a few months ago to add a bdist\_deb command
in Distutils, I told people that anything related to creating deb files
should be a project on its own. And [stdeb][] seems to have this role
now.   
  
For Windows, it's a bit different: tools like bdist\_msi are easier to
maintain and we don't have many flavors of packaging in the win32 world,
just one. The release cycle of Python's stdlib fully works here.   
  
Following this principle** bdist\_rpm has been removed from
Distutils**.   
  
So for the RPM world I want the same standalone project, that provides
RPM goodies for Pythoneers, on the top of Distutils2 a.k.a. the new
***packaging*** module in Python 3.3, to replace bdist\_rpm.   
  
As a matter of fact I've started this project a while ago for my work
at Mozilla and called it ***pypi2rpm*** then. It's called like this
because its main feature is to create for CentOS a RPM package out of a
project released at PyPI.   
  
Try it:   
   $ pip install pypi2rpm

    $ pypi2rpm.py SQLAlchemy

    ...long output...

    /tmp/ok/python26-sqlalchemy-0.6.6-1.noarch.rpm written

  
This script uses **Distutils2** to browse PyPI and sort versions, then
uses a custom version of bdist\_rpm to invoke rpmbuild. This script can
also create a RPM out of an existing project, by using an existing .spec
file. It bypasses setup.py.   
  
But this is just a quick script I've created for my needs. In the long
term, I want to rename it to Py2RPM and make it the replacer of
bdist\_rpm. The features I want it to provide are:   
-   A standalone script that can be used to create RPMs, by using a
    configurable command-line call
-   A standalone script that can be used to generate a spec file out of
    a setup.cfg file
-   A way to read all options from setup.cfg, and to avoid to duplicate
    metadata fields like name, version etc
-   A way to be aware of the differences between the various RPM-based
    distros.
-   A feature to call via RPC the various CentOS, Fedora, etc
    repositories, to check if the name is already taken, if some files
    conflicts, etc
-   A distutils2 command, so the script can be called from the top-level
    **pysetup** script if wanted.

  
On a side note (but this is another blog post), setup.cfg is being
spec-ed out and the spec will be versioned. This will allow other tools
from the RPM world, *{put a packaging system name here}*, to consume it
and provide similar features. And this file will soon be available at
PyPI so we can work with it without downloading the tarball of the
release.   
  
If you're interested into Py2RPM, please get in touch with me. I am not
a RPM expert at all, and I'd be happy to have more people involved.

  [stdeb]: http://pypi.python.org/pypi/stdeb
