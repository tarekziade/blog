Title: Firefox Sync : deploying Python apps on RPM-based systems
Date: 2010-11-04 18:43
Category: mozilla, python

The Python Firefox Sync server is going to be deployed at Mozilla in
production early next year, on RHEL-based servers. Working on packaging
matters in Python, I focused a lot on the best way to deploy our Python
applications and libraries, and make every involved party happy.   
### Our environment

  
Unlike a fully-featured website, our various web applications for
Firefox Sync don't have a lot of dependencies besides Python itself.
This means that we don't have a huge list of dependencies to deploy to
set up every part of the infrastructure. Another important point is that
unlike smaller projects where a single server/VM might manage several
applications whose dependencies can conflict, we have dedicated
environments for each application we are deploying. Hey, I am happily
running 5 small websites with 5 different environments on my own server,
thanks to zc.buildout, but for Sync it's the other way around: many
servers for the same app :)   
  
In other words, tools like zc.buildout or virtualenv -- which provide
application-level isolated environments -- are not really needed. We can
happily install the different bits in the same Python environment.   
### Repository-oriented vs Release-oriented

  
One approach I have seen is to deploy applications in a directory using
Git or Mercurial and just pull the code from a repository on a specific
tag or branch. Dependencies can be fetch the same way by using a vendor
repository, or simply installed locally using Pip or easy\_install.   
  
The biggest caveat of this approach is that there's no more static
archive that freezes everything into a single object that can be
manipulated by usual packaging systems the system provide -- The Python
packaging system or the OS packaging system --   
  
OS Packaging systems provide a lot of automation for sysadmins and more
features for pre- and post- installation steps for the packager. Instead
of using custom recipes to upgrade the application, they can use what
they are using for everything else on the system, and with much more
features like the ability to mark some files in the metadata as
configuration files and tell the installer about it to avoid overriding
existing files, etc.   
  
The Python packaging system is also simpler than a repository-based
system when you want to run the application in any Operating System. You
just install the application that was released, and don't bother with
source repositories.   
### Distutils-based and RPM-based

  
Sync is packaged in RPMs and in Distutils source archives. Every
distribution has a .spec file containing the RPM metadata and also a
setup.py file. Releasing the project into Distutils-based archive is
done so people in the community that wish to deploy the server in a
non-RPM based system can do it. In a near future, a simple "pip install
SyncServer" will do the trick for them. They'll have extra manual steps,
like hooking the app in the web server of their choice, but they won't
have to checkout many repositories and create a dedicated environment.   
  
For the RPM based distribution, I was a bit annoyed by the
**bdist\_rpm** command Python/Distutils provides. It's not good enough
to easily tweak the RPM creation process and you always end-up writing
your own *.spec* file. But build\_rpm do provide a nice automation: it
calls rpmbuild with good enough options, and for some distributions I
don't need to write a custom .spec file as long as I am able to define a
custom name for the RPM project. For instance, I prefix all my
distributions with ***python26-***.   
  
Since we've removed build\_rpm from Distutils2, I ended up writing an
enhanced version in a project called pypi2rpm, that provides two new
options: --name and --spec-file. I use them to build RPM on projects
that have custom .spec files, or when I want to force the name of the
RPM with a direct command-line option.   
  
The pypi2rpm project also provide a nice command-line script that uses
the power of Distutils2 to generate RPMs for the latest versions of any
project, as long as it is published at PyPI. That's useful to complete
my RPM collection when I cannot find a RPM for a project.   
  
So, if I want to create a RPM for the latest WebOb release, I do:   
  
$ pypi2rpm.py webob   
  
I've pushed pypi2rpm at PyPI if you want to play with it. It's a work
in progress and lacks of documentation, but is good enough for me for
what I need to do right now. If you are interested in this small project
let me know !
