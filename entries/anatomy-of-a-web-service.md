Title: Anatomy of a Web Service
Date: 2011-06-09 09:34
Category: mozilla, python

This is [cycling in my head][] for a while now, and I think it's close
to become something concrete.   
  
Let me summarize the idea: web services are most of the time doing the
same post- and pre-processing tasks over and over and there should be a
way to describe them via a DSL.   
  
Nothing revolutionary here, but what if Nginx could handle for you all
the boring parts and let you just handle the meat of your services.
Having a DSL to describe web services potentially allows such
delegation.   
### Anatomy of a Web Service

  
A Web Service is basically doing these four steps:   
1.  [**pre-processing**] Check the request body and headers, and
    potentially reject it. Rejection can be due to a Basic
    Authentication failure, an unexpected value for the request body,
    etc.
2.  [**routing**] Find what code or application should be called to
    build the response. This is usually computed with the path
    information and sometimes some headers.
3.  [**execution**] Invoke the code to build the response
4.  [**post-processing**] Return the response built and maybe do some
    post-processing or post-assertions like converting the content-type
    etc.

  
Steps **1.**, **2.** and **4**. could be delegated to a proxy as long
as it has enough details on what should be done.   
  
In Python, when you build web services using a WSGI framework like
Pylons, Pyramid, or simply Routes + WebOb, all of these steps happen in
your code. You define the **routing** using Routes descriptions, or
using more clever dispatching systems like what Pyramid offers, then
delegate the **execution** to a controller class or a simple function,
after a potential **pre-processing**. Although the pre-processing part
is often merged with the execution part because they are closely
related.   
  
For instance, if you have a web service that requires a JSON mapping in
the request body, you could write something that looks like:   
   def my_webservice(request):

        try:

            data = json.loads(request.body)

        except ValueError:

            raise HTTPBadRequest("Unknown format -- we want JSON")   # this raises a 400

        ... do something ...

  
Of course you can always generalize this by using a decorator to
clearly separate the pre-processing part:   
   @if_not_json(400)

    def my_webservice(request):

        ... do something ...

  
Same thing for the post-processing step:   
   @if_not_json(400)

    @convert_output('application/json')

    def my_webservice(request):

        ... do something ...

  
Err... well, in some [frameworks][], the routing itself is expressed as
a decorator:   
   @route('/here/is/my/webservice')

    @if_not_json(400)

    @convert_output('application/json')

    def my_webservice(request):

        ... do something ...

  
It turns out that there are a lot of pre/post steps that can be pushed
to a meta level.   
### Delegation of pre- and post-processing steps

  
A web application is most of the time accessed through a proxy. At
Mozilla Services, [we use Nginx for all our Python applications][].
NGinx is here --among other things-- to pool incoming requests and
dispatch them to our Python application. The proxying job is pretty dumb
right now, as everything that comes in is directly sent to the Python
backend.   
  
What if we were able to delegate all the pre- and post-processing we've
seen earlier to NGinx ?   
  
There would be some benefits, like a faster rejection of bad requests:
no need to invoke the Python application anymore and spend CPU cycles in
a backend for this. If some pre-requisites are not met, we can 400 right
away.   
  
Having all the pre-processing at the proxy level also make it simpler
to modify them without touching the web service code itself. That can be
a default as well of course in some cases : your application logic is
split in two parts and this can be hard to follow. But as long as the
full description of the web service is in a single place, I think it's
fine.   
  
Last, we've talked about Python, but each piece could be implemented in
a different language, as long as NGinx is able to invoke it. Using Lua
for all the pre-processing part is not a bad idea..   
### The DSL

  
The last time I've talked about this topic, someone talked about
[SPORE][] which is indeed quite similar to what I want to achieve. I
guess the biggest difference is that SPORE focuses on providing a DSL to
build clients that can interact with an existing set of server APIs.   
  
What I want on my side is to provide a DSL API developers can use to
create web services, and eventually have a proxy like NGinx use it to
run the application.   
  
A developer ideally would:   
1.  describe her web services in a DSL file
2.  implement the execution part
3.  test them in a development environment where a web server would load
    the DSL and the code
4.  deploy the web service in production with NGinx

  
I could start off with SPORE but I want to experiment with my own DSL
and build it little by little.   
  
I started to build it the other week-end, and it looks like this:   
   define path hello (

        description "Simplest app",

        method GET,

        url /,

        use python:demos.hello

    );



    define path counter (

        description "A counter",

        method GET,

        url /count,

        use python:demos.counter

    );



    define path html (

        description "An html page",

        method GET,

        url /index.html,

        use python:demos.html,

        response-headers (

            set content-type "text-html"

        )

    );



    define path service (

        description "A web service that 400 if the body is not json",

        method POST,

        url /post,

        use python:demos.post,

        request-body (

            unless type is json return 400

        )

    );

  
Some details:   
-   *python:demo.post* means here: the code to be invoked is located in
    the "demo.post" callable - that's the fully qualified name to reach
    it, so demo can be a package, or a module.
-   *unless type is xxx return xxx* is a full part of the DSL, a
    recognized structure. When parsing the file, it's loaded in an AST
    and executed on each request against the body.

  
### Implementation details

  
I used [PLY][] to read the DSL files, and it'll check many aspects of
the DSL file like:   
-   make sure the method is known (GET/POST/etc)
-   make sure the HTTP codes used are valid ones
-   control that the URL path is valid
-   etc.

  
I wrote a small Python application that loads the DSL file at startup
in an AST. Then it provides a web server that will do the
post/pre-processing, and eventually delegate the execution to some
Python code, by passing a request object using WebOb. The URL is for now
using a simple regexp pattern backed by Routes.   
  
I've also wrote:   
-   a script that validates a DSL file
-   a \_\_doc\_\_ web page in the small Python server, that displays the
    available web services
-   an \_\_api\_\_ page that just publish the DSL file for client-side
    discovery. (fwiw)

  
You can have a look at the ugly code of the prototype here:
[https://bitbucket.org/tarek/redbarrel][]   
  
The next steps in this experiment will be to rewrite one of our small
Services app with it, and see how it comes out.   
  
All in all, I am having a lot of fun doing this, and it's eating some
of the free time I have when I should be really doing some work on
Python packaging... meh ...

  [cycling in my head]: https://tarekziade.wordpress.com/2011/02/14/a-light-description-language-for-rest-web-services/
  [frameworks]: http://bottlepy.org/docs/dev/
  [we use Nginx for all our Python applications]: http://docs.services.mozilla.com/server-devguide/overview.html
  [SPORE]: http://lumberjaph.net/misc/2010/09/17/spore.html
  [PLY]: http://www.dabeaz.com/ply/ply.html
  [https://bitbucket.org/tarek/redbarrel]: https://bitbucket.org/tarek/redbarrel
