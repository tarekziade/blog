Title: Anatomy of a Web Service, part 2 - &quot;RedBarrel&quot;
Date: 2011-06-17 15:14
Category: mozilla, python

*I was talking about web services the other day: [read it back][] as an
introduction to this post.*   
  
I am pursuing this DSL experiment as I have now finished a working
prototype of a micro-framework. I've called it RedBarrel ([Monty
reference][]). I've called the DSL files "RBR files".   
  
RedBarrel is a pure Python implementation of the DSL I've described in
the previous post and does the following:   
-   loads the DSL file and run a WSGI web application (via ***rb-run***)
-   Allows you to check the syntax of an RBR file (via ***rb-check***)
-   generates a documentation page for the APIs at **/\_\_doc\_\_ **Note
    that ***description*** fields can be in reStructuredtext and are
    rendered in HTML
-   publishes the DSL file at ***/\_\_api\_\_***
-   runs the code pointed in the DSL and does the post- and pre-
    processing as described

  
Here's an example of a web service, that capitalizes the string you
sent to it -- and requires authentication and json input.   
   define path capitalize (

        description "A web service with several post/pre processing",

        method POST,

        url /capitalize,

        use python:redbarrel.demos.capitalize,



        response-status (

            describe 200 "Success",

            describe 400 "The request is probably malformed",

            describe 401 "Authentication failure"

        ),



        request-body (

            description "Send a string in json and the server returns it Capitalized.",

            unless type is json return 400

        ),



        request-headers (

            unless Authorization validates with redbarrel.demos.auth return 401

        ),



        response-headers (

            set content-type "application/json"

        ),



        response-body (

            description "The string, Capitalized !",

            unless type is json return 503

        )

    );

  
[caption id="attachment\_1862" align="alignleft" width="542"
caption="The /\_\_doc\_\_ page in RedBarrel"][![image][]][][/caption]   
  
The one thing I am not entirely sure about yet, is if I want to provide
helpers to instantiate some objects in memory when the server starts.
That's useful when you want to keep a DB connector open or simply avoid
initializing many things on every request. But that's very easy to
implement with global variables... Maybe an "application context" could
be created, for some functions to add objects inside.   
  
Anyways, I've started to re-write a few web services to see how the DSL
fits, and so far it looks useful: I have reduced a lot the boiler-plate
code and the API is self-documented.   
  
The code is *still* at [Bitbucket][] and I am looking for some feedback
or other people that are writing web services that want to experiment
with it !

  [read it back]: http://tarekziade.wordpress.com/2011/06/09/anatomy-of-a-web-service/
  [Monty reference]: http://orangecow.org/pythonet/sketches/package.htm
  [image]: http://tarekziade.files.wordpress.com/2011/06/barrel.png
    "The /__doc__ page in RedBarrel"
  [![image][]]: http://tarekziade.files.wordpress.com/2011/06/barrel.png
  [Bitbucket]: https://bitbucket.org/tarek/redbarrel
