Title: $ rsync mozilla/services community week #47
Date: 2010-11-30 14:49
Category: mozilla, python

## What's that ?

  
The various weekly updates the Mozilla projects are a good way to
follow, from a ten thousands foot point of view, what's going on   
  
I'd like to do my own contribution and launch my own weekly update,
about the work we are doing in my team (Mozilla Services) and in
particular everything related to Python. I'll try to keep it biased and
say good things about Python and bad things about PHP and Perl ;).   
  
More seriously, I think that's a good way to sync with the community
for the ones who cares about Python and Mozilla, and get some feedback.
Especially since the services we build are not direct end-user products
for people out there. Although, they play an important role in the
background. For instance, to store and retrieve your encrypted bookmarks
via the Firefox Sync add-on, you are calling our Services.   
  
I'll keep those reports short and synthetic and I'll leave it up to the
readers to ask for more details on specific points. I will try not to
use internal technical jargon.   
## Week 47

  
** [Easy Setup on new devices][] **:   
-   The [server-side][], using memcached & Python is ready. It's now
    deployed on stage using [Nginx][] and [Gunicorn][], and the security
    team is now reviewing it.
-   I worked with Richard to deploy it through rpms. The [pypi2rpm][]
    script I wrote now works well and creates a RPM out of any project
    released at PyPI, with the right options for CentOS.

  
**Firefox Sync in Python**:   
-   Rysiek (from Poland) now successfully use the server with his LDAP
    and Postgres setup, after we worked on adding options for him.
-   Ian reviewed the code of [server-core][] and I followed up with a
    few fixes.
-   Toby is now using it as well in the new project he works on, and
    gave me some feedback on the provided APIs. We fixed a few things to
    make his life easier

  
**OpenID **:   
  
I have started a [prototype][] of an OpenID server for Services. It
works now with all websites I know of, that consume Openid. It uses
[Redis][] to store the association handles and the sites tokens. For the
protocol implementation, I've first used [python-openid][] but I ended
up doing custom code. python-openid is great but a bit over-engineered
for what I need to do on server-side. Although, one really useful
feature in this project is in its examples/ folder: a client application
you can use to test your server, and vice-versa.   
  
The client part in Firefox is a[custom weave-identity][] add-on that
automatically performs the authentication on the openid server, and
removes all manual steps you need to authorize a site. It replaces the
input text where you usually type your open id identity, with a "sign
in" button.   
## Next Week Plans

  
Well, this week as of yesterday :)   
-   **Easy Setup**: Will follow Richard and Michael work on deployment
    and reviews and help them in case there's an issue
-   **Sync**: more reviews planned, need to write doc for sync-core
-   **OpenId**: need to write the script for benchmarking the server
    using [Funkload][].
-   more things !

  [Easy Setup on new devices]: https://bugzilla.mozilla.org/show_bug.cgi?id=601644
  [server-side]: http://hg.mozilla.org/services/server-key-exchange/
  [Nginx]: http://nginx.org
  [Gunicorn]: http://gunicorn.org/
  [pypi2rpm]: http://pypi.python.org/pypi/pypi2rpm
  [server-core]: http://hg.mozilla.org/services/server-core/
  [prototype]: http://bitbucket.org/tarek/server-openid
  [Redis]: http://code.google.com/p/redis/
  [python-openid]: http://pypi.python.org/pypi/python-openid/
  [custom weave-identity]: http://bitbucket.org/tarek/weave-identity
  [Funkload]: http://funkload.nuxeo.org/
