Title: Help us ironing Packaging 
Date: 2011-06-02 12:23
Category: python

**packaging** has landed [in the standard library][], but the road to
Python 3.3 is still filled with a lot of work. We've pushed the
Documentation yesterday in the tip, and it now appears here:
[http://docs.python.org/dev/packaging/][]   
  
There are a lot of stuff you can do to help us improving packaging. If
you wish to help out, read up.   
### 1. Install a Python 3 development environment

  
The first step is to install a Python development environment   
  
There's a full dev guide here: [http://docs.python.org/devguide/][] but
it basically boils down to run make on the tip:   
   $ hg clone https://hg.python.org/cpython     (very long)

    $ cd cpython

    $ ./configure && make

  
Once this is done, you'll have a Python interpreter you can run:   
   $ ./python

    Python 3.3a0 (default:94066c3e2236+, May 31 2011, 08:29:53)

    [GCC 4.5.2] on linux2

    Type "help", "copyright", "credits" or "license" for more information.

    >>> print('Python 3, yay !')       

    Python 3, yay !

  
### 2. Try out the pysetup script, as an end-user

  
This script is a global script people will be able to use to check
what's installed on a Python installation, to install things, remove
them, etc. The script has still a lot of rough edges, which is a shame
since it's just the tip of a feature-rich system.   
  
It's located in Tools/script/pysetup3 in a dev environment, and here's
a demonstration of how to install the lastest Mako release, check that
it's installed, look at some of its metadata, then remove it:   
   $ sudo ./python Tools/scripts/pysetup3 install Mako

    Checking the installation location...

    Getting information about 'Mako'...

    Installing 'mako' 0.4.1...

    [lots of output]



    $ ./python Tools/scripts/pysetup3 list

    SQLAlchemy 0.7.0 at /usr/local/lib/python3.3/site-packages/SQLAlchemy-0.7.0-py3.3.dist-info

    distribute 0.6.17 at /usr/local/lib/python3.3/site-packages/distribute-0.6.17-py3.3.dist-info

    Mako 0.4.1 at /usr/local/lib/python3.3/site-packages/Mako-0.4.1-py3.3.dist-info



    Found 3 projects installed.



    $ ./python Tools/scripts/pysetup3 metadata Mako -f Version

    Version:

        0.4.1

    $ ./python Tools/scripts/pysetup3 metadata Mako -f Author

    Author:

        Mike Bayer



    $ sudo ./python Tools/scripts/pysetup3 remove Mako

    Removing 'Mako':

      /usr/local/lib/python3.3/site-packages/mako/parsetree.py

     [lots of lines]

      /usr/local/lib/python3.3/site-packages/Mako-0.4.1-py3.3.dist-info/RECORD

    Proceed (y/n)? y

    Success: removed 52 files and 2 dirs

  
So go ahead, play with this script, discover its features and:   
-   tell us what feels wrong
-   tell us what kind of features you wish you had in this script
-   found a bug, have a patch, tell us !

  
### 3. Make your project packaging-ready, as a developer

  
The sweet thing is that adding packaging support in your project is
risk-free because it's just adding a few sections in your setup.cfg
file. setup.py can stick around, and older installers will still pick it
up.   
  
So, here is how you can do: You can tollow the tutorial if you want to
do something from
scratch:[http://docs.python.org/dev/packaging/tutorial.html][]   
  
Or you can use the magic create command in your Project root directory,
to create a setup,cfg out of your setup.py file !   
   $ sudo ./python Tools/scripts/pysetup3 create

    A legacy setup.py has been found.

    Would you like to convert it to a setup.cfg? (y/n)

        [y]: y

    Wrote "setup.cfg".

  
If you're starting your project from scratch You can also generate a*
setup.py* that will extract the options out of setup.cfg. Very handy to
provide backward compatibility and avoid maintaining two files !   
   $ sudo ./python Tools/scripts/pysetup3 generate-setup

    The setup.py was generated

  
So go ahead, learn how setup,cfg works, reads its specs at
[http://docs.python.org/dev/packaging/setupcfg.html][] and:   
-   tell us what feels wrong
-   tell us what kind of features you wish you had in this file
-   found a bug, have a patch, tell us !
-   tell us if you were unable to convert your project

  
Once the project is packaging ready, you can even register and upload a
new version of it at PyPI and check that pysetup knows how to install it
  
### 4. Give use some feedback

  
-   You can add new bugs/feature requests at[http://bugs.python.org/][]
    under the Distutils2 component, that will be really really helpful.
-   You can tell us what's weird with our documentation, what misses,
    etc. That goes to the Documentation+Distutils2 components

  [in the standard library]: http://hg.python.org/cpython/file/3dbf4c9b3ed4/Lib/packaging
  [http://docs.python.org/dev/packaging/]: http://docs.python.org/dev/packaging/
  [http://docs.python.org/devguide/]: http://docs.python.org/devguide/
  [http://docs.python.org/dev/packaging/tutorial.html]: http://docs.python.org/dev/packaging/tutorial.html
  [http://docs.python.org/dev/packaging/setupcfg.html]: http://docs.python.org/dev/packaging/setupcfg.html
  [http://bugs.python.org/]: http://bugs.python.org/
