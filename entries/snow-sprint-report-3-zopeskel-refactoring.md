Title: Snow sprint report #3 : ZopeSkel refactoring
Date: 2008-01-22 21:27
Category: plone, python, zope

Today, while the zope instances we have prepared for the benchmarks
where suffering from being fed with 40 000 documents, I have worked on a
small task I wanted to do some times ago: refactor a bit ZopeSkel and
add some tests in it.   
  
I splitted the template objects that were located in separate modules,
and added for each one of them a doctest that is running the template.
This prevents the template to be broken because when you work in it, it
is not obvious. As a matter of fact, at the time I did it, I found one
template to be broken, so I think this is going to be useful to prevent
regressions.   
  
If you work on this package and change or add a template, please,
pretty please, run the following to make sure nothing is broken:   

    $ cd ZopeSkel

    $ python boostrap.py

    $ bin/buildout

    $ bin/test

  
Also the important thing to do for now on, is to keep accurate doctests
in the docs/ folder. These files are simple to write, as I have added
primitives to simplify the work (well, I have reused what [Gael][] did
in our skels at Ingeniweb).   
  
For instance, let's have a look at the recipe doctest:   
  

[http://dev.plone.org/collective/browser/ZopeSkel/trunk/zopeskel/docs/recipe.txt][]
  
  
It actually launches the paster over the template, and also launches
the freshly created recipe's own tests.   
  
The next moves on ZopeSkel I can think of would be to:   
-   write more detailed doctests. Each one of them could become a recipe
    on how to use the given template;
-   gather in a top document all the doctest, to provide a detailed
    documentation in Zopeskel's frontal README.txt file, which is parsed
    and displayed at PyPI.

  
ZopeSkel is a very important product in my opinion, because it
insuflates a standard way to write Plone code in the community. For that
matter, the *recipe* template I have added a while ago was improved here
at the sprint, and you should check on [Dokai's blog][] about this. He's
writing a wrapup about it right now ;)

  [Gael]: http://www.gawel.org/weblog/
  [http://dev.plone.org/collective/browser/ZopeSkel/trunk/zopeskel/docs/recipe.txt]:
    http://dev.plone.org/collective/browser/ZopeSkel/trunk/zopeskel/docs/recipe.txt
  [Dokai's blog]: http://blogs.hexagonit.fi/kai/
