Title: Faking a server for client-side tests
Date: 2010-05-10 11:59
Category: python

Distutils makes some call to the PyPI server to register and upload
projects. Distutils2 will also make some calls to
[packages.python.org][] to automate the upload of documentation. This
feature was added by Janis a while ago in Distribute and is being
backported in Distutils2 during the GSOC.   
  
To test all these features, what I usually did in Distutils was to
monkey-patch the code that calls the server and record in memory the
exchanges to check them. The problem with this approach is that you have
to be careful in the way you patch the APIs the client code use. A
typical bug that can happen is to get a slightly different behavior
making your code buggy or broken when it interacts with the real server.
Of course you can run your test once with the real server then use some
mock or stub techniques. But this work can be rather tedious and complex
in my opinion.   
  
What I tend to do these days is drop completely this client-side test
fixture approach, and just run a local server that implements partially
or fully the real server API.   
  
This blog post is just to demonstrate how easy it can be to run your
own test server.   
  
For HTTP protocols, the standard library provides everything needed to
write such a server in a few lines. The [wsgiref][packages.python.org]
module for instance, is great to get a web server up and running during
your tests.   
  
Here's a full example (working for Python \>= 2.6 and Python 3):   
   import threading

    try:

        from urllib.request import urlopen

    except ImportError:

        from urllib2 import urlopen



    import time

    from wsgiref.simple_server import make_server, demo_app



    class AppRunner(threading.Thread):

        """Thread that wraps a wsgi app"""

        def __init__(self, wsgiapp=demo_app):

            threading.Thread.__init__(self)

            self.httpd = make_server('', 0, wsgiapp)

            self.address = self.httpd.server_address



        def run(self):

            self.httpd.serve_forever()



        def stop(self):

            self.httpd.shutdown()

            self.join()

            time.sleep(0.2)



    _SERVER = None



    def run_server():

        """Runs the server."""

        global _SERVER

        if _SERVER is not None:

            # we suppose it's running

            return _SERVER.address

        _SERVER = AppRunner()

        _SERVER.start()

        return _SERVER.address



    def stop_server():

        """Stops the server."""

        global _SERVER

        if _SERVER is None:

            return 

        _SERVER.stop()

        _SERVER = None



    if __name__ == '__main__':

        # 1. set up

        print('Launching the test server')

        url, port = run_server()

        print('Test server running at %s:%d' % (url, port))



        # 2. test

        try:

            print('Testing..')

            res = urlopen('http://%s:%d' % (url, port))

            assert b'Hello world!' in res.read()

        finally:

            # 3. tear down

            print('Stopping the test server')

            stop_server()

  
*run\_server() *and *stop\_server()* are driving a thread that runs a
wsgi application using the *wsgiref* helpers.   
  
In the main section you can see an example of a test fixture, and of
running a client test on the *demo\_app* wsgi application *wsgiref*
provides. It should return a "Hello world!" page. These functions are
making sure there's only one server running even if *run\_server()* is
called several times, so it's dead easy to use it from a unittest class.
  
  
From there, writing a test server is just a matter of implementing a
wsgi application that will replace the *demo\_app* one. I find this
technique superior to all the stub/mockup work required when you don't
run your own server.   
  
For other protocols than HTTP, this work can be longer and more complex
of course, unless the sdtlib or a third party project already has a
server implementation you can use (like [smtpd][]).

  [packages.python.org]: http://packages.python.org
  [smtpd]: http://www.doughellmann.com/PyMOTW/smtpd/index.html
