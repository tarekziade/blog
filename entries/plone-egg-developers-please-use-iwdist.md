Title: Plone egg developers, please use iw.dist !
Date: 2008-02-20 14:52
Category: plone, python, zope

This is my first important step in order to fullfill the Strategic
Summit task \#7817 ([http://dev.plone.org/plone/ticket/7817][]).   
  
I have released the [iw.dist][] package which is a replacement for
*register* and *upload* commands. Theses changes will be pushed in
Python 2.6 hopefully. Until then, iw.dist provides two new commands,
called *mregister* and *mupload*, which are acting the same way.   
  
Please, use them instead of *register* and *upload* ! So I can get some
feedback ;)   
  
It is quite simple to set up, see this page:
[http://pypi.python.org/pypi/iw.dist   
][iw.dist]   
  
It will not bather you at all since it does what the regular commands
do, but are the first step to a tool that will let you upload the eggs
to plone.org.

  [http://dev.plone.org/plone/ticket/7817]: http://dev.plone.org/plone/ticket/7817
  [iw.dist]: http://pypi.python.org/pypi/iw.dist
