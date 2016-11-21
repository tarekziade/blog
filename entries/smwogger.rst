Smoke testing Swagger-based Web Services
########################################

:date: 2016-11-21 15:11
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade


`Swagger <http://swagger.io/>`_ has come a long way. The project got renamed
("Open API") and it seems to have a vibrant community.

If you are not familiar with it, it's a specification to describe your HTTP
endpoints (`spec here <http://swagger.io/specification/>`_) that
has been around since a few years now ~ and it seems to be
getting really mature at this point.

I was surprised to find out how many available tools they are now. The
`dedicated page <http://swagger.io/tools/>`_ has a serious lists of tools.

There's even a Flask-based framework used by Zalando to build microservices.

Using Swagger makes a lot of sense for improving the discoverability and
documentation of JSON web services. But in my experience, with these kind of
specs it's always the same issue: unless it provides a **real** advantage
for developers, they are not maintained and eventually removed from projects.

So that's what I am experimenting on right now.

One use case that interests me the most is
to see whether we can automate part of the testing we're doing at Mozilla
on our web services by using Swagger specs.

That's why I've started to introduce Swagger on a handful of
projects, so we can experiment on tools around that spec.

One project I am experimenting on is called **Smwogger**, a silly
contraction of **Swagger** and **Smoke** (I am a specialist of
stupid project names.)

The plan is to see if we can fully automate smoke tests against
our APIs. That is, a very simple test scenario against a deployment,
to make sure everything looks OK.

In order to do this, I have added an extension to the spec, called **x-smoke-test**,
where developers can describe a simple scenario to test the API
with a couple of assertions. There are a couple of tools like that already,
but I wanted to see whether we could have one that could be 100% based
on the spec file and not require any extra coding.

Since every endpoint has an operation identifier, it's easy enough
to describe it and have a script (==Smwogger) that plays it.

Here's my first shot at it... The project is at https://github.com/tarekziade/smwogger
and below is an extract from its README


Running Smwogger
================

To add a smoke test for you API, add an **x-smoke-test** section
in your YAML or JSON file, describing your smoke test scenario.

Then, you can run the test by pointing the Swagger spec URL
(or path to a file)::

    $ bin/smwogger smwogger/tests/shavar.yaml
    Scanning spec... OK

            This is project 'Shavar Service'
            Mozilla's implementation of the Safe Browsing protocol
            Version 0.7.0


    Running Scenario
    1:getHeartbeat... OK
    2:getDownloads... OK
    3:getDownloads... OK

If you need to get details about the requests and responses sent, you can
use the **-v** option::

    $ bin/smwogger -v smwogger/tests/shavar.yaml
    Scanning spec... OK

            This is project 'Shavar Service'
            Mozilla's implementation of the Safe Browsing protocol
            Version 0.7.0


    Running Scenario
    1:getHeartbeat...
    GET https://shavar.somwehere.com/__heartbeat__
    >>>
    HTTP/1.1 200 OK
    Content-Type: text/plain; charset=UTF-8
    Date: Mon, 21 Nov 2016 14:03:19 GMT
    Content-Length: 2
    Connection: keep-alive

    OK
    <<<
    OK
    2:getDownloads...
    POST https://shavar.somwehere.com/downloads
    Content-Length: 30

    moztestpub-track-digest256;a:1

    >>>
    HTTP/1.1 200 OK
    Content-Type: application/octet-stream
    Date: Mon, 21 Nov 2016 14:03:23 GMT
    Content-Length: 118
    Connection: keep-alive

    n:3600
    i:moztestpub-track-digest256
    ad:1
    u:tracking-protection.somwehere.com/moztestpub-track-digest256/1469223014

    <<<
    OK
    3:getDownloads...
    POST https://shavar.somwehere.com/downloads
    Content-Length: 35

    moztestpub-trackwhite-digest256;a:1

    >>>
    HTTP/1.1 200 OK
    Content-Type: application/octet-stream
    Date: Mon, 21 Nov 2016 14:03:23 GMT
    Content-Length: 128
    Connection: keep-alive

    n:3600
    i:moztestpub-trackwhite-digest256
    ad:1
    u:tracking-protection.somwehere.com/moztestpub-trackwhite-digest256/1469551567

    <<<
    OK


Scenario
========

A scenario is described by providing a sequence of operations to
perform, given their **operationId**.

For each operation, you can make some assertions on the
**response** by providing values for the status code and some
headers.

Example in YAML ::

    x-smoke-test:
      scenario:
      - getSomething:
          response:
            status: 200
            headers:
              Content-Type: application/json
      - getSomethingElse
          response:
            status: 200
      - getSomething
          response:
            status: 200

If a response does not match, an assertion error will be raised.


Posting data
============

When you are posting data, you can provide the request body content in the
operation under the **request** key.

Example in YAML ::

    x-smoke-test:
      scenario:
      - postSomething:
          request:
            body: This is the body I am sending.
          response:
            status: 200


Replacing Path variables
========================

If some of your paths are using template variables, as defined by the swagger
spec, you can use the **path** option::


    x-smoke-test:
      scenario:
      - postSomething:
          request:
            body: This is the body I am sending.
            path:
              var1: ok
              var2: blah
          response:
            status: 200

You can also define global path values that will be looked up when formatting
paths. In that case, variables have to be defined in a top-level **path**
section::

    x-smoke-test:
      path:
        var1: ok
      scenario:
      - postSomething:
          request:
            body: This is the body I am sending.
            path:
              var2: blah
          response:
            status: 200


Variables
=========

You can extract values from responses, in order to reuse them in
subsequential operations, wether it's to replace variables in
path templates, or create a body.

For example, if **getSomething** returns a JSON dict with a "foo" value,
you can extract it by declaring it in a **vars** section inside the
**response** key::

    x-smoke-test:
      path:
        var1: ok
      scenario:
      - getSomething:
          request:
            body: This is the body I am sending.
            path:
              var2: blah
          response:
            status: 200
            vars:
              foo:
                query: foo
                default: baz

Smwogger will use the **query** value to know where to look in the response
body and extract the value. If the value is not found and **default** is
provided, the variable will take that value.

Once the variable is set, it will be reused by Smwogger for subsequent
operations, to replace variables in path templates, or to fill response data.

The path formatting is done automatically. Smwogger will look first at
variables defined in operations, then at the path sections.


Conclusion
==========

None for know. This is an ongoing experiment. But happy to get your feedback
on github!


