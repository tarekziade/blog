Tools for the Marketplace server
################################

:date: 2012-08-03 10:25
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

.. image:: https://marketplace-cdn.addons.mozilla.net/media/img/ecosystem/open_icon.png
   :align: right


We had an *Apps* work week in Mountain View this week and worked
with the fine folks from the WebDev team on the web app called
`Marketplace <https://marketplace.mozilla.org>`_.

We're joining the *Marketplace team* with Alexis and a couple
of other folks from Services to try to help them polishing
the app before it moves from its *preview* stage to
*production*.

**Marketplace** is the Django-based application WebDev wrote
to allow the community to publish Open Web Apps that will
be installable on your Firefox OS based phone.

This app is a derivation of the addons web app, using the same
basis: `Zamboni <https://github.com/mozilla/zamboni>`_ -- except
that add-ons are Open Web Apps in this case.

On the code side, most things are done and we'll mostly
help with the bug fixing.

Although, coming from Services, the real value we can
bring in this project is trying to apply on Marketplace
some good practices that were successful on Services
projects.

The two main things we started to work on with Alexis
are **load testing** and **connectors testing**.


Load testing => Marteau
-----------------------


If you follow this blog you know I am a
`Funkload <http://funkload.nuxeo.org/>`_ fan.
Funkload is a load testing tool we're using at Services,
written by a co-worker I had at Nuxeo back in the old days.

Funkload is cool for many reasons:

- writing load tests is done by writing vanilla unit tests
  in Python -- no Jython involved like in the Grinder.

- the load runner is a simple command line tool that can
  distribute the load across many nodes.

- Funkload creates nice HTML `reports <http://funkload.nuxeo.org/report-example/test_simple-20110126T232251/#request-stats>`_
  that are most
  of the time sufficient to detect any issue an app has.

Alexis has started to write a couple of load tests
we'll be running on Marketplace, but we thought it would
be a good idea to take it to the next stage.

Several people at Mozilla have expressed interest on being
able to run a load test on a web app without having to
worry about finding free VMs and managing a cluster.

So we've started a very simple tool called **Marteau**,
that will let people enqueue a load test through a web
interface, and execute it for them whenever there are
free resources.

We've created for this a YAML file you can simply stick
into your project repository, in which you define where
is your load test and how you want it to run.

Like how `Travis <http://travis-ci.org/>`_ does, any project
that has this YAML file is eligible for being used by **Marteau**.

The Token Server for instance has one now
`here <https://github.com/mozilla-services/tokenserver/blob/master/.marteau.yml>`_

The web interface will simply display the queue of
pending load tests, and pick free VMs to run them, then
ping you when it's done, with a link to the Funkload report.

I'll blog about it more when we have a more advanced
tool.

Connections Testing => Vaurien
------------------------------

What happens to your web app when the SQL database is down for a couple
of minutes ?

Are your connectors properly handling the case ? are you able to get back
on track once the database is back online ? can you survive when memcache
is down ? if not, are you sending back the proper 50x to the end user ?

To answer to all of these questions, you have to manually test each of of
those scenario, which can be painful.

Or you could set up a
`Chaos Monkey <http://www.codinghorror.com/blog/2011/04/working-with-the-chaos-monkey.html>`_
but I suspect this is a bit overkill in most cases.

Another way to automate these tests is to run a proxy between the web app
and the back end server, that breaks things on purpose.

The proxy can:

- add delays
- drop requests
- send back errors
- simulate any bad behavior we've already seen in a backend

Having this proxy up and running during a load test is the best
way to detect if your web application is *robust enough* to handle
those situations.

The tool we've started is called **Vaurien** and is a TCP proxy
we can run in front of any backend server the web app uses.

It pings statsd everytime it does a bad thing, so we can corellate
the application errors with the proxy actions.

It's also meant to be completely pluggable, so if you have a
specific back end behavior you want to simulate, you can write a
Python function for it and hook it via confiuguration.

The tool is currently using a configuration file where you
define a list of behaviors -- from "normal" to "total blackout" --,
and for each one of them their % of occurrences.

More on this as soon as we have a decent v1.

What's next
-----------

These two tools we're building can probably be useful to
more people around the Mozilla & Python community, so if
you are interested in helping building them, please ping us.
