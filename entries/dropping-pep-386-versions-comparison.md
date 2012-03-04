Title: Dropping PEP 386 (versions comparison)
Date: 2009-07-03 13:44
Category: distutils, python

As you might know, we are working hard on Distutils side for Python 2.7
and 3.2 upcoming releases. The biggest work is on [PEP 376][], that will
introduce among other things a uninstaller function and functions to
query installed distributions.   
  
The other "big" work is on [PEP 345][]. We want to introduce a new
metadata field called "install\_requires" to be able to express
requirements. That's from the setuptools project and is quite used by
the community. Notice that there were several attempts to define
requirements in the past in Distutils, but none of them really made it
through.   
  
For instance, if you want to define docutils as a dependency for your
distribution but a version less or equal to 0.4, you can say :   
> docutils <= 0.4

  
But as long as you want to work with such dependencies and provide a
way to express them with operators, you have to be able to compare
versions. For instance if you want to compare an installed docutils
distribution to see of it is compatible with 0.4.   
  
That's another big topic we have been working on for the last few
months, with people from various communities (Fedora, Ubuntu, etc). And
I have started to write down [PEP 386][].   
  
But comparing version appears to be a topic that cannot be generic. It
seems that Distutils, therefore Python, shouldn't enforce any rule on
this.   
  
Furthermore, since we have said that Distutils should be a lighter
package, it will not implement a complete package managment system, like
setuptools or zc.buildout does.   
  
So I've decided to propose to drop PEP 386, and stick on a very simple
rule in PEP 345, saying that requirements can be defined, with :   
> distribution\_name OPERATOR version

  
where OPERATOR is in \>, <, ==, !=, \>= or <=.   
  
Last, so the work done at Pycon and in Distutils-SIG is not lost, I
will publish the library we wrote. This could be a very good basis for
packaging managment systems out there.

  [PEP 376]: http://www.python.org/dev/peps/pep-0376/
  [PEP 345]: http://www.python.org/dev/peps/pep-0345/
  [PEP 386]: http://www.python.org/dev/peps/pep-0386/
