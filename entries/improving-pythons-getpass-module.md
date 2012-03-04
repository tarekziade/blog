Title: improving Python&#039;s getpass module
Date: 2010-02-06 23:51
Category: python

**UPDATED see the end.**   
  
The Python standard library has a module called [getpass][] you can use
to get a password from the prompt:   
   >>> import getpass

    >>> password = getpass.getpass()

    Password:          <-- non-echoed typing here

    >>> print password

    worked

  
That's nice, and Distutils uses it to ask for your password when you
register or upload a release at PyPI, if it's not found in your
[pypirc][] file. But this is annoying to type and type again your
password, so you end up saving it in **clear text** in pypirc. Thats
sucks. And the getpass module gets pretty useless if you want to store
and retrieve passwords from other places than the user brain.   
  
But wait... we have the [Keyring][] project now.. what about making
getpass use Keyring so you can safely read a password from your favorite
keyring (Keychain, KWallet, etc..) ?   
  
I've started to write a new getpass module that could do this. But
instead of adding a keyring dependency in it and struggling for months
(years) to get the addition of Keyring into the stdlib, I have made
getpass pluggable.   
  
In my improved version, you can define in a small configuration file
(getpass.cfg) an arbritrary function that will be used by getpass for
the *getpass.getpass* API. Here's such a file:   
     [getpass]

      getpass-backend = keyring:get_pass_get_password

  
Here I am configuring get pass to use the *get\_pass\_get\_password*
function from the *keyring* package. That's a function that gets
installed in your Python once Keyring is installed.   
  
This function has the same interface than the default *getpass.getpass*
API and calls keyring.   
  
The modified getpass module is here:
[http://bitbucket.org/tarek/getpass/][]   
  
And works against the current trunk of Keyring.   
  
What I would like to do now is to propose the small changes I've made
in Python's getpass for inclusion in the stdlib. They are backward
compatible changes and offers a simple, yet powerfull way to extend
getpass without adding any other module in the stdlib. And maybe adding
a setpass in there too would make sense.   
### Update from python-ideas

  
So I brought up the idea in the mailing lists and it turns out (thanks
to the folks at Python-ideas) that the way I want to introduce this
feature is not good for these reasons :   
1.  *getpass* is just a function that is used to get a password from the
    prompt. you can consider it as a potential, dummy backend for
    Keyring for example. Trying to make it extendable just denaturates
    its original purpose.
2.  the only use case right now in the stdlib is for Distutils, so it
    doesn't really make sense to have a keyring in there. People can
    just use the Keyring project directly.
3.  Now if other parts of the stdlib have the same need, it will be time
    to think about how it could be included in the stdlib level rather
    than in Distutils.

  
So, I'll work for its inclusion at Distutils level rather thah on
getpass level.

  [getpass]: http://docs.python.org/library/getpass.html
  [pypirc]: http://tarekziade.wordpress.com/2009/01/09/distutils-improved-pypirc-for-python-27-and-31/
  [Keyring]: http://pypi.python.org/pypi/keyring
  [http://bitbucket.org/tarek/getpass/]: http://bitbucket.org/tarek/getpass/
