Title: Distribute, end of the fork -- or the start of a new hope
Date: 2008-09-26 08:22
Category: plone, python, zope

*(This post is a work in progress, as things still evolve*)   
  
In a way, I am glad I have made a fork, and I am glad this is going to
be the shortest fork ever. A lot of people reacted on my proposal and I
could get a very clear picture of what is wrong in the
distutils/setuptools world, and how I could help on this.   
  
This is how I interpret it:   
  
Guido explained that the mistake made was not to integrate setuptools
in the core from the very begining. The current distutils code did not
evolve in the meantime and Phillip Eby worked on setuptools to make it
evolve. setuptools now reaches a point where it needs other contributors
to fit all the needs and solve more problems. It had one contributor in
the past, (Jim Fulton) but it needs more. It also became a mandatory
package for many folks in the Python world because Phillip did a great
work on it : it solves most problems.   
  
From what I could see, all the people that gets frustrated at some
point with setuptools, either don't use it, either try to see how it
could be changed. But when they try that, they take the same paths
others have taken before because there is a lack of info and
documentation on setuptools current status and future. And these paths
are quite long for the brain before you are able to provide a
well-thaught idea or patch.   
  
I have tried to help myself on setuptools, then I have started to blame
Phillip saying that he did not have enough time to make setuptools
evolve. But that was the wrong approach, because the only problem
really, is a lack of visibility in setuptools development. And this is
something that can be fixed quite easily I believe. The bug tracker
added some months ago helped a lot. A roadmap and one or two page around
it and that should be it.   
  
Guido also stated that it was merely impossible to work on the next
generation of distutils outside Python core. But in the meantime this
means that we need some people from the core to help us in there. And
they are really busy (I can understand that) on other matters in Python
code. We can write patches for some fixes for sure, and there are
hundreds of them to do in distutils.   
  
But to boost it we would need a core developer that gives some love to
that package. I mean, for example [I still have a patch waiting for
reviewing][], wich only adds some unit tests that are lacking. There is
no code there, just unit tests, and it is pending since 6 months...
Guido said that I could try to become a core developer, that this was
not impossible, if I started to contribute patches often to other parts
of Python as well. But that's quite a challenge.   
  
What frustrated me is that some people like Jim Fulton said they were
willing to work on a new distutils from scratch, and in the meantime I
understand what Guido says. he pointed us to Joel entry on [rewriting
from scratch][].   
### My Plans

  
I don't have the brain to drive a fork of setuptools at this time. I
knew it from the beginning, I just wanted to make people react. I think
that setuptools can be the laboratory where we can experiment things,
and distutils the place where we can apply them at some point, with
Phillip help because he has a pretty big overview of all that. It is
going to take years, but well, we are young.   
  
To help on this I will:   
-   try to gather people at the PloneConf to talk about it, maybe even
    sprint
-   try to document setuptools and distutils at my level, and write a
    roadmap for people to know what is going on. Either through a Sphinx
    site either on Python.org wiki.
-   work on patches for distutils, and try to point things in setuptools
    that might be brought into distutils
-   try to see if I have the brain to understand and work on other parts
    of Python.

  [I still have a patch waiting for reviewing]: http://bugs.python.org/issue2461
  [rewriting from scratch]: http://www.joelonsoftware.com/articles/fog0000000069.html
