Title: PloneSoftwareCenter: news from the PyPI front
Date: 2008-01-07 14:44
Category: plone, python, zope

I have almost finished the work in the pypi branch for
PloneSoftwareCenter PyPI support. There are a few things to polish but
it works. (90% of the work was already done by Sidnei, so I have done
mostly minor refactorings). I guess I'll polish it until Alex Clark
merge it into the trunk.   
  
If you want to give it a try, you can use the buildout I have added in
the collective here:   
  

[http://svn.plone.org/svn/collective/PloneSoftwareCenter/buildout/branches/pypi/
  
][]   
I also have a running prototype here:   
  
[http://products.ingeniweb.com/catalog][]   
  
were we are trying it. This will be our public PSC instance and will
soon contain all our packages and some public packages mirrored or
repackaged as eggs.   
### Current features

  
The features are:   
-   support of distutils and setuptools register and upload commands
-   automatic creation of projects and releases
-   support of PyPI's simple page, so it can be used by easy\_install
    and zc.buildout

  
If you want to try it up ask me for a user account.   
### Trove classification

  
The current default categories uses PyPI to classify the packages, and
everything is hooked to the register command. So when you upload a
package, it will appear in the proper categories in the software center.
  
  
That said, you can change the categories to manage your own. When a
package is uploaded, it will just ignore the unknown categories. I am
working on PyPI side so the Cheeseshop itself works the same way.   
(hopefully, it will be accepted, because the guys from the catalog team
are helping me out in polishing my proposal)   
  
see my document at : [http://wiki.python.org/moin/EnhancedPyPI][] (see
*Making PyPI permissive for Trove classification*)   
### Dealing with several PyPI-like servers

  
Last but not least, as a Plone developer, the final goal is to be able
to register and upload packages to both PSC and PyPI. This is a bit
tricky with the current distutils implementation and I am working on
this so it can deal with several servers.   
  
The final form will be to be able to do:   
   $ python setup.py register sdist upload -r http://example.com/repository       # registering and uploading at example.com

    $ python setup.py register sdist upload        # registering and uploading at PyPI

  
There are some default policies in PSC though, to avoid people
uploading projects and file to easily: if the user is a simple member, a
register command call will create a project and submit it, and the
upload command won't work until the project has been accepted and
published.   
### Next steps

  
I am really excited about having the same standard everywhere, and to
be able to deploy our packages in the community through a simple command
line:   
-   at the cheeseshop
-   in our private software center
-   in our public software center
-   hopefully, in plone.org when it goes Plone 3.x

  
The next steps will be:   
-   to get some feedback from the Plone community, and build a TODO list
    with it (I have to collect Wichert remarks from the ML to start to
    build it)
-   to polish the code
-   to add XML-RPC APIs, like PyPI has

  [http://svn.plone.org/svn/collective/PloneSoftwareCenter/buildout/branches/pypi/
    
 ]: http://svn.plone.org/svn/collective/PloneSoftwareCenter/buildout/branches/pypi/
  [http://products.ingeniweb.com/catalog]: http://products.ingeniweb.com/catalog
  [http://wiki.python.org/moin/EnhancedPyPI]: http://wiki.python.org/moin/EnhancedPyPI
