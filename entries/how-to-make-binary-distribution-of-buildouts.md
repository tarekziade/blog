Title: How to make binary distribution of buildouts
Date: 2008-12-09 01:26
Category: python, zc.buildout

### The Problem

  
I need to distribute pre-compiled buildouts because some projects don't
allow us to have gcc installed on the production system for security
reasons.   
  
Fair enough, we need to provide a pre-compiled buildout.   
  
If you want to distribute your buildout-based Plone application in a
binary form, so it can be installed without requiring any compiler on
the platform, you need to compile all .c modules before you provide a
tarball of your buildout folder.   
  
This is easy : just run your buildout and all .so files will be created
in the zope 2 installation. (.pyd under windows)   
  
But this will work only if you compile in a directory that is located
within the same path on the target machine, because zc.buildout uses
absolute paths when it builds scripts.   
  
Furthermore, if the python interpreter is not located in the same
place, your buildout script itself is screwed.   
  
Last but not least, plone.recipe.zope2install is not clever enough. It
will remove your zope2 installation when it detects that the path has
changed. This is pretty annoying even if you have gcc : what is the
point of compiling the c extension again since they   
are statically compiled in-place ?   
### The solution

  
I have changed plone.recipe.zope2install and added a new option called
\`smart-recompile\` (in trunk right now, not released).   
  
If you use it, the recipe will check for .so or .pyd files before
trying to ditch your zope 2 installation and recompile it. Even if you
don't use it to build binary distributions, it will make your buildout
build faster if you already have zope compiled in there.   
  
Next, I have created a special bootstrap.py, who is clever enough to
rebuild the buildout script with the right path to the used interpreter,
and with offline-mode capabilities. To make it short : boostrap.py works
no matter if you have an internet connection or not. Grab it here :
[http://ziade.org/bootstrap.py][]   
  
So now, basically you can compile your buildout and deploy it on any
system, on any path, without any internet connection, like this:   
   $ python bootstrap.py    # will rebuild the buildout script    

    $ bin/buildout

  
Of course this doesn't work if you have dynamically compiled extensions
like python-ldap. For theses, the best pick is to rely on the system
ones.   
  
[][http://ziade.org/bootstrap.py]

  [http://ziade.org/bootstrap.py]: http://ziade.org/bootstrap.py
