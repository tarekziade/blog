Title: zc.buildout recipe to build your Sphinx doc 
Date: 2008-09-11 11:41
Category: documentation, plone, python, zope

[Sphinx][] is now used by quite a few communities : [Python][],
[Django][], [Pylons][], Grok (not sure about the current status), ...   
  
No wonder, it's a blast.   
  
We are now starting to use it to produce customer documentation for our
buildout-based applications. Basically, a Sphinx structure is created in
the buildout using sphinx-quickstart, and a few tweaks are made so the
HTML and PDF outputs have a custom look.   
  
Managing the documentation like the code makes life easier. This is one
of the basic rule of [agile documentation][] : separate the content from
the layout, so you can provide documentation in any shape (html, pdf)
with a single source.   
  
To make things easier, I have released
[collective.recipe.sphinxbuilder][].   
  
This recipe:   
-   creates for you a Sphinx-based documentation in your buildout
-   creates a single script in the bin folder to build the documentation
    with one command
-   provides [an extensive set of options][] to drive Sphinx from
    buildout

  
Adding it in your buildout is as simple as :   
   [buildout]

    parts =

      sphinx



    [sphinx]

    recipe = collective.recipe.sphinxbuilder

  
I have also customized the look and feel of the output so it uses the
Plone logo and a custom css. This is configurable from the buildout
configuration file of course. By the way, if someone from the Plone
community wants to improve the CSS, please dot it ! (I am not good at
this :) )   
  
[gallery]   
  
Notice that if you use LaTex or PDF rendering, you will need to install
pdflatex. Furthermore, the recipe script will not work under Windows
unless you install a Linux-like environment, since it uses the Makefile
provided by Sphinx. I guess MSYS+MinGW should make it work, but I didn't
try.

  [Sphinx]: http://sphinx.pocoo.org/
  [Python]: http://docs.python.org/dev/
  [Django]: http://docs.djangoproject.com/en/dev/
  [Pylons]: http://docs.pylonshq.com/
  [agile documentation]: http://www.agilemodeling.com/essays/agileDocumentation.htm
  [collective.recipe.sphinxbuilder]: http://pypi.python.org/pypi/collective.recipe.sphinxbuilder/
  [an extensive set of options]: http://pypi.python.org/pypi/collective.recipe.sphinxbuilder/#supported-options
