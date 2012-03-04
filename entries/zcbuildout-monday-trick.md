Title: zc.buildout monday trick :)
Date: 2008-04-07 16:01
Category: plone, python, zc.buildout, zope

When a site used by your buildout is not responding, you can stare at it
for ... ever   
  
Add these two lines in your bin/buildout script:   
   import socket

    socket.setdefaulttimeout(10)

  
With this, the buildout will go to the next link after ten seconds.
This trick made my day :)
