Title: A PostRank plugin for Atomisator
Date: 2008-12-07 11:54
Category: atomisator, pycon, python

Yesterday, I bumped into [PostRank][]. This system is collecting data
from various social systems like Twitter and provides a service where
you can type in an url of a blog post or a entire blog. You get a
PostRank depending on the popularity of the URL.   
  
I wrote a plugin for Atomisator and ran it on my own blog. Here's the
result: [http://ziade.org/afpy/][]   
  
And the Atomisator configuration for this is :   
   [atomisator]

    sources =

        rss http://tarekziade.wordpress.com/feed/atom/



    database = sqlite:///carpet.db



    outputs =

        rss  public/rss.xml "http://tarekziade.wordpress.com/feed/atom/" "Carpet Python with PR" "Powered by Atomisator"



    enhancers =

        postrank

  
### How PostRank works

  
PostRank works with urls you provide, on their web interface or through
their web services.   
  
As long as these url are present in their big cloud-computing based
system, they provide a rank that is calculated with the number of
comments related to the blog, the number of tweet messages that refers
to it, and so on. The complete algorithm they used is secret but this is
not the point. I have secret algorithms too ;).   
  
The point is that they are trying to categorize blog entries using
social networks as indicators, and that they have a huge database.   
### Social indicators in Atomisator

  
This is one of the approach I have with [Atomisator][], when it is used
to build a planet. For instance I have a Digg plugin that will inject in
each entry the comments found on Digg if the entry was digged. It also
present the number of Digg. Of course this is done live because I don't
have a cloud-computing based system where I store data. I use Digg
webservice on the fly. (On the fly here doesn't mean Atomisator make the
calls to Digg from the Planet application of course. It means Atomisator
calls them when it creates the merged feed on the system)   
  
The benefit of this approach is that I can provide a social indicator
on a post immediatly. Systems like PostRank will not work on entries
that are too recent because their spiders have a lag of one week or so.
  
  
The pitfall of my approach is that I am unable to calculate trends
because I don't store the indicators as they vary.   
  
But if someone wanted to build a BtoC application using Atomisator,
they could implement a set of plugins based on Amazon tools to make them
store data in a more scalable way and in time.   
### Next steps

  
So I have this new PostRank plugin, and this is awesome because I have
added a treshold parameter in it. Basically if a post has a high
PostRank value, it will appear in the Planet. If it's low, it can be
automatically removed. The fact that PostRanks are lagging for new
entries is not a problem: interesting posts will eventually pop after a
few days in the Planet.   
  
This is perfect to reduce the number of entries in an aggregator.   
  
But I do want to write my own PostRank that works live, with no storage
at all. **Because the whole point of Atomisator is to provide a
framework where anyone can try out various filtering combinations**.   
  
So to be able to provide this power, it needs to work just by
collecting data directly from the social services, like the PostRank
plugin does with this PostRank "meta-service". The next step is
therefore to see if I can query services like Twitter to list the twits
related to an url, without having to store the twitter feed myself.   
  
In any case, if my talk on Atomisator at Pycon 2009 is selected, the
PostRank plugin will be shown besides the Digg plugin.

  [PostRank]: http://www.postrank.com/
  [http://ziade.org/afpy/]: http://ziade.org/afpy/
  [Atomisator]: http://atomisator.ziade.org/
