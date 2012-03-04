Title: iw.eggproxy, a smart PyPI mirror
Date: 2008-08-12 09:04
Category: plone, python, zope

Mirroring PyPI becomes a recurrent need for Zope development, because
[zc.buildout][]makes a lot of package downloads to build one
application.   
  
This is useful when you are working in an intranet with limited web
access or when you want to speed up download times. It also makes things
safer: if PyPI is down and if developers computers don't have caches,
having a mirror will save your day.   
  
While PyPI has proven its robustness (it is 100% up for months now as
far as I can see), having mirrors makes a lot of sense.   
  
We have created a small mirror application here at Ingeniweb, that we
use for our buildouts needs. This work was thaught and created by my
colleague [Bertrand Mathieu][].   
  
It is a smart proxy that will download packages at PyPI everytime they
have been asked by a buildout or an easy\_install client. When the
package is downloaded, it is kept in the proxy side for any new
requests. This means that after a while, the proxy has its own
collection of packages that corresponds to the real needs and will not
query PyPI anymore.   
  
This approach avoids having to download and synchronize PyPI with
crons, which is a heavy process since PyPI weight several gigas. The
caveat of course, is that it won't be able to get a new package if PyPI
is down.   
  
Take a look ! [http://pypi.python.org/pypi/iw.eggproxy][]   
  
By the way there is an interesting sprint coming up on all these
topics, in Germany :   
  
[http://www.openplans.org/projects/black-forest-sprint/project-home][]

  [zc.buildout]: http://pypi.python.org/pypi/zc.buildout/
  [Bertrand Mathieu]: http://zebert.blogspot.com/
  [http://pypi.python.org/pypi/iw.eggproxy]: http://pypi.python.org/pypi/iw.eggproxy
  [http://www.openplans.org/projects/black-forest-sprint/project-home]: http://www.openplans.org/projects/black-forest-sprint/project-home
