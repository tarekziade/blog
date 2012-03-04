Title: Building Web Services with Pyramid
Date: 2011-10-21 16:14
Category: mozilla, python

### Using Pyramid for now on

  
Last year, when we started to write servers apps in Python at Mozilla
Services, we've built a light micro-framework on the top of WebOb and
Routes. That made a lot of sense back then because all our applications
were pure JSON web services --except the *reCaptcha* view we display
when you register in Sync--   
  
The framework just needed to route a request to a function and let us
do our work in ***pure Python*** from there.   
  
Given the nature of our apps, we did not pick an async framework for
the sake of code simplicity. And with Gevent, you still can boost a
synchronous app that's waiting for some I/O, [by making the socket layer
cooperative][]. IOW, making your synchronous app do some work
asynchronously transparently. And that works: The Sync server uses this
feature for SQL and LDAP queries, and is able to handle much more
concurrent requests that way.   
  
When we made the choice of WebOb/Routes, Pyramid was on my radar and
seemed like a good option too, but was still a bit new, so we just used
WebOb, knowing that a move to Pyramid would be quite easy since it's
based on it too.   
  
Today, Pyramid is quite spread and mature, and for developing Sagrada
components, it makes a lot of sense to adopt it. Having Ben Bangert and
Rob Miller in the team also made that choice natural : they're involved
in the project so they can sneak in our crazy patches ;)   
### Cornice - web service builder

  
Building web services for Sagrada, or for any project as a matter of
fact, should be as simple as possible for developers. In all the
frameworks I've used in the past, it was often requiring good chunks of
boiler-plate code, or I had to use some tools that were making too many
choices for me. For example, we want to build REST APIs, but sometimes
our APIs are not strictly REST, just REST-ish I would say :)   
  
In the past week, we've worked on a little extension called Cornice,
that tries to simplify as much as possible the usage of Pyramid to write
Web Services the way we like, with the experience we had writing Sync,
Account portal, Easy Setup, and all the other services that are
currently running in prod.   
  
The result is a simple class that can be used to define a service on
the server, then you can declare your APIs.   
  
Here's an extract taken from [demoapp][],   
   from collections import defaultdict

    from cornice import Service



    user_info = Service(name='users', path='/{username}/info')

    _USERS = defaultdict(dict)



    @user_info.get()

    def get_info(request):

        """Returns the public information about a **user**.



        If the user does not exists, returns an empty dataset.

        """

        username = request.matchdict['username']

        return _USERS[username]



    @user_info.post()

    def set_info(request):

        """Set the public information for a **user**.



        You have to be that user, and *authenticated*.



        Returns *True* or *False*.

        """

        username = request.matchdict["username"]

        _USERS[username] = request.json_body

        return {'success': True}

  
Please don't look at what the code does, it's crappy. The \_USERS stuff
should be in a Pyramid registry.   
  
But look at how I've defined my service: a ***Service*** instance for a
given path on our server, followed by two functions, one for the GET,
and one for the POST. By default, the APIs are returning JSON, but you
can change every option Pyramid offers when you declare a view.   
  
And once this is done, I also get for free a documentation page at***
/\_\_apidocs\_\_*** by grabbing the docstrings and also looking at the
various Service instance that were declared.   
  
[![image][]][]   
  
Cornice is just syntaxic sugar, but we might add a few extra features
late, maybe a fine-grained description of the params of each web
services, so we could publish a manifest that could be introspected.   
  
But it's good enough for people to start building Web Services for
Sagrada in a standard, easy-to-read, fashion. They just need to call a
***config.include('cornice')*** in their Pyramid app, and use the
***Service*** class.

  [by making the socket layer cooperative]: http://www.gevent.org/intro.html#monkey-patching
  [demoapp]: https://github.com/mozilla-services/demoapp/blob/master/demoapp/views.py
  [image]: http://ziade.org/cornice-apidocs.png "apidocs in action"
  [![image][]]: http://ziade.org/cornice-apidocs.png
