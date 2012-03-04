Title: Preparing to release Distribute 0.6
Date: 2009-07-22 17:30
Category: distutils

According to the [poll][], The name of the fork will be **Distribute** !
  
  
The code should not be changed anymore at this point, and I am working
on the bootstraping so installing Distribute will work with an existing
Setuptools installation and will replace it for the applications that
requires it.   
  
This is done by detecting an installation of Setuptools, and replacing
it with a *fake* installation. This means that once you've installed
Distribute, applications and especially installers will think that
*setuptools 0.6c9* is installed.   
  
That's pretty strong and intrusive, but required for a simple switch :
even if the programs you are using have a setuptools dependency, they
will work without requiring any change on the code or in their setup.py
files. Same goes for zc.buildout apps.   
  
I still have a lot of work for this part :   
-   I don't detect and patch properly single-version-externally-managed
    setuptools installation yet (required for pip)
-   I need to fix a bug on a first run under jython
-   I need to fix a bug when virtualenv is not used with
    --no-site-packages
-   I need to do extensive tests on zc.buildout to see if it behaves
    correctly

  
If you want to help:   
1.  download [http://nightly.ziade.org/install\_test.py][]
2.  run it with the Python interpreter of your choice (possibly a
    virtualenv-ed one)

  
To uninstall, follow the Uninstallation instructions here :
[http://bitbucket.org/tarek/distribute/src/tip/README.txt][]   
***   
\*Disclaimer: it might break your installation\****   
  
If the test end up with this line: \*\*\*\* Test is OK. It worked.
Otherwise, please let me know !   
  
The next "big" step will happen with Distribute 0.7 because the plan is
to split the code in several distributions with renamed modules:   
-   **Distribute** : the core (setuptools package but renamed)
-   **DistributeInstall** : easy\_install on its own, and renamed.
-   **DistributeResource** : will contain the pkg\_resources.py module,
    renamed

  
I'll post more details on it in the upcoming days.

  [poll]: http://doodle.com/4eyxzrwgwq4a6t9s
  [http://nightly.ziade.org/install\_test.py]: http://nightly.ziade.org/install_test.py
  [http://bitbucket.org/tarek/distribute/src/tip/README.txt]: http://bitbucket.org/tarek/distribute/src/tip/README.txt
