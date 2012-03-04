Title: Words on : Distribute, Distutils, PEP 376, PEP 386, PEP 345
Date: 2009-07-24 22:56
Category: python

I am taking a break for a week starting tomorrow morning. My wife made
it clear : **my laptop and internet are totally forbidden during 7
days**. So I thought it was a good opportunity to make a status of all
the projects that are going on in the packaging world.   
### [![image][]][]Distribute

  
The setuptools fork is doing good. We've discussed the roadmap strategy
with some people at Distutils-SIG and came up with that plan:   
  
**0.6 will be released the first week of August**. It will support
Python 2.x only and will provide a bootstrap to replace an existing
version of setuptools, as described in my [previous entry][].   
  
**0.7 will support Python 2.x and 3.x** and will refactor the code in
three distributions. It will also rename all parts under new names, so
they will not compete anymore with setuptools. Its development will
start right after 0.6 is out. If you have ideas or feature requests,
please add them in our [issue tracker at bitbucket][].   
### Distutils

  
They are [some patches waiting][] for my attention, I need to work on
when I am back. But globally, if you open Distutils code, you will
notice that it has been PEP8-fied (besides a few places I need to
finishe) and test covered.   
  
Some small refactorings have been done, like removing duplicate code
and using the tar module of the stdlib instead of the tar command on the
system, thus allowing building tar archive under win32 without having to
install the tar program for example. Another nice change was done on the
upload command: it uses urllib2 now, meaning that you can use an http
proxy with a environment variable transparently. Other changes are on
their way, like fixing the mess with "compiler" option, and cleaning up
some remaining duplicate behaviors.   
  
But nothing is deeply changing yet on how Distutils works. It waits for
the PEPs we are working on to be accepted...   
### PEP 376

  
After I thaught this PEP was ready to be accepted, I sent it from
Distutils-SIG to Python-dev. Then we had very long threads on Python-dev
about it, showing that it was not ready at all...   
  
Man, I don't think I've picked the easiest topic ;)   
  
Anyways, people gave a lot of thaught on the topic, and Paul Moore
helped building a PEP 302-compatible version of the prototype, you can
see at [bickbucket][]. From there, we still need to fix the problem of
the absolute/relative paths in the RECORD file, and try to have real
world uses cases, with various package managers applications. But we
will eventually have an acceptable PEP, I hope, within a few months.   
  
This pep will add query APIs in pkgutils in the stdlib, so you know
what's installed in your Python. It will also provide tools to uninstall
installed ditributions.   
  
It's a hot topic because we are dealing with the fuzzy boundary between
*Python the extendable language*, where you can install distributions
using distutils-based tools, and *Python the interpreter*, that gets
extended with packages managed by an OS-based package manager like APT
under Debian for example. So for the latter, all our tool are getting
too much in the way and should not make it hard for system packagers to
extract the metadata they need to re-package distutils-based
distributions.   
### PEP 386

  
Man, this PEP would make our life easier. It's all the work we started
during Pycon, to find an *acceptable* way to compare versions. By
acceptable I mean that could be used in our community **and** workable
by OS packagers. I said I would drop it, because there were too much
controversy, but quite a few people would like to see it accepted.   
  
I doubt Guido will accept a PEP that would enforce a version scheme
though.   
  
I had created this PEP, so we could move forward on **PEP 345**, where
we want to introduce "install\_requires", the field used in setuptools
to list dependencies.   
  
The prototype for PEP 386 is in bitbucket too : [verlib][]   
  
Whatever happens, I'll probably publish it. Its useful to build a
package system, and it has a function to translate most
distutils/setuptools version schemes.   
### Now about my addiction

  
I know that sounds stupid, but I don't know what is going to happen
next week. It's been years since I've not been fully offline for a week.
I already have right now so many threads to catch up on various mailing
lists that I am scared of how it's going to be in 7 days...   
  
But it's probably a good thing for me to do this :)   
  
I am off, see you in 7 days !

  [image]: http://farm2.static.flickr.com/1327/1068561077_dc14096ad3_o.gif
    "Internet Addicted"
  [![image][]]: http://www.flickr.com/photos/9009139@N08/1068561077/sizes/o/
  [previous entry]: http://tarekziade.wordpress.com/2009/07/22/preparing-to-release-distribute-0-6/
  [issue tracker at bitbucket]: http://bitbucket.org/tarek/distribute/issues/
  [some patches waiting]: http://bugs.python.org/issue?@columns=title,id,activity,status&@sort=-activity&@group=priority&@filter=components,status&@pagesize=10&@startwith=0&status=1&components=3&@dispname=Distutils
  [bickbucket]: http://bitbucket.org/tarek/pep376/
  [verlib]: http://bitbucket.org/tarek/distutilsversion/
