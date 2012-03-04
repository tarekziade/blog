Title: iw.recipe.backup and other zc.buildout recipes
Date: 2008-03-25 07:20
Category: plone, python, zc.buildout, zope

A new recipe has been added to the iw.recipe.\* family:
[iw.recipe.backup][].   
  
If you use zc.buildout to deploy Python applications in production,
this one can be used to backup a buildout folder, before any upgrade is
attempted, or for a daily backup. It creates an archive with a timestamp
on its name, in a defined folder, with the whole folder content. Some
directories can be excluded if needed.   
  
This script is not doing fine-grained backups of the Data.fs like
repozo.py does, but can be combined with it if this finesse is required.
The recipe creates two scripts in the bin folder: **backup** and
**restore**.   
  
**backup** creates an archive and takes no parameters, whereas
**restore** takes an archive name and decompress it into the buildout
folder. The latter does a backup before it decompresses the archive for
more safety.   
  
Last, it will raise an error if the backup folder is located within the
buildout folder ;), and logs all commands into a log file. This is a
tiny recipe, but provides a simple way to backup your buildouts in a
single call, no matter the platform you are in.   
  
Other recipes we provide at this time are:   
-   [iw.recipe.cmd][]: provides a way to execute shell calls, or inline
    Python calls. This is useful when you need to set a few things when
    a buildout is built, that does not worth creating a new recipe;
-   [iw.recipe.fetcher][]: similar to wget. We use it to build
    python-win32.zip archive, to get all installers on the web;
-   [iw.recipe.fss][]: will let you configure FileSystemStorage, so no
    extra step is required;
-   [iw.recipe.pound][]: compiles Pound load balancer, and creates its
    configuration file, so it can be run directly;
-   [iw.recipe.sendmail][]: set zope.sendmail as the default mail sender
    in a Zope 2-based application. This is useful if you wish to have a
    fast and robust mailhost service in your Plone sites;
-   [iw.recipe.squid][]: This recipe installs all parts needed to run a
    Squid server dedicated to serve a Zope application, staying friendly
    with Apache and setting things nicely for Plone;
-   [iw.recipe.subversion][]: recipe to checkout a svn location into a
    part. It is different from [infrae.subversion][] because it creates
    a tarball out of the subversion checkout, and put it in the
    downloads folder. In other words, it works offline as well as long
    as the tarball was built once. It doesn't have the nice feature
    infrae.subversion provides which is a code checker that will raise
    an error when buildout tries to remove a changed file. But as we use
    the develop feature of buildout to create our code, we didn't need
    that feature. Subversion checkouts are useful to us when we want to
    use a bleeding-edge version of a third-party package that has not
    been released yet;
-   [iw.recipe.template][]: this one provides a way to write files based
    on Cheetah templates, like Python Paste does, and is useful for
    micro-needs, like iw.recipe.cmd.

  
If you use one of those recipes and whish to make a feature request or
a bug report, I have created a new space on plone.org to have a bug
tracker for all recipes: [http://plone.org/products/iw-recipes/issues][]

  [iw.recipe.backup]: http://pypi.python.org/pypi/iw.recipe.backup#detailed-documentation
  [iw.recipe.cmd]: http://pypi.python.org/pypi/iw.recipe.cmd
  [iw.recipe.fetcher]: http://pypi.python.org/pypi/iw.recipe.fetcher
  [iw.recipe.fss]: http://pypi.python.org/pypi/iw.recipe.fs
  [iw.recipe.pound]: http://pypi.python.org/pypi/iw.recipe.pound
  [iw.recipe.sendmail]: http://pypi.python.org/pypi/iw.recipe.sendmail
  [iw.recipe.squid]: http://pypi.python.org/pypi/iw.recipe.squid
  [iw.recipe.subversion]: http://pypi.python.org/pypi/iw.recipe.subversion
  [infrae.subversion]: http://pypi.python.org/pypi/infrae.subversion
  [iw.recipe.template]: http://pypi.python.org/pypi/iw.recipe.template
  [http://plone.org/products/iw-recipes/issues]: http://plone.org/products/iw-recipes/issues
