Title: iw.* recipes release festival
Date: 2007-12-14 10:02
Category: plone, python, zope

A lot of buildout recipes have been created lately at Ingeniweb, you can
list them here:
[http://pypi.python.org/pypi?%3Aaction=search&term=iw.recipe&submit=search.][]
  
  
Let me present them quickly:   
-   [iw.recipe.cmd][] : yet another command line recipe. This is useful
    when you need to perform some pre or post installation steps that
    don't worth a recipe.
-   [iw.recipe.fetcher][] : this recipe is a wget-like command, that
    knows how to downloads a file given by an url.
-   [iw.recipe.fss][] : this recipe creates folders and configuration
    file when you use [File System Storage][] in your Plone application.
-   [iw.recipe.squid][] : automates the configuration of [Squid][], and
    is [Cache-Fu][] friendly
-   [iw.recipe.pound][] : compiles and installs [Pound][] in your
    buildout, and creates its configuration file.
-   [iw.recipe.subversion][] : this one is a bit like
    [infrae.subversion][] but it doesn't make controls of modified files
    (which can be very long when you update a buildout), and it
    generates in download-cache when it is given, a tarball of the
    subversion branch. This allow us to perform offline installation
    with subversion branches without having to change the cfg files.
-   [iw.recipe.template][] : this recipe knows how to render a cheetah
    template like Paster does for instance. It makes it easy to add a
    few custom files in our buildouts

  
If you use them please let us know !   
  
Other recipes are beeing created, like *iw.recipe.pen*, which does like
*iw.recipe.pound* but for Pen. I will blog sometimes about [Pen][],
which can be used instead of Pound when you need an universal load
balancer that can work on any platform.

  [http://pypi.python.org/pypi?%3Aaction=search&term=iw.recipe&submit=search.]:
    http://pypi.python.org/pypi?:action=search&term=iw.recipe&submit=search.
  [iw.recipe.cmd]: http://pypi.python.org/pypi/iw.recipe.cmd
  [iw.recipe.fetcher]: http://pypi.python.org/pypi/iw.recipe.fetcher
  [iw.recipe.fss]: http://pypi.python.org/pypi/iw.recipe.fss
  [File System Storage]: http://ingeniweb.sourceforge.net/Products/FileSystemStorage/
  [iw.recipe.squid]: http://pypi.python.org/pypi/iw.recipe.squid
  [Squid]: http://www.squid-cache.org/
  [Cache-Fu]: http://plone.org/products/cachefu
  [iw.recipe.pound]: http://pypi.python.org/pypi/iw.recipe.pound
  [Pound]: http://www.apsis.ch/pound/
  [iw.recipe.subversion]: http://pypi.python.org/pypi/iw.recipe.subversion
  [infrae.subversion]: http://pypi.python.org/pypi/infrae.subversion/
  [iw.recipe.template]: http://pypi.python.org/pypi/iw.recipe.template
  [Pen]: http://siag.nu/pen/
