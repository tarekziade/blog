Title: Distribute, a setuptools fork. 
Date: 2008-09-24 13:10
Category: plone, python, zope

[**EDIT: Read this new entry**][]   
  
That's enough !   
  
Setuptools is now a big part of our Python development and release
infrastructure.   
  
But we have been struggling with the setuptools development process for
months around here. The project is run by one single man, who is really
busy on other things as well. I am not blaming him, he's doing a great
job. I am just saying that setuptools needs to be more open.   
  
Yesterday, I had, like the week before, some developers complaining
about some incompatibility between setuptools and Subversion 1.5.   
  
It is not like it is a hard to fix, and as a matter of fact it is fixed
now in the trunk of the project. But not released since quite a long
time now. So I have to ask my developers to checkout the trunk on their
buildout, and use the ==dev tag elsewhere. I proposed some help to do
the release, but my mails were just ignored.   
  
There are also a lot of improvments to do in this tool, so Python gets
the distribution tool it deserves.   
  
But having one single person with the commiter rights is not possible
on such an important package for the community. It has to be
community-driven.   
  
Enough talking, I am launching a setuptools fork, which will be
community-driven, and wich will remain 100% compatible with setuptools
at this point.   
  
You can react, of follow the reaction on the distutils-SIG I started
here :
[http://mail.python.org/pipermail/distutils-sig/2008-September/010031.html][]
  
  
Maybe my attempt to make such a tool belong to the Python community
will fail, I don't know. Maybe people will not like seeing someone
forking like that and will continue to sleep and to unsubsribe
themselves from the distutils-SIG.   
  
But at least I am trying something because Python is suffering from a
lack of a good, robust distribution tool at this point and there are a
lot of people that could contribute if the development process is more
open and the maintainer(s) more available and reactive.   
  
I have contributed a bit in distutils in the past year, but the Python
core development team has a lack of interest in this part of Python at
this time. Thanks to some of the core team members, I could have some
patch applied in the trunk, like the multiple servers pypirc. But we
won't be able to create what I would call 'distutils 2' in Python itself
at this point. And setuptools seems to be the best candidate for a
distutils replacement in the future.   
  
As long as the community can work on it of course ! We are the
community, we are distributing large application to our customers.   
  
So that's what "Distribute" is about.

  [**EDIT: Read this new entry**]: http://tarekziade.wordpress.com/2008/09/26/distribute-end-of-the-fork/
  [http://mail.python.org/pipermail/distutils-sig/2008-September/010031.html]:
    http://mail.python.org/pipermail/distutils-sig/2008-September/010031.html
