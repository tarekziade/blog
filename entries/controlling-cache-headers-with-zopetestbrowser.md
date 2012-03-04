Title: Controlling Cache headers with zope.testbrowser
Date: 2007-11-11 10:26
Category: plone, python, zope

On a Plone website, setting the cache headers with [CacheFu][] or other
tools is quite easy, but when you need to check on a given page which
headers are inserted, it's not always easy to know what will be called
in the stack of rules you have set.   
  
You can look at each page properties in you web browser to check this,
but it is a pain and you won't be able to make sure nothing is broken
when you change, for example, your CacheFu settings.   
  
So, having a dedicated functional test to control your website cache
settings is a good way to avoid regressions. [zope.testbrowser][] allows
you to write this on a doctest, so it's easy to gather all your cache
headers control in one text file. To install it, you can use [Easy
Install][]:   

    $ easy_install zope.testbrowser

  
Here's an example of such doctest (cache.txt):   

    =============

    Testing cache

    =============



        >>> from zope.testbrowser.browser import Browser



    This method is used to print a page headers::



        >>> def headers(url, login=None, password=None):

        ...     b = Browser()

        ...     if login is not None and password is not None:

        ...         b.addHeader('Authorization',

        ...                     'Basic %s:%s' % (login, password))

        ...     b.open(url)

        ...     print b.headers



    Let's try on the python front page::



        >>> headers('http://python.org')

        Date: ...

        Server: Apache/2.2.3 (Debian) DAV/2 SVN/1.4.2 mod_ssl/2.2.3 OpenSSL/0.9.8c

        Last-Modified: ...

        ETag: "60193-3fd1-b811ca00"

        Accept-Ranges: bytes

        Content-Length: 16337

        Connection: close

        content-type: text/html; charset=utf-8



    The page returns an ETag header, which tells the browser if the page has changed.



    Let's try Plone's one::



        >>> headers('http://plone.org')

        Server: nginx/0.5.26

        Date: ...

        Connection: close

        Content-Language: en

        X-Cache-Headers-Set-By: CachingPolicyManager: /plone.org/caching_policy_manager

        Expires: ...

        Vary: Accept-Encoding

        Last-Modified: Sun, 04 Dec 2005 12:13:31 GMT

        X-Cache-Rules-Applied: yes

        X-Caching-Rule-Id: frontpage

        Cache-Control: max-age=0, s-maxage=3600, must-revalidate

        X-Header-Set-Id: cache-in-proxy-1-hour

        Content-Length: 44947

        X-Varnish: 783893351 783878475

        Age: 3364

        Via: 1.1 varnish

        Content-Type: text/html;charset=utf-8

        imagetoolbar: no



    It has more complex cache information (CacheFu) used by Varnish cache software.

  
Notice the use of Ellipsis (...) that replaces changing data like
Dates. It can be called using a python module that can look like this:   

    import os

    import unittest

    import doctest



    OPTIONFLAGS = (doctest.REPORT_ONLY_FIRST_FAILURE |

                            doctest.ELLIPSIS |

                            doctest.NORMALIZE_WHITESPACE)



    def test_suite():

        return doctest.DocFileSuite(os.path.basename('cache.txt'),

                                             optionflags=OPTIONFLAGS)



    if __name__ == '__main__':

        test_suite()

  
This is not specific to Plone, and can be used on any website. Added to
the stack of tests, this helps a lot on making sure the cache settings
are doing what they are supposed to.

  [CacheFu]: http://plone.org/products/cachefu
  [zope.testbrowser]: http://cheeseshop.python.org/pypi/zope.testbrowser/3.4.2
  [Easy Install]: http://peak.telecommunity.com/DevCenter/EasyInstall
