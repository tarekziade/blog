Title: The new .pypirc format in Python / distutils
Date: 2008-05-12 12:45
Category: plone, python, sprint, zope

Thanks to the sprinters in Washington D.C., (Andrew who worked on
merging it, Alex, etc.) and people that helped in the discussion (Fred,
Martin), my patch to Python for multiple servers handling in .pypirc
file has been integrated in 2.6 trunk.   
  
This patch will allow using distutils *register* and upload *commands*
with several servers, using the -r option and storing for each one of
them the appropriate username/password in the configuration file. See
[http://wiki.python.org/moin/EnhancedPyPI][] for more details.   
  
The [collective.dist][] package provides the same feature for Python
2.4 and 2.5, through new commands: *mregister* and *mupload*.   
  
The new format is also pretty convenient to store several profiles per
servers. For instance, if you have several accounts on PyPI, one for
your company (acme) and one for your own usage, you can define them like
this:   
   [distutils]

    index-servers =

        pypi

        acme



    [pypi]

    username:user

    password:password



    [acme]

    username:acme_user

    password:password

  
Then use them depending on the package you work in:   
   $ python setup.py register -r acme

    $ python setup.py register    # default, which is pypi

  
When plone.org will go Plone 3 (this is happening soon), the pypirc
file can be extended with this new target:   
   [distutils]

    index-servers =

        pypi

        acme

        plone



    [pypi]

    username:user

    password:password

    [acme]

    username:acme_user

    password:password

    [plone]

    repository:http://plone.org/products

    username:plone_user

    password:password

  
From there, setuptools aliases can be used in each package to simplify
things:   
   $ python setup.py alias plone_org register -r plone sdist bdist_egg upload -r plone

  
Which will allow you to upload the package to the website in one simple
command:   
   $ python setup.py plone_org

  
The patch aslo corrects a few minor bugs in distutils, such as:   
-   .pypirc was not found on Windows
-   pydistutils.cfg was not found on Windows

  [http://wiki.python.org/moin/EnhancedPyPI]: http://wiki.python.org/moin/EnhancedPyPI
  [collective.dist]: http://pypi.python.org/pypi/collective.dist/
