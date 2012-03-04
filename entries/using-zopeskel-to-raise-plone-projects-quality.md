Title: Using ZopeSkel to raise Plone projects quality 
Date: 2007-11-30 11:05
Category: plone, python, quality, zope

At Ingeniweb, we have started to define standards for our Plone projects
using [ZopeSkel][]. [IngeniSkel][] is a thin layer on the top of
ZopeSkel, that was:   
-   injecting Archetype content within existing products
-   defining standard tests skeletons for all elements contained in
    products.
-   providing other templates like the recipe one, that creates a
    skeleton for zc.buildout recipes

  
The injection idea was previously [proposed by Martin][], and
[Mustapha][] started to implement it in a [branch][]. Erik F. has added
the archetype content injection yesterday.   
  
It means you can now inject new archetype based content with the Paster
directly with ZopeSkel:   

    $ paster create -t archetype my.package $ cd my.package  $ paster --help

    usage: paster [paster_options] COMMAND [command_options]

    options:

      ...

    Commands:

      create       Create the file layout for a Python distribution

      ...

    ZopeSkel local commands:

      addcontent   Adds plone content types to your project  $ paster addcontent --list

    Available templates:

      contenttype:  A content type skeleton

      portlet:      A Plone 3 portlet

      view:         A browser view skeleton

      zcmlmeta:     A ZCML meta directive skeleton $ paster addcontent

  
This is great, now the only thing it misses so we can drop IngeniSkel
in favor of this enhanced version of ZopeSkel is generating tests
modules on all templates and local commands, and the same way everytime.
I started such a work in another branch to backport what we have it and
I will propose it.   
  
Why ? Because having tests that are written the same way on all layers
of a Plone project is important to:   
-   automate some QA and documentation tasks
-   make sure a newcomer won't get lost on how to startup a new piece of
    code, with the right test fixture. If he takes too much time to
    prepare the test fixture, he'll probably drop the TDD approach...

  
Edit: I have merged the the recipe template into ZopeSkel trunk
already, as I've been asked to

  [ZopeSkel]: http://plone.org/products/zopeskel
  [IngeniSkel]: http://pypi.python.org/pypi/IngeniSkel
  [proposed by Martin]: http://martinaspeli.net/articles/a-cool-project-if-you-have-the-time
  [Mustapha]: http://www.mustap.com/pythonzone_post_234_zopeskel-with-local-commands
  [branch]: https://svn.plone.org/svn/collective/ZopeSkel/branches/
