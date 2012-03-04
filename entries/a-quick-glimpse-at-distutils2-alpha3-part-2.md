Title: A quick glimpse at Distutils2 alpha3 - part 2
Date: 2010-10-03 13:37
Category: python

It seems that doing a little bit of teasing on the next release
generates valuable feedback. So I'll do more :)   
  
In the next version we have this really useful module called
**depgraph** ([full doc][]). It creates a dependency graph to study
installed distribution, but also to-be-installed distributions. This is
the basis of any installer script but is also useful for users who want
to know what's installed.![image][]   
  
Setuptools has a module called **pkg\_resource**s that would allow to
create such a feature, but distutils2 used an enhanced version of the
stdlib module **pkgutil** which now supports [PEP 376][] but also offers
a compatibility mode to be able to browse packages that were installed
by pre-PEP 376 installers like Pip or easy\_install. The new **pkgutil**
module lives in a \_backport package in distutils2 but will be pushed
back to the stdlib as soon as we reach a stable version for distutils2.
It will make pkg\_resources obsolete for the part that let you iterate
on installed projects and will provide more. (Note that pkg\_resources
contains much more features besides.)   
  
But enough talking, try to build your depgraph yourself ! depgraph can
be called as a script to generate dependency graphs in the stdout, or as
.dot (graphviz) files.   
  
Here's a small demo:   
   # installing the latest tip

    $ sudo easy_install http://bitbucket.org/tarek/distutils2/get/bdfaec90d665.gz

    Downloading http://bitbucket.org/tarek/distutils2/get/bdfaec90d665.gz

    Processing bdfaec90d665.gz

    ...



    # what do we have installed ?

    $ python -m distutils2.depgraph

    Dependency graph:

     PasteDeploy 1.3.3

     virtualenv 1.4.9

     pyflakes 0.4.0

     ...

     Distutils2 1.0a3

     ropemode 0.1-rc2

       rope 0.9.3 [rope (>= 0.9.2)]

    ...



    # let's create a dot file of the dependencies

    # if a distribution don't have a dependency it's not added - so you don't get crazy graphs

    $ python -m distutils2.depgraph -d

    Dot file written at "depgraph.dot"



    # let's create an image

    $ dot -Tpng depgraph.dot > depgraph.png

  
Try it out and let us know how it worked for you !

  [full doc]: http://distutils2.notmyidea.org/library/distutils2.depgraph.html#
  [image]: http://distutils2.notmyidea.org/_images/depgraph_output.png
    "Depgraph example"
  [PEP 376]: http://python.org/dev/peps/pep-0376
