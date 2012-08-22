Marteau - Distributed load tests
################################

:date: 2012-08-22 12:26
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

.. image:: http://blog.ziade.org/marteau.png
   :align: right

As I've described `a few weeks ago <http://blog.ziade.org/2012/08/03/tools-for-the-marketplace-server>`_,
we've started to build a tool called **Marteau** which is a web app to run distributed load
tests using `Funkload <http://funkload.nuxeo.org/>`_.

The application is now working quite well and let us manage several servers used to hammer some of our
web services. The load test don't interpret the JS like Selenium and just focus on simulating a lot of load
on the server side, like Apache JMeter or The Grinder.

Developers can write Funkload tests like `this one <https://github.com/mozilla/marketplace-loadtest/blob/master/loadtest.py>`_
and publish it through a `.marteau.yml file <https://github.com/mozilla/marketplace-loadtest/blob/master/.marteau.yml>`_.

From there Marteau can discover the load tests and run them.

We've built it using Pyramid & `retools <http://retools.readthedocs.org/>`_ & Redis. It's basically a
queue of jobs you can feed from the Web UI. *retools* provides a *worker* script which is a standalone
program that will retrieve work to do in the queue and perform them, and the Marteau server has a few of them
running so we can have several load tests going on in parallel.

Once your load test is over, you get a mail pointing to the full Funkload report.

As for the nodes (=the servers that are driven to hammer the web app to load test), each worker picks
some of them and they are marked as busy during the test.

Here's a small screen cast I've put together to demonstrate how it works. Pardon the flicks, I am not
an avidemux expert:

.. image:: http://blog.ziade.org/marteau-index.png
   :target: https://plus.google.com/photos/106436370949746015255/albums/5779218083785434033/5779218087304312258


A community service ?
---------------------

Using Vagrant and a Cloud service, I am wondering if it would be useful to put together a
public Marteau server for the community, so people can load test their apps without having to deploy
themselves several testing servers.

There are several things that need to be addressed in order to be able to offer this:

- being able to control that the user *owns* the domain she will load test. This can
  be done by asking her to put a specific secret key on the web app, Marteau can control.

- being able to put some quotas on the number of nodes and the disk space the user can have.

- I have no idea how much this would cost to host such a service, depending
  on the number of users and the frequency of usage. I'd need to try out a few run in a Cloud
  service in order to measure it.

Last but not least, how many people would find such a service useful ? I know I'd love to
be able to run a quick load test on some of my own apps I have.

