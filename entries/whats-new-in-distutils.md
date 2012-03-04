Title: What&#039;s new in Distutils ?  
Date: 2009-02-15 10:35
Category: distutils, python

Since Python 3.0.1 was released this week, here's a quick wrapup of what
is going on in Distutils.   
### Code work (since one month)

  
#### New features

  
-   Issue 2563 : now the manifest is embed in windows extensions
-   Issue 4394 : the storage of the password in .pypirc file is optional
    now

  
#### Fixed bugs

  
-   Issue 4524: distutils was failing to build scripts with the
    '--with-suffix=3'
-   Issue 5132 : build\_ext command was failing under Solaris with
    '--enabled-shared'
-   Issue 5075 : bdist\_wininst was depending on the vc runtime

  
#### Refactoring

  
-   Issue 2461 : added test coverage for util.py
-   Issue 3986 : removed string and type usage from distutils.cmd
-   Issue 3987 : removed type usage from distutils.core

  
#### Documentation

  
-   Issue 5158 : added documentation for depends option for extensions
-   Issue 4987: updated README info
-   Issue 4137 : SIG web pages were updated

  
### Design work

  
The main topics that are being discussed are:   
-   Improving the console script story. [thread starts here][].
-   Publishing a Survey on Distutils before the Language Summit. [thread
    starts here][1].
-   Adding an uninstall command to unistall packages in the sdtlib :
    [thread starts here][2]
-   Adding a get\_metadata API in pkgutil to get the metadata of an
    arbritary package The same code can also be used for various lookups
    (uninstall, console script) : [thread starts here][3]
-   Having a new PEP to make egg.info a directory and clearly define
    PKG-INFO and its match with metdata. [thread starts here][4]

  [thread starts here]: http://mail.python.org/pipermail/distutils-sig/2009-February/010980.html
  [1]: http://mail.python.org/pipermail/distutils-sig/2009-January/010782.html
  [2]: http://mail.python.org/pipermail/distutils-sig/2009-January/010866.html
  [3]: http://mail.python.org/pipermail/distutils-sig/2009-January/010711.html
  [4]: http://mail.python.org/pipermail/distutils-sig/2009-February/010968.html
