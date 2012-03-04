Title: The fate of Distutils - Pycon Summit + Packaging Sprint detailed report
Date: 2010-03-03 23:27
Category: python

### The summit

  
I quickly [posted an entry][] right after the [Language Summit][] we
held before Pycon in Atlanta. Basically, all the work I have being doing
in Distutils and the PEPs we've prepared for the "big refactoring" will
not be done in the standard library. Distutils in the stdlib trunk will
be reverted to its current 2.6.x state.   
  
I was quite despaired right after the summit. All the work we did
during in the past year would not land into the standard library for
2.7, and all the pre- refactoring work I did, like making the test
coverage decent, was going to be useless for the stdlib. Having that
work included in 2.7 was one of my goal and I worked hard on making sure
most of the important PEPs would be accepted before the feature freeze
for 2.7 happened (the first beta, freezing new features, is in 4 weeks.)
  
  
I was even more depressed because I started to pull out of Distutils
the "sysconfig" module and simplified the code in distutils, while
making sure that the backward compatibility was kept.   
  
I had a twenty minutes meeting with Guido after the Summit to clarify
the situation and he helped me understand why this was the right path
and worked with me on what to do next in the stdlib front and outside
the stdlib.   
  
Basically, **a package that comes in the standard library has a foot in
the grave** (I am paraphrasing Guido here.). Its APIs is frozen, and
people don't really expect nothing from it, but small new features and
bug fixes. Refactorings are dangerous, if not impossible.   
  
I have hit that problem in the past, in one of the 2.6 bug fix release,
where I broke Setuptools compatibility because of an internal change I
have made in a private method. The breakage was partly because
Setuptools overrides a private method and partly because a public method
that was not clearly documented was affected.   
  
A few weeks ago the problem happened again : someone complained on
python-dev because a declaration (an exception class) was missing from
Distutils. An exception class was imported from the *errors* module into
another Distutils module, but not used anymore there. And the module it
was imported in didn't have an *\_\_all\_\_* attribute. A third-party
tool was importing the exception from the wrong module, so when I
cleaned it up the third party module was broken.   
  
So basically, any change I make in Distutils, even a simple cleaning,
and worse, even a private method change, potentially breaks third-party
tools.   
  
You could argue that they should be careful in how they use Distutils,
and never patch it or change its internal etc., and for edge cases like
missing imports, just fix them.   
  
But hey, Python 2.7 is out of the door in five weeks, and the user
experience will be that *Python has broken third-party libraries*.   
  
And the worse part of it : some of these libraries like Setuptools are
not really maintained anymore and expect Distutils not to evolve
anymore. But Setuptools is used nevertheless since it solves some
problems Distutils doesn't. So the end user is the one that will suffer
from those regressions.   
  
In other words, project like Setuptools slows down the work we want to
do in packaging because the current eco-system depends on a big,
monolithic, messy pile of code that is located in different projects
with different maintainers.   
  
At this point, I understood that the easiest way for Distutils to
evolve was to get away from this pile and grow on another namespace
called **distutils2**.   
### Welcome Distutils2

  
If you have followed what is going on with packaging since last year,
you might think: "distutils, setuptools, distribute and now distutils2
?, oh no!!!"   
  
But that is going to be for the benefit of everyone. See the roadmap in
image below.   

  
  
  
[caption id="" align="alignnone" width="385" caption="State of
packaging"][![State of packaging][]][][/caption]   
  
So basically, I have forked Distutils and renamed its package into
**Distutils2**. The project is located in
[http://hg.python.org/distutils2][] and the goal is to put it back into
the standard library as soon as it reaches a state where it starts to be
used by the community. Distutils will just die slowly, probably pulling
Setuptools and Distribute with it.   
  
The Distribute project is still important because it can help us
releasing bug fixes or Python 3 support things ***today***.   
  
Distutils2 will be 2.4 to 3.2 compatible and will get back from
Distribute the good bits and implement the PEPs that were accepted
lately [PEP 345 and PEP 386][].   
  
And I am happily removing old code we don't want/need anymore without
worrying about backward compatibility. Yeah !   
### The packaging sprint

  
After the conferences, we started a packaging sprint and I was
surprised because many people showed up and worked on the topic.   
  
[caption id="" align="alignnone" width="484" caption="Brainstorming on
PEP 376"][![Brainstorming on PEP 376][]][][/caption]   
  
We created a few teams to work on PEP 376, mkpkg, the Hitchicker's
Guide to Packaging (HHGP), and Distribute. I won't say the name of each
person, I am too scared to forget someone :D.   
### PEP 376

  
Like last year, people from various distributions (Fedora, Ubuntu,
Debian) and I worked on packaging issues. They worked on PEP 386 last
year mainly (the versioning scheme) and focused on [PEP 376][] this
year. This PEP is about setting up a standard for installed packages,
and an installation index that allows to query what packages are
installed, and get their metadata. In extend, it provides an uninstall
feature. The goal is to have a standard for all package managers of
course.   
  
One part of the PEP is about describing the data files that are
installed with the project (like configuration files or documentation)
so they can be removed and maybe relocated. The group focused on
describing the files a project contains in a static way (in setup.cfg)
with variables that can be expanded an installation time (which values
are provided by Python, but globally configurable by the OS packagers.)
  
  
We did quite some work and brainstorming on this, and even focused on
removing setup.py ! A fully static description of a project
(metadata+file list) is the key to a better packaging tool !   
  
Expect a proposal soon on distutils-SIG, for PEP 376. If you want to
have a look, the draft proposal is here: [draft][].   
### mkpkg and Distribute

  
We had two one-member teams at some point, so I can name them without
being scared of forgetting someone ;)   
  
Sean worked on a nice add-on for Distutils2, a script that builds a
setup.py file after asking you a few questions. [He blogged about it][].
so I don't need to get into further details :)   
  
Noufal worked on fixing some bugs in [Distribute][]. We should do a
release at some point.   
### The HitchHicker's Guide to Packaging

  
Another group worked on the guide. The goal is to provide some help for
people that want to package things **today** and are despaired with the
sparse documentation they can find. Which tool to use ? how ? when ?   
  
The work done was quite amazing, look at it :
[http://guide.python-distribute.org][]   
  
I have spoken with Georg Brandl to see how we could move it to
docs.python.org and make it grow there.   
### Distutils2 coding

  
Besides PEP 345, I worked on making Distutils2 work for 2.2, 2.5, 2.6
and this is now over. I have also almost fully implemented PEP 345 in
there.   
  
There's now a metadata module with a dict-like [DistributionMetadata][]
class that knows how to read and write PKG-INFO files. It also knows how
to interpret the micro-language we've defined: the [environment
markers][].   
  
Last, I've added the [PEP 386][] version module : [version.py][]. This
one is used now by the metadata class to control versions.   
  
More to come !   
### Next sprint at Confoo.ca

  
The [next packaging sprint][] will happen in Montreal, where I am going
as a speaker next week. We will continue the worked started, so stay
tuned.

  [posted an entry]: http://tarekziade.wordpress.com/2010/02/18/python-language-summit-summary-of-the-packaging-track/
  [Language Summit]: http://www.google.com/url?sa=t&source=web&ct=res&cd=1&ved=0CAYQFjAA&url=http://us.pycon.org/2009/about/summits/language/&ei=TNWOS9WfNMHM4gbx0vitDQ&usg=AFQjCNG3uKSR65UU2riqyQDEAgFng5b2eg
  [State of packaging]: http://guide.python-distribute.org/_images/state_of_packaging.jpg
    "State of packaging"
  [![State of packaging][]]: http://guide.python-distribute.org/introduction.html#current-state-of-packaging
  [http://hg.python.org/distutils2]: http://hg.python.org/distutils2
  [PEP 345 and PEP 386]: http://tarekziade.wordpress.com/2010/02/10/pep-345-and-386-accepted-summary-of-changes/
  [Brainstorming on PEP 376]: http://lh3.ggpht.com/_BBU4XN71nJo/S45d_jRywdI/AAAAAAAAAl4/ggtwGaVkKwU/s720/IMGP7237.jpg
    "Brainstorming on PEP 376"
  [![Brainstorming on PEP 376][]]: http://lh3.ggpht.com/_BBU4XN71nJo/S45d_jRywdI/AAAAAAAAAl4/ggtwGaVkKwU/s720/IMGP7237.jpg
  [PEP 376]: http://www.python.org/dev/peps/pep-0376
  [draft]: http://hg.python.org/distutils2/file/243df45d7f6f/docs/design/wiki.rst
  [He blogged about it]: http://www.tummy.com/journals/entries/jafo_20100302_003614
  [Distribute]: http://bitbucket.org/tarek/distribute
  [http://guide.python-distribute.org]: http://guide.python-distribute.org
  [DistributionMetadata]: http://hg.python.org/distutils2/file/243df45d7f6f/src/distutils2/metadata.py
  [environment markers]: http://www.python.org/dev/peps/pep-0345/#environment-markers
  [PEP 386]: http://www.python.org/dev/peps/pep-0386
  [version.py]: http://hg.python.org/distutils2/file/243df45d7f6f/src/distutils2/version.py
  [next packaging sprint]: http://www.montrealpython.org/2010/02/upcoming-sprints/
