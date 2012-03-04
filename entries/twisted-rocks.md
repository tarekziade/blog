Title: Twisted rocks !
Date: 2010-09-30 18:14
Category: mozilla, python

When your LDAP server or your MySQL server starts to get really slow for
any reason, you better make sure your web application don't wait too
much for them. Otherwise you will just have more and more requests
piling up, waiting for your HTTP server to kill them when they reach the
server timeout. Apache default timeout is 300 seconds by the way, so
depending on how many users your application serves, you might end up
with a big bottleneck in your application and a potential disaster on
the server resources.   
  
One solution is to make sure your web application handles itself the
problem, by configuring a tight timeout for every third party server it
calls, like a SQL server or a LDAP Server. So whenever things gets too
slow, you can return immediately a 503 to the client and free the
thread. A [Retry-Later][] header can also be added to inform the client.
  
  
For Sync, we have another header that is specifically looked up when
things gets bad on server side, which is X-Weave-Backoff. But that
header is used only on successful operations to gently ask the client to
back off for some time.   
  
Anyways, in theory it's quite simple to add some* try..except timout:*
code in your application but in practice you better test it for real by
benching your application with slow third party servers and check that
the server does not melt in that case.   
  
Not all servers (LDAP, SQL, etc) provide a way to make things slower
and not all Operating Systems provide a simple way to slow down the
network between two applications. [netem][] is a nice tool but you might
need to recompile your kernel to use it, and you have to be on some
flavor of BSD or Linux for that.   
  
Twisted excels for such tasks. I could write a port-forwarding script
to simulate delays in less than 15 lines (that would take probably 100
lines using plain socket/asyncore).   
   import time

    from twisted.internet import reactor

    from twisted.protocols import portforward



    class LoggingProxyServer(portforward.ProxyServer):

        def dataReceived(self, data):

            time.sleep(20)

            portforward.ProxyServer.dataReceived(self, data)



    class LoggingProxyFactory(portforward.ProxyFactory):

        protocol = LoggingProxyServer



    if __name__ == '__main__':

        fwd = LoggingProxyFactory('localhost', 389)

        reactor.listenTCP(390, fwd)

        reactor.run()

  
Once this script is launched, my application can use the port 390 to
connect to LDAP, and deal with the timeouts.   
  
From there, I am [exploring different ways][] to delay the calls in a
realistic manner. Like making the delay get bigger at every call until
it reaches a max, then reducing it, etc. It's also a good way to log all
the TCP conversations between the apps without having to set up a
dedicated app like [WireShark][].   
  
I already knew this, since Twisted was the framework we used in my
previous company, but let me say it again: when it comes to write little
network tools like that, **Twisted just rocks**.

  [Retry-Later]: http://webee.technion.ac.il/labs/comnet/netcourse/CIE/RFC/2068/201.htm
  [netem]: http://www.linuxfoundation.org/collaborate/workgroups/networking/netem
  [exploring different ways]: http://bitbucket.org/tarek/sync-server/src/tip/tests/delay/delay.py
  [WireShark]: http://www.wireshark.org/
