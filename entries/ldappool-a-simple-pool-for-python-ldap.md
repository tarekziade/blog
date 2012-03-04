Title: ldappool: a simple pool for python-ldap
Date: 2011-10-28 19:16
Category: mozilla, python

Over the past few months, we've done quite some tweaking at Mozilla
Service to make our Python platform work well for the Sync platform. One
bottleneck we have is the number of open connections we can have on a
given LDAP server.   
  
On very high load, we needed to make sure we could control the flow of
open connections, and when possible reduce the number of connectors as
much as possible, by recycling/reusing them.   
  
[python-ldap][] does not come with a pool, so we've built our own with
the Ops team.   
The pool keeps LDAP connectors alive and let you reuse them,
drastically reducing the time spent to initiate a ldap connection.   
  
The pool has useful features like:   
-   transparent reconnection on server restarts, or timeouts/downtimes
-   configurable pool size and connectors timeouts
-   a context manager to simplify acquiring and releasing a connector
-   configurable max lifetime for connectors

  
The *max lifetime* feature is useful when you add a new server in a
pool of ldap servers: if the pool is already filled with connectors, a
server you will introduce will never have a chance to get a connector.   
We avoid this problem by introducing a max lifetime for our connectors:
the pool gets fresh connectors after a bit of time and can access all
our resources.   
  
The pool is used via a context manager, and is recycled when you leave
the with block:   
   from ldappool import ConnectionManager



    cm = ConnectionManager('ldap://localhost')



    with cm.connection('uid=user,ou=logins,dc=mozilla', 'password') as conn:

          .. do something with conn ..

  
I have extracted it from our code based and released it on its own at
pypi: [http://pypi.python.org/pypi/ldappool/][]   
  
Let us know if you try it !

  [python-ldap]: http://python-ldap.org/
  [http://pypi.python.org/pypi/ldappool/]: http://pypi.python.org/pypi/ldappool/
