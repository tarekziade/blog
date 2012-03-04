Title: ZODB vs SGBD ? Give me a standard, it&#039;s about time !
Date: 2007-01-09 14:16
Category: python, zope

I've been reading [Carlos' post about Zope 3][], and his thaugths on the
role of the framework.   
  
I want to react on this and give my opinion on Zope future and on
Python Web developement as well, because I feel that people are not
debating on the right thing.   
  
Since a few months, a lot of people in Zope community are seeing Zope 3
as packages that can be used in Zope 2 or elsewhere. This is probably
true. A lot of people are also using CherryPy, Django, TurboGears, ..,
and dropping Zope for some reasons. These reasons are probably right.
(my reason to drop Zope would be the ZODB).   
  
But beside this reasons, (every framework has pro's and con's) there's
a missing brick in the Python Web Developement ecosystem that exists in
Java world: a standard for document repositories. It's called [JCR or
JSR-170][]. Some people in Zope community [have talked about it][] in
[the][] [past][]. Nuxeo did a bind as well with [nuxeo.jcr][], then
dropped Zope/Python for Java (which is totally logical given where CPS
software is heading).   
  
I strongly believe that the future and the maturity of all Python web
frameworks relies at the first place on a common document repository
standard, like DB API did with SQL.   
  
Python web developers, it's time for all of us to cooperate and create
such a standard in Python, and an implementation based on SQLAlchemy.
This would let Zope drop the ZODB (yepee) and let every web developer
use the best of all frameworks (the Zope Component Architecture, the
Django approach, etc.) since they would all be able to work with a given
repository.   
  
I would like to see the PSF and all framework core developers support
such a project.   
edit: oups.. I just realized I have used a french acronym in the title
(SGBD). The english one is RDBMS

  [Carlos' post about Zope 3]: http://blog.delaguardia.com.mx/index.php?op=ViewArticle&articleId=72&blogId=1
    "Carlos"
  [JCR or JSR-170]: http://jcp.org/en/jsr/detail?id=170 "JSR-170"
  [have talked about it]: http://blogs.nuxeo.com/sections/blogs/fermigier/2005_06_25_jsr_170_java_content
  [the]: http://faassen.n--tree.net/blog/view/weblog/2005/07/20/0
  [past]: http://palladion.com/home/tseaver/obzervationz/jsr170_doodling_20050711
  [nuxeo.jcr]: http://svn.nuxeo.org/trac/pub/browser/nuxeo.jcr/trunk/src/nuxeo/jcr/
