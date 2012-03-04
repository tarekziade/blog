Title: Firefox Sync Server in Python - Take 2
Date: 2010-09-21 17:11
Category: mozilla, python, sync

It's been more than a month since the last update on my work on Firefox
Sync. Time for a quick update.   
### The Code

  
The application grew quite well and was splitted in four separate
projects:   
-   **SyncCore**: contains the authentication back-ends and various
    utilities like the CEF logger or various WSGI helpers.
-   **SyncReg**: that's the User application. Implements:
    [https://wiki.mozilla.org/Labs/Weave/User/1.0/API][]. Can be used as
    a standalone WSGI application
-   **SyncStorage**: Contains the storage back-ends and implements
    [https://wiki.mozilla.org/Labs/Weave/Sync/1.0/API][] (and the
    upcoming 1.1.) Can be used as a standalone WSGI application.
-   **SyncServer**: This is just a glue application that can be used to
    run in the same server both Reg and Storage servers. By default this
    application will run sqlite back-ends for storage and
    authentication, which means it can be launched with a zero-config
    environment.

  
I moved the code to bitbucket, and will clone it back to hg.mozilla.org
once we set dedicated repositories for the Python server there. If you
want to run your own Sync server, it's still very simple. Make sure you
have the latest virtualenv installed, Mercurial and Make, then run:   
   $ hg clone http://bitbucket.org/tarek/sync-server Sync

    $ cd Sync

    $ make build

  
Then you can run your server on port 5000 by using the built-in web
server:   
   $ bin/paster serve development.ini

  
Of course, a real setup should be done using SSL, a real web server
like Apache/mod\_wsgi and MySQL for the DB. But the default setup is
useful and can replace the minimal-server Toby wrote.   
### Benching

  
One thing I want to make sure is that the Python server is as fast as
possible, and faster than the PHP application. Since a Python web
application can reuse the same interpreter in memory, there's a lot of
room for improvements like connection pooling and light memory caching.
I also wanted to bench out various configurations for the DB, like using
postgresql instead of mysql etc.   
  
The team is currently working on stress testing our Sync infrastructure
and the tool that we use is [Grinder][]. Grinder is a Java tool that
uses Jython for writing tests, and provides a simple console to drive
it. The results Grinder return are raw results, and there's quite some
work left to do if you want to generate nice reports.   
  
I used another tool to bench the server called [Funkload][]. It's a
Python tool that uses unittest classes to run benches, and provides a
functional test tool to query a web server and do some assertions like
[WebTest][]. It produces HTML reports that are containing a lot of
metrics. Some I don't use because they are specific to web sites. But
it's good enough to stress-test the Sync server and compare PHP and
Python speed. One caveat is that it cannot be distributed. There's a
project called [BenchMaster][] that adds this feature, that I need to
try.   
  
The stress test is the same than the Grinder one, and here are some
reports using various configuration :
[http://sync.ziade.org/funkload][]/   
  
[![image][]][]While Python already appears to be slightly faster than
PHP, those were done on my MacBook with 100 users loaded in the DB, 6000
objects each, so don't mean a lot. Just that the Python application is
not borked :D .   
  
I'll probably run Funkload in the same environment we run Grinder at
Mozilla, where we have a realistic setup. I also want to have this kind
of reports generated every day, so I can keep an eye on how the Python
server performs. Making sure the app does not slow down when it grows is
one important part of continuous integration.   
### Caching: Redis vs Memcached

  
I used [Redis][] to do a bit of caching in the Python app, instead of
Memcached like the PHP app. See my previous post for the rational.   
  
Redis was very stable during my benches, but I have heard from some
other projects that they had quite a few problems with it in production
[I might post more details here in another blog post]. I still think
this is the tool we should use in Sync, and I also want to experiment
writing a full back-end for Sync using it. But the first version of the
Sync server we will deploy on our servers will probably use Memcached
since it's proven to work well right now and since I don't really need
all the extra features Redis offers if the usage is restricted to
volatile caching.   
### Continuous integration

  
![image][1]I am still working alone on the Python app, but a continuous
integration server is something we really want to have. I am a big fan
of buildbot but I wanted to give a try at Hudson. The management
interface is brilliant and I could set up a Hudson server for Sync in an
hour. I eventually moved it at [https://hudson.mozilla.org/job/Sync][]
with other Mozilla projects from the WebDev team. It contains Pylint
reports, test coverage report, and of course Chuck Norris keeps the code
safe.   
### What's next ?

  
The Python app is mostly done, besides a few things to clean up. The
next big step will be to bench it alongside the PHP application on
realistic data, fix any problem that will rise, then work on pushing it
in production. The production switch will probably happen gradually
since every node is standalone. And since the rest of the team is quite
busy to make sure everything is ready for the upcoming Firefox 4 final
release which includes Sync natively, switching to Python is not the \#1
priority right now. I expect it to happen before the end of the year
though.   
  
In the meantime once the benches are done and the code is rock-solid.
I'll start to play with different back-ends. A full Redis back-end and
maybe something based on Riak or Cassandra.

  [https://wiki.mozilla.org/Labs/Weave/User/1.0/API]: https://wiki.mozilla.org/Labs/Weave/User/1.0/API
  [https://wiki.mozilla.org/Labs/Weave/Sync/1.0/API]: https://wiki.mozilla.org/Labs/Weave/Sync/1.0/API
  [Grinder]: http://grinder.sourceforge.net/
  [Funkload]: http://funkload.nuxeo.org/
  [WebTest]: http://pythonpaste.org/webtest/
  [BenchMaster]: http://pypi.python.org/pypi/benchmaster
  [http://sync.ziade.org/funkload]: http://sync.ziade.org/funkload/
  [image]: http://sync.ziade.org/funkload/python-postgres/requests_rps.png
    "Funkload Report"
  [![image][]]: http://sync.ziade.org/funkload
  [Redis]: http://code.google.com/p/redis/
  [1]: https://hudson.mozilla.org/plugin/chucknorris/images/alert.jpg
    "Chuck Norris"
  [https://hudson.mozilla.org/job/Sync]: https://hudson.mozilla.org/job/Sync/
