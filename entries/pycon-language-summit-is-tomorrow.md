Title: Pycon Language Summit is tomorrow
Date: 2009-03-26 02:38
Category: distutils, pycon, python

Tomorrow is the [Language Summit][], yeepee. :)   
  
The *package and distribution* part of the Summit is going to be great
since we have key people coming up.   
  
zc.buildout and pip leaders (Jim Fulton and Ian Bicking) will be
present, and many others. I'll be representing Distutils, since I am its
current maintainer. Unfortunately Philip Eby (setuptools) can't make it,
but he should be reachable via IRC (I am trying to set something up for
tomorrow).   
  
Anyway, one of the goal of the Summit is to validate the new features
and enhancements we want to introduce in Distutils and PyPI. It's
important to make sure they play well with third-party tools like
zc.buildout, setuptools and pip. We also need to make sure these tools
will evolve in the same direction in the future.   
  
We have reached a point in Python where we need to concentrate all the
packaging effort to build a common standard in the standard library,
because it is badly needed.   
  
Here's a draft of the slides I will present tomorrow, during the first
5/10 minutes, as a session leader:   
-   Packaging Survey results overview
-   Topics to discuss   
   -   setting up an organized network of mirrors (see [PEP 381)][]
    -   discuss about other PyPI enhancements
    -   improve the package installation / uninstallation (see [PEP
        376)][]
    -   discuss the package dependencies problem and see if we can come
        up with a PEP
    -   discuss the multiple version problem and see if we can come up
        with a PEP
    -   discuss the isolated environment vs the OS vendor approach and
        see what can be done to improve their coexistence.

      

  
Summit schedule:   
-   13:20 -\> 13:30 : presentation
-   13:30 -\> 14:30 : discussions/work in small groups
-   14:30 -\> 14:50 : "tour de table"
-   14:50 -\> 15:10 : break
-   15:10 -\> onwards: sprint !

  
I am not sure about the 'work in small group' part yet, because I don't
know how many people will show up, and what people will want to focus
on.

  [Language Summit]: http://us.pycon.org/2009/about/summits/language/
  [PEP 381)]: http://www.python.org/dev/peps/pep-0381
  [PEP 376)]: http://www.python.org/dev/peps/pep-0376/
