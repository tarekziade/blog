Title: Monitoring a Zope 2 application
Date: 2009-05-19 09:29
Category: zope

We have a simple need for a customer project that runs a Zeo server and
a few Zeo clients : being able to check the status of every Zeo client,
and monitor what they are doing.   
  
[DeadlockDebugger][] almost provides this feature since it is able to
produce a dump of the execution stack for every thread a Zope instance
is running.   
  
Based on this tool, I have developed [ZopeHealthWatcher][], that
provides a console script to query a Zope instance, and get back a
status for every running thread. It tells you if the thread is idling or
if it's running some code. The script also returns an exit code
depending on the number of busy threads, so it can be used in tools like
Nagios.   
  
When there are 4 or more busy threads, the script will return the
execution stacks for every busy thread and some extra info like the
system load and memory info. The returned info will be extendable
through plug-ins in the next version, but right now the provided info
are enough for our needs.   
  
I have also created an HTML version, so when the dump is requested from
another tool than the console script (e.g. a browser), it displays a
nice human-readable interface (check the PyPI page for more info and a
screenshot).   
  
Notice that DeadLockDebugger is hackish since it patches the Zope
publisher at startup. But we won't change this part: we need this tool
to run from the oldest to the newest Zope 2 version. And the patch just
works fine, so...   
  
The provided version should run out of the box in a buildout-based
Plone 3 application, but requires manual installation steps on older
Plone or CPS versions.   
  
I didn't mention these manual steps in the documentation. I think I am
the only person in the world interested in running this tool on the
dead-but-still-in-production-in-many-places Nuxeo CPS.   
  
By the way: kudos goes to Marc-Aurèle Darche, who is maintaining CPS
for years now, making it one of the most bug-free and stable CMS
solution out there. Ok it's probably easier to reach this level of
quality since the platform is very stable and only evolves very slowly
thanks to [Georges Racinet][].

  [DeadlockDebugger]: http://plone.org/products/deadlockdebugger
  [ZopeHealthWatcher]: http://pypi.python.org/pypi/ZopeHealthWatcher/
  [Georges Racinet]: http://www.racinet.fr/index.php?pages/Nuxeo-CPS
