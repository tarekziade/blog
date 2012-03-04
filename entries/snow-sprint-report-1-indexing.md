Title: Snow sprint report #1 : indexing
Date: 2008-01-20 23:25
Category: plone, python, sprint, zope

So we are here in Austria, sprinting on Zope and Plone (thanks to
[Lovely Systems][]). I have proposed a task on building an alternative
indexer system for Plone. So, we worked with Dokai and Tom on this.
Those guys rock, really !   
  
Our goal was to create a plone 3 buildout that provides an out of the
box solution.   
### Background

  
Let me give you some background about indexing in Zope before
presenting our work. The default indexing system is quite effective, as
long as your instance is not getting too big. Some years ago, we had to
create an alternative indexer for CPS at Nuxeo, that would externalize
the catalog because we figured out that :   
-   50% of the size of the ZODB was the catalog (I am talking about
    gigas here)
-   50% of the time on object creation was taken by indexing tasks, and
    was getting quite slow as the instance was growing.

  
Those values are approximate, but quite near the reality back then (I
know some people worked on making indexing better on Zope lately).   
  
Julien then wrote a XML-RPC server that would take care of the indexing
tasks and reply to queries. The software behind it was Lucene, together
with [PyLucene][]. The overall solution was quite good, beside the pain
we had to install it on some specific Linux back then.   
  
Anyway. What did Julien some years ago exists now and is called
[Solr.][] I also had some experiences a while ago with [Xapian][] (as
Sidnei did too), which is quite efficient too, and easier to use from
Python (see [here][])   
### Solr, Xapian

  
So the first task to do was to decide what to use. I called Alan from
[Enfold Systems][] because the guys over there have been working on the
topic for years.   
  
As a matter of fact, they have created a package for Python that bind a
Solr server.   
They also have a Plone integration that provides an utility to index
content on Solr.   
Since the guys are releasing all of this very soon as open source, we
decided   
to go with this solution for the sprint.   
  
It is not a technological choice (Lucene) because Alan and some guys
from   
Lemur are actually considering a drop-in replacement for Solr based on
Xapian.   
  
In other words, the work done will be compatible with both Lucene and
Xapian technologies. Xapian is pretty interesting since it avoids
deploying Java ;)   
### The sprint task

  
The task was quite "simple" since the Enfold guys did all the hard work
:)   
So we worked on:   
1.  a buildout that builds a Solr server and launches it
2.  a Plone integration to use Solr seamlessly

  
### The buildout

  
The buildout done and usable (We tried it under Windows, MacOSX and
Debian)   
It uses new recipe we wrote:   
  
- [collective.recipe.an][]t : build Java softwares using ant   
- c[ollective.recipe.solrinstance][] : builds a Solr instance and
provide a script to launch it   
  
If you want to try it, here's (roughly) how (comment the blog entry in
case of a problem)   

    $ svn co https://svn.enfoldsystems.com/public/enfold.solr/branches/snowsprint08-buildout buildout

    $ cd buildout/plone-3.0.5/

    $ python2.4 bootstrap.py

    $ bin/buildout -v

    $ bin/solr-instance &     <-- launches solr (python bin\solr-instance under Windows

    $ bin/instance fg         <-- launches Zope

  
Then, on Zope, install SolrIntegration in the quick\_installer. The
next document you will publish will be indexed on Solr side, and
searchable with the search box.   
  
The portal\_catalog remains though, so it is indexed twice ;) you can
empty it to check   
Solr is acting right.   
### Plone integration

  
The last part we need to work on is to make the SearchableText index
100% Solr based. Whit advices us to create a storage for TextIndexNG so
that's where we are heading on (should be done tomorrow hopefully)   
  
We would also like to do some benchmarks to compare the speed and ZODB
size. We will   
probably use [Jmeter][] for this.   
  
I would like to thank Alan, Leonardo, Sidnei for their work on this
area, and for releasing it as open source: I really believe that it will
become a great indexing solution for Plone in the next months. I was
really waiting for this momentum in indexing in the Plone community.

  [Lovely Systems]: http://www.lovelysystems.com/
  [PyLucene]: http://pylucene.osafoundation.org/
  [Solr.]: http://lucene.apache.org/solr/
  [Xapian]: http://xapian.org/
  [here]: http://tarekziade.wordpress.com/2007/06/12/indexation-service-with-xapian/
  [Enfold Systems]: http://www.enfoldsystems.com/
  [collective.recipe.an]: http://svn.plone.org/svn/collective/buildout/collective.recipe.ant
  [ollective.recipe.solrinstance]: http://svn.plone.org/svn/collective/buildout/collective.recipe.solrinstance/
  [Jmeter]: http://jakarta.apache.org/jmeter/
