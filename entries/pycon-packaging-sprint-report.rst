Pycon - Packaging Sprint/Bof Report
###################################

:date: 2012-03-15 14:54
:tags: python
:category: python
:author: Tarek Ziade


We did a packaging open space and a sprint during Pycon and the talks and 
work we did was quite constructive. The good thing is that most people
that are involved in the maintenance of the packaging tools in our
eco-system were present -- that helps a lot.

I don't want to go into great details here, mostly because I am currently
in a train going back to Dijon, completely jet-lagged from the Pycon
trip. But I do want to blog about it now to make sure I write down
while it's fresh.

.. note::

   Just a quick note on the terms I use to avoid confusion:

   - **distutils** is now frozen in Python
   - **packaging** is the new distutils, with backward incompatible changes
   - **distutils2** is the backport of packaging for Python 2.5 to 2.7


On to the top of my head, here what we've decided to do and 
worked on. I am adding a **[status]** marker for the ones I know.

- release a Python 2 Distutils2 alpha version for people to play with [done]
- add oauth support in PyPI
- make SSL the default way to register and upload projects on PyPI
- intensive testing and debugging of Distutils2 [lots done here, but ongoing]
- poke at using Distutils2 in zc.buildout [ongoing]
- start a discussion on Distutils-SIG about the *next* binary format [done]
- publish setup.cfg at PyPI so tools or humans can read it without
  downloading and/or executing some code.

That does not sound like a lot of achievements, but this Pycon was in my 
opinion the best Pycon ever to put all the people involved in packaging
on the same page and agree on some plans for the future.

That did not include the people from the scientific community, like last 
year or the year before. I was told that's because they have an aversion
for the Distutils codebase. Guess what - mee to :)

But I think we can find a mutual ground for several reasons:

- what we're building in Python is based on **standards** we define in PEPs.
  So that's orthogonal to an implementation. For example Scientific build 
  tools could definitely consume our metadata, or our setup.cfg
  (http://docs.python.org/dev/packaging/setupcfg.html).

- the **packaging** package in the standard library has been revamped, uses
  clean, modern python. It has useful tools in it -- for example, if you 
  need to browse PyPI or the installed packages, you have now reference 
  implementations there, that will be used by pip and zc.buildout in the
  long term. Notice that they are backported in the standalone distutils2 
  package so they can already be used 

- the compilers part is still horrible, but we made it pluggable. If you 
  build a build tool, distutils2 can be configured to use it. So you can
  hate that code, but you should try to be compatible with at least the
  definition of extensions in setup.cfg.

So, like last year and the year before, I'd like to say again that 
anyone from the scientific community interested in helping in the 
standards or anything else is more than welcome.

If you're curious, you can see the etherpad we used here during Pycon:

- http://etherpad.mozilla.org/packaging-bof
- http://etherpad.mozilla.org/packaging-sprint

On a side-note, using a pad like this was extremely useful during the 
open space, since everyone could interact live in it.

Oh by the way, kudos to Eric Araujo for the work he's been doing in the
last months in packaging.

