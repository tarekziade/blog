Fun with AngularJS & Cornice
############################

:date: 2013-02-13 12:22
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

.. image:: http://blog.ziade.org/dashboard.png
   :align: right
   :scale: 50


I `blogged about it <http://blog.ziade.org/2013/01/25/a-new-development-era-essay/>`_
a few weeks ago: in my opinion, we're moving to
an ecosystem where our web applications are built of JSON web services
and of Javascript applications that use those services to fetch
data and display them.

In other words, server-side templating is fading away and client-side
templating based on frameworks like AngularJs is getting a
lot of traction.

As a Python developer in the Mozilla Services team, one tool that
is starting to play an important role is `Cornice <https://cornice.readthedocs.org>`_,
because it's the perfect companion for building a Javascript application.

Cornice features that are really useful in this context:

- `CORS <http://www.w3.org/TR/cors/>`_ support
- based on a robust & mature framework: `Pyramid <http://www.pylonsproject.org/>`_
- dead-simple Mozilla Persona integration, thanks to a
  `vibrant Pyramid ecosystem <https://www.rfk.id.au/blog/entry/securing-pyramid-persona-macauth>`_
- standard machine-parseable errors
- can run everything in async mode


Busting the myth about Python & async programming
=================================================

Before I talk about the topic, I want to make a little digression and
bust a myth about Python vs Javascript.

I have heard this sentence several times in Javascript and Node.js developers circles:

    *Python doesn't support async programming*

I've even heard some people explaining that Python couldn't be used as an async
language because of the `GIL <https://en.wikipedia.org/wiki/Global_Interpreter_Lock>`_ !

Talking about the GIL in this context is completely out of topic. Like Python,
Javascript has something similar to the GIL (locks in "Isolates" in V8).
But the GIL becomes an issue only when you run several threads in the same process.

And in web programming, we don't really use threads anymore.

Node.js is single-threaded and uses `libuv <https://github.com/joyent/libuv>`_
to run an event loop, and feeds the loop with callbacks.

Python has also libraries and frameworks that provide event loops. In fact,
Node.js was `inspired by Twisted <http://nodejs.org/about/>`_.

There are libuv, libevent & libev bindings in Python. And frameworks and
libraries that use those bindings to provide event loops.

That said, I am not a huge fan of callback programming, I find it quite hard to
read and debug. I like it better when I am working with thread-like objects.

Fortunately in Python we have `gevent <http://www.gevent.org/>`_ that will
provide *greenlets*, which are pseudo-threads that wrap callbacks and
an event loop - and you don't have to do callbacks anymore.

Gevent takes care of the gory details and let you do linear, functional programming
that can be traced, debugged, without falling into an horrible maze of callbacks.

A code like this...

.. code-block:: python

    import urllib2, gevent

    urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

    def print_head(url):
        print ('Starting %s' % url)
        data = urllib2.urlopen(url).read()
        print ('%s: %s bytes: %r' % (url, len(data), data[:50]))

    jobs = [gevent.spawn(print_head, url) for url in urls]

    gevent.wait(jobs)


...will asynchronously download all URL pages, and let you work with *greenlets*.

Some people don't like this approach and use tools like Tornado, that
will let you start an event loop and define callbacks, like Node.js.

But enough said - my point is made:

Yes, the Python ecosystem has the same tools than the Javascript/Node.js
ecosystem to do async programming. **And** it has much more to offer in fact.


Cornice for the JSON APIs
=========================

For the Marketplace, we're working on building a separated application to provide
a metrics dashboard.

The goal is to display interactive dashboards filled with some `Highcharts <http://www.highcharts.com/>`_
based charts.

The primary goal is to replace the ones we have in the Marketplace application,
that give to the users info like the number of downloads for their web apps.

For this, we're going to provide a set of JSON APIs on the top of an Elastic Search server,
using Cornice.

Cornice acts as a proxy in front of the Elastic Search server, but also provides a
few extra APIs and features we need - it also integrates the excellent *pyelasticsearch*
library.

To give you an idea of how hard is to build such an application with Cornice,
here's the core of the code:

.. code-block:: python

    es = Service(name='elasticsearch', path='/es')

    @es.post(validators=(valid_json_body,), renderer='json')
    def query_es_time(request):
        try:
            return request.es.search(request.validated['body'], index='time_*')
        except ElasticHttpError as e:
            request.response.status = e.status_code
            return e.error


The Service class provided by Cornice does a lot of automation here, like
sending back a clean JSON error message in case the query is malformed. It also
checks that we don't return a JSON list - since that can be a security hole.
It makes sure the server returns a 405 if it's called with the wrong method,
etc.

You get the idea: Cornice takes care of the things we never think about,
and don't want to think about.


AngularJS for the client-side
=============================

I tried out `Ember.js <http://emberjs.com/>`_ and quickly disliked the way the
templating works in it, and the fact that they define objects for every
element you want to add in the DOM.

Cedric gave a more detailed comparison of `Ember vs Angular <http://beust.com/weblog/2012/12/29/migrating-from-ember-js-to-angularjs/>`_,
and I really liked how Angular looked, so I gave it a shot and
instantly liked it.

Angular will let you define new DOM directives, that get
expanded on the client side at runtime.

For the dashboard, it means I can define something like this::

    <dasboard server="http://data.marketplace.mozilla.org/">
        <chart title="Downloads" type="series" field="downloads_count"/>
    </dashboard>

And have a nice Highchart dashboard that grabs data out of the
Cornice server that's behind *http://data.marketplace.mozilla.org* (Fake URL!)

Defining directives in Angular is done by providing an HTML template
and a bit of Javascript glue code.

In our case we also make the **chart** directive a sub-directive
of the **dashboard** directive - here's an extract of the code so you
get an idea::

    var app = angular.module('components', []);

    app.directive('dashboard', function() {
        return {
            restrict: 'E',
        scope: {},
        transclude: true,
        controller: function($scope, $element, $attrs) {
            this.server = $scope.server = $attrs.server;
            var charts = $scope.charts = [];
            this.addChart = function(chart) {
                charts.push(chart);
            }
        },
        template:
        '<div class="tabbable">' +
        '<h3>Monolith Dashboard</h3>' +
        '<div class="tab-content" ng-transclude></div>' +
        '</div>',
        replace: true
        };
    });


Full code: https://github.com/mozilla/monolith/blob/master/monolith/media/app.js#L30

What I like about Angular is that it's easy to build something that's
based on a collection of *Plain Old Javascript Objects*, so I actually made a
separate library that takes care of creating a chart and interacting with the
server and the user, given a few tags ids:
https://github.com/mozilla/monolith/blob/master/monolith/media/lib/monolith.js#L194


On testing Javascript
=====================

I had no idea what was the state of the art for testing Javascript applications
since I am a backend developer, so I used what the Angular.js team use and partially built:
`Testacular <http://vojtajina.github.com/testacular/>`_ & `Jasmine <http://pivotal.github.com/jasmine/>`_.

Testacular is a nice command-line too that will spawn a Firefox instance and run your tests
in it. It has nice features like auto-running when a JS file changes, and you can
remote-controll it because it uses a Node.JS server to provide interactions.

Although, one thing that annoys me in Javascript (as opposed to Python), is the fact that it's
not easy to run processes in your tests fixtures.

What I needed to do is:

- run an Elastic Search server & add content in it
- run the Monolith Server
- then, run the JS tests.

In Python-land, all of this can happen in your test classes. In Javascript, unless
I missed the obvious, I had to wrap it in a Makefile: https://github.com/mozilla/monolith/blob/master/Makefile#L30

It's still a bit clunky because I cannot garantee the two servers are really stopped.
I should do something better. Maybe I'll end-up wrapping testacular in a Python unit tests... :)

Overall, I quite like building this kind of applications - and I think this pattern of
having a light Python web service on the server side, and some kind of JS MVC-based tool on
the client-side, is soon going to be the norm.


