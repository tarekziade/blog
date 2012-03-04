Title: PyPI : CDN vs Mirrors
Date: 2011-09-29 18:30
Category: mozilla, python

We had a few discussions in the last days about what would be a good way
to make PyPI more reliable.   
  
It think there were a bit of confusion about the mirroring protocol
(PEP 381) and its goals, versus the reliability of the current PyPI main
server.   
  
Some people were basically saying (I am paraphrashing)   
> *** Just move PyPI to a CDN and be done with it, this mirroring thing
> is too complicated.***

  
Well, ok. We could set up a CDN for our PyPI files and have all our
archives at Amazon or elsewhere.   
  
But since the mirroring protocol is implemented and available on
server-side (We have [5 active mirrors][]), and since Pip already
supports switching to a mirror, the shortest path to a better PyPI is
simply to :   
> ***create a new mirror in a <put the name of the best provider\> CDN
> and register it as a mirror at PyPI***

  
And if it's so better, so reliable and fast, maybe we'll move it up in
the mirrors list, as the first one so all clients should pick it by
default.   
  
And the day <put the name of the best provider\> is down. (yeah it
happens, remember EC2 a few months ago), you will all be thankful that
we have other mirrors and a protocol to switch over them !   
  
So, if you think a CDN is the magic solution, go ahead. Grab
[pep381client][], set up your monster infrastructure, and let me know so
I add it in the list or mirrors. And maybe we will never ever call
another server again. Or maybe not.   
  
For further info, here is a detailed summary of PyPI status we've built
with Noah: [http://wiki.python.org/moin/BetterPyPI][]   
  
Related: I am going to submit a tutorial on how to work with PyPI,
mirrors, private packages etc., to show how I do at Mozilla

  [5 active mirrors]: http://pypi.python.org/mirrors
  [pep381client]: http://pypi.python.org/pypi/pep381client
  [http://wiki.python.org/moin/BetterPyPI]: http://wiki.python.org/moin/BetterPyPI
