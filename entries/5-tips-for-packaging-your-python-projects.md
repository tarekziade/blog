Title: 5 tips for packaging your Python projects
Date: 2011-08-19 16:05
Category: mozilla, python

Next week I am keynoting at [Pycon Japan][], and one thing I will talk
about is packaging of course. And in particular: what advice can I give
my audience on how to package Python projects ***today*** ?   
  
This is a hard task, because we are in some kind of transitional state.
  
  
Anyways, I wrote down a list of advices and removed everything that was
dependent on the tools we did not release yet -- that's another part in
my keynote.   
  
Here's a list. Most of them are not controversial. If you see something
missing or want to rant about one, please comment.   
### Tip \# 1 -- Use a [PEP 386][] compatible scheme for your versions

  
Having several version scheme in our eco-system is pure madness. It
breaks interoperability, and makes it impossible to write tools that
handle versions properly. By using a [PEP 386][]-friendly scheme now,
you are making your project future-proof !   
  
PyPI already rejects any [Metadata 1.2][] project that does not comply
to this policy. You probably don't know this because no tools produces
Metadata 1.2 packages yet. But that's going to be the default in Python
3.3 and distutils2.   
  
So long "devdevdev123" and "3765-2011-test" versions !   
### Tip \#2 -- try to make setup.py as dumb and simple as possible

  
***setup.py*** is not your personal build system. I have seen crazy
things in some projects. Remember that setup.py is used by installers
for a lot of different tasks. Like getting the metadata fields of the
project.   
  
Here's a simple test: make sure ***"python setup.py --name"*** (double
dash) eturns the name field without any external dependency, and without
calling any function or method.   
  
Remember that *setup.py* is going away in Python 3.3 and distutils2,
replaced by simple options in ***setup.cfg***. Don't be scared, you will
still able to do complex tasks.   
  
My advice: don't do anything else that feeding ***setup()*** with
options in there. Put all your build things in another place, and if
they need to be called by setup.py, make sure they are called only when
needed.   
### Tip \#3 -- Do not make any assumption about which installer will be
used

  
Make sure your ***setup.py*** can be run by a vanilla Python
(==distutils). Even if you use setuptools or distribute, in most case
you can manage to have it working in both tools. You can always tell the
user to do extra steps manually if he needs to.   
  
Forcing the installation of an installer, by using the ***ez\_setup***
script for instance, without asking, is a bit rude to the end-user. It's
basically forcing the end user to use a new installer. If you do this in
your setup.py, ask first !   
  
Or simply tell the user "This project only works with the XXX installer
-- install it if you want. Aborting."   
### Tip \#4 -- Do not release unstable releases at pypi

  
Our installers are not --*yet*-- smart enough to prefer stable releases
when they are asked to get a project at PyPI. That's how PyPI is built:
every project has a directory with all releases and it's up to the
installer to decide which one is the "latest". The only tool out there
that's smart about it is zc.buildout.   
  
So when you push an alpha release or a rc release at PyPI, it's going
to land in people environments unless they have mature processes to
update their stuff -- or simply because they make the assumption that
PyPI is where stable release go. So do not make assumptions about how
your users are updating your project.   
  
Prefer another explicit channel for your beta testers. All installers
know how to install from any url or directory.   
### Tip \#5 -- Be cautious about your data files

  
Distutils or Distribute or Python itself have no way to explicitly make
a difference between a doc file or a media file or a configuration file.
They are all ***data files***. Worse, since they are no universal place
for data files on the various OSes, people tend to treat their data
files like Python modules so they are able to find them back on the
target system without trouble.   
  
Yeah that's broken, and we've fixed it in 3.3. But until then, that's
unfortunately the most protable way to do this. So what you can do is
document clearly how you handle your data files and create a single
function or module that reads them. That'll help the downstream
maintainers to handle your project.

  [Pycon Japan]: http://2011.pycon.jp/english-information
  [PEP 386]: http://www.python.org/dev/peps/pep-0386/
  [Metadata 1.2]: http://www.python.org/dev/peps/pep-0345/
