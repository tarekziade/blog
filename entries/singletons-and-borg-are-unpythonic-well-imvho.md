Title: Singletons (and Borg) are unpythonic (well.. imvho)
Date: 2009-01-22 23:19
Category: python

Alex Martelli wrote a review about my latest book (can't find a
permanent link on this, just look at Amazon.com you'll find it).   
  
Amongst the negative parts there's one noticeable part I'd like to
discuss in my blog, because I disagree with Alex's analysis.   
  
Alex says:   
> This also holds for the chapter on design patterns, with such
> egregious claims as "Singletons should not have several levels of
> inheritance" -- they should have as few as practical and feasible,
> \*exactly like any other class\*; the desire to limit the number of
> distinct instances (which is mostly about STATE) is quite orthogonal
> to the issues with subclassing (which is mostly about BEHAVIOR). From
> this original "totally missing the point" follows a classic howler
> (which I've seen repeated in a review above): "why not use a module?".
> I have news for you, Tarek: a module supports \*ZERO\* inheritance --
> which is quite a bit stricter than even the unjustified "should not
> have several level" claim above. Having to completely give up the
> usefulness of inheritance just because you want to limit instantiation
> would be a very limiting engineering tradeoff! If there's no need for
> inheritance then \*of course\* you want to use a module - DOH! - but
> if there IS (or if special methods can really help you) then it's not
> an option.

  
I think that the Singleton (and Borg) pattern is totally useless in
fact. That's not the philosophy of Python in my humble opinion. And I
think my book is right to advise people not to use this pattern.   
  
I don't see the point of bending down a class so it only has one
instance, where you can simply create an instance of that class in a
module, add a "\_" prefix to that class, and tell the world that this
instance is your singleton. I don't see why a class should deal with
that kind of STATE.   
  
Frankly, I doubt that this singleton/borg pattern is really used in the
community.   
  
The only place where I really had to use singleton classes was in Zope.
But that was more like a marker than anything else, and the class was
registered under a "single" name in a global mapping (eg. its id in its
container, in the ZODB tree). And in that case, we were creating one
mixin class that used a singleton class, and we called it a "tool", with
all the desired BEHAVIOR inside of it.   
  
And well, if we would had several instance of it, for sure nothing bad
could really happen, because the real unicity was provided by the id of
the object. And nowadays those "tools" are going away and they are now
called "utilities", and I don't think any singleton class is still
really present or used. Just simply because a class is not the right
place to enforce this.   
  
I'd also say that there's an architectural problem when you enforce
things like this in Python. If a programmer tells me that he wants to
use a Singleton on his class because it holds a DB connector he wants to
be instanciated once in his application, I am asking him right away to
review the way the program is structured.   
  
So what is the closest element in Python that will let you mark an
object as unique ? what is the most convenient way to mark an object
with an id in a container ?   
  
*A simple variable in a module*. (or a simple declaration in a zcml
file if you are a zopish guy)   
  
I love Python for this because it's multiparadigm unlike Java : you
don't have to set up over-engineered OOP stuff for this kind of needs
(and it is surely not a tradeoff to use well engineered OOP besides).   
  
Last, when I am claiming in Frenglish, that "Singletons should not have
several levels of inheritance". This is just to warn people that, since
these patterns are trying to break the way classes work, *you might get
screwed at some point* when singletons are subclassed. A descriptor or a
metaclass or whatever can just break your singleton stuff because Python
was not meant to be used like that. It's not robust.
