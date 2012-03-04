Title: Using RelStorage with Plone 3
Date: 2008-02-02 23:10
Category: plone, python, zope

Last week, Shane Hattaway made available [RelStorage][] on svn.zope.org.
This product replaces PGStorage and allows you to switch from
FileStorage (the Data.fs file) to a Postgresql or Oracle storage for
ZODB pickles. ZEO is not needed anymore in that configuration, and each
Zope instance calls the same Postgresql server.   
  
According to Shane, RelStorage handles high concurrency better than the
standard combination of ZEO and FileStorage. So I have started to make a
few tests with it to see how we can use it on some projects.   
  
I have made a few changes to plone.recipe.zope2instance to be able to
define a buildout that uses RelStorage, and created a buildout on the
collective that runs a Plone 3 over RelStorage.   
  
The buildout sets a relstorage configuration and patches the ZODB 3.7
code. Instead of a file-storage option in the buildout.cfg file, a
rel-storage option is added:   
   rel-storage =

        type postgresql

        dbname zodb

        user postgres

        host localhost

        password postgres

  
If you want to try it with your Postgres or Oracle server, you can get
it from the collective here:
[http://svn.plone.org/svn/collective/collective.relstorage/trunk/][]   
  
Notice: the script that patches the ZODB code does a system call
instead of using the difflib module, so you need to have the patch
program available at the prompt. So I guess it will fail under windows.
  
  
Notice 2: The buildout installs psycopg2 egg, but not the oracle one.

  [RelStorage]: http://wiki.zope.org/ZODB/RelStorage
  [http://svn.plone.org/svn/collective/collective.relstorage/trunk/]: http://svn.plone.org/svn/collective/collective.relstorage/trunk/
