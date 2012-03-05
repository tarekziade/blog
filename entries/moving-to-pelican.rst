Moving to Pelican
#################

:date: 2012-03-05 20:44
:tags: python
:category: python 
:author: Tarek Ziade

So, in my current quest of reducing the ads around me, I realized my blog 
hosted at wordpress.com was full of them.

So I decided to move to Alexis' Pelican blog system : http://pelican.notmyidea.org

Pelican creates a static html blog using reStructuredText or Markdown files 
and that makes it easy enough to push blog entries at github and have them 
published automatically on a server.

Pelican can work by default with Disqus and has a default CSS that's 
simple and readable.

What I am losing from Wordpress is the whole Dashboard that I really liked,
and in particular the stats. Knowing that one of my blog post made it to
Reddit or hacker news was a good thing -- I could go there and answer questions
or read the comments.

I almost got myself a pro account at wordpress because I did not want to 
maintain yet another stats tool on my server. But getting away from wordpress
and getting back under my own domain was more tempting.

Pelican has an import feature for Wordpress, that failed to produce the
proper reStructuredText for me, but worked quite well with Markdown.

I was also able to tweak the URLs so they would look exactly like the 
Wordpress ones, that is, URL with the year, month and day. I was also
lucky enough about the slug part of the URL: the import generated
the **same** slugs than Wordpress ! In other words a simple redirection
of the domain does the trick to avoid losing any indexing.

I am paying 12 bucks to wordpress to get this redirect but that's worth
it because people hitting tarekziade.wordpress.com should find back
the result transparently on blog.ziade.org.

I also missed a way to create static *pages*, like what Wordpress has.
So I added this feature to Pelican and will propose it for inclusion
to Alexis.

Overall I really recommend Pelican. It's well crafted, easy to use and
it's Python ! 

Thanks to Alexis and other contributors.
