Title: zc.buildout on-going work
Date: 2008-06-10 09:20
Category: plone, python, zc.buildout, zope

Just a quick post about the work going on in zc.buildout.   
  
Work published lately:   
-   Malthe and Mustapha have added a nice option to be able to add or
    substract values in variables that are inherited from an extended
    cfg file (already available, see the doc [here][])
-   I have added an allow-hosts option, that behaves like easy\_install
    one, which can be used to restrict some accesses (see [here][1])
-   Sidnei fixed some annoying bugs (missing quotes in some process
    calls)

  
On-going work:   
-   I am working on a timeout config option, to be able to set the
    socket timeout (see [my previous post][] on this). Andreas added a
    command-line option a bit ago as well, but we need to refactor it a
    bit to have it as a config file option.
-   I work on a python API so the buildout can be driven from the code.
    This useful for instance to create tests that are not using a
    os.popen or os.system call to build a buildout: a separated process
    is hard to debug.
-   We are having some thaughts on having a multiple-index enabled
    buildout. Still brainstorming.

  [here]: http://pypi.python.org/pypi/zc.buildout/1.0.4#variable-substitutions
  [1]: http://pypi.python.org/pypi/zc.buildout/1.0.4#allow-hosts
  [my previous post]: http://tarekziade.wordpress.com/2008/04/07/zcbuildout-monday-trick/
