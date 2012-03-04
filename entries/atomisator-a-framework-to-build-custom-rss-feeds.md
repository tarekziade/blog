Title: Atomisator, a framework to build custom RSS feeds
Date: 2008-08-20 16:56
Category: plone, python, zope

We are all overwhelmed by the amount of data in our feed readers. While
this problem is unavoidable if you keep on adding new feeds in it, they
could be automatically filtered and categorized to reduce the flow of
data.   
  
I wanted for a long time to try out some custom filters over my feeds
to find for example related entries, by trying to understand the meaning
of the posts, using tools like [NLTK][].   
  
So I needed a playground for this, where I could play with feeds.   
  
I think the closest tool for this is to use [Yahoo Pipes][] but as far
as I know, the only way to create custom filters is to run a web service
and call it from Yahoo Pipes.   
  
Anyways, I started to code a framework (at first it was an example for
[my latest book][]) that looks a lot like Yahoo Pipes in its principles.
I don't have any User Interface at this time of course, but a simple
plugin-based tool that will let me combine my code snippets with feeds.
  
  
It is called Atomisator (see [http://atomisator.ziade.org][]).   
  
[caption id="" align="alignnone" width="539" caption="The big
picture"][![The big picture][]][The big picture][/caption]   
  
The process is quite simple:   
1.  **Readers** are plugins that know how to read a source and provide
    entries out of it.
2.  **Filters** are plugins that know how to remove unwanted entries, or
    enhance them (change their title, summary, etc.). They can be
    combined.
3.  the entries are then pushed in a database. This is useful to avoid
    doublons, and to keep track of past entries.
4.  to create the feed, the entries are read from the database
5.  **Enhancers** are plugins that will add to entries extra info.
    Typically info that can't be stored, like Digg comments if the entry
    is detected on Digg, or Google related searches, and so on
6.  The feed is then generated.

  
Right now I am focusing on making it fast, which is not simple because
the plugins can play with all entries in the database.   
  
It is in early stage and undertested, but it kinda works. I pushed it
at PyPI to see of it meets interest. If it does, I will document the
process of writing plugins.   
  
Make sure you have SQlite installed, and give it a try :   
   $ easy_install atomisator.main

  
   $ atomisator -c atomisator.cfg

  
   $ atomisator

  
You will have an atomisator.xml feed created. You can add other feeds
in atomisator.cfg as well and try them.   
  
Now with this environment, I can start to try out custom algorithms
over my feeds.   
  
I've been told the name doesn't sound right in Ehglish, but it does in
French so I keep it ;)

  [NLTK]: http://nltk.sourceforge.net/
  [Yahoo Pipes]: http://pipes.yahoo.com/pipes/
  [my latest book]: http://tarekziade.wordpress.com/2008/08/08/a-new-python-book-expert-python-programming/
  [http://atomisator.ziade.org]: http://atomisator.ziade.org
  [The big picture]: http://www.ziade.org/atomisator/atomisator.png
