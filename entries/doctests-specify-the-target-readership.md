Title: Doctests: specify the target readership
Date: 2008-04-05 13:53
Category: documentation, plone, python, zc.buildout, zope

Ben Bangert was [reacting][] about [zc.buildout][] doctests, saying that
they are hard to read from the PyPI page, and the examples hard to use
and follow.   
  
I agree with Ben as these doctests are very hard to read when you are
not familiar with zc.buildout testing modules, which provides a set of
API the doctests relies on.   
  
But from a developer point of view, adding a feature to such a package
is best done through doctests, using zc.buildout.testing goodies. And a
developer that is familiar with this package, will find this doctest
very useful.   
  
zc.buildout in any case, is trying to structurize its PyPI front page,
and push a maximum amount of doc for users, so ... kudos !   
  
I think the problem is more about **specifying the target readership**.
  
  
I would like to point another example that comes in zc.buildout:
dependency-links.   
  
The main doctest that appears at PyPI as a light, human-readable
section: [http://pypi.python.org/pypi/zc.buildout\#dependency-links][]   
  
And the very same section is continued in a specific doctest that does
not appear on the main page:
[http://svn.zope.org/zc.buildout/trunk/src/zc/buildout/dependencylinks.txt?rev=81182&view=markup][]
  
  
So what happened here is that the developer specified two kind of
readers:   
-   people that will reach the package through its PyPI page
-   people that will go deeper in how the package works, through recipes
    or tutorials

  
From there I think there's a simple guideline that could be applied to
enhance the package documentation when adding a feature:   
-   resume the feature in the main page (long\_description) with
    examples that does not rely on specific testing API. In other words
    it should be made of plain english and plain python when needed;
-   leave doctest that relies on internal testing API as complementary
    documentation.
-   define for each doctest its nature (recipe, tutorial, etc)

  
How could we help people doing such structuration ?   
  
The distutils metadata could be a good place to do it, by adding an
extra\_doctests list for example, that would contain a list of doctests.
From there, PyPI could display the long\_description text as usual, and
add a "more information section".   
  
Let's take an example:   
   def _(f)

    return open(f).read()



    setup('my.package', ...

    long_decription=_('README.txt'),

    extra_description=

    {'recipe': [_('create_this.txt'),

    _('do_that.txt')],

    'tutorial': [_('how_to_use.txt')

    _('how_to_2.txt')]}

  
From there, PyPI could provide a Table of content, with a structurized
documentation, and additional pages for the package, grouped by types
(recipe, tutorial) etc. -\> Maybe a Sphinx-powered PyPI ? :)   
  
By the way, I have another post related, which tries to summarized good
pratices in technical writing :
[http://tarekziade.wordpress.com/2007/02/23/technical-writing-the-seven-laws][]

  [reacting]: http://groovie.org/articles/2008/04/04/sacrificing-readability-for-automated-doc-tests
  [zc.buildout]: http://pypi.python.org/pypi/zc.buildout
  [http://pypi.python.org/pypi/zc.buildout\#dependency-links]: http://pypi.python.org/pypi/zc.buildout#dependency-links
  [http://svn.zope.org/zc.buildout/trunk/src/zc/buildout/dependencylinks.txt?rev=81182&view=markup]:
    http://svn.zope.org/zc.buildout/trunk/src/zc/buildout/dependencylinks.txt?rev=81182&view=markup
  [http://tarekziade.wordpress.com/2007/02/23/technical-writing-the-seven-laws]:
    http://tarekziade.wordpress.com/2007/02/23/technical-writing-the-seven-laws
