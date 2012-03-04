Title: Cornice -- web services with Pyramid
Date: 2011-11-29 11:18
Category: mozilla, python

Since we've [initially started Cornice at Services][], we had more
discussion about how we could make it easier for developers to validate
an incoming request.   
  
Our goal is :   
-   to be able to validate a request and if needed, to convert it to
    specific data structures
-   to complete the documentation of our web services in Sphinx with
    those validation steps

  
Here's a concrete example: A *PUT* request used to create a user in a
database should come as a JSON object in the request body, which content
would be validated and turned into a Person object, then sent to a SQL
backend.   
  
The web service needs in that case to reject any malformed request with
a 400, and we'd also want to document this constraint in the web service
documentation.   
  
There are some existing tools in the validation arena, like
[FormEncode][] or [Colander][].   
  
FormEncode and Colander both provide data validation via schemas, and
FormEncode offers HTMLform generation.   
  
When you need to validate an incoming request in your web service,
those tools can fit your needs or simply be overkill. So, we wanted to
integrate a validation step in Cornice without forcing the usage of a
specific validation tool.   
### A simple callable

  
What we did is added a *validator* option that needs to point to a
callable. The callable receives the request object and has to return an
HTTP error code followed by a reason in case the request does not
comply.   
  
Here's an example, a ***GET /foo*** that will return a 402 if the***
X-Paid*** header is missing :   
       from cornice import Service



        foo = Service(name='foo', path='/foo')



        def has_paid(request):

            """The request must have an X-Paid header containing a token.



            This header proves the user has paid

            """

            if not 'X-Paid' in request.headers:

                return 402, 'You need to pay !'



        @foo.get(validator=has_paid)

        def get_value(request):

            """Returns the value.

            """

            return 'Hello'

  
From there, Cornice will call *has\_paid* prior to *get\_value*.
Cornice is also able to build the documentation of the web service, by
merging the docstrings of *get\_value* and *has\_paid*.   
### Sphinx integration

  
We provide a Sphinx extension for documenting a Cornice based project.
You can inject in your Sphinx document the web service description, via
a ***service*** directive.   
   .. services::

       :package: demoapp

  
In this example, the directive looks for all Cornice definitions in the
***demoapp*** package by scanning it, and injects their documentation in
the Sphinx document.   
  
The service directive provides a few options. For instance the
***name*** option will let you inject the documentation of one specific
web service.   
### Colander integration

  
I said earlier simple callables where good enough for simple validation
cases. Let's take a more complex example.   
  
Let's say, you have a ***Person*** schema in Colander, that defines a
person's attributes -- [See Colander docs for details][].   
  
And you want to provide a ***PUT*** Web Service to create a person,
where the request body is the person data serialized in JSON.   
  
Here's the full Cornice definition   
      from cornice import Service

       from cornice.schemas import save_converted, get_converted



       def check_person(request):

          """The request body must be a JSON object describing the Person"""

          try:

              person = json.loads(request)

          except ValueError:

              return 400, 'Bad Json data!'



          schema = Person()

          try:

              deserialized = schema.deserialized(person)

          except InvalidError, e:

               # the struct is invalid

               return 400, e.message



          save_converted(request, 'person', deserialized)



        service = Service(name='person', path='/person/{id}')



        @service.put(validator=check_person)

        def data_posted(request):

            person = get_converted(request, 'person')

            ... do the work on person ...

  
In this example, the validator checks that the request body is valid
Json, then pass the unserialized mapping to Colander to check that it's
a valid Person record. Last, it uses the ***save\_converted*** function
we provide, to save the Person object into the request.   
  
The web service then can pick it up with the ***get\_converted***
function.   
### Next Steps

  
Our next steps is to build a library of useful built-in validators.
Things like:   
-   is the request body is JSON ?
-   do we have param X, if yes is it an integer ?
-   any reusable validator we'll think about

  
The final goals here are :   
1.  have our web services code written in two phases: the validation
    phase, and the code itself. Because they are a lot of reusable bits
    in that first phase.
2.  reuse as much as possible docstrings to document our web services,
    to avoid the *doc-is-not-up-to-date-anymore* plague

  
You can follow the development of Cornice here:
[https://github.com/mozilla-services/cornice][]   
  
And even participate by joining our Mailing List:
[https://mail.mozilla.org/listinfo/services-dev][]

  [initially started Cornice at Services]: https://tarekziade.wordpress.com/2011/10/21/building-web-services-with-pyramid/
  [FormEncode]: http://www.formencode.org/en/latest/index.html
  [Colander]: http://docs.pylonsproject.org/projects/colander/en/latest/
  [See Colander docs for details]: http://docs.pylonsproject.org/projects/colander/en/latest/basics.html#defining-a-schema-imperatively
  [https://github.com/mozilla-services/cornice]: https://github.com/mozilla-services/cornice
  [https://mail.mozilla.org/listinfo/services-dev]: https://mail.mozilla.org/listinfo/services-dev
