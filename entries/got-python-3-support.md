Title: Got Python 3 support ?
Date: 2009-09-26 20:06
Category: distribute, distutils, python

One thing that slows down the adoption of Python 3 is the low number of
available third party projects. If your project depends on some other
projects, you are pretty lucky if they are all available under Python 3.
  
  
I don't think that the problem comes from the Python 3 syntax adoption,
because Python provides a pretty powerful tool to convert your Python 2
code into Python 3 code, called [2to3][]. (notice that the backward
process is also available since this summer : [3to2][]).   
  
The biggest issue in my opinion is the lack of packaging support.
Distutils itself works fine on Python 3, but I am talking about
Setuptools, which is widely used in the community and doesn't work under
Python 3. So if your project, or one of its dependency uses Setuptools,
you can't switch to Python 3.   
  
Well, I am glad to say that this is not true anymore, thanks to Martin
von Löwis, [Lennart Regebro][] and Alex Grönholm that have been working
on Distribute's Python 3 support lately.   
  
The [Distribute][] project is a fork of the Setuptools project and is
now fully compatible with Python 3.   
  
If you are using Setuptools, install Distribute 0.6.3, read its
docs/python3.txt file and add Python 3 support to your project.   
  
And if you need help in porting your distribution to Python 3, drop in
[Distutils-SIG][], we will help you.

  [2to3]: http://docs.python.org/library/2to3.html
  [3to2]: http://pypi.python.org/pypi/3to2
  [Lennart Regebro]: http://regebro.wordpress.com/2009/09/25/setuptools-on-python-3-status-pretty-damn-good/
  [Distribute]: http://pypi.python.org/pypi/distribute
  [Distutils-SIG]: http://mail.python.org/mailman/listinfo/distutils-sig/
