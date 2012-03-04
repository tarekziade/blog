Title: mod_ntlm in FreeBSD
Date: 2009-06-30 13:39
Category: python

We had to install [mod\_ntlm][] under a FreeBSD 6.4 server with a
colleague, but the port for this package seems broken at least for
FreeBSD 6.2 and 6.4. It just doesn't work when it initiates an NTLM
session through SMB, and it seems to be compiled without the log support
so the last log you get doesn't give any useful hint on what's wrong.   
  
So we had to recompile it to activate the log and try understand what
the problem was. But Apache doesn't not support threaded mode under
FreeBSD 6.x (or I couldn't manage to make it work howsoever), so
mod\_ntlm failed to compile since it uses Apache's thread mutexes to
perform some locks on some operations.   
  
We've deactivated them and recompiled the module, and now it works now
like a charm. It's weird because it means that the binary package for
this module is completely broken. I couldn't find any place mentioning
this.   
  
Anyways, I know this is an old software combination, but since Google
doesn't give any hint on this problem, I wanted to blog about it and
join the diff I made out of mod\_ntlm2 at
[https://modntlm.svn.sourceforge.net/svnroot/modntlm/trunk][] here:[diff
file][]   
  
So if you bump into this problem, you will hopefully reach this page
and save a few hours.

  [mod\_ntlm]: http://modntlm.sourceforge.net/
  [https://modntlm.svn.sourceforge.net/svnroot/modntlm/trunk]: https://modntlm.svn.sourceforge.net/svnroot/modntlm/trunk
  [diff file]: http://www.afpy.org/Members/tarek/mod_ntlm2.diff
