Title: Plone Conference 2008 in Washington D.C. - summary
Date: 2008-11-06 16:54
Category: conference, plone, python, zope

I am back from the Plone Conference in D.C., and the jetlag is gone. The
jetlag is gone for weeks now but it's hard to find the time to blog
these days :/   
## On the talks I have seen and topics I have chatted about

  
There were a lot of great talks in D.C., and it was hard to decide
which one to look at. In any case it was easy to meet the speaker if I
had missed the talk, because the Plone Conference, unlike big
conferences like OSCON, is a place where everyone hangs around the same
spot after a talk is over.   
  
Here's a list of some topics I have seen or I have talked about with
some people.   
### Deliverance - Ian Bicking

  
If you look at what Ian has produced in the past 5 years, he is one of
the most prolific contributor of tools that become standards in the
Python web development web community. Think about Python Paste or
virtualenv, and many others. Deliverance might be the next big one.   
  
Take a bunch of micro web applications you want to join to build a full
web system, for historical reasons or just because you believe a
particular feature just won't fit in Plone but will do great in Pylons.
  
  
Now ask a designer to glue everything together under the same look. He
(or the guy that integrates his design) will probably hates you: he will
have to learn how to integrate in heterogeneous environments. This is
easy under some systems that let you stick a layout and a css in a
simple way. This is not easy under Plone, unless you learn how to do it
(but this will be improved in the future).   
  
Deliverance is a proxy that let you skin any application that spits
html content, by running some XPATH rules on the content and applying
some changes to produce a new output. Basically, you have a simple html
page that just provides the layout you want to have, without any
content, and a xml file that explains how to extract some content from
the page produced by the third-party application and where to inject it
in your empty html page. The great thing is that you can call different
third-party servers given the path you are in, and even call several
servers to build one single page. This opens a lot of perspectives.   
  
The first caveat of this approach is that you have to provide a
Single-Sign On feature to avoid people having to connect several times.
This can be a problem sometimes with some applications if they are not
open enough to let you do it. But most of the time, it is not a problem
: if the users are all located in a LDAP it is easiy.   
  
Furthermore, if you use only Python-based applications, you can use a
WSGI envrionment and a middleware like repoze.who to glue together let's
say, a Plone app and a Pylons app. Products.oopas is the PAS plugin that
can be used for that on Plone side to grab the authentication context
and use it.   
  
The second problem I can see is about response headers. One example: if
a page is composed of elements that comes from several pages, and if the
page has a Last-Modifier header, I don't think Deliverance handles this
correctly yet, to make sure to present the newest Last-Modified header
from all third-party servers that where called to build that page. But
this more likely to be a detail compared to the single authentication
problem.   
  
In any case this is a very promising tool !   
### Content Mirror - Kapil Thangavelu

  
I didn't see that talk, but I have talked about this tool with a few
people. The idea is to serialize the content of a Plone instance into a
relational database (eg Postgresql), as it happens, using events.   
  
I need to give a try and check it deeper, to see how the overhead is
dealt, and how the aggregator I have read about is doing (it collects
mirorring operations to perform in a transaction, and optimize the calls
at the end of the transaction to avoid redudant calls if I understood
correctly). I don't know yet for example if there's a pool of jobs for
the mirroring tasks to avoid a point of failure. But I am pretty sure
this is taking care of. The other point I need to see if there's a round
trip. e.g. if there's a way to apply a relational database change back
into Plone.   
  
But in any case I can already see various use cases for my customers.
For instance, having a plone instance as a back office, with complex
workflows for editors and contributors, and a lightweight Pylons
application as the front application, that concentrates into displaying
the relational database as fast as possible, makes a lot of sense in big
environments. It just scales better.   
  
So this is a interesting tool as well.   
### repoze.bfg - Chris McDonough

  
Chris gave a talk about repoze.bfg, which is a new web framework that
takes back the good bits from Zope and push them into a WSGI world,
using the Pylons approach I would say. That is : "here's the template
engine you can use in repoze, but really, use the one you like".   
  
Frankly, I am really seeing this new effort as one of the most
promising one in the Zope community. Already, repoze.auth is a major
middleware in WSGI : Zope's Pluggable Authentication Service outside
Zope, usable with any WSGI application. This is a blast !   
  
And people are starting to contribute a lot of interesting middlewares
under the repoze namespace.   
  
Now I didn't really try repoze.bfg itself yet, but given the people
that are behind it, I am pretty sure this framework will meet success in
the future. Having a MVC framework ala Pylons that let you use Zope
packages with a "this zope package is repoze/wsgi compliant" label on
each one of them is very cool.   
### collective.indexing - Andreas Zeidler and al

  
At the snow sprint, we worked with the Enfold crew that did a great
work in integrating the Solr/Lucene system so it can be used from Plone.
We replaced a few fields like the searchable text and indexed it on Solr
side, just to give it a try. The snow work was really focusing on
providing a buildout, a few recipes and a bench to say : "Hey, Plone
community, this is a blast ! let's do more of it"   
  
Later Andreas Zeidler and a few other guys continued the work on
indexing matter and they delivered collective.indexing, which provides
two things:   
-   a queue that collects all indexing to be done, and optimize the call
    to the catalog
-   a bridge to use collective.solr

  
I didn't follow the latest development and I didn't know how far the
guys went, but I had the chance to hang around with Andreas and Tom
Lazar in D.C., so now I know that this package is production ready :D   
  
So in other words : I'll probably use it as a mandatory package for all
the big plones out there.   
  
The queuing part imho, should go into the catalog itself because
there's no other way to make sure a third-party product is not calling
the catalog during the transaction wile another product does the same.   
### Server-Side Include (SSI)

  
Tom Lazar worked during the Snow Sprint on lovely.remoteinclude to make
Plone portlets accessible via unique URLs. From there, it is possible to
push a page that contains a list of urls rather than the calculated
page, to a front server that knows how to read SSI directive, and builds
the page.   
  
This is great for performances, and is a lot like ESI (Edge Side
Include) we use to have in CPSSkins.   
  
I am wondering if both could be implemented in the same tool in fact.   
  
Tom told me that he will try to continue this work at the performance
sprint in Bristol in december, so let's keep an eye on this !   
  
*I have seen many other talks and topics, but these few ones where the
ones I really needed to talk about.*   
## On the conference organization

  
I am helping in the organization of Pycon FR in Paris since 2 years
now. I know what is means to organize such events : it is a LOT OF WORK.
  
  
**You know when an event is well organized when you don't feel it is
organized. **   
  
That was the case in D.C. Bravo Alex, Amy and all the others !   
  
The only problem (wifi) was not the organizers fault, and I have never
been to any event where it is not cahotic at some point (besides OSCON)
so... :)   
## On the community

  
I love you all guys. It is an amazing community.
