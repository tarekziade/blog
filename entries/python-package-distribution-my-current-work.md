Title: Python package distribution - my current work 
Date: 2008-11-26 00:16
Category: plone, python, zc.buildout, zope

I found a bit of time to work on distribution matters. Here's a status
of what I am doing there.   
  
There are two topics I am focusing on right now.   
-   clean up and enhance Python's distutils package
-   implement the mirroring infrastructure at PyPI

  
### distutils work

  
Nathan Van Gheem proposed a cool patch in [collective.dist][], (this
package is a port of the new features I have added in distutils so they
are available in 2.4 and 2.5).   
  
Nathan proposed a patch to be able to avoid the storage of the password
in the .pypirc file. The prompt is used in that case. This is something
that was in my pile for a long time.   
  
I have added a few things to Nathan's patch, and a test, and proposed
it to Python. I am now waiting for its integration in 2.7 trunk:
[http://bugs.python.org/issue4394][]. If it's accepted, I will backport
it to collective.dist.   
  
There are some other tickets I am waiting to be accepted:   
-   [http://bugs.python.org/issue4400][]
-   [http://bugs.python.org/issue2461][]
-   [http://bugs.python.org/issue3992][]
-   [http://bugs.python.org/issue3985][]
-   [http://bugs.python.org/issue3986][]

  
I am not sure when those will be integrated. The average time for the
integration of tickets in distutils in Python is between 6 months and 8
months. hihihi. :D   
### PyPI mirroring

  
The job I am doing in PyPI will be in three phase :   
-   **Phase 1**: implement the mirroring infrastructure in PyPI
-   **Phase 2**: promote it, and propose patches for the mirroring tools
    out there so they use the protocol
-   **Phase 3**: promote and propose patches for [pip][] so it can use
    the mirrors efficiently (fail-over and nearest mirror
    infrastructure).

  
**Phase 1: so far, so good. **   
  
With some insights from [Richard Jones][] and Martin von Löwis, I am
currently implementing the mirroring infrastructure for PyPI we have
defined during the D.C. sprint (I still owe a blog entry about this
sprint). The code lives [in a branch on the python svn folder][]
dedicated to PyPI.   
  
The idea of the mirroring infrastructure is to be able to get a list of
official mirrors for PyPI, that can be used as alternatives sources .
(It is described here: [http://wiki.python.org/moin/PEP\_374][]). A
great behavior could be that the client application interacts with the
nearest mirror location automatically, and switch to another if it goes
down.   
  
So, a list of mirrors will be made available at */mirrors*, and the
client applications will be able from there to use an alternative
location for every package. The hardest part concerns the stats : we
want to display in PyPI the download counts for each package by summing
downloads from every mirror.   
  
So every mirror will have to provide its "local stats" that can be
visited by PyPI. That's the biggest part of the work I am doing. It will
build the stats for PyPI by parsing its Apache log file. And hopefully,
this code should be reusable by the mirrors themselve so they can build
their stats the same way.   
  
*Of course this infrastructure could be used for any PyPI-compatible
server even if is not a mirror of PyPI (like a private PyPI server)*   
  
**Phase 2** will consist in promoting the infrastructure to the
mirroring softwares out there. Maybe Pycon will be a good place for
that.   
  
**Phase 3** is the most interesting one : make sure the client
applications use the mirrors ! I think Ian Bicking's pip project could
be the right place for these innovations.   
  
Next topics in the pile:   
-   **index-merging**: describe in a PEP-like document the index-merging
    feature that would allow clients to merge several indexes with a
    content that differe. For example: PyPI + a private PyPI server. I
    have written a first draft of such a patch in setuptools in the past
    ([http://bugs.python.org/setuptools/issue32][]) but I have lost all
    my hopes to see this project moving forward lately.
-   **Brainstorming**: try to understand the **Python Packaging
    Paradox**. That is = how come the community, which is composed of
    many briliant people, is unable to move forward in packaging
    matters.
-   ***Distribute the return*** :D

  [collective.dist]: http://pypi.python.org/pypi/collective.dist/0.2.0#what-is-collective-dist
  [http://bugs.python.org/issue4394]: http://bugs.python.org/issue4394
  [http://bugs.python.org/issue4400]: http://bugs.python.org/issue4400
  [http://bugs.python.org/issue2461]: http://bugs.python.org/issue2461
  [http://bugs.python.org/issue3992]: http://bugs.python.org/issue3992
  [http://bugs.python.org/issue3985]: http://bugs.python.org/issue3985
  [http://bugs.python.org/issue3986]: http://bugs.python.org/issue3986
  [pip]: http://pypi.python.org/pypi/pip
  [Richard Jones]: http://www.mechanicalcat.net/richard/log/Python
  [in a branch on the python svn folder]: https://svn.python.org/packages/branches/tarek-pypi/pypi/
  [http://wiki.python.org/moin/PEP\_374]: http://wiki.python.org/moin/PEP_374
  [http://bugs.python.org/setuptools/issue32]: http://bugs.python.org/setuptools/issue32
