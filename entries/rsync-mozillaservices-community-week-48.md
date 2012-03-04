Title: $ rsync mozilla/services community #week 48
Date: 2010-12-04 16:16
Category: mozilla, python

What's this ? read [this post][]   
## Week 48

  
**[Easy Setup on new devices][]:** I have benched the server on stage
using Funkload to make sure everything works nicely, and realized that
the Nginx + Gunicorn setup is not currently optimal using a single
worker. I need to use a single worker because I have coded an IP
filtering system that relies on a memory queue for speed reasons. In
other words, all requests on one server need to share the same memory.
The solution is to use an async worker like [gevent][] that can be used
without having to change the application code (Thanks Benoit!). GEvent
uses libevent and greenlets and will allow a single process to run an
event loop to handle requests, ala Twisted. So that's my next task.   
  
**Firefox Sync in Python**: We finally landed the Python Sync server in
dev servers, using our full environment. The server itself works since a
while now, and is successfully used by people in the community, but I
didn't have the chance to get it running with our fully-fledge
infrastructure yet at Mozilla. So I had a few bugs to fix this week,
related to that. For instance the ACLs on the Ldap are set so the bind
user cannot read all fields on users entries. Anyways, this is now
looking good.   
  
**OpenID / Identity**: The bench script is ready. There's not much left
to do on the server at this point. Maybe promote the server a little bit
to see if some people in the community have an interest in such a thing.
  
## Next Week Plans

  
Next week I plan to:   
-   Test the gevent worker with GUnicorn
-   Start some documentation
-   Integrate code reviews for Sync, hopefully
-   Prepare the 1/2 Python gathering I have planned mid-december in
    Moutain View Offices
-   etc.

  [this post]: http://tarekziade.wordpress.com/2010/11/30/rsync-mozillaservices-community-week-47/
  [Easy Setup on new devices]: https://bugzilla.mozilla.org/show_bug.cgi?id=601644
  [gevent]: http://pypi.python.org/pypi/gevent/
