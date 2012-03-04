Title: How to generate proper reStructuredText titles with Python Paste
Date: 2007-09-21 09:54
Category: plone, python, zope

[Python Paste][] and [ZopeSkel][] are just great, if you don't know them
and you are working on Zope packages, you should really take the time to
look at them.   
-   Python Paste provides, besides other features, a engine to generate
    any kind of package structures based on templates. The templates can
    be written in [Cheetah][] syntax;
-   ZopeSkel is a serie of templates that helps a Zope and/or Plone
    developer to start a Python, Zope or Plone package, taking care of
    all the boiler plate code generation, to make sure the packages are
    done in a egg-compatible, standard way.

  
Basing my work on ZopeSkel, I have started to create a serie of custom
templates to speed up and simplify package coding bootstraps. The
documentation in these packages are in [reStructuredText][], and I
bumped into a small problem: when you create for example a "README.txt"
in your template, which has a title that uses the project name, for
example:   
   ======================

  
   $project documentation

  
   ======================

  

  
   blablabla

  
the result may vary depending on the variable value:   
   ======================

  
   kool documentation

  
   ======================

  

  
   blablabla

  
or even:   
   ======================

  
   i_like_long_names_for_packages documentation

  
   ======================

  

  
   blablabla

  
It's ugly, and the reST file won't compile if you try to generate html
or PDF with [docutils][].   
  
Since Paste uses Cheetah, we can fix this, by calculating the length of
underlines:   
   #repeat $len($project) + 13

    =#slurp

    #end repeat



    $project documentation

    #repeat $len($project) + 13

    =#slurp

    #end repeat

  

  
   blablabla

  
This will create the proper length. You might argue it's a detail, but
that saves me almost ten seconds for each new package now ;)

  [Python Paste]: http://pythonpaste.org/
  [ZopeSkel]: http://plone.org/products/zopeskel
  [Cheetah]: http://www.cheetahtemplate.org
  [reStructuredText]: http://docutils.sourceforge.net/rst.html
  [docutils]: http://docutils.sourceforge.net/
