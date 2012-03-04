Title: Packaging Survey first results
Date: 2009-03-26 03:35
Category: distutils, packaging, pycon, python

Around 570 people answered the survey, which is a great number I didn't
expect. Thanks again to Massimo for his help on this.   
  
I have a lot of work to read all the open question answers, and all the
comments that goes with the "other" answer, but I wanted to publish the
results of the closed questions before the summit.   
  
I don't want to comment the results yet. I will after I have studied
all answers, so it'll be a little while ;)   
## Who are you ?

  
  
  
  
Professional developer using Python exclusively.
  
  
  
  
  
  
  
  
  
283
  
  
  
Professional developer using Python unable to use Python "at work".
  
  
  
  
  
  
  
  
  
34
  
  
  
Professional developer using Python sometimes.
  
  
  
  
  
  
  
  
  
196
  
  
  
Hobbyist using Python.
  
  
  
  
  
  
  
  
  
116
  
  
  

* * * * *

  
## Where are you located ?

  
  
  
  
USA
  
  
  
  
  
  
  
  
  
212
  
  
  
Western Europe
  
  
  
  
  
  
  
  
  
268
  
  
  
Eastern Europe
  
  
  
  
  
  
  
  
  
42
  
  
  
Asia
  
  
  
  
  
  
  
  
  
18
  
  
  
Africa
  
  
  
  
  
  
  
  
  
9
  
  
  
Other
  
  
  
  
  
  
  
  
  
70
  
  
  

* * * * *

  
## If you are a web programmer, what is the framework you use the most ?

  
  
  
  
Pylons
  
  
  
  
  
  
  
  
  
55
  
  
  
TG 2
  
  
  
  
  
  
  
  
  
14
  
  
  
TG 1
  
  
  
  
  
  
  
  
  
15
  
  
  
Django
  
  
  
  
  
  
  
  
  
184
  
  
  
Zope (including Plone)
  
  
  
  
  
  
  
  
  
137
  
  
  
Other
  
  
  
  
  
  
  
  
  
207
  
  
  

* * * * *

  
## How do you organize your application code most of the time ?

  
  
  
  
I put everything in one package
  
  
  
  
  
  
  
  
  
171
  
  
  
I create several packages and use a tool like zc.buildout or Paver to
distribute the whole application
  
  
  
  
  
  
  
  
  
137
  
  
  
I create several packages and use a main package or script to launch the
application
  
  
  
  
  
  
  
  
  
198
  
  
  
I use my own mechanism for aggregating packages into a single install.
  
  
  
  
  
  
  
  
  
67
  
  
  

* * * * *

  
## For libraries you don't distribute publicly, do you you create a
setup.py script ?

  
  
  
  
Yes
  
  
  
  
  
  
  
  
  
321
  
  
  
No
  
  
  
  
  
  
  
  
  
249
  
  
  

* * * * *

  
## What is the main tool or combination of tools you are using to
package and distribute your Python application ?

  
  
  
  
None
  
  
  
  
  
  
  
  
  
80
  
  
  
setuptools
  
  
  
  
  
  
  
  
  
150
  
  
  
distutils
  
  
  
  
  
  
  
  
  
127
  
  
  
zc.buildout and distutils
  
  
  
  
  
  
  
  
  
10
  
  
  
zc.buildout and setuptools
  
  
  
  
  
  
  
  
  
107
  
  
  
Paver and setuptools
  
  
  
  
  
  
  
  
  
9
  
  
  
Paver and Distutils
  
  
  
  
  
  
  
  
  
3
  
  
  
Other
  
  
  
  
  
  
  
  
  
64
  
  
  

* * * * *

  
## How do you install a package that does not provide a standalone
installer (but provides a standard setup.py script) most of the time ?

  
  
  
  
I use easy\_install
  
  
  
  
  
  
  
  
  
241
  
  
  
I download it and manually run the python setup.py install command
  
  
  
  
  
  
  
  
  
139
  
  
  
I use pip
  
  
  
  
  
  
  
  
  
34
  
  
  
I move files around and create symlinks manually.
  
  
  
  
  
  
  
  
  
7
  
  
  
I use the packaging tool provided in my system (apt, yum, etc)
  
  
  
  
  
  
  
  
  
81
  
  
  
Other
  
  
  
  
  
  
  
  
  
33
  
  
  

* * * * *

  
## How do you remove a package ?

  
  
  
  
manually, by removing the directory and fixing the .pth files
  
  
  
  
  
  
  
  
  
275
  
  
  
I use one virtualenv per application, so the main python is never
polluted, and only remove entire environments.
  
  
  
  
  
  
  
  
  
154
  
  
  
using the packaging tool (apt, yum, etc)
  
  
  
  
  
  
  
  
  
178
  
  
  
I don't know / I fail at uninstallation
  
  
  
  
  
  
  
  
  
79
  
  
  
I change PYTHONPATH to include a directory of the packages used by my
application, then remove just that directory
  
  
  
  
  
  
  
  
  
31
  
  
  
Other
  
  
  
  
  
  
  
  
  
10
  
  
  

* * * * *

  
## How do you manage using more than one version of a library on a
system ?

  
  
  
  
I don't use multiple versions of a library
  
  
  
  
  
  
  
  
  
217
  
  
  
I use virtualenv
  
  
  
  
  
  
  
  
  
203
  
  
  
I use Setuptools' multi-version features
  
  
  
  
  
  
  
  
  
46
  
  
  
I build fresh Python interpreter from source for each project
  
  
  
  
  
  
  
  
  
16
  
  
  
I use zc.buildout
  
  
  
  
  
  
  
  
  
109
  
  
  
I set sys.path in my scripts
  
  
  
  
  
  
  
  
  
48
  
  
  
I set PYTHONPATH to select particular libraries
  
  
  
  
  
  
  
  
  
49
  
  
  
Other
  
  
  
  
  
  
  
  
  
23
  
  
  

* * * * *

  
## Do you work with setuptools' namespace packages ?

  
  
  
  
Yes
  
  
  
  
  
  
  
  
  
178
  
  
  
No
  
  
  
  
  
  
  
  
  
344
  
  
  

* * * * *

  
## Has PyPI become mandatory in your everyday work (if you use
zc.buildout for example) ?

  
  
  
  
Yes
  
  
  
  
  
  
  
  
  
228
  
  
  
No
  
  
  
  
  
  
  
  
  
294
  
  
  

* * * * *

  
## If you previously answered Yes, did you set up an alternative
solution (mirror, cache..) in case PyPI is down ?

  
  
  
  
Yes
  
  
  
  
  
  
  
  
  
77
  
  
  
N/A
  
  
  
  
  
  
  
  
  
277
  
  
  
No
  
  
  
  
  
  
  
  
  
166
  
  
  

* * * * *

  
## Do you register your packages on PyPI ?

  
  
  
  
Yes
  
  
  
  
  
  
  
  
  
239
  
  
  
No
  
  
  
  
  
  
  
  
  
281
  
  
  

* * * * *

  
## Do you upload your package on PyPI ?

  
  
  
  
Yes
  
  
  
  
  
  
  
  
  
205
  
  
  
No
  
  
  
  
  
  
  
  
  
314
  
  
  

* * * * *

  
## If you previously answered No, how do you distribute your packages ?

  
  
  
  
One my own website, using simple links
  
  
  
  
  
  
  
  
  
139
  
  
  
One my own website, using a PyPI-like server
  
  
  
  
  
  
  
  
  
50
  
  
  
On a forge, like sourceforge
  
  
  
  
  
N/A
  
  
  
  
  
  
  
  
  
251
  
  
  
Other
  
  
  
  
  
  
  
  
  
56
  
  

