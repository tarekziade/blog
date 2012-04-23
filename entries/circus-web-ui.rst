A Web admin for Circus
######################

:date: 2012-04-23 18:51
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziadé


We're working on adding a Web Administration Panel to Circus. Like many tools
out there, the idea is to let you control Circus from the web.

.. raw:: html

    <a href="http://blog.ziade.org/circus-web-panel.m4v">
      <img src="http://blog.ziade.org/circus-web-ui.png" height="200px" width="600px"
            title="Click to see the screencast">
      </img>
    </a>

This new feature is currently built with:

- The `Bottle Framework <http://bottlepy.org/>`_ -- A one-module wsgi framework.
- The `Sparkline jQuery Extension <http://omnipotent.net/jquery.sparkline/>`_ -- A JS lib
  to draw cute little charts.
- The `Circus Client class <https://github.com/mozilla-services/circus/blob/master/circus/client.py>`_,
  that let you connect to a Circus system and interact with it via ZMQ messages.

The prototype currently does AJAX Polls to update the data on the page every
second, but a lot of things are being worked out to improve this.

For instance, the web app keeps in memory the last 100 stats calls in order
to build the charts series, and serves them to the clients on every poll.

We're going to change this by collecting and building the series on the client
only.

We'll also add a bit of `Memoization <https://en.wikipedia.org/wiki/Memoization>`_ so we
serve back the same stats values in a given timespan to avoid overloading Circus with
web stats calls.

This is especially important when the Web UI displays charts for hundreds of
processes.

And err... we need to make the UI pretty and usable. I am doing my best
here, but let's face it -- I suck at CSS :)

If you are a designer and want to help there...

You can see a screencast of the prototype here: http://blog.ziade.org/circus-web-panel.m4v

This screencast was built with the *crypto* demo of the Powerhose project at:
https://github.com/mozilla-services/powerhose/blob/master/examples/crypto.ini

This demo runs crypto workers, a broker, and a web app.

In this screencast I do the following:

1. connect the Circus Web Admin app to a Circus system
2. check how the processes of the *workers* watcher do
3. add & remove some processes
4. start & restart the *web* worker


Links:

- the doc: http://circus.readthedocs.org/en/latest/index.html
- the repo: https://github.com/mozilla-services/circus

Please let us know what you think !
