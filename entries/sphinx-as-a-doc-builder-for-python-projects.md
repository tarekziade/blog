Title: Sphinx as a doc builder for Python projects
Date: 2008-03-23 09:08
Category: documentation, plone, pycommunity, python, zope

Last year, I worked on a documentation builder based on doctest and
reStructuredText format called [PyCommunity][]. This tool is collecting
doctests from Python packages and from special places on a source
repository, basing its work on a set of project good practices I had
presented and used in a Pycon 2007 tutorial ([slides][]).   
  
Basically, it uses the best practices described in Andreas Ruping book,
called *Agile Documentation*, applied to Python projects using TDD and
doctests. It can be called Document-Driven Development.   
  
I have never found the time to finish the tool and I was looking
forward to get back to it. As a matter of fact, George Brandl has
released the tool that is used to generate Python documentation, called
[Sphinx][], which does many things I still have in my TODO list, like
[pygments][] integration, and many other things.   
  
See how Sphinx generates Python doc here:
[http://docs.python.org/dev][]   
  
From there, it becomes dead simple to generate a website for a Python
project, based on packages doctests and text files and on a specific
doc/ structure.   
  
Sphinx annoucement is really exciting, and it shouldn't be too much
pain to bundle it in a buildout recipe to manage a project
documentation. Since it is based on templates and configuration files, a
default structure can be generated to startup a project documentation
together with a code base.   
  
I have to try and see if Sphinx allows me to set everything up. In
other words, replay my Pycon tutorial with it.

  [PyCommunity]: http://hg.programmation-python.org/browser/pycommunity/pycommunity
  [slides]: http://programmation-python.org/pycommunity/pycon/PyCon07/slides.html
  [Sphinx]: http://sphinx.pocoo.org
  [pygments]: http://pygments.org/
  [http://docs.python.org/dev]: http://docs.python.org/dev
