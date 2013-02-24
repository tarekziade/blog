Flake8 2.0 released
###################

:date: 2013-02-24 22:50
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

**Flake8** is a extensible code checker. It unifies tools like **PyFlakes**
or **pep8** so you can check your Python code with a single command line call
- or directly in Git & Mercurial.

Get the new version at `PyPI <http://pypi.python.org/pypi/flake8/2.0>`_
or simply::

    $ pip install flake8

The project looks like it's getting quite popular - over **113,000** downloads,
according to `crate.io <https://crate.io/packages/flake8/>`_

There are many projects out there that also bundle FLake8 in VIM, like
`vim-flake8 <http://nvie.com/posts/vim-flake8-flake8-for-vim/>`_,
`flake8-vim <http://www.vim.org/scripts/script.php?script_id=4440>`_,
`Syntastic <http://www.vim.org/scripts/script.php?script_id=2736>`_ or
`Khuno <https://github.com/alfredodeza/khuno.vim>`_ -- wow, 4 projects.

Ian Cordasco took over the maintenance of `Flake8 <http://flake8.readthedocs.org/>`_
a few months ago and did an amazing work of cleaning the code.

The code still had a local copy of *PyFlakes*, I've hacked back when I started,
to make it compatible with Python 3. The plan was to have the upstream project
compatible with Python 3 and make Flake8 depend on it - and Ian worked hard
on fixing this dependency issue - among other stuff.

In parallel, Florent Xicluna also worked on the Python 3 porting in PyFlakes and
also started to help the maintenance of pep8.

The *very* good news is that we've all joined forces to synchronize our efforts,
and we've released together a 2.0 version of Flake8 that now uses all upstream
projects as dependencies and also provides a nice way to add new extensions.

Check out how to create new extensions at : http://flake8.readthedocs.org/en/latest/extensions.html

Good times, thanks Ian and Florent.

By the way : we'd like to add a logo to the project - Ian and other people
on Twitter suggested a snow flake with 8 branches. If you're an artist/designer
and want to contribute a logo - please contact me.

