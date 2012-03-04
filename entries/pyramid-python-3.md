Title: Pyramid @ Python 3
Date: 2011-12-25 11:15
Category: python

If you have been following closely the latest work done by Chris on
WebOb, you know that WebOb and eventually Pyramid became Python 3
compatible.   
  
That makes Python 3 a very tempting target for a new web project.   
  
Paste & PasteScript still need to be ported to Python 3 and the Pyramid
team has chosen not to. They have created their own paster replacer
instead, which can be used to initiate a Pyramid project or run the app
using the *.ini* file.   
  
I am wondering if it would not be simpler at this point to drop Paste
and use this replacer for all Python 3 frameworks that are using the
Paste script and templates features.   
  
Besides all the features Pyramid and its libs turns out most of the
libs you usually need to build a classical web app already support
Python 3, like SQLALchemy and PyMysql for MySQL access, Pylibmc for
Memcached;   
  
Things I am still missing in Python 3:   
-   gevent
-   gunicorn
-   python-ldap
-   Cornice -- I will port it soon

  
If you want to give it a shot, get the latest Python 3.2 and grab more
details at :[https://github.com/Pylons/pyramid/wiki/Python-3-Porting][]
  
  
And if you miss one lib, [add it here][]   
  
Merry Christmas !

  [https://github.com/Pylons/pyramid/wiki/Python-3-Porting]: https://github.com/Pylons/pyramid/wiki/Python-3-Porting
  [add it here]: https://plus.google.com/u/1/106436370949746015255/posts/SAwkyVyUhWV
