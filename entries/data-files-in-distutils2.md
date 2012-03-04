Title: Data files in Distutils2
Date: 2011-01-23 17:00
Category: distutils, packaging, python

I am preparing [next week's sprint at Logilab][], trying to isolate
several interesting tasks people will be able to achieve without having
to dig in the whole code base.   
  
One task we need to achieve in Distutils2 is a better description of
the data files in a project, and in particular a way to categorize them
so an OS packager knows how to make a difference between a documentation
file and a configuration file. Also, we need to let the packager decide
where these files need to land in the system at installation time,
without breaking the developer's code.   
  
So far in Python, people tend to include all files within their Python
packages and access them using the *\_\_file\_\_ *variable:   
   import os.path

    here = os.path.dirname(__file__)

    images = os.path.join(here, 'images_dir')

  
This technique has its limits:   
-   If you use *easy\_install* to install your projects, you might end
    up with a zipped egg, meaning that the directory is in a zip file.
    So this code will not work unless you've installed the project with
    the -Z option, or you use the zipimport helper to work with your
    files.
-   Installing data files in site-packages is not a best practice in
    most Linux distributions, and if the OS packager wants to move them
    in the "right" place, he needs to review all the code and patch it
    everywhere it makes an assumption on the location of the file.
-   If the developer does the right thing for *Debuntu* with his data
    files, he'd need to do it for every other Linux distribution, but
    also define a specific behaviour for Mac OS X and Windows.

  
Last year at Pycon we've worked on that topic and came up with an
elegant design on the paper:   
-   Python will provide in the *sysconfig* module a list of default
    categories for data files, with a default location for each target
    system
-   The developer will define its data files in categories in setup.cfg,
    and add if needed new categories
-   Linux distributions will be able to change the paths for each
    categories via a configuration file global to Python --
    sysconfig.cfg
-   Distutils2 will look at the paths of each categories at installation
    time, and install the files there.
-   The developer will use a special open() API to be able to locate the
    file no matter on what system the code runs, or even if the code
    runs on a development tree.

  
The draft of this feature is here:
[http://hg.python.org/distutils2/file/tip/docs/design/wiki.rst][] and
starting to code this design for real is a perfect task for this sprint
because it does not require a lot of knowledge about the Distutils2 code
base.   
  
If you are in Paris, or available online, and want to sprint with us,
make sure you register to the wiki page !

  [next week's sprint at Logilab]: http://wiki.python.org/moin/Distutils/SprintParis
    "Sprint@Logilab"
  [http://hg.python.org/distutils2/file/tip/docs/design/wiki.rst]: http://hg.python.org/distutils2/file/tip/docs/design/wiki.rst
