Title: Mozilla Services / Week 10/11
Date: 2011-03-23 15:09
Category: mozilla, python

What's this ? read [this post][].   
### What happened

  
Well.. Firefox 4 is out and the number of downloads is impressive.
Check this page: [http://glow.mozilla.org/][]. It's almost 7 millions
right now !   
  
Back to my Services dev topics :D   
  
It's been a while since I've posted a bi-weekly status update, because
I was busy traveling to Pycon, then to Vancouver to work with the
messaging team on F1. If you've never heard of it, check [Bryan's
post][]. Then [go there][], install the Add-on and enjoy it.   
  
The work there was quite interesting as we've started to think about
how to scale F1 so it can be used by millions of users. On server-side
--the part I am the most interested in-- they have built a Pylons
application that acts like a oauth proxy, used by the Add-On to send
tweets, e-mails etc to third-party services like Twitter, GMail or
Facebook.   
  
The choice of Pylons made sense back when the project started because
there was a database that stored some user data, and a few panels that
are displayed when you want to manage your settings. But that database
has been removed from the server and the code has shrinked to a few
static pages and an oauth lib used to communicate with the various
services.   
  
One thing we will do is to move to a lighter web application and just
use WebOb and Routes. Pylons became overkill for that application, and
has now joined the cemetery of deprecated frameworks (Pyramid is the new
thing).   
  
On the scaling part, we're still working hard to come up with the best
design, and we're trying to keep this wiki page up-to-date with that
work: [https://wiki.mozilla.org/Services/F1/Server/Architecture][]. Note
that this is a work in progress, so nothing is settled in stone. The
most interesting part is to decide if we do a synchronous architecture
or asynchronous one. I personally think a synchronous architecture is
simpler to start with, since we already have a working application that
does what we want, and since we can always move to an async model later.
  
  
Another interesting part I am working on is how to do functional tests
against our application, knowing that most APIs will call in turn a
third-party server like Twitter or GMail. We need to mock those but in
the meantime find a smart way to replay real sessions. I've worked on
this topic in the past and blogged about it. I had created an initial
version of a small mock tool but not really used it until this week.   
  
Mark Hammond has been working on the topic as well and we need to
synchronize our efforts next, but the general idea we've discussed and
we'll use is to record a session that occurs with the real servers, dump
it in a file, then allow the tests to reuse the recorded session instead
of calling the real server again. This also needs to be done through a
real TCP call to a third party server, and not mocked in Python, for a
realistic behavior.   
  
My first take on this is a simple proxy called **recproxy** which is a
new version of my previous proxy. You can use it like this:   
   class TestSendController(unittest.TestCase):

        @recproxy('https', 'twitter.com', 'test_send.rec')

        def test_send(self):

           ....

  
This proxy does the following:   
-   A proxy server is launched on the localhost
-   Any call via urrlib2 which destination is https://twitter.com/xxxx
    is intercepted and sent to the local proxy
-   The local proxy reads the test\_send.rec file that contains
    request/response pairs. If a request in that file corresponds to the
    request, the response is returned.

  
Of course, this means that the *test\_send.rec* has to be created
first. To do it, all you have to do is to run the tests with a
***PROXY*** environment variable set to 1. This will call the proxy
server, but instead of returning values found in the file, it will proxy
the requests to the real server and record the responses into the file.
  
  
Since we want to share the recorded files and obfuscate sensitive data,
you can replace those data by *XXX* in the file. The proxy will match
the incoming requests using a regular expression that will replace XXX
by anything.   
  
Here's an example of such a rec file:   
   POST /statuses/update.json HTTP/1.1

    Accept-Encoding: identity

    Connection: close

    Content-Length: XXX

    Content-Type: application/x-www-form-urlencoded

    Host: localhost:65535

    User-Agent: Python-urllib/2.6



    oauth_consumer_key=XXX&oauth_nonce=XXX&oauth_signature_method=HMAC-SHA1&oauth_timestamp=XXX&oauth_token=XXX&oauth_version=1.0&status=%20http%3A%2F%2Fwp.me%2FpgWjI-7X&oauth_signature=XXX

    ====

    200 OK

    Content-Type: application/json; charset=UTF-8

    Content-Length: 11



    {"id": 123}

    =======

  
This is basically a mock of a successful status update. And since the
proxy works as a test function decorator, you can create records for bad
behaviors as well, when you are fixing a bug that happens when there's a
unexpected answer from the third party server.   
  
You can also mock several servers (like bit.ly and twitter) by simply
adding more decorators to the function.   
  
The recproxy code is [here][]. It's still an early version and will
probably evolve a lot.   
### What's planned

  
In the next weeks we will continue to work on the architecture for F1,
and also add more tests with Mark & Shane.   
  
I am looking forward to synchronize my testing work with what Mark has
done. Also, I'll probably make the proxy tool a lib, because that's what
we want to use in other projects.

  [this post]: http://tarekziade.wordpress.com/2010/11/30/rsync-mozillaservices-community-week-47/
  [http://glow.mozilla.org/]: http://glow.mozilla.org/
  [Bryan's post]: https://mozillalabs.com/messaging/?p=343
  [go there]: http://f1.mozillamessaging.com/
  [https://wiki.mozilla.org/Services/F1/Server/Architecture]: https://wiki.mozilla.org/Services/F1/Server/Architecture
  [here]: https://github.com/tarekziade/f1/blob/develop/linkdrop/tests/functional/proxy.py
