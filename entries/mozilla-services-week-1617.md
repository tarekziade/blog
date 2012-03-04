Title: Mozilla Services, week 16/17
Date: 2011-05-02 16:43
Category: mozilla, python

What's this ? read [this post][].   
### What happened

  
I took a bit of vacation and came back last week. I took a lot of
pictures and I love [this one taken at the Amneville Zoo near Metz][]. I
was quite amazed by the quality of this Zoo by the way.   
#### Share Server (F1)

  
We're continuing our work to get the F1 server ready, and Rob Miller,
who joined last month (yay!) is helping me in this task. We're working
on:   
-   removing the Pylons layer and using our own WSGI micro-framework
    like in other Services Apps -- since the F1 server is just a small
    oauth proxy, that should depend on nothing else than the library for
    every service (GMail, Twitter, etc.)
-   setting up the Services Status DB. This is explained here:
    [https://wiki.mozilla.org/Services/F1/Server/ServicesStatusDB][].
    Basically this will let us turn on and off the proxy for a given
    service
-   continuing the *Grand Split*. The static web pages are now living on
    their own.

  
The Services Status DB involved some research/brainstroming with Shane,
on the best way to do it, and we decided we would:   
  
1/ Use Membase to store the status of every service. Membase provides
[vbuckets][] and has a really nice web managment interface to
add/remove/modify the cluster. Pylibmc and libmemcached do not
understand vbuckets yet, but I am working on it.   
  
2/ Reject calls at the Nginx level when the service is down. I first
wrote a [NGinx module in C][] but we will not use it. The problem with
NGinx modules is that everytime you change them you need to recompile
and redeploy Nginx. *Meh*. Instead, as I was suggested in the Nginx
mailing list, we're adding the Lua module in Nginx, that will allow us
to script the behavior we want from within the Nginx config files.   
#### Documentation

  
Hey check this out : [http://docs.services.mozilla.com][].   
  
This is the sweet documentation center I've set up for Mozilla
Services. I have started to add more content about each one of our
Service, basically extracting what we have here and there in our wiki. I
am trying to follow a similar pattern for each one of them.   
  
While wikis are awesome to work collectively on specs, I love
[Sphinx][] because it makes it so easy to consolidate documentation for
a project, and share a glossary, terms, definitions etc. And the
documentation is treated like code, all in an Hg repository here:
[https://hg.mozilla.org/services/docs/][]   
  
There's a lot of content to gather from various places in the wiki(s)
in order to build a complete list of our services, but the idea is to
add documentation there once the API has stabilized.   
### What's planned

  
More Share Server work. I will also try to push on more docs.   
  
Also there's a new side project I've started that might be interesting
to share here, I will try to blog later in the week about it. In a few
words: it's a tool that should help [MoPy][] people to share knowledge
and try to maximize cross-team reuse of code when possible.

  [this post]: http://tarekziade.wordpress.com/2010/11/30/rsync-mozillaservices-community-week-47/
  [this one taken at the Amneville Zoo near Metz]: http://bit.ly/irH6AC
  [https://wiki.mozilla.org/Services/F1/Server/ServicesStatusDB]: https://wiki.mozilla.org/Services/F1/Server/ServicesStatusDB
  [vbuckets]: http://dustin.github.com/2010/06/29/memcached-vbuckets.html
  [NGinx module in C]: https://bitbucket.org/tarek/nginx-sstatus/overview
  [http://docs.services.mozilla.com]: http://docs.services.mozilla.com/
  [Sphinx]: http://sphinx.pocoo.org
  [https://hg.mozilla.org/services/docs/]: https://hg.mozilla.org/services/docs/
  [MoPy]: https://wiki.mozilla.org/MoPy/
