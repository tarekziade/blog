Title: Simple command-line vault : CLVault
Date: 2010-02-01 17:26
Category: python

I am pretty happy with the [Keyring][] project. I use it now everywhere
in my Mercurial-based projects, thanks to [mercurial\_keyring][].   
  
There's one other place I've started to use it: I needed a simple
command-line based tool to save passwords and read them. The tool I've
used so far was [KeePass][], but I need to run it then click on its UI.
This is time consuming when I simply want to push a password in the
clipboard to use it to unlock something.   
  
So I've wrote these two very simple scripts that use Keyring to store
and retrieve passwords   
   $ clvault-set blog

    Set your password:

    Password set.



    $ clvault-get blog

    The password has been copied in your clipboard

  
The code that copy the passwords in the clipboard was tested under Mac
OS with its Keychain, but should work under Windows and Linux as well.   
  
I think these scripts can be useful for people like me who spend most
of their time in a bash prompt when they are not in Vim or Emacs. So I
created a project called CLVault.. You can grab it at the PyPI: [CLVault
PyPI page][]   
  
or install it like this with Pip:   
   $ pip install clvault

  
Let me know if it's useful to you !

  [Keyring]: http://pypi.python.org/pypi/keyring
  [mercurial\_keyring]: http://pypi.python.org/pypi/mercurial_keyring
  [KeePass]: http://keepass.info/
  [CLVault PyPI page]: http://pypi.python.org/pypi/CLVault
