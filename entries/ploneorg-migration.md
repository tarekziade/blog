Title: plone.org migration 
Date: 2008-07-01 22:03
Category: plone, python, zope

Plone.org migration to Plone 3 is taking a bit longer than expected, but
it should turn into reality soon.   
  
There will be many improvements on the set of packages the website uses
(I am thinking in particular about **Maurits**'s work on POI that will
speed up the trackers, but it is just an example), and blobs should be
used for the products section (more than 700 projects are registered
there).   
  
I worked last week-end on the products section, by finishing
[collective.psc.mirroring][], which will copy all packages that are
uploaded at plone.org into a file system directory. This directory will
be published directly by Apache so the website will become a new package
location for zc.buildout (find-links section) and easy\_install calls
without invoking the Plone instance.   
  
Now I am focusing on PloneSoftwareCenter (PSC) migration. It is a
pretty interesting topic: for every project located in the products
folder with releases, I am going to extract its "distutils ids". These
ids are the name set in the setup.py file for each release.   
  
I will then look at PyPI through XML-RPC if the package is also
released, using the id. In that case, and if the author email is the
same on both side, I will validate that the project on plone.org "owns"
the given distutils id. From there PSC will act like PyPI and will
reject uploads of packages if the user is not the owner of the project
that owns the package id.   
  
Of course there will be errors and some people might feel like their
package has been hijacked if they cannot upload their packages. But this
should be minor and should be OK after a while. A mail will soon be send
to the community to ask people to check that they are synced between
PyPI and plone.org.   
  
I am really excited about this work because plone.org will then be
compatible with distutils *register* and *upload* commands, which means
that people will be able to update plone.org products section like they
do with PyPI : through a single commande line.   
  
Hey Sidnei, what you thought of several years ago is about to turn
true. ;)   
  
**Edit**: My apologies goes to Maurits, who did the work on POI, not
Reinout, his brother ;)

  [collective.psc.mirroring]: http://pypi.python.org/pypi/collective.psc.mirroring
