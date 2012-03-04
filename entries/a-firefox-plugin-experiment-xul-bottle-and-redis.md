Title: A Firefox plugin experiment. XUL, Bottle and Redis
Date: 2010-04-14 22:36
Category: python

I am experimenting Mozilla's XUL to write Firefox plugins. I never had a
chance to give it a shot before, so let's roll.   
  
To try it out, I decided to implement a very simple **Twitter Firefox
plugin** that works a bit like TweetDeck: The plugin adds a new action
in the contextual menu labeled "Twitt it!". When you click on it, a
window pops, with a text box containing a short url for the current
page. The user can complete the text and send a twitter about the page.
  
  
[![image][]][]   
  
I am pretty sure there are hundreds of similar plugins out there, but
it's a pretty simple use case to learn XUL :)   
### The shortener

  
Before I could start to write the Firefox plugin, I needed a url
shortener. I had two options: a shortener local to the plugin or an
online service. A local shortener is probably more efficient, but an
online service is more fun and more interesting to code: it can be
shared across clients and it's a first step to a more complex plugin
that works with online services.   
  
Services likes [bit.ly provide such API][], but you have to register of
course, and you have a limited number of calls to the service.   
  
It's not like I am going to make a zillions calls to such a service,
but it's so simple to implement that I decided to write my own.   
  
To store the URLs I used a Redis storage. This is of course overkill
for an experiment, but it was a good excuse to try it out and see how
Redis fits my brain.   
#### Redis

  
Setting up a Redis server on my MacBook was done in a matter of
minutes. You just have to compile the source and you get a redis-server
binary you can launch and eventually daemonize:   
   $ ./redis-server

    14 Apr 23:07:28 * Warning: no config file specified, using the default config. In order to specify a config file use 'redis-server /path/to/redis.conf'

    14 Apr 23:07:28 - Server started, Redis version 1.2.6

    14 Apr 23:07:28 - DB loaded from disk

    14 Apr 23:07:28 - The server is now ready to accept connections on port 6379

    14 Apr 23:07:28 . DB 0: 1 keys (0 volatile) in 4 slots HT.

    14 Apr 23:07:28 . 0 clients connected (0 slaves), 294928 bytes in use, 0 shared objects

  
From there, you can use the redis Python client, which provides all
Redis commands. The great thing about this client (I didn't try all of
them though) is that it is self-documented. All you have to do is read
the Redis Commands Reference here :
[http://code.google.com/p/redis/wiki/CommandReference][]. Lower-case
them and you have the Python methods.   
  
Redis can be used as a classical key/value storage, but also has
convenient APIs to work with lists and sets. In other words Redis can
handle [many use cases][] out of the box.   
  
To store URLs in Redis, I used the simple set/get APIs and stored two
key/value per URL: long\_url/short\_url and short\_url/long\_url. This
takes more room but makes all lookups efficient (that is, 0(1)).   
  
Here's the code:
[http://bitbucket.org/tarek/urltotwit/src/tip/shortener/shortener/urlstore.py][]
  
  
I am pretty new to Redis, so if you think this is not optimal, let me
know !   
#### The web service

  
The web service is just composed of two methods:   
1.  **/urls/short\_id** : when reached, redirect to the page
    corresponding to the short\_id
2.  **/shortener**: a GET method that returns a short url, given an url

  
This is a perfect use case for the [**Bottle**][] micro-framework !   
  
Nothing particular here, besides the fact that it took me 30 lines or
so to write it !   
  
The code is here :
[http://bitbucket.org/tarek/urltotwit/src/tip/shortener/shortener/main.py][]
  
  
One thing I have to add is a security layer once this is published on
my server.   
### The Plugin

  
To start things out, I used the Extension Wizard located at
[http://ted.mielczarek.org/code/mozilla/extensionwiz][] that generated a
skeleton of the plugin. The Firefox versions in *install.rdf* are a bit
outdated, so I had to change the **em:maxVersion** value to **3.5.\***
so it would work with my 3.5.9 version. I am not 100% sure the layout is
still fully compliant with the best practices but it worked.   
  
From there, I created a new XUL file called *send\_twitter.xul* in
*content*. This file contains the window that is displayed by the
plugin. It uses jQuery so its simple to call the shortener via Json.   
   <window id="twitit-window"

     title="Twit it !"

     orient="horizontal"

     xmlns:html="http://www.w3.org/1999/xhtml"

     xmlns="http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul"

     onload="centerWindowOnScreen();">



     <script src="chrome://global/content/dialogOverlay.js" />

     <script src="jquery-1.4.2.min.js"/>

     <script language="javascript"><![CDATA[



     function initTwit() {

       var current_url = window.opener.gBrowser.contentDocument.location.href;

       $.getJSON("http://localhost:8080/shorten", {url: current_url},.

       function(json) {

         document.getElementById('twit-text').value = json.result;

       });

     }



     function send(twit) {

       /* TO BE DONE */

     }



     initTwit();

     ]]></script>



     <box>

     <vbox>

     <label value="Enter your Twitter message for this page:"/>

     <spring flex="3" style="max-height: 5px;"/>

     <textbox id="twit-text" style="min-width: 100px;".

     rows="4" cols="80" multiline="true" maxlength="140">

     </textbox>

     <hbox>

     <button id="ok" label="OK" default="true" accesskey="t"

     onclick="send($('twit-text'));"/>

     <button id="cancel" label="Cancel" default="false" accesskey="c"

     onclick="window.close();"/>

     </hbox>

     </vbox>

     </box>

    </window>

  
*initTwit()* calls the shortener via Json, and fills the text box with
the short url. This version points to my local Shortener instance.   
  
What stroke me when building this window was the need to rebuild the
plugin and relaunch Firefox everytime I changed it. And working with XUL
windows is not obvious because of the way the layout works (v/hboxes). I
ended up working with a Live Xul editor:
[http://ted.mielczarek.org/code/mozilla/xuledit/xuledit.xul][]   
  
The part that I still miss is TDD: how to set up a healthy Javascript
TDD environment to work with Firefox Plugins ? Investigating..   
  
The (unfinished) code is here:
[http://bitbucket.org/tarek/urltotwit/src/tip/urltotwit%40tarek.ziade.org][]
  
  
If you are a XUL coder, please comment !   
### Conclusion

  
I need to finish the work on the part that sends the twitter via the
user account. So far I found XUL pretty nice. It feels like working in
an enhanced HTML language. I also need to read some about the security
model and the development best practices.   
  
On Python side, I am pretty happy with the Redis+Bottle small stack,
and I'll probably add a small web UI and make it available on ziade.org.
I'll be the third one at my Python User group to have my own url
shortener ;) ([Gawel][], D[avid'Bgk][])

  [image]: http://tarekziade.files.wordpress.com/2010/04/picture-36.png?w=1024
    "Twitter Plugin example"
  [![image][]]: http://tarekziade.files.wordpress.com/2010/04/picture-36.png
  [bit.ly provide such API]: http://code.google.com/p/bitly-api/wiki/ApiDocumentation
  [http://code.google.com/p/redis/wiki/CommandReference]: http://code.google.com/p/redis/wiki/CommandReference
  [many use cases]: http://www.paperplanes.de/2010/2/16/a_collection_of_redis_use_cases.html
  [http://bitbucket.org/tarek/urltotwit/src/tip/shortener/shortener/urlstore.py]:
    http://bitbucket.org/tarek/urltotwit/src/tip/shortener/shortener/urlstore.py
  [**Bottle**]: http://bottle.paws.de/
  [http://bitbucket.org/tarek/urltotwit/src/tip/shortener/shortener/main.py]:
    http://bitbucket.org/tarek/urltotwit/src/tip/shortener/shortener/main.py
  [http://ted.mielczarek.org/code/mozilla/extensionwiz]: http://ted.mielczarek.org/code/mozilla/extensionwiz
  [http://ted.mielczarek.org/code/mozilla/xuledit/xuledit.xul]: http://ted.mielczarek.org/code/mozilla/xuledit/xuledit.xul
  [http://bitbucket.org/tarek/urltotwit/src/tip/urltotwit%40tarek.ziade.org]:
    http://bitbucket.org/tarek/urltotwit/src/tip/urltotwit@tarek.ziade.org/
  [Gawel]: http://a.pwal.fr/
  [avid'Bgk]: http://code.welldev.org/bgk/src
