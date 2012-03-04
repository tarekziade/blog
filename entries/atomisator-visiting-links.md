Title: Atomisator, visiting links
Date: 2008-08-27 19:50
Category: atomisator, python

I am writing a plugin for [Atomisator][] that detects when a post is a
[Reddit][] or a Delicious entry, and adds a sample from the page it
links to.   
  
On a Reddit feed for example, you will basically get a meaningful
title, and summary that will look like this:   
   [link] [comments]

  
This is not really useful in a feed...   
  
So basically, the plugin I am writing is detecting this kind of entries
and is grabbing a sample out of the linked page, so the entry is
transformed like this:   
   Extract from the link:

  
       ... blablablba

  
       blablabla...

  
   [link] [comments]

  
The extracted text is a pure text, extracted using [BeautifulSoup][]
and the SGML parser from the standard library.   
  
This is quite useful as long as the begining of the web page is
meaningful, which is rarely the case... Most of the time the web page
starts with a gibberish text, like a menu bar content for instance.   
  
So I am trying to detect what is the "best" part of the web page
pointed by the link.   
  
To do so, I am using the title of the entry, which is suppose to make
sense. Since there are good chances the text will contain the words used
in the title, I am looking for them into the page.   
  
I have tried several combinations, even by trying to find the smallest
sample where I get the maximum number of words from the title by doing
some cartesian products. But this was too slow.   
  
Instead, I am trying to detect the real beginning of the post by trying
some common patterns : most of the time the body of the post is a div
tag with a class attribute like body, content, article-content, etc..   
  
I am running it now over the [Python feed at Reddit][], and the results
start to look nice so far (==you can understand what the page talks
about most of the time). See
here:[http://www.ziade.org/atomisator/filtered.xml][]   
  
Now I will try to run it over a fair amount of entries and with various
sources to try to tune up the extractor.   
  
This code will also be a useful base to visit links of any kind of
entry, but it needs a lot of cleanup: I have spotted some quadratic
complexity parts I need to get ridd of.   
  
**Try it yourself :**   
1.  make sure you have SQLite installed
2.  install atomisator with easy\_install atomisator
3.  create your atomisator.cfg file with the content below
4.  then run it by calling 'atomisator' in the folder atomisator.cfg
    lives

  
atomisator.cfg content :   
   [atomisator]

    sources =

        rss http://www.reddit.com/r/Python.rss reddit



    database = sqlite:///atomisator.db

    file = atomisator.xml

    title = Meta feed

    description = Automatic feed created by Atomisator.

    link =

    filters =

        reddit

  [Atomisator]: http://tarekziade.wordpress.com/2008/08/20/atomisator-a-framework-to-build-custom-rss-feeds/
  [Reddit]: http://www.reddit.com/
  [BeautifulSoup]: http://www.crummy.com/software/BeautifulSoup/
  [Python feed at Reddit]: http://www.reddit.com/r/Python.rss
  [http://www.ziade.org/atomisator/filtered.xml]: http://www.ziade.org/atomisator/filtered.xml
