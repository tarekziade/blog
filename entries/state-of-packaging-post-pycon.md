Title: State of packaging (post-Pycon)
Date: 2011-03-21 12:11
Category: python

### Language Summit

  
The language summit this year was less focused on packaging since the
work is ongoing in this front. But we still made a few important
decisions:   
-   Distutils2 will be named "**packaging**" in the standard library and
    released with Python 3.3
-   A backport for 2.4 to 3.2 will be provided and be called Distutils2

  
The reason for this is to avoid any name clash in the future when
people will have to deal with the two versions.   
### Conferences

  
I gave a talk about Distutils2 and people seemed to like it. At the end
I had to hide behind the desk because people asked questions I did not
want to answer ;)   
  
[The video is here][].   
### Questions

  
I have run [a Google Moderator][] before Pycon so people could ask
questions. Here are the answers.   
  
Q: In your long term view, should distutils2 completely replace pip?   
A: No. But Pip will probably move to a thiner layer on the top of
packaging, to provide its specifics (requirements freeze etc)   
  
Q: What's the future of "entry points" ?   
A: packaging will allow adding extra custom metadata. So the plan is to
create a third-party project that provides a similar feature than entry
points.   
  
Q: Can distutils grow better support for compiling shared modules that
are accessed via ctypes? This doesn't work on Windows because the wrong
symbols are exported   
A: Distutils is the poor's man tool for compiling shared modules. The
plan is to make it easier too hook third-party tools to do this. We will
still provide a minimal support, but nothing much fancier than what we
already have. Although, your ctype problem sounds like a bug to me, we
could fix.   
  
Q: In PEP 345, why is license optional? I understand there are many
packages today that don't declare their license (which sucks!), but has
there been any talk of changing that?   
A: It's not really planned since people can simply add a licence text
in their releases if they want. If it was mandatory what would be the
default license ?   
  
Q: How can we get dependency resolution in an \*offline mode\* without
running a local index (aka web server) and/or find links (aka clunky
solution)?   
A: By building a local cache of the metadata information   
  
Q: Will distutils2 manage the dependecies with packages or will left
that to pip?   
A: Distutils2 will manage them   
  
Q: How about a standard binary distribution format, with metadata like
dependencies, like eggs but without the bad bits?"   
A: What about the existing one ? (bdist)   
  
Q: Is there a mechanism to provide more information about C-extensions,
specifically, which are needed and which are cPython specific
accelerators.   
A: You can specify flags or environment variables, but nothing has
changed here compared to the previous version   
  
Q: Considering Python's "batteries included" philosophy, why should
distutils2 not include pip and virtualenv in its scope?   
A: Virtualenv is being added under the pythonv name --work in
progress--. Pip2 will stay a third party project and just provides what
Distutils2 does not in the future: developer tools that should not be
placed in the stdlib.   
  
Q: There are only one question - when? Python 3.3, I hope?"   
A: Yes 3.3. The merge is imminent.   
### Sprints

  
We worked on porting Distutils2 into the stdlib, and it's almost ready
here: [https://bitbucket.org/tarek/cpython/][] The merge is imminent !   
  
Other interesting features we're adding:   
-   People will be able to add extra metadata in their projects. They
    will be published at PyPI and also installed and queriable.
-   **setup.cfg **will have its own specification and will be versioned.
    It will be published at PyPI as well so people can get all kind of
    information about project without downloading the tarball ! Also,
    other tools like Bento will be able to read the cfg file and use it
    to provide their build features.
-   lots of other stuff I have to remember -- I will add them here
    later.

  [The video is here]: http://pycon.blip.tv/file/4880990/
  [a Google Moderator]: http://www.google.com/moderator/#15/e=6439e&t=6439e.40
  [https://bitbucket.org/tarek/cpython/]: https://bitbucket.org/tarek/cpython/
