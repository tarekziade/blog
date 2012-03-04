Title: Distutils 2 - Summary of the GSOC
Date: 2010-08-19 09:35
Category: python

Man this has been an amazing summer. We had 5 students working on
Distutils 2 and the work done was really great. Most important, I think
we managed to find new contributors for the future.   
  
Thanks to Josip, Alexis, Konrad, Eric and Zubin ! Also, thanks to their
respective mentors: Michael, Fred, Titus and Lennart.   
  
Let's have a very high-level summary of the tasks that were done. As a
reminder, Distutils2 aims to provide two things: a toolbox for third
party projects that want to provide packaging features, and a
full-featured package installer/manager for Python.   
### What was done

  
Distutils2 has now an **index** package, containing tools to work with
PyPI (or any PyPI-like server). This package contains classes to work
with the Simple Index protocol as well as the XML-RPC APIs PyPI has. We
think that the latter should be replaced by static REST calls, but
that's another topic. If you want to build a tool that uses PyPI, that's
the package you want to use. See [this doc][] (temporary location) for
more info.   
  
Another thing we added is an installer script. This script is a very
light script that uses the index package I've mentioned before, but also
a dependency graph builder we now have. The graph builder allows you to
analyze relations between installed projects, but also any project you
want to install. See [this doc][1]. This installation script will be
completed by an uninstallation feature very soon hopefully. You might
wonder why we did this since there are existing scripts like Pip or
easy\_install. The reasons are quite simple:   
  
1) we wanted to exercise all the modules Distutils2 provides to work
with PyPI, metadata and installed projects in a high level script. The
long-term goal is to have projects like Pip or Distribute use
Distutils2-the-toolbox since they'll use the same standards in the
future.   
  
2) Distutils2-the-package-manager wants to provide a basic
installer/uninstaller.   
  
Oh by the way, the depgraph tool is PEP 376 compatible, as we have now
a new version of pkgutil that supports PEP 376. See [this doc][2]. The
next task will be to put this new version in Python 3.2, and that should
happen fairly soon.   
  
Speaking of which, we are not sure yet if we are going to include an
plugin system like the entry points in Distutils2. Discussions on this
has been controversial on Python-dev. In the meantime you can enjoy the
[extensions][] project, which is a quick hack to have entry points
without depending on Setuptools or Distribute --and it's now Distutils2
and PEP 376 compatible--.   
  
Distutils2 is *almost* Python 3 compatible. The student in charge is
working hard to finish this task. See his [repo][]. As usual, the last
problems to be solved are about unicode, strings, bytes, you named it.
But I expect to include this work in one of the alpha version of
Distutils2 1.0.   
  
Last but not least, we worked on the commands front of Distutils2:   
-   **test** was added -- a command to run the project tests, inspired
    from Setuptools
-   **upload\_docs** was added -- a command to upload docs at
    packages.python.org. Originally created by Jannis Leidel and present
    in Distribute
-   **check** was added and improved -- a command that I created to
    check a project before releasing/uploading it. It checks its
    metadata, its description reST compliancy etc.
-   A command post/pre hook system -- similar to what RPM has so you can
    point code to be run before and after a Distutils command is run.
    Very powerful and useful -- but to be used with caution. You
    wouldn't want to add to the install process a code dependency you
    are not sure to have. But in the meantime, being able to run a code
    every time a project is installed on your system is sweet ;)

  
I am forgetting a million things, but I guess its not important, since
all our students are blogging about it ;)   
  
Thanks to Google, the GSOC is a great program. Distutils2 just got a
really serious boost, we are very close to a good, useful release.   
  
As a conclusion, to make things clear for the few people that still see
all these efforts as reinventing the wheel since packaging has been
kind-of-solved already elsewhere: Every extensible system, whether its
an OS like Debian or Fedora, or a language like Python, will *always*
provide its own custom packaging system, that is built on the top of the
community experience and needs. The only thing that really matters is to
have this work based on standards so inter-operability is manageable.
That's the goal of some of the PEP we have written, like PEP 386 and PEP
345 and that will make OS packagers life easier in the future. An
universal packaging system is an utopia.

  [this doc]: http://distutils2.notmyidea.org/library/distutils2.index.html
  [1]: http://bitbucket.org/josip/distutils2/src/tip/docs/source/depgraph.rst
  [2]: http://bitbucket.org/josip/distutils2/src/tip/docs/source/pkgutil.rst
  [extensions]: http://bitbucket.org/tarek/extensions
  [repo]: http://bitbucket.org/zubin71/distutils2-py3
