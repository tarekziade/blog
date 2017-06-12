Molotov, Arsenic & Geckodriver
##############################

:date: 2017-06-12 08:05
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade


`Molotov <http://molotov.readthedocs.io/>`_ is the load testing tool we're using
for stressing our web services at Mozilla QA.

It's a very simple framework based on asyncio & aiohttp, that will let you run
tests with a lot of concurrent coroutines. Using an event loop makes it quite
efficient to run a lot of concurrent requests against a single endpoint. Molotov
is used with another tool to perform distributed load tests from the cloud. But
even if you use it from your laptop, it can send a fair amount of load. On one
project, we were able to kill the service with one macbook sending 30,000
requests per second.

Molotov is also handy to run integration tests. The same scenario used to load
test a service can be used to simulate a few users on a service and make sure it
behaves as expected.

But the tool is able to only test HTTP(S) endpoints via aiohttp.Client, so if
you want to run tests through a real browser, you need to use a tool like
Selenium, or drive the browser directly via Marionette for example.

Running real browsers in Molotov can make sense for some specific use cases. For
example, you can have a scenario where you want to have several users interact
on a web page and have the JS executed there. A chat app, a shared pad, etc..

But the problem with Selenium Python libraries is that they are all written (as
far as I know) in a synchronous fashion. They can be used in Molotov of course,
but each call would block the loop and defeat concurrency.

The other limitation is that one instance of a browser cannot really be used by
several concurrent users. For instance in Firefox, even if Marionette is
internally built in an async way, if two concurrent scripts are trying to change
the active tab at the same time, that would break their respective scenario.

Introducing Arsenic
-------------------

By the time I was thinking about building an async library to drive browsers, I
had an interesting conversation with Jonas whom I met at Pycon Malaysia last
year. He was in the process of writing an asynchronous Selenium client for his
own needs. We ended up agreeing that it would be great to collaborate on an
async library that would work against the new `WebDriver
<https://www.w3.org/TR/webdriver/>`_ protocol, which defines HTTP endpoints a
browser can serve.

WebDriver is going to be implemented in all browsers and a library that'd use
that protocol would be able to drive all kind of browsers. In Firefox we have a
similar feature with Marionnette, which is a TCP server you can use to driver
Firefox. But eventually, Firefox will implement WebDriver.

Geckodriver is a small proxy we can use until Firefox has its WebDriver
implementation. Geckodriver is an HTTP server that translates WebDriver calls
into Marionette calls, and also deals with starting and stopping Firefox.

And Arsenic is the async WebDriver client Jonas started. It's already working
great. The project is here on Github: https://github.com/HDE/arsenic


Molotov + Arsenic == Molosonic
------------------------------

In order to use Arsenic with Molotov, I just need to pass along the event loop
that's used in the load testing tool, and also make sure that it runs at the
most one Firefox browser per Molotov worker. We want to have a browser instance
attached per session instance when the test is running.

The **setup_session** and **teardown_session** fixtures are the right place
to start and stop a browser via Arsenic. To make the setup even easier, I've
created a small extension for Molotov called `Molosonic
<https://github.com/tarekziade/molosonic>`_, that will take care of running a
Firefox browser and attaching it to the worker session.

In the example below, a browser is created every time a worker starts
a new session::

    import molotov
    from molosonic import setup_browser, teardown_browser

    @molotov.setup_session()
    async def _setup_session(wid, session):
        await setup_browser(session)

    @molotov.teardown_session()
    async def _teardown_session(wid, session):
        await teardown_browser(session)

    @molotov.scenario(1)
    async def example(session):
        firefox = session.browser
        await firefox.get('http://example.com')


That's all it takes to use a browser in Molotov in an asynchronous
way, thanks to Arsenic. From there, driving a test that simulates
several users hitting a webpage and interacting through it requires
some synchronization subtleties I will demonstrate in a tutorial
I am still writing.

All these projects are still very new and not really ready for
prime time, but you can still check out Arsenic's docs at
http://arsenic.readthedocs.io

Beyond Molotov use cases, Arsenic is a very exciting project
if you need a way to drive browser in an async program. And
async programming is tomorrow's stand in Python.

