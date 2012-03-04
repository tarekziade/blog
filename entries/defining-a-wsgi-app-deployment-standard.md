Title: Defining a wsgi app deployment standard
Date: 2012-02-10 00:14
Category: mozilla, python

Next month at Pycon, we'll have a web summit and I'm invited there to
talk about how I deploy web applications. This is not a new topic, as it
was already discussed a bit last year -- [see Ian Bicking's thought on
the topic][].   
  
My presentation at the summit will be in two parts. I want to 1/
explain how I organized our Python deployments at Mozilla (using RPMs)
2/ make an initial proposal for a deployment standard that would work
for the community at large - I intend to work on this during Pycon and
later on the dedicated SIG.   
  
Here's an overview of the deployment standard idea...   
### How we deploy usually

  
If I want to roughly summarize how people deploy their web applications
these days, from my knowledge I'd say that there are two main
categories.   
1.  Deployments that need to be done in the context of an existing
    packaging system -- like RPM or DPKG
2.  Deployments that are done in no particular context, where we want it
    to *just work*. -- like a directory containing a virtualenv and all
    the dependencies needed.

  
In both cases, preparing a deployment usually consists of fetching
Python packages at PyPI and maybe compile some of them. These steps are
usually done using tools like *zc.buildout* or *virtualenv + pip*, and
in the case of Mozilla Services, a custom tool that transforms all
dependencies into RPMs.   
  
In one case we end up with a directory filled with everything needed to
run the application, except the system dependencies, and in the other
case with a collection of RPMs that can be deployed on the target
system.   
  
But in both cases, we end up using the same thing: **a complete list of
Python dependencies**.   
  
The trick with using tools like zc.buildout or pip is that from an
initial list of dependencies, you end up pulling indirect dependencies.
For instance, the *Pyramid* package will pull the *Mako* package and so
on. A good practice is to have them listed in a single place and to pin
each package to a specific version before releasing the app. Both pip
and zc.buildout have tools to do this.   
  
Deployments practices I have seen so far:   
-   a collection of rpms/debian packages/etc are built using tools like
    bdist\_rpms etc.
-   a virtualenv-based directory is created in-place in production or as
    a pre-build binary release that's archived and copied in production
-   a zc-buildout-based directory is created in-place in production or
    as a pre-build binary release that's archived and copied in
    production

  
The part that's still fuzzy for everyone that is not using RPMs or
Debian packages is how to list system-level dependencies. We introduced
in PEP 345 the notion of *hint* where you can define system level
dependencies which name may not be the actual name on the target system.
So if you say you need ***libxml-dev***, which is valid under Debian,
people that deploy your system will know they'll need ***libxml-devel***
under Fedora. Yeah no magic here, it's a tough issue. [see
Requires-External][].   
### The Standard

  
***EDIT : Ian has a much more rich standard proposal [here][]. (see the
comments)***   
  
The standard I have in mind is a very lightweight standard that could
be useful in all our deployment practices - it's a thin layer on the top
of the WSGIstandard.   
  
A wsgi application is a directory containing:   
-   a text file located in the directory at ***dependencies.txt***,
    listing all dependencies - possibly reusing Pip's requirements
    format
-   a text file located in the directory at
    ***external******-dependencies.txt***, listing all system
    dependencies - possibly reusing PEP 345 format
-   a Python script located it the directory at ***bin/wsgiapp*** with
    an "application" variable. The shebang line of the Python script
    might also point to a local Python interpreter (a virtualenv
    version)

  
From there we have all kind of possible scenarios where the application
can be built and/or run with the usual set of tools   
  
Here's one example of a deployment from scratch :   
-   The repository of the project is cloned
-   A virtualenv is created in the repository clone
-   pip, which gets installed with virtualenv, is used to install all
    dependencies describes in*** dependencies.txt***
-   gunicorn is used to run the app locally using "cd bin; gunicorn
    wsgiapp:application"
-   the directory is zipped and sent in production
-   the directory is unzipped
-   virtualenv is run again in the directory
-   the app is hooked to Apache+mod\_wsgi

  
Another scenario I'd use in our RPM environment:   
-   The repository of the project is cloned
-   a RPM is built for each package in ***dependencies.txt***
-   if possible, ***external-dependencies.txt*** is used to feed a spec
    file.
-   the app is deployed using the RPM collection

  
That's the idea, roughly -- a light standard to point a wsgi app and a
list of dependencies.

  [see Ian Bicking's thought on the topic]: http://blog.ianbicking.org/2011/03/31/python-webapp-package/
  [see Requires-External]: http://www.python.org/dev/peps/pep-0345/#requires-external-multiple-use
  [here]: https://github.com/ianb/pywebapp/blob/master/docs/spec.txt
