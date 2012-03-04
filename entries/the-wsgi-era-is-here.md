Title: The WSGI era is here
Date: 2008-09-19 11:30
Category: plone, python, zope

This is probably obvious for the people that uses [Repoze][] or
[Pylons][], or early adopters in the [Plone][] world, but from a Plone
or a Zope developer perspective, you could live without it until now.   
  
Now [WSGI][] is everywhere.   
  
I remember when Martijn Faassen brought the idea in 2006, of [hooking
Grok and Zope 3 into the WSGI][]. Maybe someone else talked about it
before but that was the first time I could picture what WSGI could
bring.   
  
Now with the work done by people like:   
-   The repoze team, that made it easier to run a Plone-based
    application in WSGI
-   The [Paste Script / Paste Deploy][] team, that provided a simple way
    to describe a WSGI chain

  
And major WSGI middlewares like :   
-   [repoze.who][] which allows you to deal with authentication
    separately
-   [Deliverance][], which let you theme any application and let this
    application focus on delivering a content
-   Things like [Beaker][], which let you use memcached for instance, to
    store session data and cache arbitrary things

  
From a CTO point of view, a WSGI environment brings me the ability to
think about a web application and build it without having to stick into
one framework and try to bend all technologies inside it.   
  
For instance:   
-   I can write a Plone application and use Beaker to deal with
    sessions, without having to wrap Memcached into a custom plone
    package.
-   I can ask a graphic designer to work on a CSS and a layout without
    having to do it into Plone. It's not that Plone design tools are
    bad, but the learning curve of writing a rule file in Deliverance
    and apply it to any piece of application makes the designer more
    productive than becoming a specialist of one skinning tool.

  
-   If my customer use [moinmoin][] as a Wiki, I can put it into my
    Plone site transparently by defining a composite section in my Paste
    configuraton file.
-   ...

  
You could do all the mentioned thing without WSGI, just by importing
the packages and/or dealing with proxies at Apache level. But that is
not the point.   
  
The point is that WSGI brought the idea of making all web frameworks
and libraries interact together to build one web application.   
  
It is not the silver bullet of course, but my gut feeling is that this
will create some kind of reunification in Python Web development
communities: people are starting to look at a wider range of package,
beyond the framework they use everyday.

  [Repoze]: http://repoze.org/
  [Pylons]: http://pylonshq.com/
  [Plone]: http://plone.org/
  [WSGI]: http://www.wsgi.org/wsgi/
  [hooking Grok and Zope 3 into the WSGI]: http://faassen.n--tree.net/blog/view/weblog/2006/11/29/0
  [Paste Script / Paste Deploy]: http://pythonpaste.org/script/
  [repoze.who]: http://static.repoze.org/whodocs/
  [Deliverance]: http://www.openplans.org/projects/deliverance/project-home
  [Beaker]: http://pypi.python.org/pypi/Beaker
  [moinmoin]: http://moinmo.in/
