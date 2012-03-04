Title: An installer for a buildout-ready Windows 
Date: 2008-01-20 20:05
Category: plone, python, windows, zope

When you need to run a buildout under Windows, you have to take care of
setting up quite a few things, like installing MinGW and linking it to
Python, and setting up a svn command-line client for most buildouts.   
  
We created a simple package that contains everything needed to make
your windows buildout-friendly. It is a simple zip file that contains a
batch script and third-party installers. When the batch is run, the
environment variables are set as well, and win32-compatible buildouts
should run without problems from there.   
  
**EDIT: the downloads urls have changed (thanks [Sasha][]!)**   
  
You can get it here:   
  
[http://dl.dropbox.com/u/3265240/python2.4.4-win32.zip][]   
  
and another version that adds developing tools like vim and tail:   
  
[http://dl.dropbox.com/u/3265240/python2.4.4-win32-dev.zip][]   
  
This zip file is built itself with a buildout that we might publish
soon so you can make a custom zip file.

  [Sasha]: http://www.theotheralex.com/
  [http://dl.dropbox.com/u/3265240/python2.4.4-win32.zip]: http://dl.dropbox.com/u/3265240/python2.4.4-win32.zip
  [http://dl.dropbox.com/u/3265240/python2.4.4-win32-dev.zip]: http://dl.dropbox.com/u/3265240/python2.4.4-win32-dev.zip
