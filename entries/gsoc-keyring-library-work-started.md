Title: Gsoc : Keyring library work started !
Date: 2009-05-03 10:49
Category: gsoc, python

I am very proud to be a [Gsoc][] mentor this year on a very interesting
topic : an universal keyring library for Python.   
### About the topic

  
In Distutils, if you want to interact with PyPI, you have to register
in the website and you get a login/password so you can register and/or
upload your packages.   
  
Before Python 2.6, the only way you could interact with PyPI was by
storing these info into your .pypirc file in **clear text**. This was
not the best solution. For example we have in my company some staging
servers we share, and from whom we upload packages to various PyPI-like
servers. So we have to store PyPI login/password info in them. This
means that if Bob wants to push his package from that server, he has to
put his password into a clear text file which is most of the time
readable by everyone. It's not such a big deal in our company since we
can trust each other, but it's a very bad practice.   
  
So I ended up changing this in Python 2.6 so people could type their
password in a prompt when working with packages, using
**getpass.getpass**. So they wouldn't have to store them anymore.   
  
But this is not enough : we need to provide something better. We need
**getpass.getpass** to be able to interact with keyring libraries like
[KeyChain][], [Gnome Keyring][], etc. So the login/password info are
safely stored and can be reused.   
  
This service will be useful for Distutils, but also for any Python
application.   
  
The idea of the GSOC task is to provide an unified keyring library for
Python, and it's harder that it sounds. For instance, we need to find a
way to provide something that works under Windows. So the whole work is
quite challenging and interesting, and the goal is to end up with a
keyring library we can use into Distutils and propose for inclusion in
getpass.   
### About Kang

  
Kang Zhang is the student that was selected for this work. Congrats !
He has started to work on it. You can follow his work in his [blog][]. I
have a strong feeling that he will succeed in this work and come up with
something good.   
  
Take a look at the [Python Soc planet][] too, where all students
involved in Python GSOC are blogging about their ongoing work.

  [Gsoc]: http://socghop.appspot.com/org/home/google/gsoc2009/python
  [KeyChain]: http://en.wikipedia.org/wiki/Keychain_(Mac_OS)
  [Gnome Keyring]: http://en.wikipedia.org/wiki/GNOME_Keyring
  [blog]: http://kangzhang-en.blogspot.com/
  [Python Soc planet]: http://soc.python.org/
