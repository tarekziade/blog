A Pelican web editor
####################

:date: 2016-01-21 10:40
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade


The benefit of being a father again (Freya my 3rd child, was born last week) is
that while on paternity leave & between two baby bottles, I can hack on fun stuff.

A few months ago, I've built for my running club a Pelican-based website, check it out
at : http://acr-dijon.org. Nothing's special about it, except that I am not
the one feeding it. The content is added by people from the club that have zero
knowledge about softwares, let alone stuff like vim or command line tools.

I set up a github-based flow for them, where they would add content through the
github UI and its minimal reStructuredText preview feature - and then a few
of my crons would update the website on the server I host.
For images and other media, they are uploading them via FTP using FireSSH in Firefox.

For the comments, I've switched from Disqus to `ISSO <https://posativ.org/isso/>`_
after I got annoyed by the fact that it was impossible to display a simple Disqus
UI for people to comment without having to log in.

I had to make my club friends go through a minimal
reStructuredText syntax training, and things are more of less working now.

The system has a few caveats though:

- it's dependant on Github. I'd rather have everything hosted on my server.
- the github restTRucturedText preview will not display syntax errors and warnings
  and very often, articles get broken
- the resulting reST is ugly, and it's a bit hard to force my editors to be stricter
  about details like empty lines, not using tabs etc.
- adding folders or organizing articles in the Pelican content directory freaks out
  my editors.
- editing the metadata tags is prone to many mistakes

So I've decided to build my own web editing tool with the following features:

- resTructuredText cleanup
- content browsing
- resTructuredText web editor with live preview that shows warnings & errors
- a little bit of wsgi glue and a few forms to create articles without
  having to worry about metadata syntax.


resTructuredText cleanup
========================

The first step was to build a reStructuredText parser that would read some
reStructuredText and render it back into a cleaner version.

We've imported almost 2000 articles in Pelican from the old blog, so I had
a **lot** of samples to make my parser work well.

I first tried `rst2rst <https://github.com/benoitbryon/rst2rst>`_ but that
parser was built for a very specific use case (text wrapping) and was
incomplete. It was not parsing all of the reStructuredText syntax.

Inspired by it, I wrote my own little parser using **docutils**.

Understanding docutils is not a small task. This project is very powerfull
but quite complex. One thing that cruelly misses in docutils parser tools
is the ability to get the source text from any node, including its children,
so you can render back the same source.

That's roughly what I had to add in my code. It's ugly but it does the job:
it will parse rst files and render the same content, minus all the extraneous
empty lines, spaces, tabs etc.


Content browsing
================

Content browsing is pretty straightforward: my admin tool let you browse
the Pelican content directory and lists all articles, organized by categories.

In our case, each category has a top directory in content. The browser
parses the articles using my parser and display batched lists.

I had to add a cache system for the parser, because one of the directory
contains over 1000 articles -- and browsing was kind of slow :)

.. image:: http://ziade.org/henet-browsing.png


resTructuredText web editor
===========================

The last big bit was the live editor. I've stumbled on a neat little tool
called **rsted**, that provides a live preview of the reStructuredText
as you are typing it. And it includes warnings !

Check it out: http://rst.ninjs.org/

I've stripped it from what I needed and included it in my tool.

.. image:: http://ziade.org/henet.png

I am quite happy with the result so far. I need to add real tests and
a bit of documentation, and I will start to train my club friends on it.

The next features I'd like to add are:

- comments management
- media management
- spell checker

The project lives here: https://github.com/AcrDijon/henet

I am not going to release it, but if someone finds it useful, I could.

It's built with Bottle & Bootstrap as well.
