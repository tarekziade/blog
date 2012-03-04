Title: Distutils 2 alpha 4 - work in progress
Date: 2010-11-07 23:53
Category: python

Time flies, and we did not hit the first beta of Distutils2 yet. It's
quite clear now that we won't make it for Python 3.2. But that's not a
big issue because people will be able to install Distutils2 from Python
2.4 to 3.x and use it until it gets back into Python standard library.   
  
We are going to have a sprint next week-end and try to wrap up a new
alpha.   
  
It should contain:   
-   The work done by **Eric** on the configure command during the GSOC.
    The** configure command** let you create a config file that can be
    used by the **build** or the **install** command. This fixes one
    issue people have: the install command will not have to run the
    build command again, just to get the options that were used to build
    the project.
-   The work done by **Alexis** on the installation script. We are
    adding **a 'pysetup' script** people can use to drive installations,
    un-installations and running any command or feature Distutils2 has.
    One script to rule them all.
-   The work done by **Zubin** to make Distutils2
    **Python3-compatible**.

  
### Other stuff I've added

  
You can now configure the sub command list the ***install*** or the
***build*** command uses in distutils.cfg, or setup.cfg. -- Or any other
subcommands in fact -- This means that people will be able to provide a
new sub command that extends **install** or **build**, without having to
override the hardcoded list of subcommands they contain. They will also
be able to define the ordering of all subcommands.   
  
The **sdist** command has a new option called **manifest\_builders**,
where you can provide hooks that will be called ***just after*** the
sdist command has created the list of files to include in the
distribution, and ***just before*** the manifest is written. In other
words, you can use it to add or remove files through code.   
### Other stuff I am working on

  
The compilers in Distutils are still messy and did not get any
attention yet. I'd like to clean them up, to make it easier to register
a new compiler, and to add a tutorial on how to write a new compiler.   
  
Compilers are something I am not very familiar with. Jeremy Kloth, who
worked on 4Suite and on Distutils2 should be of a good help in this
area. I wished we would get some help from other folks from the Python
scientific community since they have specific compiling needs. But
according to David Cournapeau, [*"Several extremely talented people in
the scipy community have indepedently attempted to improve this in the
last decade or so, without any success"*][] .. reading his whole blog I
am quite surprised because part of the problems he described with
Distutils are getting solved right now in Distutils2 --some of them
during the GSOC after his criticisms on python-dev-- and other problems
don't sound like unsolvable issues.   
  
Oh well, I can understand that people got fed up with Distutils, it's a
very long process to improve it. And it's a good thing that other people
build other tools. The Python community can have as many build tool as
it wants. The more tools the better. **As long as we all share the same
standards when it comes to publish things at PyPI or install projects in
Python. Interoperability matters. **   
  
And that's where Distutils2 has an important role to play. Besides the
command system it provides to build and package stuff, it also provides
implementation of all the latest packaging standards we have built
through PEPs. The one that will be used in the future at all levels in
PyPI and Python. So if you plan on building yet another build tool, you
should have a look at them.   
### Help us !

  
Distutils2 support can be added **today** in your project without
interfering with the existing Distutils1/Setuptools/Distribute support.
You can add in your project's *setup.cfg* new sections that are specific
to Distutils2 and that will make your project Distutils2 compatible
without any harm. This would be of a great help for us to get some
feedback from real-world projects on Distutils2. If you are interested
and want to help, let me know.   
  
And, if you have any frustration with distutils, or feature request, we
want to hear them. You can drop by \#distutils on Freenode or drop a
mail in our [mailing list][].

  [*"Several extremely talented people in the scipy community have
  indepedently attempted to improve this in the last decade or so,
  without any success"*]: http://cournape.wordpress.com/2010/10/13/271/
  [mailing list]: http://groups.google.com/group/the-fellowship-of-the-packaging
