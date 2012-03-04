Title: python-weave released
Date: 2010-04-06 15:42
Category: python

I did more experiments on Weave last week-end, and released
[python-weave][] at PyPI, which is basically Mozilla's Python client for
Weave, plus some work I did to make it a Distutils-based project so it
can be installed easily.   
  
If you want to play with it, make sure you have Swig installed, then
run:   
   $ pip install python-weave

  
You can also use easy\_install or a plain *setup.py install* call. Once
this is done, you will have a ***weave*** package in your Python
installation, containing the Weave client.   
  
My first goal with this client was to publish my Firefox bookmarks in
an RSS feed online in my Pylons website (ziade.org), so I could share
them with others. I have now a cron job on my server that gets the
bookmarks on my Weave account every hour, and creates a RSS2 feed out of
it.   
  
The result is here : [http://ziade.org/bookmarks.xml][]   
  
It simplifies my bookmarking workflow and make it dead simple for other
people to grab them (I can drop delicious and use exclusively FF to mark
pages).   
  
I have added this script as a small example in the source release, see:
[http://bitbucket.org/tarek/python-weave-client/src/tip/examples/bookmarks2rss.py][]
  
  
The next steps in my experiments will be:   
1.  display the xml feed in a Pylons view, sorting the bookmarks with
    their tags/keywords
2.  have a way to mark some bookmarks as private, and some as public
    (maybe through folder organization)
3.  add some social features on the top of it. (enable comments, etc.)
4.  let my friends register their own Weave accounts (pointing to any
    Weave server, not necessarily Mozilla's), so they can publish their
    own bookmarks.

  
I realize that 4. is potentially dangerous because it can allow a third
party server to retrieve and store data that was protected by Mozilla's
Weave server. But one of the goal of Weave is to allow several devices
to get the users' data and Firefox is just one client. There's a lot of
potential to build applications outside Firefox too. I have seen that
Weave has an [OAuth][] service (not sure yet if its implemented), so I
need to experiment that. But I'd also need to display other people'
bookmarks. So maybe the best solution for this would be to have a single
Weave account all people share. And allow a single Firefox to manage
multiple accounts: a personal one and a shared one accessed by several
people. That would resolve 2. :)   
  
Anyways, this whole experiment is about building something similar to
what delicious provides, but with a tighter integration in Firefox and
on an open standard.

  [python-weave]: http://pypi.python.org/pypi/python-weave/
  [http://ziade.org/bookmarks.xml]: http://ziade.org/bookmarks.xml
  [http://bitbucket.org/tarek/python-weave-client/src/tip/examples/bookmarks2rss.py]:
    http://bitbucket.org/tarek/python-weave-client/src/tip/examples/bookmarks2rss.py
  [OAuth]: https://wiki.mozilla.org/Labs/Weave/OAuth
