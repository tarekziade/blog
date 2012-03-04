Title: Pycon hallway session #1: a keyring library for Python
Date: 2009-03-27 14:55
Category: pycon, python

Before I sit down and clean up my summit notes to send them to
python-dev, I wanted to post an entry about a small project which I
think could be a great task for a student at the Summer of Code (I doubt
it can fill 4 months of work but it could be done amongst other tasks).
  
  
Yesterday, we did a late session with Martin von Loewis, Jim Fulton and
Georg Brandl about PyPI and the fact that it needed a better way to
handle passwords on client side. That is, the fact that you have to
store your password in the .pypirc file if you want to upload your
package to PyPI.   
  
This is unsafe and unwanted. A few months ago, I have made a small
change in Distutils so it would prompt for the password using the
getpass module if it doesn't find it in the .pypirc file. (This was a
contrbution of Nathan Van Gheem).   
  
Anyways, this is not enough. Jim suggested to set up a SSH server on
PyPI using Paramiko, so we could use a standard ssh connection and
benefit from ssh-agent. But this is unfortunately not universal.   
  
So let me get back to the idea I sent some time ago :
[http://mail.python.org/pipermail/python-ideas/2009-January/002465.html][]
  
>   
>     What about having an option in getpass to store and reuse passwords in
>
>     system keyrings ?
>
>
>
>         getpass(prompt[, stream])
>
>
>
>     would become:
>
>
>
>         getpass(prompt[, stream, keyring])
>
>
>
>     where keyring would be a callable that can be use to retrieve the
>
>     password from a keyring system
>
>     and store it the first time.
>
>
>
>     The getpass module could provide some keyring support for:
>
>
>
>     - ssh-agent under Linux
>
>     - keychain under Mac OS X
>
>     - ...
>
>     ss
>
>
>
>     And let the developers use their own keyring system by providing a callable.
>
>   

  
As Greg Smith said in the thread, the first task is to create a library
that supports all standard keyring systems out there, including things
like KWallet, Internet Explorer, Fireforx and so on...   
  
I'll mentor this project if any student would like to do it.

  [http://mail.python.org/pipermail/python-ideas/2009-January/002465.html]:
    http://mail.python.org/pipermail/python-ideas/2009-January/002465.html
