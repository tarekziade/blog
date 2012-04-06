GitHub based services
#####################

:date: 2012-04-06 10:20
:tags: python, mozilla
:category: python
:author: Tarek Ziade


Ok, maybe I am late at the party, and some people will think what I am writing
here is obvious, but nevermind. ;)

There's a trend these days on Github-based online services. That is -- point
me your Github repo and I'll do something with it everytime you push a change.

Notification hooks have existed for years now, and a lot of teams have their
own Jenkins CI (we do at Mozilla), or their checkins mailing list. But the
thing is : what's the point to maintain your own stuff anymore when there's a
service for it you can hook in a few minutes.

For a Python project there are two absolutely awesome services:

- `ReadTheDocs <http:.//readthedocs.org>`_ -- creates a website out of your
  project
  Sphinx docs, exactly
  like what we've set with http://packages.python.org but it's all automatically
  done for you on every commit. **win**

- `Travis-CI <http://travis-ci.org>`_ -- run your tests on every change.
  Sends mail on failure. Again, nothing's new here, but  as a developer, the
  only thing you have to do is to add a YAML file in your
  repo. **win**

Travis does not replace functional tests or tests you want to run on a
specific infrastructure. But for day-to-day usage it's perfect.

In fact, there are more and more people that have standardized their README
page that appears at PyPI with those two tools.

For example, look at Circus -- http://pypi.python.org/pypi/circus

It displays the Travis build status directly on PyPI, and provides a link
to Read the docs.

Out of my head here are some services I'd love to enable from my Github
admin panel:

- A `Coverage <http://nedbatchelder.com/code/coverage/>`_ Dashboard like
  this one -- http://nedbatchelder.com/code/coverage/sample_html/

- A similar Dashboard but with profiling info, using
  http://www.hexacosa.net/project/pyprof2html.

- A `Funkload Trending <http://funkload.nuxeo.org>`_ Dashboard. Read about
  this here: http://ziade.org/2011/06/10/continuous-load-testing-wint-funkload

The first and second ones are simple to produce - all it takes is a call to
the script that generates the HTML report. It needs to run in some VM though.

Ah. mm wait. Maybe the ReadTheDocs project could add support to these,
or maybe I can try to sneak in those dashboards as Sphinx extensions...

The last one is harder because it involves some thoughts on the
load testing architecture and well, it won't tell you if your application
is slow on *your* hardware -- it will just detect that your web service
got suddenly slower after that commit.

There are hundreds of services on Github already -- curious to know
which ones Python folk use.


