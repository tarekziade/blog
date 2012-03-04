Title: A quick glimpse at Distutils2 1.0 alpha3
Date: 2010-10-02 15:44
Category: python

We're busy preparing the third alpha of Distutils2 1.0. I am pretty
excited about it because all of the hard work that was done during the
GSOC is starting to surface.   
  
The major feature in alpha3 will be the fact that** setup.py is gone**.
Everything is now driven from scripts you can run using -m.   
  
To describe your project you can now use **setup.cfg**, or better : use
the **mkpkg** wizard which will ask you a few questions and create it
for you.   
  
In the demo below, I am installing distutils2 in a virtualenv and I am
creating a setup.cfg for a project that contains the 'mycode' package.
Then I am creating a distribution, installing it and testing it.   
   # creating a temp dir with a virtualenv in it

    $ cd /tmp/demo/

    $ virtualenv --no-site-packages .

    New python executable in ./bin/python2.6

    ...



    # installing Distutils2 from the tip

    $ bin/easy_install http://bitbucket.org/tarek/distutils2/get/tip.gz

    Downloading http://bitbucket.org/tarek/distutils2/get/tip.gz

    Processing tip.gz

    ...



    # creating a Python package to include to the project

    $ mkdir mycode

    $ echo print \"I am alive\" > mycode/__init__.py



    # running the wizard that creates a setup.cfg for me

    # Thanks god it takes care of the Trove classifiers for me now !

    $ bin/python -m distutils2.mkpkg

    Project name [demo]:

    Current version number: 1.0

    Package description:

       > short demo

    Author name [Tarek]: Tarek

    Author e-mail address [tarek@ziade.org]:

    Project Home Page: http://bitbucket.org/tarek/distutils2/wiki/Home

    Do you want to add a package ? (y/n): y

    Package name: mycode

    Do you want to add a package ? (y/n): n

    Do you want to set Trove classifiers? (y/n): y

    Please select the project status:



    1 - Planning

    2 - Pre-Alpha

    3 - Alpha

    4 - Beta

    5 - Production/Stable

    6 - Mature

    7 - Inactive



    Status: 3

    What license do you use: GPL

    Matching licenses:



       1) License :: OSI Approved :: GNU General Public License (GPL)

       2) License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)



    Type the number of the license you wish to use or ? to try again:: 1

    Do you want to set other trove identifiers (y/n) [n]: n

    Wrote "setup.cfg".



    # checking the result

    $ more setup.cfg

    [metadata]

    name = demo

    version = 1.0

    author = Tarek

    author_email = tarek@ziade.org

    description = short demo

    home_page = http://bitbucket.org/tarek/distutils2/wiki/Home



    classifier = Development Status :: 3 - Alpha

        License :: OSI Approved :: GNU General Public License (GPL)



    [files]



    packages = mycode



    # trying to build a source distribution

    $ bin/python -m distutils2.run sdist

    running sdist



    # installing the distribution in the virtualenv'ed Python

    $ bin/python -m distutils2.run install

    running install

    ...



    # is my project properly installed ?

    $ bin/python

    Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41)

    [GCC 4.4.3] on linux2

    Type "help", "copyright", "credits" or "license" for more information.

    >>> import mycode

    I am alive

  
  
I'm hoping to have alpha3 released this week-end or early next week.   

