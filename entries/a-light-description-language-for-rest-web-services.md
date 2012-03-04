Title: A light Description Language for REST web services ?
Date: 2011-02-14 01:07
Category: mozilla, python

**tldr**: I have this idea that comes back and forth in my head since a
few months now, working on the Sync, Easy Setup and Identity servers. I
want to create a light DL to describe what REST web services an
application implements, and use it to automate the request dispatching
but also the documenting and testing of the services.   
  
When we create web services, there's a lot of things we do that are
quite systematic:   
1.  Describe the web services in a document.
2.  Define what code should be executed.
3.  Validate and transform incoming requests and outgoing responses.
4.  Run functional and security tests on the web services.

  
### 1. Describe the web services (=API)

  
Documenting the web services the application needs to offer is the
first step to build it. A document needs to list the URL paths, the
methods to use, what goes it and comes out.   
  
For the Easy Setup server (a.k.a the J-Pake server), I've documented an
initial design of the web services here:
[https://wiki.mozilla.org/Services/Sync/SyncKey/J-PAKE\#Server\_API][]
and we worked with Stefan and Philipp to refine the design iteratively.
  
  
Once the application is built, that's a non implementation-specific
description that anyone can use to build a new client that interacts
with our server.   
### 2. What code should be executed ?

  
The next step is to build the code that does the job. On a request, we
need to define what piece of code should be called to build a response
and execute it in order to return a response.   
  
It can be a set of regexps managed by dispatcher tool, which output --
That's [Routes][]. It can also be a simple function decorator -- That's
[Bottle][]. Some other approaches are consisting of using the code
namespace to dispatch the request, like implementing the
*Root.get\_index* method for a GET on the /index url.   
  
At Services, we use Routes and feed it with a list that contains a
description of the URLs. See this example:
[http://hg.mozilla.org/services/server-storage/file/78762deede5d/syncstorage/wsgiapp.py\#l65][].
  
### 3. Validate & Filter Requests and Responses

  
Beside the feature code itself, the application usually do a series of
validation or/and transformation on the incoming request -- like
checking its headers, or extracting objects from a JSON body. This can
also be done on the outgoing responses.   
  
Those steps are usually generic enough to be reused for all web
services. And those steps, most of the time, should not be implemented
as WSGI Middlewares -- *one simple question to ask yourself to know if
you should create /use a middleware: does your application breaks if you
remove that middleware ? If so, it means that your application may not
work without the middleware, thus it should become a library on which
the application has a hard dependency.*   
  
Some Examples:   
-   an authorization function that checks the *Authorization* header and
    set in the execution context a user name.
-   a function that controls that the body contains parseable JSON, and
    unserialize it in the execution context.
-   a function that serialize all response bodies into JSON

  
### 4. Create functional and security tests

  
Like I said in *1.*, building a new client against the server should be
possible simply by reading the documentation.   
  
That's how we build our functional test suite, which runs for each web
service a series of requests, and checks that the responses are the ones
expected. These tests are simply validating that the server acts as
documented.   
  
Depending on the security expectations, another series of tests can
check for the server behavior when it receives unexpected responses.   
### A light, implementation-specific, DL

  
So, the idea would be to describe everything in a static file, that can
be used:   
-   by the **application** to:   
   -   automatically dispatch the requests to some callable
    -   execute some functions before and after the main callable, to
        transform and filter data

      
-   by the **testers** to use a generic HTTP client powered by the DL
    file.
-   by the **documentation** to generate an HTML or Wiki version of that
    DL file.

  
After investigation, I found [WADL][] and got scared. That's probably
the XML effect :D   
  
WADL is very close to what I am looking for, see an [example][]. But
while less complex than WSDL, it still seems a bit overkill for what I
want to do. I am not sure for instance, that I want to fully describe
the structure of the responses. And well, WADL is only documenting the
web services, and not pointing the code that implements them.   
  
I want to do both things in the DL, and keep implementation-specific
parts light enough that they will not really annoy anyone. But they're
still useful when your not in the application itself: for example, a
wiki output could link to an online view of the code that's used.   
  
Here's a *(very quick)* draft in pseudo-YAML out of my head:   
   POST "/the/webservice/is/here":

      id: cool_service

      description: The cool service does this and that.



      request:

        headers:

          Authorization: description of the supported token etc.

        body: explains here what the body should contains     



      response:

        body: explains what the body contains

        headers:

           Header-1: description of that header

        content-type: application/json

        codes:

          200: explains here what getting a success means

          503: explains here when you might get a 503

          400: explains here when it's a bad request  



      implemented_by: module.class.method,

      pre-hooks:

          authenticate

          extract_json_from_body

      post-hook:

          jsonify

  
The first part is really, documenting your web service.   
  
But it's also detailed enough to be able to automatically create an
HTTP client that can be the basis for tests. e.g.:   
   def post_cool_service(body, authorization):

        """The cool service does this and that.



       Arguments:

           Authorization: description of the supported token etc.

           body: explains here what the body should contains     



       Returns:  code, body, headers



        """

        ... generic curl-y code...

  
Not sure about the generative aspect though, because it's hard to
maintain. Maybe a dynamic introspection of the DL file is a better idea
here...   
  
The second part tells the server what code should be run, something
that would be similar than:   
   def cool_service(request):

        """The cool service"""

       authenticate(request)

       extract_json_from_body(request)

       response = module.class.method(request)

       return jsonify(response)

  
In other word, I could strip all the boiler-plate code I have around
the code that implements the features themselves, and just combine them
with a few helper functions via the DL.   
  
This approach is quite similar to Zope's ZCML glue, but without the ZCA
layer --which I tend to find heavy and overkill--

  [https://wiki.mozilla.org/Services/Sync/SyncKey/J-PAKE\#Server\_API]: https://wiki.mozilla.org/Services/Sync/SyncKey/J-PAKE#Server_API
  [Routes]: http://routes.groovie.org/
  [Bottle]: http://bottle.paws.de/docs/dev/index.html
  [http://hg.mozilla.org/services/server-storage/file/78762deede5d/syncstorage/wsgiapp.py\#l65]:
    http://hg.mozilla.org/services/server-storage/file/78762deede5d/syncstorage/wsgiapp.py#l65
  [WADL]: http://en.wikipedia.org/wiki/Web_Application_Description_Language
  [example]: http://www.w3.org/Submission/wadl/#x3-40001.3
