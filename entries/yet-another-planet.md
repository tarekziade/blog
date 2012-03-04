Title: Yet another Planet
Date: 2008-09-04 21:20
Category: atomisator, python

[Atomisator][] is a framework so it is hard to get an idea of its
features until a real application uses it.   
  
That is why I wrote a small application in Pylons called [Yap][] (Yet
Another Planet), that is basically displaying the XML file produced by
an Atomisator instance. Since Atomisator does all the work, the Pylons
apps is really small (one or two controllers, that's it).   
  
My first use case was to produce a nice, smart Planet for our user
group [Afpy][].   
  
Here's a first draft: [http://ziade.org/afpy/][]   
  
You can play with 'j', 'k' and arrows to open and close posts, but I am
still working on this, so it will also scrolling the window when you are
on a post.   
  
Anyways, it grabs various French sources for Python and uses these
plugins from Atomisator:   
-   filter : reddit
-   filter : delicious
-   filter : doublons
-   enhancer : related
-   enhancer : digg

  
The result is basically following reddit and delicious links to display
an extract of the page linked, and display digg comments as well.
Duplicate are removed as well. A list of related entry are also added to
each entry.   
  
It is based on this configuration file, Atomisator uses to generate an
XML file for Yap in a cron:   
   [atomisator]



    sources =

        rss     http://del.icio.us/rss/tag/python+fr    Delicious

        rss     http://www.afpy.org/search_rss?portal_type=AFPYNews&sort_on=Date&sort_order=reverse&review_state=published Afpy News

        rss     http://feeds.feedburner.com/Baderlog/python Bader

        rss     http://www.biologeek.com/journal/rss.php?cat=Python Biologeek

        rss     http://www.gawel.org/weblog/rss/python/afpy/zope/zope3/rss.xml  Gawel

        rss     http://www.haypocalc.com/blog/rss.php?cat=Python    Haypo

        rss     http://jehaisleprintemps.net/blog/rss/  No

        rss     http://programmation-python.org/sections/blog/exportrss Tarek

        rss     http://api.blogmarks.net/rss/tag/python,fr  Blogmarks



    # put here the database location

    database = sqlite:///afpy.db



    # this is the file that will be generated

    file = /home/tarek/www/packages/Yap/trunk/yap/public/afpy.xml



    # infos that will appear in the generated feed.

    title = Planet Python Francophone

    description = Le planet de l'Association Python Francophone, et des gens heureux.

    link =  http://www.afpy.org/planet/



    filters =

        reddit

        delicious

        doublons



    enhancers =

        related

        digg

  
### What's Next ?

  
Since now, there were no attempt to try to automatically classify
entries. The next plugin I am working on will provide a Naive Bayesian
filter to classify entries, together with a way to train it through the
Yap web interface. basically a 'keep'/'ditch' button.   
  
I will also set an english Planet Python to see how things go with more
sources.

  [Atomisator]: http://atomisator.ziade.org/
  [Yap]: https://svn.afpy.org/misc/atomisator.afpy.org/packages/Yap/trunk/
  [Afpy]: http://afpy.org
  [http://ziade.org/afpy/]: http://ziade.org/afpy/
