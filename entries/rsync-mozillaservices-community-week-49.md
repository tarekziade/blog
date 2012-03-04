Title: $ rsync mozilla/services community #week 49
Date: 2010-12-10 20:11
Category: mozilla, python

What's this ? read [this post][]   
## Week 49

  
**[Easy Setup on new devices][]:** I worked on doing distributed tests
and [blogged about it][]. Turns out using gevent does not speed up the
application because it uses a memcached lib that works with sockets and
it looks like it's locking Gevent. So I'll just use the regular worker
and change some of the design later to be able to use several workers.   
  
**Firefox Sync in Python**: Integrated some reviews from Ian and did
some minor cleanup.   
  
**OpenID / Identity**: I passed the project to JR, our new team member.
(Welcome ;))   
  
**QA**: I set up a Hudson server that runs the tests for the Sync and
the Pake server and also builds the RPMs. This way the packages are
continuously built and any error related to that part is also detected.
  
## Next Week Plans

  
This week-end and next week, I plan to:   
-   Write some script to automate the deployment of the RPM built by
    Hudson
-   Start some documentation
-   Have an intensive work week in Moutain View
-   Prepare [the 1/2 Python gathering we will have Tuesday there][].
-   etc.

  [this post]: http://tarekziade.wordpress.com/2010/11/30/rsync-mozillaservices-community-week-47/
  [Easy Setup on new devices]: https://bugzilla.mozilla.org/show_bug.cgi?id=601644
  [blogged about it]: http://tarekziade.wordpress.com/2010/12/09/funkload-fabric-quick-and-dirty-distributed-load-system/
  [the 1/2 Python gathering we will have Tuesday there]: https://wiki.mozilla.org/Services/AllSnakes
