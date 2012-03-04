Title: Annoucing collective.eggproxy, the smart PyPI mirror
Date: 2008-09-24 09:15
Category: plone, python, zc.buildout, zope

I just wanted to announce the release of collective.eggproxy
([http://pypi.python.org/pypi/collective.eggproxy/0.2.0][])   
  
collective.eggproxy is a smart mirror for PyPI, thaught and coded by my
colleague [Bertrand Mathieu][].   
  
It will collect packages on PyPI only when a program like easy\_install
or zc.buildout asks for it. In other words, unlike some mirrors that act
like rsync and get the whole PyPI base (more than 5 gigas)
collective.eggproxy will only get what you need.   
  
At first run collective.eggproxy downloads pypi index and builds a page
of links. When a software asks for a specific package, version, etc.
collective.eggproxy downloads it if needed and stores it locally.   
  
Want to give a try ? try it in two lines with easy\_install:   
   easy_install collective.eggproxy

    eggproxy_run

  
That's it !

  [http://pypi.python.org/pypi/collective.eggproxy/0.2.0]: http://pypi.python.org/pypi/collective.eggproxy/0.2.0
  [Bertrand Mathieu]: http://zebert.blogspot.com/
