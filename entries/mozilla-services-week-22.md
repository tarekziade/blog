Title: Mozilla Services - Week 22
Date: 2011-05-31 14:27
Category: mozilla, python

What's this ? read [this post][].   
## What happened

  
I am getting ready for an important push today, that will switch some
services under Python. Things are looking good.   
  
On a side note: my fishes kept on dying in my aquarium and I finally
found the problem by having the water analyzed. The[nice little river][]
in my small town (175 people), that looks so clean, is basically
saturated with Nitrates. I used it for my aquarium because I did not
want to use tap water combined with some products to remove the
chlorine. I thought I was helping out those poor fishes with nice river
water, but I was killing them. This is insane.   
### Cross-team reviews

  
During the previous summit, we discuss at the MoPy meeting an
interesting idea. What if people could ask for a code review from anyone
from another team, that has the skills to do the review. I first thought
about doing some kind of plugin for Bugzilla and have for every
registered user a set of skillx, then propose a reviewer in the patch
UI.   
  
But that means people need to use the Bugzilla review process, and
sometimes they use something else. I also wanted this review to be just
an extra review with a low-commitment from the reviewers. In Bugzilla,
if you are asked to review something, it will stay there waiting for
your review for ever even if you don't review it. I don't think there's
a way to *timeout* a review.   
  
Last, cross-team review could be something broader than Mozilla teams.
What about getting a review from someone in another Python project ?   
  
Anyways, I started "Bug Brothers", a prototype to do this. There's a
demo running here: [http://bugbro.ziade.org][] and the code is here:
[https://bitbucket.org/tarek/bugbro][]. This was a good opportunity to
try Pyramid, and yeah <blush\> no tests and the code is not very clean.
  
  
It's not finished but it already allows people to ask for reviews,
provide a link to a diff. When you review something you get credits, and
when you ask for a review you pay credits. Everything is email-driven.   
  
The next steps are to add more features like [Rietveld][]. a tighter
integration to Bugzilla, github. etc -- but without introducing a
dependency to any tool so it can work for every team.   
### Mozilla Pulse

  
Coming from the Plone/Zope/Python world, I miss my checkins mailing
lists in Mozilla projects. That is, getting a mail everytime a commit is
done in one of the projects you work on. You can always read the Atom
feeds in the various Mercurial repos, but that's not the same.   
  
What I want is a diff in a mail can quickly look at. This is very
useful to get instant reviews from other people. You usually catch more
typos or mistakes. It also help initiating coding discussions.   
  
Christian Legnitto has started the [Mozilla Pulse][] project, which is
exactly what I needed: a way to get notified on every change in the
Mozilla eco-system. I was waiting for Pulse to get hooked in all our
repos and this is now done.   
  
The script to send e-mails on commits is very simple:
[https://bitbucket.org/tarek/services-pulse/src/tip/consumer.py][]. I
need to add a diff view in the e-mail and a few options, but that's
basically it. For now, it keeps only events happening in
hg.mozila.org/services, and it will send e-mail to our services mailing
list.   
  
Overall, Pulse is a good way for anyone to watch a particular area in
the Mozilla project   
### Stop guessing encodings

  
We had a bug in our Services code, related to a password containing an
non-ascii character. It's a shame that as a French I did not insist on
unicode vs str before. So here we go.   
  
In Python 2 we have two types to deal with strings. We can use the
**str** type or the **unicode** type. The **str** type is basically
storing ***bytes*** so a string is encoded using a particular encoding,
By default the encoding is ascii. The **unicode** type encodes strings
as 16 or 32 bits integers and covers the unicode table. The most common
error is to make no assumption whatsoever on the type of the string you
get. What will happen is that some functions that need bytes will simply
try to decode unicodes using the ascii coded, or vice-versa:   
   >>> import base64

    >>> def encode(data):

    ...     return base64.encodestring(data)

    ...

    >>> encode('I am oke')

    'SSBhbSBva2U=\n'

    >>> encode(u'I am oké')

    Traceback (most recent call last):

      File "<stdin>", line 1, in <module>

      File "<stdin>", line 2, in encode

      File "/usr/lib/python2.7/base64.py", line 315, in encodestring

        pieces.append(binascii.b2a_base64(chunk))

    UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position 7: ordinal not in range(128)

  
One solution that comes in mind is to check for the type of the string
in your function:   
   >>> def encode(data):

    ...     if isinstance(data, unicode):

    ...         data = data.encode('utf8')

    ...     return base64.encodestring(data)

    ...

    >>> encode(u'I am oké')

    'SSBhbSBva8Op\n'

  
This is tempting but leads to another issue: if by default your program
is able to deal with string or unicode for all your strings, there are
high chances that you'll miss to check for the type somewhere or combine
str and unicode in some places.   
  
A much better approach is to use internally in your program only
unicode and deal with conversions in inputs and outputs. In a Python web
app it boils down to check that all inputs are unicode (beware of JSON).
  
  
The other issue is the encoding and the decoding. What codec should we
use ? The asnswer is utf-8, because it's the most universal. To make
sure there's no misunderstanding: a unicode is a *decoded* string, and a
str is *encoded*. So you can decode() str and encode() unicode:   
   >>> u'é'.encode('utf8')

    '\xc3\xa9'

    >>> 'é'.decode('utf8')

    u'\xe9'

  
So, use only unicode in your apps, and when encoding, use the utf8
codec by default.   
  
More on this here: [http://docs.python.org/howto/unicode.html][]   
## What's next

  
-   More Python deployments
-   Some benches in the Sync server

  [this post]: http://tarekziade.wordpress.com/2010/11/30/rsync-mozillaservices-community-week-47/
  [nice little river]: http://fr.wikipedia.org/wiki/Oze_(rivière)
  [http://bugbro.ziade.org]: http://bugbro.ziade.org/
  [https://bitbucket.org/tarek/bugbro]: https://bitbucket.org/tarek/bugbro
  [Rietveld]: http://code.google.com/p/rietveld/
  [Mozilla Pulse]: http://pulse.mozilla.org/
  [https://bitbucket.org/tarek/services-pulse/src/tip/consumer.py]: https://bitbucket.org/tarek/services-pulse/src/tip/consumer.py
  [http://docs.python.org/howto/unicode.html]: http://docs.python.org/howto/unicode.html
