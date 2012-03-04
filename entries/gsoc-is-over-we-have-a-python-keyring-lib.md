Title: Gsoc is over, we have a Python Keyring lib 
Date: 2009-08-25 12:04
Category: gsoc, python

The Google Summer of Code is over and the[first version of the keyring
library was released][] last week by Kang at PyPI.   
## How Keyring works, the big picture

  
This library implements a simple plugin system. Each plugin has to
implement a set of methods described in an abstract class and can wrap
any underlying Keyring system. We called those plugins "***backends***".
The nice thing about it is that you can implement your own custom
backend and make it available through the Keyring configuration file.   
  
Kang has coded various Keyring backends in C and C++ extensions, for
KWallet, Keychain, and Gnome. We also have added a Keyring
implementation that uses the Win32Crypto API so windows users can use
the lib.   
  
When the Keyring lib is used, all declared plugins, whether they are
provided by the lib itself or by a third party package, will be loaded.
Then they will be asked a simple question:   
> "Can you run in this environment ?"

  
The backend can answer one of these:   
-   "Yes, I could work in this environment"
-   "No, I can't"
-   "Yes and you should use me !"

  
The library filters out backends that can't work on the target, sort
the remaining ones, and get one of the best backend. This doesn't
happens of course if you explicitely define which backend you want to
use, which is possible.   
## What's next

  
Keyring 0.1 is out and there will probably be 1 or 2 releases to
stabilize the code.   
  
The next steps will be :   
-   to use it in Distutils, with a soft dependency : Distutils will let
    you use it through configuration if it detects Keyring is installed.
-   to promote its usage and in particular see if projects like
    Mercurial could use it
-   to work on a PEP for its integration in Python stdlib, in the
    getpass module

  [first version of the keyring library was released]: http://pypi.python.org/pypi/keyring
