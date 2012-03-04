Title: How to be disappointed with the &quot;printed&quot; in &quot;printed book&quot;
Date: 2008-11-22 17:23
Category: plone, python, quality, zope

I feel really bad about this comment on my book : [How To Be
Dissappointed in Something You Recommend][].   
  
Just a quick word about the try, return finally code pattern, since I
had some feedback about it. I would like to mention that this code
pattern is perfectly right:   
   def function():

        try:

          return something

        finally:

          do something

  
I should have explained it better, because this pattern is not used a
lot by people, so you can think that "do something" is called after the
return of the function, which is not the case.   
  
For the typos now:   
  
**The first thing I did wrong**: when I started the book, I wanted, as
I did in [my previous book][], to run unit tests on the book itself to
avoid those mistakes. That said, the previous one was in Latex, which is
quite simple to interact with, and this one is in OpenOffice, because
that is how the editor works. I had to write a script to extract the
Python code from the Ooo file, to unit test it. I didn't. I simply ran
out of time, as usual when you have deadlines on books.   
  
**The second thing I did wrong**: I should have told the editor to wait
a bit, I didn't.   
  
But Packt does Print On Demand, so I know that the Errata page I am
maintaining here : [http://atomisator.ziade.org/wiki/Errata][], is being
processed by the editor, and that the typos will be removed from the
book at some point, without having to wait for a second edition.   
  
I'll update this blog entry as soon as I know the status on this.   
  
I am really sorry [Calvin][], and all the people that are suffering
from these typos.

  [How To Be Dissappointed in Something You Recommend]: http://techblog.ironfroggy.com/2008/11/how-to-be-dissappointed-in-something.html
  [my previous book]: https://www.amazon.fr/dp/2100508830
  [http://atomisator.ziade.org/wiki/Errata]: http://atomisator.ziade.org/wiki/Errata
  [Calvin]: http://techblog.ironfroggy.com
