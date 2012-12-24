New Year's Python Meme 2012
###########################

:date: 2012-12-23 21:07
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

I did this in `2009 <http://blog.ziade.org/2009/12/28/new-year039s-python-meme>`_
& `2011 <http://blog.ziade.org/2011/12/20/new-year039s-python-meme-2011/>`_, let's try again.


**1. What’s the coolest Python application, framework or library you have discovered in 2012 ?**

`PyZMQ <https://github.com/zeromq/pyzmq>`_ - This library for **ZeroMQ** is much more than a simple binding.
It has great features
like its own event loop based on Tornado's one -- **MinRK**, the guy behing this library is
involved in `IPython <http://ipython.org/>`_ which uses ZeroMQ. So since IPython is growing
big, PyZMQ is getting a lot of love :-)

I used it in `Circus <http://circus.io>`_ and `Powerhose <http://powerhose.readthedocs.org>`_
and had lots of fun.

One thing that was painful was its bad interaction with **gevent** but this is not
an issue anymore, now that *PyZMQ* includes a *green* subpackage.


**2. What new programming technique did you learn in 2012 ?**

Since most of my projects now use Gevent - I learned **how to detect and fix bugs
related to Gevent interactions**. Things like: a library using the stdlib Queue module
and that suddenly locks.

This does not sound like an extraordinary thing, but I've seen people banging their
heads for hours on those. I banged my own head quite hard but I am getting better at detecting
and fixing those now.


**3. Which open source project did you contribute to the most in 2012 ? What did you do ?**

**Circus**. I've coded a big chunk of it - and worked in most areas except the signals -
https://github.com/mozilla-services/circus/graphs/contributors with Alexis and a couple of new
contributors. Benoit is #2 with over 300k lines but that's because he accidentaly commited a 300k lines log file ;)


**4. Which Python blog or website did you read the most in 2012 ?**

Reddit again this year.


**5. What are the three top things you want to learn in 2013 ?**

In 2013 I want to learn more about **photography**, **electronics** & **writing**. Yeah nothing
related to Python this time :-)


**6. What is the top software, application or library you wish someone would write in 2013 ?**

I whish we could continue our cool *leaf recognizer* project with Olivier & Ronan:
http://whatthefeuille.com/ - because it would be a great app if it takes off.



Want to do your own list ? here's how:

- copy-paste the questions and answer to them in your blog
- tweet it with the `#2012pythonmeme <https://twitter.com/search/realtime?q=%232012pythonmeme&src=typd>`_ hashtag

