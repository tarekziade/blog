Title: Planet and Wordpress buggy title
Date: 2008-01-08 10:13
Category: plone, python, zope

I have found out why my entry titles are removed in all planets.
Wordpress recently added in their feeds a new tag in each item of the
feed:   
   <media:title type="html">tarek</media:title>

  
That's the one which get caught in feedparser, instead of the item real
title. This bug was already noticed and added in the bug tracker:
http://code.google.com/p/feedparser/issues/detail?id=83&q=wordpress.   
  
So I guess it's just a matter of time for Lennart, me, and some other
people, to appear right in all Planets.
