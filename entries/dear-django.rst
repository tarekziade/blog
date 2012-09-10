Dear Django, help Python Packaging
##################################

:date: 2012-09-10 11:00
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade


Dear Django,

We don't know each other very well, but I wanted to write you this little
letter to tell you that today, you have an opportunity
to do something to help cleaning up the packaging mess we have in Python.

Some people have suggested that Django should move to tools like
Setuptools to offer a better packaging support.

I think that would be a bloody mistake, and that would put Django
in the same sorry state that the rest of the community: a mixed-bag
of various packaging standards that are not always inter-operable.

I won't get into all the gory details, but I think you should by all
means avoid using Setuptools or Distribute in your core and be more
ambitious.

We've been working in the last few years on new standards
for packaging, like PEP 376, PEP 345 and PEP 386. These PEPs take back the
good ideas from the various tools out there and try to define simple
standard for project versioning, dependencies definitions,
installation database and so on.

One of the great change in these standards is setup.py going away.
The central idea is that a project description should be a set of metadata
we can share at places like PyPI and that we should not depend on
running some third party code to get those metadata back.

That's what most of the packaging systems do in other programming languages
or in system-level packaging systems.

If you want more background you can read http://www.aosabook.org/en/packaging.html

There are more good things to come if you lurk at pyton-dev or distutils-SIG
these days, and active people in the matter.

Some people will tell you that the new things we've built are not
*production-ready* or that they don't match the features Setuptools provides.
But ask yourself if those Setuptools features are really something you want
or are subcultures additions from some specific communities.

Django, as it is today, **works**. People can install it and use it.
And I can tell you as someone that worked on this topic for quite some time
that I see little to no benefit to switching to Setuptools.

Instead, I think you could become a key player by being an early adopter
for the new standards we've created.

*How can this be done ?*

The first step would be to add in Django PEP 345-style metadata -- since
it does not interfere with existing standards, and see with the folks at
distutils-SIG how an installer like **pysetup** digs it.


Sincerely,
Tarek
