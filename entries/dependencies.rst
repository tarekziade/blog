Declaring dependencies in Python
################################


:date: 2013-04-13 09:15
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

In Python Packaging, when you are giving for your project
a list of dependencies, the right approach is to do whatever
works for the *majority* of your users because there's a
plethora of techniques used by people out there
to deploy Python software.

That's the case for 2 main reasons:

1. Most Python projects can be deployed in different operating
   systems - and unless you're doing a specific packaging work
   for each one of them, you are doomed to provide a good enough
   generic package.

2. There are different installers with different approaches
   and your Python projects should try to be compatible with
   all of them.

Some of users *will* have issues with your projects, you have
to accept this fact and just make sure you provide enough
documentation and hints for them to work around those issues.

This blog entry tries to summarize my current knowledge on what's
the best way to defining dependencies - I hope I'll have some feedback so
I can update it with better techniques. Also, note that I have not
applied this to all my projects. I should.

So if you disagree on my approach please comment !

.. note::

   I am not talking about Virtualenv on purpose here, to avoid
   extra complexity.


Nature of your project
----------------------

The first thing to think about is the nature of your project. They are two
kind of projects in the Python world that can be installed by users:

1. library & tools that will be used in conjunction with other
   Python projects.

2. End-user applications that are using a plethora of other
   Python projects themselves.


The first category is what we create most of the time: utility modules,
extensions for some frameworks, library to connect to a database, etc.

The second is a bit specific. It can be a framework, a website or a
desktop application - Most of the time it's driving the whole Python
environment it's running in and dictates what should be installed.


Library & tools
---------------

For library & tools, my advice is to do the following:

1. provide a setup.py file that uses distribute/setuptools *install_requires*
   option, and when appliable provide a pure distutils fallback.

2. **do not pin any dependencies** in your setup.py - it turns out it's
   making people's life a pain when they want to tweak the versions of the
   libraries themselves in tools like zc.buildout

3. provide a pip `requirements <http://www.pip-installer.org/en/latest/cookbook.html#requirements-files>`_
   file where everything is pinned. That's your dependencies documentation.
   It says what versions of each dependencies your project depends on.
   When possible, add indirect dependencies as well in it.

4. In your installation instructions, explain that using the pip
   requirements file is the recommended way -- I usually even provide
   a Makefile that does it - but that running *pip install* directly
   should work fine.

5. In your continuous integration tool - *you are using one, right? ;)*
   use `tox <http://tox.readthedocs.org/en/latest/>`_ to run your tests in all
   Python versions you are supporting, and also by deploying your code
   with pinned dependencies *and* unpinned dependencies.


Here's a setup.py example:

.. code-block:: python

    try:
        from setuptools import setup

        install_requires = ['gevent', 'requests']

        try:
            import argparse
        except ImportError:
            install_requires.append('argparse')

        kws = {'install_requires': install_requires}
    except ImportError:
        from distutils.core import setup
        kws = {}


    setup(name='yourproject', version='1.1', etc.., **kws)


And the Pip requirements file for Python 2.6 ::

    gevent==0.13.8
    requests==1.2.0
    argparse==1.2.1


End-user application
--------------------

Not maintaining one myself, I have no clue what's the best way to do this
but I suspect you really want to maintain a list of projects versions that
are working with a given version of your project.

I recall Zope has this pretty neat thing called the **Known Good Set** (KGS)
where they maintain a list of versions that are known to work well together:
https://pypi.python.org/pypi/zope.kgs

In any case, deploying a whole Python stack in real life cannot be done with a simple
*pip install PROJECT* call, unless it's a small thing. So maintaining a pip requirements
file sounds like a good approach here.

So all-in-all I guess every advice I gave in the first section can be applied for
end-user applications as well - as long as you make it clear that running
*pip install PROJECT* won't be enough.


