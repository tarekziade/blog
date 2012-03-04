Title: Sagrada - Creation and Hosting of Web Services
Date: 2011-09-22 16:01
Category: mozilla, python

### tl;dr

  
I am building for [Sagrada][] a web application that can be used to
create and deploy web services through the web with a few Python
functions.   
  
[See the prototype demo quick screencast][] -- If you can't view it in
your browser, download it and use VLC -- The music is [MC Jack IN the
Box CC-AN 3.0][]   
  
***EDIT*** Here's a better demo, with Ace integration, where you can
edit/create Python files in the browser --
[http://ziade.org/redbarrel4.mpeg][]   
  
Now read below for the long story :)   
### The Sagrada Project

  
We had a all-hands last week in San Jose, which gathered +600
Mozillians (yes, we're growing fast).   
  
My team has started to brainstorm about Sagrada, the big project we're
starting, and I've started to think about a few topics.   
  
One long term goal of Sagrada is to let developers deploy on our
servers their own web services. It's quite hard to put a strict
definition for the term "web service", but the term is usually used
these days to describe a server-side application that can be queried via
the HTTP protocol, receiving and sending back Json objects.   
  
So, the intent is to provide a **Service Container** for developers
that need a server side for their applications.   
  
The server side of Firefox Sync is a good example: It's a set of web
services Firefox calls to power Sync. [See the API definitions here][].
  
  
For Sagrada the specific question I am interested to solve is :   
  
** What would be the easiest way to write and deploy web services into
our infrastructure ?**   
  
To start off, here are a few assumptions I am making about what
developers would probably expect from this kind of service -- *but those
are my own assumptions, and will change with the feedback I'll get in
the process* :   
  
**1. Building and deploying a web service should be easy to do whether
you are a Python programmer or a JavaScript programmer.**   
  
While Python is our main target, being able to write JavaScript on
server side should also be a goal -- *And if the tool is extensible
enough, why not other languages in the future ?*   
  
Moreover, most steps when building web services are not specific to a
language. For instance, describing what HTTP method should be used,
what's the web service URL, what kind of request body is expected, etc,
is usually done in a specification document.   
  
For example, when I've built the Easy Setup server for Sync, I've
written this specification document :
[http://docs.services.mozilla.com/keyexchange/apis.html][]   
  
It contains a description of each web service used by Firefox when you
add a new device to your Sync account. The only thing that is not
expressed in this document is the just the piece of code that does the
job.   
  
So, what if this document could be used directly by the server to run
the application ? The only thing that would miss is a few functions.   
  
The bottom line is that web services can be described in a [Domain
Specific Language][] (DSL) that can be used to generate the
documentation automatically (and it stays accurate and up to date) but
also to set up in the server things we usually do on the code side: the
request dispatching.   
  
In that case, the portion of code to write is reduced to building the
response itself.   
  
Even if we just support Python in a v1, if building a web service boils
down to writing a specification document, and a few Python functions to
build responses, I think that lowers the barrier enough for most
developers.   
  
And if we hide the DSL behind a nice user interface developers can use
to build their apps, that's even better. That's what's happening in the
screencast I've recorded. The forms generate portions of DSL.   
  
**2. The tool should be framework-agnostic if possible.**   
  
While tools like [Node.js][] or [Pyramid][] or *<put your favorite
framework here\>* provide great features to write web apps, web services
people will build will be running in specific environments, where we
will want to set up and control our own stack.   
  
In other words, we'll want to isolate as much as possible the code
written by developers.   
  
Ideally, we'd just pass a request to a function and ask for a response.
Python for instance has a CGI-like standard called [WSGI][], where the
request is described in a mapping and the response is a sequence of
string + a mapping of headers.   
  
So telling developers: *"Hey, your function will receive a WSGI
request, send me back a WSGI response"*, sounds like a good basis.   
  
I am pretty sure we can do the same in Javascript. And if we don't have
such standard in Javascript, let's create it.   
  
**3. The tool should provide a Web UI, and CLI and a standalone
server.**   
  
Web services should not be locked in our servers, developer should be
able to edit them through the web, or via the console even if it's
remote. They should be able to upload or download their apps in our
environment, like what they would do with [Google App Engine][].   
  
But they should also be able to create, run their apps on their own
environment e.g. have a independent web server that can run their
services. Not a toy server used for development only, but something they
can really deploy in production.   
  
For the remote console, [Benoit][] was telling me this morning: why not
[iPython][] ? I dig this: editing web services through iPython would
rock. If you don't know about this tool check it out it's amazing. It
provides among other things, a way to build an interactive shell for a
distant app.   
### A web service DSL

  
Back to our DSL. When you write a web service, it's always the same
story no matter what framework you're using, you're basically doing
these steps (I am over-simplying for now)   
1.  Define a route for your service on the server
2.  Build the response
3.  Send back the response

  
These steps can be described in a simple DSL.   
  
Here's a basic example:   
>   
>     path hello_world (
>
>      description "Simplest application: Hello World!",
>
>      method GET,
>
>      url /hello,
>
>      use python:somemodule.hello
>
>      );
>
>   

  
With a function *hello* located in *somemodule* that can look like this
:   
   def hello(request):

        return 'Hello World'

  
The application in that case is composed of   
-   a DSL file
-   a Python file with a single function

  
It's easy from there with the proper DSL parser to:   
-   deploy those two files in our infrastructure
-   run the app
-   provide auto-generated documentation for the service

  
### Architecture

  
The prototype I've written for the demo does the following:   
-   The tool is a web application that provides forms to create Service
    Containers
-   Each Service Container has a unique root on the server
-   In each container you can add web services.
-   For each container, the DSL is built on the fly, then the
    corresponding AST is kept in memory. The web UI allow users to
    modify it on the fly
-   When a request comes in, it's rooted to the right Service Container
    depending on the beginning of the path, then the AST is used to find
    out what function(s) should be used. The function is then executed
    in a sandbox.

  
The prototype also provides a command-line tool to start a server by
loading an arbitrary DSL file.   
### The DSL Parser

  
I will not go in to great details here, you can look at my previous
posts mentioning **RedBarrel**.   
  
The current DSL is implemented with [PLY][] and can be found [here][].
  
### Sandboxing the code

  
One thing we want to do when a developer uploads some code that is
potentially going to be executed, is to sandbox it.   
  
This is not really for security reasons, because we'll still need to
protect our users by setting up VMs. This is mostly to   
pre-configure what the user is allowed to do in the code and provide
some useful feedback when he's doing things   
we did not allow, like writing to the filesystem or using sockets *-- I
am not saying we will allow or disallow these*   
* particular ones, I don't know yet.*   
  
In the current prototype, I've used [pysandbox][] from Victor Stinner .
It's used to load and execute the uploaded code.   
see [how I use it][].   
### What's Next

  
Right now the web interface to build an application is simplistic
compared to what the DSL can do. For instance you could chain several
functions to perform pre- and post- processing for a request. So some
functions can be reused in several services, like authentication.   
  
Also, we want to provide our own Mozilla libs, like a way to
authenticate against our own user database, or use a key-value storage.
Basically, all the libraries we're currently building for Sagrada.   
  
It's unclear at this point what imports we will allow in the scripts,
and how we will publish our own libraries people will be able to use. I
intend to clarify these in the upcoming days, and enhance the prototype
to allow it to do more things.   
  
Also, I'd like to write the Easy Setup server using this tool. I'll
also try to organize a coding/brainstorming sprint since I have 5/6
people that worked with me on these topics to hack on this.   
  
If you are interested or have some feedback, please comment !

  [Sagrada]: https://wiki.mozilla.org/Services/Roadmaps/Server/Sequence
  [See the prototype demo quick screencast]: http://ziade.org/redbarrel3.mpeg
  [MC Jack IN the Box CC-AN 3.0]: http://ccmixter.org/files/mcjackinthebox/33612
  [http://ziade.org/redbarrel4.mpeg]: http://ziade.org/redbarrel4.mpeg
  [See the API definitions here]: http://docs.services.mozilla.com/storage/apis-1.1.html
  [http://docs.services.mozilla.com/keyexchange/apis.html]: http://docs.services.mozilla.com/keyexchange/apis.html
  [Domain Specific Language]: https://secure.wikimedia.org/wikipedia/en/wiki/Domain-specific_language
  [Node.js]: http://nodejs.org/
  [Pyramid]: https://www.pylonsproject.org/
  [WSGI]: http://www.wsgi.org/en/latest/index.html
  [Google App Engine]: https://code.google.com/appengine/
  [Benoit]: https://twitter.com/#!/benoitc
  [iPython]: http://ipython.org/
  [PLY]: http://www.dabeaz.com/ply/
  [here]: https://bitbucket.org/tarek/redbarrel/src/9f466fd5c2eb/redbarrel/dsl/parser.py
  [pysandbox]: http://pypi.python.org/pypi/pysandbox/
  [how I use it]: https://bitbucket.org/tarek/redbarrel/src/9f466fd5c2eb/redbarrel/libraries.py
