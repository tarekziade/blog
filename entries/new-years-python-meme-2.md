Title: New Year&#039;s Python Meme
Date: 2011-12-20 11:28
Category: python

Hey [I did this in 2009][], let's try again -- I am adding one extra
question this year   
  
**1. What’s the coolest Python application, framework or library you
have discovered in 2011 ?**   
  
**GEvent & Pyramid**. Not discoveries, but a daily usage. GEvent was
for me a fantastic way to make the Firefox Sync Python server scale
without being forced to write callback-style code. Pyramid is a very
elegant framework, that takes the simplicity from Pylons and the power
and experience from Repoze & the Zope world. A good sign for me is that
we don't have to deal with the ZCA ;)   
  
**2. What new programming technique did you learn in 2011 ?**   
  
**Better behaviour in high loaded server apps**. During the last year,
when we wrote all the pieces that makes Firefox Sync today, I've learned
how to be more careful on how my apps would react when a back-end breaks
or cease to reply, when a database gets slow, or when some service
that's used restarts -- or when my own app restarts, still hammered by
many requests. I did a fair amount of work on this, like smart pools of
connectors and better testing techniques, and make decisions on what
features survive when some third-party server is down, and what features
just go 503.   
  
**3. What’s the name of the open source project you contributed the
most in 2011 ? What did you do ?   
**   
  
**Mozilla**. I have not contributed as much as last year in Python
because my work at Mozilla takes most of my time, but the good news is
that all our stuff is open source so.. The most useful stuff for the
community we've started is probably [Cornice][]. But we've written and
writing a myriad of apps and libs. See
[https://github.com/mozilla-services][] and
[http://hg.mozilla.org/services][]   
  
In Python I still interact a bit with what's going on in Packaging and
hope I'll be able to spend more time on it in 2012. But some packaging
work I needed at work was also useful for the community, like pypi2rpm.
  
  
**4. What was the Python blog or website you read the most in 2011 ?**
  
  
Like in the past few years, Python Reddit. And I think I am not alone
in that case. 90% of my blog hits come from Reddit ![:-)][]   
  
**5. What are the three top things you want to learn in 2012 ?**   
  
I'd like to learn how to program in a few new languages, just to give
them a shot. Maybe Haskell. I'd also like to finish a spare project I
have started with Benoit, and try to launch it, promote & market it.
Last, I'd like to learn more about Firefox arcanes -- just for my
culture.   
  
**6. What are the top software, app or lib you wish someone would write
in 2012 ?**   
-   I want to take a picture of a wine bottle and have it recognized in
    an online app, where I can share my thoughts about its taste.
-   I want an Android virtual ping-pong application, where you can use
    your phone as paddle and see the e-ball through the camera & play
    with a friend.

  
Want to do your own list ? here's how:   
-   copy-paste the questions and answer to them in your blog
-   tweet it with the [\#2012pythonmeme][] hashtag

  [I did this in 2009]: http://tarekziade.wordpress.com/2009/12/28/new-years-python-meme
  [Cornice]: https://github.com/mozilla-services/cornice
  [https://github.com/mozilla-services]: https://github.com/mozilla-services
  [http://hg.mozilla.org/services]: http://hg.mozilla.org/services
  [:-)]: https://s-ssl.wordpress.com/wp-includes/images/smilies/icon_smile.gif?m=1305848327g
  [\#2012pythonmeme]: https://twitter.com/#!/search/#2012pythonmeme
