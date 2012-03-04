Title: 2009 plans, part #1 : Distutils 
Date: 2009-01-04 19:52
Category: pycon, python

Happy New year all !   
  
I am going to make a few posts on the things I would like to achieve in
2009. Each entry will focus on a topic. This one is about Distutils.   
  
I was granted a commit privilege in Python, specifically to work on
Distutils maintenance. This is a huge privilege, and I try will do my
best in this job. I have worked on a few tickets already and closed
some. I learnt the Python development process, which requires to
backport and to forward-port changesets in various Python versions.
While this can be taken care of automatically by someone else if you
don't do it, it's better that every commiter takes the time to merge his
own work.   
  
So what's next ?   
-   There are [132 tickets][] that are open in the Python tracker, that
    match the word distutils, and some of them are 5 years old !
-   There's a [Python language summit][] to be held in Chicago right
    before Pycon, and I volunteered to champion the task about
    Distutils, PyPI and packaging matters.

  
I am planning to :   
-   review and classify all the tickets in the tracker;
-   fix the maximum amount of them before the summit;
-   make Distutils a first class citizen in test coverage;
-   make Distutils code more modern.

  
Besides, I will try to build a roadmap for Distutils I will present in
Chicago.   
  
To build this roadmap, I will ask for input in the [distutils-SIG
mailing list][] in the coming days, and see what people will come up
with. There's no crowd in this list these days but sometimes some
threads are hot when it comes to the future of packaging in Python.   
  
The roadmap I am planning to build will not address all the issues
people have when it comes to distribute a Python application, since
there is no consensus yet on the best practices. It will rather try to
see if the current version of Distutils can be enhanced to adress some
problems, and at least be the bridge to something new in the future.
Maybe by including some best practices from third-party tools (the
pre-condition for all of this imho is to make the Distutils code base
healthier).   
  
Anyway, I hope that the lead developers of: [zc.buildout][], [pip][],
[setuptools][], [paver][] (and those projects I forget about right now)
will participate in this discussion, and that we will be able to find
pragmatic enhancements.

  [132 tickets]: http://bugs.python.org/issue?@sort0=activity&@sort1=&@group0=&@group1=&@columns=id,activity,title,creator,assignee,status&@filter=status&status=-1,1,3&@search_text=distutils&@pagesize=50&@startwith=0
  [Python language summit]: http://mail.python.org/pipermail/python-dev/2008-December/083819.html
  [distutils-SIG mailing list]: http://mail.python.org/mailman/listinfo/distutils-sig/
  [zc.buildout]: http://pypi.python.org/pypi/zc.buildout
  [pip]: http://pypi.python.org/pypi/pip
  [setuptools]: http://pypi.python.org/pypi/setuptools/
  [paver]: http://pypi.python.org/pypi/Paver
