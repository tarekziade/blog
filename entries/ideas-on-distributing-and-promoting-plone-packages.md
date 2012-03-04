Title: Ideas on distributing and promoting Plone packages
Date: 2007-12-21 11:10
Category: plone, python, zope

**Edit: **Just after I posted this, I found [Sidnei's work][], so it is
basically what I was thinking of. Good job :)   
  
**How to promote Plone packages today ?**   
  
Since eggs became a standard in Zope, distribution of Plone packages
can be done directly to the [Cheeseshop][]. This is quite nice since
anyone can invoke an upload command like this:   
   $ python setup.py bdist_egg upload

  
This makes the package uploaded and available to anyone. This also made
anyone able to promote his work without having to set up a web site or
to study how the community works on that point.   
  
I am pretty new to the Plone community, and I am trying to find the
best way to promote Plone packages we do here.   
  
My guess is that the Cheeseshop is perfect for Python package but not
enough for Plone packages: in order to promote them, the best place is
the [plone.org software center][]. It brings a tracker, a front page and
a release folder. In other words, anyone who wants to publish a Plone
product that is seen by the whole community has to take care of
uploading its packages into plone.org, or setting a link there, and to
the cheeseshop.   
  
If you have a better way to promote your Plone products, let me know !
  
  
I think this process could be enhanced a little bit through automation.
  
  
**Making plone.org pypi-compatible**   
  
The Pypi index has two main features [PloneSoftwareCenter][] does not
afaik:   
-   it implements a [file\_upload method][], that is called by
    setuptools when the upload command is invoked
-   it provides package index pages that allow [easy\_install][] to look
    for a package

  
These two features are very simple, and could be added in Plone
Software Center by:   
-   adding a file\_upload view on the products page
-   providing an index-compatible view (PSC has a [DOAP][] support
    though)

  
In other words, that would allow calling the upload command on
plone.org like this:   
   $ python setup.py bdist_egg upload --repository=http://plone.org/products/

  
Another command could be added in setuptools to distribute a plone
package automatically:   
   $ python setup.py plone_promote

  
plone\_promote would invoke bdist\_egg then make an upload on
cheeseshop and/or plone.org. In other words, that would allow package
developers to promote their work without pain.   
  
Having such feature would also allow people to create their own
Pypi-compatible private software center when they deal with private
package they want to make available for instance to private project
buildouts.   
  
If people think it's a good idea, I am willing to code it in PSC (I
made a proposal on the bug tracker).

  [Sidnei's work]: http://awkly.org/2006/01/28/pypi-like-functionality-to-plonesoftwarecenter/
  [Cheeseshop]: http://cheeseshop.python.org/pypi
  [plone.org software center]: http://plone.org/products
  [PloneSoftwareCenter]: http://plone.org/products/plonesoftwarecenter
  [file\_upload method]: https://svn.python.org/packages/trunk/pypi/webui.py
  [easy\_install]: http://peak.telecommunity.com/DevCenter/EasyInstall
  [DOAP]: http://usefulinc.com/doap/
