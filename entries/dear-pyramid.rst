Dear Pyramid, help Python Packaging
###################################

:date: 2012-09-12 21:38
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade


Dear Pyramid,

My previous letter to Django drew a lot of drama. So I guess I
had to send you a letter too.

Some members of the community seemed to have seen my attempt to warn
Django about Setuptools like rejecting how *you* handle packaging
and deployement.

Fear not, most of the ideas and innovations Setuptools brought have
been included in the standardization effort we've done in the past 3 years.

We wanted to build standards based on Setuptools innovations, and
in the same time provide a sane ground for a new implementation.

Namely:

- PEP 345 - The new metadata that `includes dependencies <www.python.org/dev/peps/pep-http://www.python.org/dev/peps/pep-0345/345/#requires-dist-multiple-use>`_ !
- `PEP 376 <http://www.python.org/dev/peps/pep-0376/>`_ - a *single* installation database all tools can share
- `PEP 386 <http://www.python.org/dev/peps/pep-0386/>`_ a unified versionning scheme that seems to work for the Python community at large
- Namespace packages - still ongoing, see http://mail.python.org/pipermail/import-sig/2012-March/000421.html

and oh.. I can stop writing here. Brett wrote a summary here : https://plus.google.com/u/0/115362263245161504841/posts/UcBQK8P4jw3


Subculture
==========

When I used the world **subculture** to describe features we don't
really need at large in the Python community, I was a bit vague.

Here's what I am thinking about:

- **entry points**. It's a great feature but just an ad-hoc plugin
  system that is not a standard.

- **eggs** and **zipped eggs**. The original intent was to create
  a plugin system when one could drop a zip file and have it loaded
  as a new package. As far as I know, a few projects use this for
  their plugin systems. But it became de-facto an installation
  standard on its own -- and that added a lot of mess.

- the **develop** command. I know many people that just tweak their
  Python path. I don't think you can blame a project for not
  providing Setuptools just because you can't run *develop*.
  It seems to me that this feature could be written in
  a script that does not force projects to have *Setuptools*.

- **console scripts**. Besides the fact that they are entry points
  (I don't see why they have to) - they are just another implementation
  of the existing Distutils *scripts* feature.

  You like the console script implementation better ? You think the
  exe wrapper is the way to go ? Just send a diff, I don't see
  why we would not use this.

  But this is just an implementation detail.

- **extras** - this is an underused feature as far as I know in
  the world of setuptools-based projects.
  Turns out it's been added in `PEP 426 <http://www.python.org/dev/peps/pep-0426/#provides-extra-multiple-use>`_


Maybe I am forgetting some, but those are the ones I recall right now.


So what ?
=========

I am still thinking Django should not embrace Setuptools but rather
slowly adopt all those new standards.

Simply because using Setuptools in Django would mean jumping into the
wagon we're trying to slowly remove from the packaging train.

Turns out, after I blogged, I was told Django was not planning to
use Setuptools -- so it looks like we're agreeing on this.

It's not 100% clear yet on what would be the exact roadmap for this, and
I'll try to think about one -- a bug was opened in the Django tracker
for this.

As I said the first step is to write a **setup.cfg** file that follows
the new standard for the metadata and the data file description
and start from there.


How can you help ?
==================

A few things I guess:

- If you are frustrated about anything we've done in our PEPs, tell us
  at python-dev or distutils-SIG

- If you think there's something from setuptools we miss & need, let's
  talk about it and start a standardization process.

Python packaging will be sorted out by going through a standardization
& PEP process for everything -- for the sake of inter-operability.

We'll succeed the day every packaging tool out there will rely on the
same set of standards.

I've learned the hard way that a packaging tool not based on a
standard is doomed to stay on its own out there.

Sincerely,
Tarek
