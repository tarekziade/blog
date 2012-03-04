Title: sys.setdefaultencoding is evil
Date: 2008-01-08 10:45
Category: plone, python, quality, zope

I have recently found some *UnicodeDecodeError* bugs on some products,
that some people couldn't reproduced. The bug was due to a call to a CMF
API that was doing a *str()* over the object, right before using it.   
  
This is perfectly fine in that case, because the object is supposed to
be a ZODB id, so it has to be full ASCII.   
  
So the bug looks like this :   

    >>> id = u'éou'

    >>> str(id)

    Traceback (most recent call last):

    File "<stdin>", line 1, in <module>

    UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in

    position 0: ordinal not in range(128)

  
The people that couldn't reproduced it because they use that ugly hack
which consists of setting Python's default encoding to utf8:   

    >>> import sys 

    >>> sys.setdefaultencoding('utf8')

    >>> id = u'éou'

    >>> str(id) 

    '\xc3\xa9ou'

  
  
This will be applied to the whole process, and Python itself
dynamically removes the method from the module at it first use. From the
official doc:   
   setdefaultencoding(name)

  

    Set the current default string encoding used by the Unicode implementation.

    If name does not match any available encoding, LookupError is raised.

    This function is only intended to be used by the site module implementation and,

    where needed, by sitecustomize. Once used by the site module, it is removed from

    the sys module's namespace. New in version 2.0.

  
I can't find the link back, but I have read once that this built-in was
to be removed because it should not be used outside site.py   
  
The problem is that people tend to add a sitecustomize.py in their
environment, then work with str() and unicode() calls and forget about
doing it right. The result is a major   
misused of strings and unicodes and the code created will be buggy on
other computers.   
  
So never ever use this in your code. If you have a UnicodeDecodeError
it probably means the function is waiting for a string. If you have a
UnicodeEncodeError, it should be unicode. In the same way, do not guess
the encoding in your code. You should work with one type (str or
unicode) and know exactly what is its encoding.   
  
I think this misued is partly due to a lack of warning here:
[http://www.diveintopython.org/xml\_processing/unicode.html][]   
  
Because that's one of the first page a developer finds when he tries to
understand why   
  
he has such bugs.   
  
See a similar entry on the topic 2 years ago here:
[http://faassen.n--tree.net/blog/view/weblog/2005/08/02/0][]

  [http://www.diveintopython.org/xml\_processing/unicode.html]: http://www.diveintopython.org/xml_processing/unicode.html
  [http://faassen.n--tree.net/blog/view/weblog/2005/08/02/0]: http://faassen.n--tree.net/blog/view/weblog/2005/08/02/0
