Title: How to prevent drowning in the huge rss daily feed you receive
Date: 2006-11-06 19:32
Category: buzz, datamining, marketing, python, rss, zope

Feeds, feeds, feeds everywhere. I can't keep up with all incoming data.
**I am drowned** !   
  
I thought digg and similar services would help me on this, but it just
raised the problem on a meta-level.   
  
It takes me at least 20 minutes per day to:   
-   Remove duplicates entries
-   Look over hundreds of entries to select the one that worth a
    reading, by looking at the title, the origin and the tags. (80% of
    the time)
-   Read my selection, and even though I know this will make it worse,
    add news feeds I've found from my selection.

  
I had to automate some of this daily activity. **I had to cut off this
huge amount of data** and to get closer to what I needed to read.   
  
But how ?   
  
First of all, let's analyze a bit what a feed reader wants. It can be
resumed in two things:   
-   She wants to get the best news on her field of interest, out of a
    huge list of rss feeds.

  
-   She wants to keep an eye on what's going on out there, and make her
    field evolve with some indexes.

  
Most of the work can be done by pieces of software. I think this is
called webmining but I am not an expert. Webmining would be a part of
[Datamining][]. But let's cut off the big words: **a couple of Python
script can do the job**.   
  
That's **"Atomisator"** job !   
  
![Atomisator][]   
  
*Atomisator* grabs multiple feeds out there, removes duplicate news by
using the distance of [Levenshtein distance][], and create a new feed
out of it.   
  
It also provides a way to filter up entries on the fly, by looking at
each entry content. Simple filters for instance, will validate an entry
if it contains certain words. The filtering system is pluggable, and
works as a transformation chain, so new filter can be written to
fine-tune the entries. This makes it possible to create several custom
feeds form the same pile of data.   
  
Another field of investigation was to use a bayesian network to filter
entries but it doesn't work well : pertinency moves too fast on this
kind of news, and an inference mechanism would work on static news
topics (Historic events maybe ?)   
  
Last but not least, a special filter is used to collect statistics, and
compute **a buzz-o-meter report**. This report indicates the top 50 most
used words over all sources, and is filtered with an english common
words dictionnary. It doesn't use the tags like most tag clouds, because
people often use the same tags over and over, without really thinking
about it.   
  
**A scan of the post content is way better: you get the REAL tags**.   
  
That's how I keep an eye on what's the most talked about, even though
it's not on my custom feed: I can adapt it afterwards.   
  
Ok now here's the feeds I use, updated every 30mn :   
-   ["Meta Feed" Not filtered, but not redundant][]
-   [Python/Zope oriented (lots of filtering)][]
-   [Live buzz-o-meter][]

  
**[Get it all here in this page][]**   
  
**[][Get it all here in this page]**   
This is pretty handy for my daily job. The buzz-o-meter is for fun, but
I see from time to time new words that pops in the list, I can
investigate on. It also shows that Ajax and Ruby lead the buzz-o-sphere.
  
  
[The source code is GPL and available here][], but still poorly
documented and not packaged, should be better soon. The version running
the feeds is a bit different from the trunk and some merging will be
done soon. This was a project started some months ago I just wrapped and
re-lauched yesterday.   
  
N.B.: I had a few comments on how poorly written was this blog entry.
If you find some mistakes or badly turned sentences, don't hesitate:
tell me ! (i am french ;) )

  [Datamining]: http://en.wikipedia.org/wiki/Datamining "Damamining"
  [Atomisator]: http://programmation-python.org/metafeed/atomisator.jpg
  [Levenshtein distance]: http://en.wikipedia.org/wiki/Levenstein
    "Levenstein"
  ["Meta Feed" Not filtered, but not redundant]: http://programmation-python.org/metafeed/getMetaFeed
    "Metafeed"
  [Python/Zope oriented (lots of filtering)]: http://programmation-python.org/metafeed/getCustomFeed
    "Python feed"
  [Live buzz-o-meter]: http://programmation-python.org/metafeed/buzz
    "buzz"
  [Get it all here in this page]: http://programmation-python.org/metafeed/buzz
    "Atomisator"
  [The source code is GPL and available here]: http://svn.gna.org/viewcvs/atomisator/
    "Atomisator code"
