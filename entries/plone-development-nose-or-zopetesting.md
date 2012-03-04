Title: Plone development: Nose or zope.testing ?
Date: 2008-08-28 15:25
Category: plone, python, zope

Python needs a better testing tool, hopefully this will happen [some
days][].   
  
Until then we, Plone developers use [zope.testing][] for the best and
the worst.   
-   the best because zope.testing provides [layers][] and the Zope/Plone
    stack provides really nice things to work with them.
-   the worst because sometimes it just gives me some headaches to
    figure out how to set my test fixtures correctly.
-   the worst because I cannot easy-install zope.testing and just call
    it from the prompt to run some tests (this should get better
    sometimes see [here][])

  
That said, when you work with a zc.buildout based environment, it is
easy to use zope.testing, thanks to [zc.recipe.testrunner][].   
  
But since the eggification of Zope, we write more and more code that
would benefit from a lighter test framework. [Nose][] has this lighter
approach, I love it to write simple tests without the Java-like heavy
UnitTest framework. I can just write:   
   def test_something():

  
       assert 1 == 1

  
And call *nosetests*. Test fixtures are easy to set at all levels as
well, using the *with\_setup* decorator.   
  
I tried to write some tests that could be launchable from both
frameworks, by making some bridges, but I came up to the conclusion that
a package should fully use either zope.testing, either Nose.   
  
So now, I use two test scripts in my zc.buildout environments, and
decide depending on the package. I have written another recipe for
buildout to bind Nose: [pbp.recipe.noserunner][].   
  
From there, I create two sections in my buildout.cfg file:   
   [buildout]

    parts =

        ...

        nose

        ztest



    [nose]

    recipe = pbp.recipe.noserunner

    eggs =

        egg1

        egg2



    [ztest]

    recipe = zc.recipe.testrunner

    eggs =

        egg3

        egg4

  
These will generate two test scripts   
-   nose to run nosetests with egg1 and egg2 in sys.path
-   ztest to run zope.testing with egg3 and egg4 in sys.path

  
Here's my grid of choices when I am coding:   
-   zc.buildout recipes : zope.testing (doctests using zc.buildout
    testing framework)
-   Plone packages: zope.testing
-   Python packages and 'everything' else: Nose

  [some days]: http://www.mail-archive.com/python-dev@python.org/msg31411.html
  [zope.testing]: http://pypi.python.org/pypi/zope.testing
  [layers]: http://pypi.python.org/pypi/zope.testing#layers
  [here]: http://mail.zope.org/pipermail/zope-dev/2008-May/031851.html
  [zc.recipe.testrunner]: http://pypi.python.org/pypi/zc.recipe.testrunner/1.1.0
  [Nose]: http://www.somethingaboutorange.com/mrl/projects/nose/
  [pbp.recipe.noserunner]: http://pypi.python.org/pypi/pbp.recipe.noserunner
