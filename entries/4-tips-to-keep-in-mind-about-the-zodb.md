Title: 4 tips to keep in mind about the ZODB
Date: 2007-10-04 02:26
Category: plone, python, zope

Plone is a great tool, probably one of the best CMS out there, that let
you rapidly create an advanced web application. But there are some real
pitfalls you might fall into if you are not familiar to the underlying
technology. This post provides a list of tips that can help you out. I
am not pretending to give you a set of solutions to make your website
fast and scalable, but by following those tips, you will think the way
experienced Zope developers think when they code an application.   
1.    
   **Ask you customer what will be the load**.

      
    It's very important to know it when you are starting a Plone
    project. That might affect a lot how you are going to work: if the
    application needs to deal with hundreds of hits per minute, and
    store gigas of datas, you won't organize it the same way than if the
    load is ridiculous, like a few hits a day. Project the data load in
    the future also: how big will be the site in one month ? one year ?
    If the data load grows, you might need to set up a cyclic purge to
    make sure the stuff doesn't get huge.
2.    
   **Ask yourself what data will be stored in the ZODB**

      
    The ZODB is a great database, and provides a lot of features for
    CMS: each object (e.g. Document) is automatically saved on each
    change. This persistent layer, à la Hibernate, is nice. But this has
    a cost: if hundreds of objects are created by hundreds of users per
    minute, it won't work. It will technically work but will become very
    slow because the ZODB has to deal with concurrency changes on the
    objects. You might argue that this won't be a problem if you take
    care of who changes the data and how, but you won't be able to deal
    with how base objects work in the ZODB. For example, BTrees objects,
    that are supposed to be fast and to be able to deal with many items,
    are not really scalable on writes: on my Intel MacBook, on a
    BTreeFolder containing 1000 items, running 4 concurrent threads that
    are creating objects in a pace of 300 ms, will generate conflict
    error on 10% of the requests. You should really ask yourself if you
    need ZODB features on some data. Maybe they will fit better in a SQL
    database if they don't need versionning or sophisticated workflows.
      
      
    The ZCatalog in its classical shape, is also a particular case. It
    can weight 40% of the ZODB total size, so if you index a lot of
    things, and a lot of features on your websites are based on queries,
    it's maybe a good idea to used a specialized database, like
    [Xapian][] or Lucene. It's faster, and it won't make your ZODB grow.
    Hey, why indexes are stored in the ZODB anyway ?
3.    
   **Don't hide your code behind caches**

      
    SQUID, memcached, CacheFu. All those tools are wonderful and
    mandatory when you put your site in production. But you should not
    hide your code behind them : that's the best way to code a crappy,
    badly architectured application. You should take care on how your
    application scales and on your code effectiveness before you think
    about caching. Be careful about the complexity of each of your
    function, and how they scale.
4.    
   **Be careful of the pound/ZEO mirage**

      
    Making a cluster of ZEO nodes will not make your application
    faster, it will just raise the number of concurrent threads your
    application can handle simultaneously. Each node needs to be
    synchronized behind the scene everytime a data is changed. So the
    more nodes you have the more network traffic you will get. This can
    damage the overall performance of the application as well.

  
There's a lot of work going on in this area. I am looking forward for
what people will do on this sprint for example:
[http://plone.org/events/sprints/copenhagen-performance-sprint][]

  [Xapian]: http://tarekziade.wordpress.com/2007/06/12/indexation-service-with-xapian/
  [http://plone.org/events/sprints/copenhagen-performance-sprint]: http://plone.org/events/sprints/copenhagen-performance-sprint
