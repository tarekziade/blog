Title: Mozilla Services - Weeks 01-02
Date: 2011-01-11 17:41
Category: mozilla, python

What's this ? read [this post][]   
  
I did not post a weekly update last week because things slowed down
during vacations. I've also decided:   
-   to change the title to a less geeky one, that is easy to understand
    :D
-   to publish the post every two weeks instead of every week. It seems
    to be a more natural pace. We'll see

  
### What happened

  
My talk at Pycon about Firefox Sync was [accepted][] ! I've added a
Wiki page containing the outline so you can help me if you see some
missing things or want me to talk about -
[https://wiki.mozilla.org/Services/Sync/Pycon2010][]   
  
Hudson now runs all kinds of tests over the Sync and Pake servers. The
functional tests are running on a real Sync infrastructure, and that
helped me find bugs that are happening only when the server has been
running for a while. I could fix for instance a bug that was filling the
pool of LDAP connectors without freeing them properly. We'll work on
having such CI setups for every Services projects in the future.   
  
The RPM-based release process for all the Python apps is working like a
charm and I need to take it to the next stage. We will set up a in-house
PyPI proxy to avoid calling pypi.python.org on every build. We will
probably use [collective.eggproxy][]. That'll be helpfull for the tests
as well.   
  
I also started to work with Stefan on hardening the [J-Pake protocol][]
for the Sync easy setup. The goal is to make sure it works well when the
device is in a flaky network/wifi environment.   
### What's planned

  
I'll focus on finishing small bits in the Sync Server and make sure the
Pake server meets all the requirements for the grand Firefox 4 release.
Beside the work with Stefan, we need to add more logs in the server to
make it easier to see what going on: successfull transaction, failures
with reasons etc. I'll work with Richard on this.   
  
Globally, the next two weeks are about "serrer les vis" :D

  [this post]: http://tarekziade.wordpress.com/2010/11/30/rsync-mozillaservices-community-week-47/
  [accepted]: http://us.pycon.org/2011/schedule/sessions/83/
  [https://wiki.mozilla.org/Services/Sync/Pycon2010]: https://wiki.mozilla.org/Services/Sync/Pycon2010
  [collective.eggproxy]: http://pypi.python.org/pypi/collective.eggproxy
  [J-Pake protocol]: https://wiki.mozilla.org/Services/Sync/SyncKey/J-PAKE#Server_API
