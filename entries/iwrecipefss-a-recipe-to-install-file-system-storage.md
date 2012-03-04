Title: iw.recipe.fss : a recipe to install File System Storage
Date: 2007-10-23 07:56
Category: plone, python, zope

  

  
  
# What is FSS ?

  
When you need to work with a lot of static files in your Plone website,
you should consider using [File System Storage][] (FSS). It's an
Archetypes storage that can handle files like PDF, images or small
videos. It prevents the growth of the ZODB. It's not like [Blobs][],
because the files are not transactionals. This means you won't have to
worry about network performances when you use ZEO: nothing will be
copied from a node to another. You just have to use a NFS point to make
sure all nodes uses the same files.

  
The missing part though, was to be able to easily deploy FSS using the
standard way.   

  
  
# Deploying FSS

  
In Plone world, [zc.buildout][] is now the leading project in the
deployment area. Everyone should read [Martin's tutorial][] on how to
use it. It makes a typical Plone deployable in a matter of minutes with
no pain. It is based on a configuration reader that instanciate recipes
objects in charge of installing a part of the system. You have recipes
for apache, ldap, etc. [See existing public recipes at Cheeseshop][].   
  
[iw.recipe.fss][] is a recipe that takes care of creating file system
folders and the configuration file used by the Product.   
  
To use it, just insert a section in your buildout file (it's called a
part in buildout language) that describes each system storage, and the
path to the configuration file:   
   [buildout]

    parts:

        ...

        fss

        ...



    [fss]

    recipe = iw.recipe.fss

    conf = ${zopeinstance:location}/etc/plone-filesystemstorage.conf



    storages =

        storage_name /site/storage_path directory

  
See the recipe's [README.txt][] for all options.   
  
That's it. I love buildout.   

  
  
# More recipes to come

  
There are a lot of recipe available in the Python Index, but we still
missing some to perform every kind of deployment. Besides the Plone
recipes here are the recipes that I find realy usefull:   
-   [**infrae.subversion**][]: clean, simple way, to checkout a piece of
    code from a Subversion repository. It's a perfect one to create
    developer buildouts.
-   [**zc.recipe.cmmi**][]: the configure-make-make install recipe. Will
    perform a compilation and local installation) of Makefile compatible
    packages under BSD/Linux.
-   [**zc.recipe.egg**][]: this one is very useful if an egg needs a
    special environment. For example if it needs a compiled library
    created with zc.recipe.cmmi.

  
We have more recipes that are being coded here at Ingeniweb, to cover
our needs in deploying Plone instances with buildout. I'll try to blog
on them everytime we update the Cheeseshop. If you create recipes
yourself I encourage you to share them on Cheeseshop. Sharing recipes,
in my humble opinion, is an important thing to do in a community: it
helps standards to raise because it shows how people uses software in
real infrastructures.

  [File System Storage]: http://ingeniweb.sourceforge.net/Products/FileSystemStorage/
  [Blobs]: http://tarekziade.wordpress.com/2007/09/14/to-blob-or-not-to-blob/
  [zc.buildout]: http://cheeseshop.python.org/pypi/zc.buildout/1.0.0b30#detailed-documentation
  [Martin's tutorial]: http://plone.org/documentation/tutorial/buildout
  [See existing public recipes at Cheeseshop]: http://cheeseshop.python.org/pypi?:action=search&term=recipe&submit=search
  [iw.recipe.fss]: http://pypi.python.org/pypi/iw.recipe.fss/0.1c
  [README.txt]: http://cheeseshop.python.org/pypi/iw.recipe.fss/0.1bdev-r6471
  [**infrae.subversion**]: http://cheeseshop.python.org/pypi/infrae.subversion/1.0dev-r26037
  [**zc.recipe.cmmi**]: http://cheeseshop.python.org/pypi/zc.recipe.cmmi/1.0.2
  [**zc.recipe.egg**]: http://cheeseshop.python.org/pypi/zc.recipe.egg/1.0.0b5
