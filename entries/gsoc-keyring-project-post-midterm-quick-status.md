Title: Gsoc Keyring project - post-midterm quick status
Date: 2009-08-05 21:24
Category: gsoc, python

[Kang][] (my Gsoc student) work is going very well on the Python
Universal Keyring Library. He's basically finished to implement back
ends for major keyring systems:   
-   Apple KeyChain
-   Gnome Keyring
-   KDE Wallet

  
And for Windows users, there's an extra back end based on
Win32CryptoKeyring, which stores a crypted version of the password in a
file. Last, there's another File-based crypted back end based on the
PyCrypto lib.   
  
The library is extensible and there's an abstract base class that
provides an interface you can use to write your own back end. Each back
end has to return a "recommandation" value depending on the execution
context (the platform, and anything the back end wants to check). 0
means the back end is not compatible, 1 means it will work, 2 means it's
recommended to use it. This allows us to pick the best back end
automatically depending on the execution context.   
  
Check the code here : [http://bitbucket.org/kang/python-keyring-lib/][]
  
  
Kang is tweaking the API names, modules names etc, and then will:   
-   add some documentation
-   write a patch for getpass.getpass
-   start a web page for the lib

  
For the latter we are brainstorming on the project name before we
release it.   
  
I've asked on Twitter, here are some proposals so far (thanks guys!):   
-   @nightlybuild: **Vercotti** ? ( the recurring Sicilian connected
    gangster, played by Michael Palin - [http://tiny.cc/luigi][]
-   @pmclanahan: I like "**Zoot**". From The Holy Grail, the name of the
    naughty sister in the perilous castle Anthrax.
-   @tpherndon: **Bridge Keeper** - "Answer me these questions three!"
-   @gurneyalex: you could consider **creosote** too
-   @jessenoller: Call it **bucket**. From meaning of life.
-   @regebro: "**Biggles**". Because he chains an old woman to a wall.
    [http://www.ibras.dk/montypython/episode15.htm][]
-   @gurneyalex: **BrightSide**

  
And you, what's your proposal ?   
  
Once the name is picked, we will start promoting the lib. I'll work on
distutils integration, and we will propose it to projects like Mercurial
(it makes sense to allow the removal of those clear-text passwords from
your hgrc when you are doing http auth).   
  
Have I said it already ? being a GSoc mentor is a great experience,
especially when you have the chance to pick students like Kang.

  [Kang]: http://kangzhang-en.blogspot.com/
  [http://bitbucket.org/kang/python-keyring-lib/]: http://bitbucket.org/kang/python-keyring-lib/
  [http://tiny.cc/luigi]: http://tiny.cc/luigi
  [http://www.ibras.dk/montypython/episode15.htm]: http://www.ibras.dk/montypython/episode15.htm
