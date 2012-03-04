Title: how to run your own private PyPI (Cheeseshop) server 
Date: 2008-03-20 11:26
Category: plone, python, zope

  
PloneSoftwareCenter 1.5 is heavily developed and not yet released, but
the current trunk code is working well to use it as a PyPI-like server.
It can be really useful for companies that develop Python software and
are looking for a way to centralize their eggs internally. That's what
we use now at Ingeniweb to work on customer projects.
  
  
  
This tutorial explains how to set a cuttting-edge PloneSoftwareCenter
server, if you want to be an early-adopter of what will be the next
version running on plone.org software center in a few months (but this
code is to be used at your own risks of course ;))
  
  
  
# Why a private PyPI ?

  
You have some python packages you want to treat the same way the
Cheeseshop does. In other words you want to work with them with
[*easy\_install*][], *[zc.buildout][]*, etc..   
  
But these packages are private to your company...   
  
The simplest way is to store your eggs on some network folder. But
*distutils* and *setuptools* provide a nice set of commands to
automatically build and upload eggs at PyPI or any server that
implements PyPI apis.
  
  
# How ? PloneSoftwareCenter !

  
The Plone community provides a nice tool to manage Python packages, and
it is PyPI compatible. In other words it can act like Cheesehop to
interact with your command line tools.   
  
It also provides an extensive set of features to manage your releases,
run your bug trackers, etc.   
  
See the [plone.org products section][], it is powered by PSC.
  
  
# 4 steps to install

  
Thanks to zc.buildout, a Plone Software Center (PSC) is really easy to
setup. There's no binary distribution yet though, so you need to compile
a few things.   
  
## Step 1 - Pre-requests

  
If you are under Windows, grab this archive :
[http://release.ingeniweb.com/third-party-dist/python2.4.4-win32.zip][]
  
decompress it, and run "install.bat". It will install Python 2.4
together with a set of tools, and PATH updates.   
  
If you are under Linux, make sure you have gcc, subversion and make
installed. Then install easy\_install and PIL,   
like this:   
   $ wget http://peak.telecommunity.com/dist/ez_setup.py

    $ python ez_setup.py

    $ easy_install http://release.ingeniweb.com/third-party-dist/PILwoTk-1.1.6.4.tar.gz

  
  
  
## Step 2 - installing PSC

  
1.    
   Make a directory on your system called *softwarecenter*

      
2.    
   Get into it and grab PSC code with the svn command line:

      
      
       $ svn co http://svn.plone.org/svn/collective/Products.PloneSoftwareCenter/buildout/trunk .

      
3.    
   run the buildout with this set of commands:

      
      
       $ python bootstrap.py

        $ bin/buildout

      

  
> It will take some time, to grab all elements needed to build PSC.

  
4.  run the server   
       $ bin/instance start

      
5.    

      

  
  
  
## Step 3 - setting up PSC

  
Let's create a Plone website with a PloneSoftwareCenter instance:   
1.  Open a browser and go to [http://localhost:8080/manage][]. The
    login/password is admin/admin.
2.  On the left part, there's a dropbox, select "Plone Site" the hit the
    add button
3.  In the form, set the id to "plone" and hit enter.
4.  Go to [http://localhost:8080/plone/prefs\_install\_products\_form][]
5.  Check "PloneSoftwareCenter" on the left side and hit "Install"
6.  Go to [http://localhost:8080/plone][]
7.  In the "Add new..." menu, Click on "software center"
8.  In the form, in the Title, put "Catalog"
9.  Check Use Classifiers to display Categories (with Topic :: \*) under
    Classifiers
10. Hit the Save button

  
Your Software Center is ready and available at
[http://localhost:8080/plone/catalog][]
  
  
## Step 4 - setting up the client-side

  
Now let's set the client-side so people can use your Software Center:   
1.    
   install iw.dist:

      
      
       $ easy_install iw.dist

      
2.    
   create a file in your home directory, called .pypirc with this
    content:

      
      
       [distutils]

        index-servers =

          pypi

          local



        [pypi]

        username:YOUR_PYPI_LOGIN

        password:YOUR_PYPI_PASSWORD



        [local]

        repository:http://localhost:8080/plone/catalog/

        username:admin

        password:admin

      

  
Of course, the localhost value will differ if you are located on
another machine..   
  
iw.dist adds two new commands in distutils: mregister and mupload.
These commands enhance register and upload to make distutils work with
multiple servers. This should be merged hopefully in Python 2.6 very
soon.
  
  
  
# Let's use it !

  
Now, you will have two new commands in distutils, called '*mregister*'
and '*mupload*' that will let you use either your PSC either PyPI.   
  
Let's upload an egg into PSC:   
   $ python setup.py mregister sdist bdist_egg mupload -r local

  
Let's upload an egg into PyPI:   
   $ python setup.py mregister sdist bdist_egg mupload -r pypi

  
if -r is omited, pypi is the default one.   
  
If you want to use PSC in zc.buildout or easy\_install, you can provide
[http://localhost:8080/plone/catalog/simple][] as a find-links or index
value:   
   [buildout]  find-links = http://localhost:8080/plone/catalog/simple

  
Or:   
   $ easy_install -f http://localhost:8080/plone/catalog/simple my.egg

  
  
That's it !

  [*easy\_install*]: http://peak.telecommunity.com/DevCenter/EasyInstall
  [zc.buildout]: http://pypi.python.org/pypi/zc.buildout
  [plone.org products section]: http://plone.org/products/
  [http://release.ingeniweb.com/third-party-dist/python2.4.4-win32.zip]:
    http://release.ingeniweb.com/third-party-dist/python2.4.4-win32.zip
  [http://localhost:8080/manage]: http://localhost:8080/manage
  [http://localhost:8080/plone/prefs\_install\_products\_form]: http://localhost:8080/plone/prefs_install_products_form
  [http://localhost:8080/plone]: http://localhost:8080/plone
  [http://localhost:8080/plone/catalog]: http://localhost:8080/plone/catalog
  [http://localhost:8080/plone/catalog/simple]: http://localhost:8080/plone/catalog/simple
