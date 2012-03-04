Title: Expert Python Programming book, more details + sample chapter
Date: 2008-09-24 16:26
Category: plone, python, zope

It seems that my book is now officialy available, so I should give more
details about its content.   
### Who should get this book ?

  
I think Shannon described the targetship of my book quite well in the
foreword:   
*If you're looking to progress from knowing Python to mastering Python,
this is the   
book for you. In fact, this is exactly the type of book I wish I had
had ﬁve years ago.   
What took me years to discover by steadfastly attending talks at PyCon
and my local   
Python users' group is now available in a succinct book form. *   
  
What is means is that this book does not only focus on Python syntax,
but also covers how to use Python in a professional environment. Beyond
writing a program that works, a good Python developer uses continous
integration principles and tries to think about the maintainability of
his code. Taking care of choosing good names for instance, will
naturally make the code better. Test-Driven Development make the code
better too.   
  
The book tries to synthesize these good practices and explain why they
are good. So if you are using Python and know how to write a program,
and want to push it further, this is a book for you.   

### On the code

  
All the code of the book lives here:[http://atomisator.ziade.org][]. So
it can evolve.   
### On my English

  
I am French. My english is far from being perfect. The Packt team did a
great work on improving it, but you will probably feel my french touch
in the book. I hope you won't mind.   
### On the structure

  
Depending on your needs, you might feel that the ordering of the
chapters is not what you were expecting. The current ordering is the one
I would use when writing an application, but this is my own vision. If
you are a manager you probably have your own way. I worked this out with
one concern in mind : every chapter is independant. So feel free to jump
to any chapter when you have finished one.   
### Sample chapter

  
I am giving away Chapter 10, as an appetizer: [chapter 10 of "Expert
Python Programming"][]   
  
This chapter is about documentation. It gives principles and good
practices to document your Python projects. It is an invitation to use
Sphinx and reStructuredText, together with a set of good practices.   
### More details on each chapter

  
**Chapter 1**, Getting Started. I took me a long time to decide whether
I should drop or not this chapter. It describes how to install an
environment to work with Python. Since the book is for people that
already knows how to use Python a bit, it seemed out of topic.   
  
A few things convinced me to let it in: I have a friend that works with
Python under Windows for years, but don't know anything about distutils
or setuptools and how to set the proper MinGW environment to be able to
install packages without having any trouble. Secondly: I am making some
assumptions there for the rest of the book examples to work and I am a
setuptools fan. Last but not least: this is a small chapter compared to
the size of the book (less than 10%)   
  
**Chapter 2, Syntax Best Practices—Below the Class Level**, I had a lot
of fun there. I am talking about topics like coroutines and contextlib.
Pure Python joy !   
  
**Chapter 3**, **Syntax Best Practices—Above the Class Level**, This
chapter explains amongst other topics why super() is dangerous, how the
MRO works, meta-programming, etc. Lots of fun too. I think people will
enjoy it a lot.   
  
**Chapter 4**, **Choosing good names**, Writing a program that works is
a good thing. Writing a program that can evolve and that is
comprehensible by other developers is harder. This chapter will give you
some clues on choosing good names, beyond the PEP8 guide, and how to
organize and build a modular application by working out the API.   
  
**Chapter 5**, **Writing a package**. The main ideas here are: write
and distribute all your packages the same way, so use templates and
distutils.   
  
**Chapter 6**, **Writing an application**. Same as chapter 5, but at
the application level. This field is very different depending on what
frameworks you use and what community you are part of. I tried to come
up with something that seems to be the way all developers are tending to
take. Maybe I am a bad visonnary, maybe I am wrong. I don't think I am.
If you disagree, you will still find interesting stuff in there.I am
presenting a micro case study to make things clearerild a modular
application by working out the API.   
  
**Chapter 7**,** Working with zc.buildout**. Buildout is widely use in
Plone and Zope. There are other tools out there of course. But buildout
rocks imho. This chapter show how it work and how to use it to work and
distributeyour application.   
  
**Chapter 8**,** Managing code**. Its starts with a state-of-the-art of
version control systems and continuous integration principles. I am
explaining how you can work using mercurial and buildbot.   
  
**Chapter 9**,** Managing lifecyle**. Same as chapter 8, but focusing
on software lifecycles, and why the iterative approach rocks. Also show
how trac can be used.   
  
**Chapter 10**,** Documenting your projects, ** Just read it :)   
  
**Chapter 11**,** Test-Driven Development, **This is my TDD manifesto
:)   
  
**Chapter 12 and 13**,** Optimisation,** Ever wondered how to calculate
the complexity of the code ? how to benchmark and optimize ?   
  
**Chapter 14,** **Useful design patterns,** Design patterns revisited,
because the GoF did not know enough about Python :)   
### Feedback !

  
It is really frustrating in some way to write a printed book on a topic
like Python. By the time I have finished the book and gave it back to
the editor, I was already thinking on some changes and some improvments
I could make.   
  
I created a website for the readers : [http://atomisator.ziade.org][]   
  
You can add a ticket there for the v2 !

  [http://atomisator.ziade.org]: http://atomisator.ziade.org
  [chapter 10 of "Expert Python Programming"]: http://tarekziade.files.wordpress.com/2008/09/chapter-10.pdf
