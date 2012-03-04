Title: Smoke testing in Distutils
Date: 2009-05-28 15:38
Category: distutils, python

I am not really sure **smoke testing** is the best name to describe what
I am trying to set up.   
  
Wikipedia says:   
> In computer programming and software testing, smoke testing is a
> preliminary to further testing, which should reveal simple failures
> severe enough to reject a prospective software release. In this case,
> the smoke is metaphorical.

  
But I think it describes well the need I have : being able to test the
output of several releases of Distutils, without relying on unit tests
for that. Simply because they did not exist on early versions of
Distutils.   
### Why do I need "smoke tests"

  
Lately, I was working on Distutils, removing some old bugs and adding
some tests. Working on an under-tested package is like opening a can of
worms : when you change something you can introduce some regressions.
It's hard to avoid for sure, because even if you add some tests
subsequently for some features, you are not really doing proper TDD,
where the tests and the code grow together. So there might be some
uncovered cases left even if the coverage is improving slowly.   
  
Regression also happens when you correct a behavior that was broken for
years : if third party tools used a broken behavior without knowing it,
fixing the behavior at some point becomes a regression from them.   
  
But these pitfalls are unavoidable. Hopefully they don't last for too
long in a big project like Python. They are quickly reported, either by
buildbots, either by someone from the community.   
  
The last behavior problem I had was on the **build\_ext command**.
There's a string option called *"compiler"*, were you can force the
compiler type. You can put for instance **'linux**' and build\_ext will
use the *UnixCompiler* compiler class.   
  
Although this option name is misleading. It should have been called
*"compiler\_type"* in the first place. And the *build\_ext* command adds
another problem : it turns the *compiler* attribute of the class where
the option value is stored, into a compiler instance. No need to say a
class attribute value should not have several types.   
  
The first application to suffer from this is Python itself. It uses
*build\_ext.compiler*, as a compiler instance to build its modules.   
  
This means that "compiler" is now doomed to be both an option and a
compiler attribute. It's not easy to fix and will require a deprecation
step.   
  
So the idea of the smoke test is to make sure Distutils still knows how
to produce releases of existing projects.   
### The Smoke testing buildbot

  
I have built a buildbot instance using [collective.buildbot][]. The
script the slaves run is quite simple: it gets some projects source and
run their setup.py script, using various versions of the Python
interpreter, then the trunk itself. The commands run so far are
**sdist** and **bdist**.   
  
Then it compares every file contained in the archive created to make
sure produced archives are similar.   
  
I will encouter some exceptions, when the package I am testing includes
different files in its distribution depending on the Python version, but
those exception will be managed.   
  
Last, I cannot run this test on every package out there, for security
reasons. Until I have the proper virtual environment to do that, I'll
work on a white list of packages I "trust". So far, there's just a
package of mine, and NumPy. But this list will grow.   
  
If you are curious to know if your package builds under Python trunk,
get in touch with me, I'll probably add it if I know I can trust it.   
  
The last problem I have with this system yet is the fact that
setuptools is not working anymore with the Distutils trunk, so I am
unable to test setuptools-based packages.   
  
The buildbot is located here : [http://buildbot.ziade.org/waterfall][]

  [collective.buildbot]: http://pypi.python.org/pypi/collective.buildbot
  [http://buildbot.ziade.org/waterfall]: http://buildbot.ziade.org/waterfall
