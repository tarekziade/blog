Title: PloneSoftwareCenter Christmas mini-sprint
Date: 2007-12-26 04:06
Category: packaging, plone, python, zope

I made a mini-sprint on PSC for Christmas, since everyone around me was
sitting watching christmas movies on TV and trying to digest.   
  
Here's a wrapup for comment, and for upcoming work.   
### Current branch (pypi)

  
I've merged Sidnei's work into a new branch, with the current trunk
since his work was done 2 years ago. I have made a few changes from his
initial implementation:   
-   the PyPI API is now coded in a browser view instead of a persistent
    object, since it has no properties to keep at all;
-   when a release is uploaded, a new release object is created for the
    given version if it doesn't exists instead of raising an error and
    asking the user to manually create it inside the PSC;
-   the doctest was simplified and uses sample tarballs and eggs.

  
I need to finish up a few things and to add some features such as:   
-   **automatic project creation**. When a package is uploaded and no
    project corresponds to it, a new project is created using the egg
    name and provided metadata. This will make the PSC acts like the
    CheeseShop. (an option will be added in PSC to activate/deactivate
    this feature to prevent automatic creation of projects if not
    wanted).
-   **trove web service** the TROVE.txt file created by Sidnei needs to
    be replaced by a call to the categories; (see next section)
-   **multiple uploads**. Make sure everything works fine when several
    files are uploaded for one release;
-   **more tests** I need to write more tests from various clients and
    platform to make sure it works good. (by recording
    setuptools/distutils calls and creating tests with this).

  
This work should be done this week if everyone is OK with what I have
proposed.   
### About the Trove classification

  
The Cheeseshop provides a Trove classification (see
[http://www.python.org/dev/peps/pep-0301][]) which evolves. For instance
the "Django framework" category was added last week IIRC.   
  
Obviously, Plone eggs should follow this classification but when they
are uploaded in a PloneSoftwareCenter they might find specific
categories defined locally (these categories might be specific to the
project). I think we should let people freely define their classifiers
in setup.py and let each server take the ones they have in their list.   
  
The problem with Cheeseshop implementation is that it fails silently
when a item in the 'classifiers' list doesn't exists on the server side.
The package metadata seem to be lost after that. (this looks like a bug
to me, I didn't digg the PyPI code yet). I need to ask over
distutils-sig about this and see if we can come up with a Cheeseshop
that will pick the categories it knows out of the classifier list, and
let the other alone. This would allow PSC to deal with extra categories.
  
  
Then the PSC will have to implement the trove web services and serve
its categories, so the "list-classifiers" option of the register command
works.   
  
Until then I guess we can leave the classification settings manual.   
### About the .pypirc file

  
This file that is used with the register command is working just for
one server and will not allow having several set of login/password. This
is not a problem when the login of your plone with your PSC is the same
than the one in PyPI. Otherwise it won't work.   
  
Furthermore, this command is using a hardcoded 'pypi' realm if you look
at distutils/commands/register.py:   
   auth.add_password('pypi', host, username, password)

  
The real solution here is to make distutils evolve so the *.pypirc*
file allows having several login/password for each server, using the
host url and the realm (the realm can be queried automatically too).
Until then we have to make the PyPI api return a 'pypi' realm on 401
error (and this was done by Sidnei's work).   
  
To avoid maintaining several *.pypirc* files and forcing the realm on
401 errors though, we should create a new register command, that can
work with a enhanced version of the file and allow adding passwords for
several hosts. IMHO, the disutils package code is PyPI-centric but was
primarly intented to work over any release server, so it has to evolve
on that point.   
### About sdist and bdist\_egg

  
We have discussed in my latest entry about having a new command to
upload the package in the PSC:   
    $ python setup.py plone_upload

  
The idea is to be able to upload the release to plone.org and to the
Cheeseshop in one step. People reacted over this because in my example I
used *bdist\_egg* instead of *dist* for the packaging. I think it's a
false debate because it's up to the developer to decide how he releases
his work, using a tarball that is compiled by the target system, and/or
an egg.   
  
So we can just define an enhanced *upload* command that replaces the
original one, to automate the upload on several servers, and let the
developer manually call *sdist* and/or *bdist\_egg*.   
  
Servers could be picked up by the user at the prompt.   
### Schedule & tasks

  
This are my plans in PSF this week and next week:   
-   finish my current work on the branch, so the basic implementation
    works;
-   provide an enhanced version of the register and upload command, for
    multiple servers uploads. This will be done in a new package, since
    it's more like a distutils enhancement;
-   implement the trove webservice using PSC categories.

  [http://www.python.org/dev/peps/pep-0301]: http://www.python.org/dev/peps/pep-0301
