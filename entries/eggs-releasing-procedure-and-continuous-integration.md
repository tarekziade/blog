Title: Eggs: releasing procedure and continuous integration 
Date: 2008-06-08 11:27
Category: plone, python, zc.buildout, zope

*Disclaimer: this post is Subversion-centric*   
  
When releasing a setuptools based-package to the world, developers will
eventually tag it as a stable version, then upload it to PyPI or to
their own website. So typically they create a **branch** out of the
**trunk**, fix the **version**, then create a **tag** for the release.   
  
Now for continuous development releases, where people get for example a
daily snapshot from the trunk, having a dev suffix to the egg version
makes it possible to distinguish it from a stable release, so
'my.package-2.4dev' will not superseed 'my.package-2.4'. So a given
package will need a *dev* prefix in its trunk, that gets removed in the
branch where the next release occurs.   
  
From there, easy\_install will be able to distinguish them.   
  
The question is: **how should we do this ?**   
### The Zope 3 way

  
The Zope 3 egg collection has a simple way to manage it, describe here:
[http://svn.zope.org/\*checkout\*/Sandbox/philikon/foundation/releasing-software.txt][].
The packages have a dev tag suffix in the version metadata, that is
removed in the subversion branch used to tag and release   
  
This is simple and straight forward. Although, releasing the trunk has
to be done manually. The problem is that any release of the trunk will
have the same name for a given version (my.package-2.4dev) , and in some
case people won't upgrade their environment because the archive keeps
the same name.   
### The setuptools way

  
Setuptools comes with a continuous integration feature that allows
people to push the *dev* tag in setup.cfg. Then it adds it automatically
to the archive name when it is generated.   
  
see:
[http://peak.telecommunity.com/DevCenter/setuptools\#managing-continuous-releases-using-subversion][]
  
  
Building a release will then consist of using the same process than
Zope 3 one, except that the tag is removed from the setup.cfg file this
time.   
  
Now if you try to release the trunk using disutils *sdist* or
*bdist\_egg* command you will automatically get a dev suffix and the
Subversion revision number sticked to it. This means that each new
revision can generate a new version that will have a distinct name:   
-   my.package-2.4dev-r1245
-   my.package-2.4dev-r1246
-   ...

  
easy\_install will grab the latest trunk revision when
"my.package-2.4dev" is required, and handle upgrades the right way. This
is better that a manual dev tag because when you re-release a new
version of the trunk, it will superseeds and therefore upgrades previous
revisions.   
  
Another nice feature is to be able to provide to easy\_install a
subversion link directly, as long as you append the egg full name to the
link:   
   easy_install http://my.svn/my.package/trunk#egg=my.package-dev

  
### collective.releaser

  
The problem with setup.cfg is that if you forget to remove the dev tag
from it when releasing a stable version (you bad boy), you will get the
dev-r4565 suffix in the egg name.   
  
[collective.releaser][] takes care of this with a new setuptools
command called **release**, by creating a release branch and removing
the dev tag automatically. It upgrades the CHANGES.txt file and
version.txt for Plone products.   
  
It also registers and uploads the package to any PyPI-like server. To
decide where the package should be sent, it looks at the
*release-packages* variable into the *.pypirc*, to see if the package
name matches it. To release all packages to PyPI a default file would
be:   
   [distutils]

    index-servers =

      pypi

  
   [pypi]

    username:tarek

    password:secret

    # regular expression-based variable

    release-packages =

      .*

  
From there, making a release is as simple as:   
   $ python2.4 setup.py release

    running release

    This package is version 0.1.1

    Do you want to run tests before releasing ? [y/N]: n

    Do you want to create the release ? If no, you will just be able to deploy again the current release [y/N]: y

    Enter a version [0.1.1]: 0.1.2

    Commiting changes...

    Creating branches...

    ...

    Running "mregister sdist bdist_egg mupload -r pypi"

    running mregister

    Using PyPI login from /home/tarek/.pypirc

    Registering iw.resourcetraverser to http://pypi.python.org/pypi

    ...

    running mupload

    Using PyPI login from /home/tarek/.pypirc

    Submitting dist/iw.resourcetraverser-0.1.2.tar.gz to http://pypi.python.org/pypi

    Submitting dist/iw.resourcetraverser-0.1.2-py2.4.egg to http://pypi.python.org/pypi

    ...

    0.1.2 released

  
As described on its PyPI page, it has a plugin system to perform extra
steps when a release is made. For instance, it is provided with a mail
hook to be able to send mails everytime a release is made.   
  
The tool is pretty new and needs to be smoothed up. For instance, we
need to add a few extra controls like making sure long\_description is
reST-valid. But It works, and is being used by a few fellows in the
Plone community already :).   
  
Last, for continuous releases from the trunk, you can set up an alias:
  
   $ python setup.py alias devrelease mregister sdist mupload

  
You will then be able to upload trunk releases with a single call:   
   $ python setup.py devrelease

  
The idea is to provide it as the standard tool to release add-on
Products when Plone.org will be upgraded and able to interact with
distutils commands. I will promote it through the work I am doing for
the PSPS task I am championning ([Improve release procedures for add-on
products][]), but it has to live a bit.   
  
Help and opinions welcome !

  [http://svn.zope.org/\*checkout\*/Sandbox/philikon/foundation/releasing-software.txt]:
    http://svn.zope.org/*checkout*/Sandbox/philikon/foundation/releasing-software.txt
  [http://peak.telecommunity.com/DevCenter/setuptools\#managing-continuous-releases-using-subversion]:
    http://peak.telecommunity.com/DevCenter/setuptools#managing-continuous-releases-using-subversion
  [collective.releaser]: http://pypi.python.org/pypi/collective.releaser/
  [Improve release procedures for add-on products]: Improve%20release%20procedures%20for%20add-on%20products
