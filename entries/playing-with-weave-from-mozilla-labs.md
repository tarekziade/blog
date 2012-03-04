Title: Playing with Weave from Mozilla Labs
Date: 2010-03-27 23:12
Category: python

Mozilla Labs has launched an interesting project called Weave some times
ago. The idea is to provide an online service where your Firefox
instance can save personal data, like bookmarks or passwords. You can
grab a Firefox Add-On here and get started :
[http://mozillalabs.com/weave/][]   
  
[![Weave Logo][]][]   
  
The personal data is encrypted by Firefox using a scheme based on AES
256 and private/public keys. See
[https://wiki.mozilla.org/Labs/Weave/Developer/Crypto][] for more
details.   
  
The Weave protocol is quite simple and is documented here
:[https://wiki.mozilla.org/Labs/Weave/API][], and I have seen some
Python implementations around for the server-side. Although Mozilla's
implementation for their Firefox service looks like it's in PHP right
now.   
  
Mozilla also provides [a small Python client][] for the protocol, which
can be used to get and set data to a Weave server:   
  
I was curious about Weave so I started to play around with the Python
client, and ended up [cloning it on Bitbucket][], to add a few things to
try it out. The original code in Mozilla's repository is not packaged
(yet) and you just get a few Python modules. Although it has a command
line that will let you grab some data from the server, but I wanted to
try it out from my code.   
  
So I've made it an installable Python package in my clone so I could
install the client with Pip or easy\_install.   
  
Then I wrote a small class to try it to get my Firefox bookmarks:   
   import json

    from weave.client import WeaveStorageContext, WeaveCryptoContext



    _DEFAULT_SERVER = 'https://auth.services.mozilla.com'



    class WeaveClient(object):



        def __init__(self, user_id, password, passphrase, server=_DEFAULT_SERVER):

            self.storage = WeaveStorageContext(user_id, password, server)

            self.crypto = WeaveCryptoContext(self.storage, passphrase)



        def _deserialize(self, payload):

            return json.loads(self.crypto.decrypt(json.loads(payload)))



        def get_bookmarks(self):

            for bookmark in self.storage.get_items('bookmarks'):

                bookmark = self._deserialize(item['payload'])[0]

                if bookmark['type'] != 'bookmark':

                    continue

                yield bookmark['title'], bookmark['bmkUri']



    if __name__ == '__main__':

        client = WeaveClient('tarek.ziade', 'password', 'passphrase')

        for title, url in client.get_bookmarks():

            print title, url

  
  
Here, a storage context class and a crypto context class are created
with my login information, and the get\_items() API gives me back a list
of encrypted bookmarks. Weave organizes its data into collections, and
bookmarks is just a label for one collection. There are other
collections ([see
https://wiki.mozilla.org/Labs/Weave/Sync/1.0/API\#Collections][]), but
Weave could be used to store and retrieve any kind of data.   
  
If you want to replay my example, or play with the client, you can
install it using my bitbucket repository like this:   
   $ pip install http://bitbucket.org/tarek/python-weave-client/get/tip.gz

    or

    $ easy_install install http://bitbucket.org/tarek/python-weave-client/get/tip.gz

  
Beware that this is not a release, just my custom clone :). But I'll
probably ping the author to see if he has any interest in packaging his
modules like I did, so we get it at PyPI.   
  
What I am really looking forward about Weave now is how the project is
going to grow and securely handle millions of user's data. This will
probably end up in a very interesting infrastructure, with some
similarities with projects like Dropbox or [Tahoe][].

  [http://mozillalabs.com/weave/]: http://mozillalabs.com/weave/
  [Weave Logo]: https://services.mozilla.com/images/weave-logo.png
    "Weave Logo"
  [![Weave Logo][]]: https://services.mozilla.com/
  [https://wiki.mozilla.org/Labs/Weave/Developer/Crypto]: https://wiki.mozilla.org/Labs/Weave/Developer/Crypto
  [https://wiki.mozilla.org/Labs/Weave/API]: https://wiki.mozilla.org/Labs/Weave/API
  [a small Python client]: http://hg.mozilla.org/labs/weaveclient-python
  [cloning it on Bitbucket]: https://bitbucket.org/tarek/python-weave-client/
  [see https://wiki.mozilla.org/Labs/Weave/Sync/1.0/API\#Collections]: //wiki.mozilla.org/Labs/Weave/Sync/1.0/API#Collections
  [Tahoe]: http://allmydata.org/~warner/pycon-tahoe.html
