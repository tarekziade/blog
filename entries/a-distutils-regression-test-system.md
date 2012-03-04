Title: A Distutils Regression Test System ?
Date: 2009-02-08 17:18
Category: distutils, python

I am making some progress in Distutils. I closed something like 10 bugs
last week, and I am reaching issues that were added 8 months ago. Not
that everything is entirely cleaned up in the newest issues, but they're
almost all being processed. Every commit comes with at least a test, to
get the code base back into a state were it is easier to make things
evolve without the risk of breaking it up.   
  
It comes through tiny little changes, with tests and an eye on the
coverage.   
  
Now I am facing an unpleasant situation : since the test coverage is
still low, I am always scared of breaking something in Distutils when I
am fixing a bug or making a change.Buildbots are watching, and I run
some of my own packaging work with the current trunk.   
  
But still, this is an unpleasant situation, and I don't want to cause
the package to be broken in the next Python version...   
  
But the regression tests exists ! They are there, hidden, in the
community. It's everyone package.   
1.  Joe adds an issue in the Python bug tracker, because Distutils
    didn't work as expected on his package because of a bug
2.  At some point the bug is (was) fixed.
3.  The test to make sure the bug is fixed is "Joe is running Distutils
    over his package again, and makes sure it is properly installed,
    compiled, etc".
4.  The bug is closed.

  
So how can I get back this test to make sure Joe's package is still
working properly, so he doesn't hate us at the next major Python release
?   
### A Distutils Regression Test Server

  
If Joe's package is on PyPI, we can set something up. A dedicated
server that watches the PyPI changelog and triggers a buildbot when:   
-   a new release of Joe's Package comes out
-   we change something in Distutils code

  
The precise test to be run is still unclear to me but, I am thinking
about some generic strategies and I think it's possible. Let's call this
test **a distutils regression test**. (If you have a better name, I'll
buy it)   
  
Of course it doesn't have to be on all the packages that are uploaded
out there at PyPI. Just Joe's one, because he came up with a problem we
fixed. And we would be ashamed if the bug comes back on Joe's package.   
  
This requires of course a server, and probably a vmware-like system if
Joe runs Windows or Solaris, to make buildbot slaves etc. It also
requires that Joe uses the right metadata in his package so we know if
it works under Python 2, Python 3, etc. [MvL added enough classifiers
lately for this][].   
### A Distributed Distutils Regression Test

  
But some package are not on PyPI, for privacy or conveniency in the
packaging process of the person in charge. So, what if the **distutils
regression test** is provided in a Distutils command ? It can run the
same test the server runs, and come up with a report that is sendable or
sent by mail to a special mailing list or so.   
  
This supposes that the developer is cooperative. So maybe it can even
be automatically triggered in case of any failure on any Distutils
command, and ask the user if he would like to send a report ?   
  
The good thing here is that it doesn't require CPU power on the test
server, and that anyone can run that test.   
### So what ?

  
Well I am just throwing an idea here, because I am really concerned
about the potential regression problems. Even if Distutils is 100%
covered with tests, it's not possible to test all combinations. The real
world environment is the only test that can be trusted at the end in the
packaging area.   
  
I'll throw this idea at the Language Summit in March, and if it catches
people interest, maybe a Google Summer of Code task could be done for
that topic ? Can't implement it myself, I am overwhelmed already in
Distutils maintenance :D   
  
Just out of curiosity, how do \*you\* test your packages to make sure
they get installed correctly ?   
  
**   
**

  [MvL added enough classifiers lately for this]: http://mail.python.org/pipermail/distutils-sig/2008-October/010419.html
