Title: The fear of CRUD
Date: 2012-01-03 00:17
Category: mozilla, python

[Cornice][] is growing steadily, and we are thinking about the different
ways to use it for our needs. One use case that comes often when we
build web services is the need to publish a SQL Database via HTTP.   
  
For instance, in a project I am working on, we might expose a list of
servers and some information about them, that are stored in a SQL DB .
The goal is to allow some management scripts to interact with the DB, to
set and retrieve information about the servers, like: "can I use *server
12* as a node for *application X* ?"   
  
Interacting with CURL or a similar tool is simpler and more portable
than coding yet another SQL client for this, so the idea is to see how
this kind of web service can be done is the minimum pain with Cornice.   
  
What I am thinking about building is a small [CRUD][] interface that
glues Cornice and SQLAlchemy. The latter has a way to define a database
schema explicitly via [*mappings*][] meaning that it's easy to write a
generic layer that exposes the database to the web via Cornice
definitions. The work consists of transforming POST & PUT requests that
contains data to write to the DB into SQLAlchemy objects, and
transforming select results asked via GET requests into the proper
responses.   
  
Nothing very new, there are tons of existing systems that implement
CRUD on the top of [ORMs][] or plain SQL libraries. The only reason to
build yet another one is to use it in the context of our current toolset
which is composed of Cornice, Pyramid & SQLAlchemy for most projects.
The whole code will probably be less than 300 lines at the end anyways.
  
  
***Oh my**.*   
  
Turns out this idea is really freaking out some people around me.
There's a strong aversion of some coders against anything that looks a
bit like [Active Records][] -- in the Rails Context. In other words
anything that would completely automate the serialization &
deserialization layer and make it hard to tweak some code.   
  
Another criticism is that a CRUD system would not be able to scale in
the context of a big database, like Firefox Sync, that uses numerous
databases to shard data.   
  
Turns out building a CRUD on tools like SQLAlchemy or Pyramid is not
really going to ruin your scalability as long as:   
-   you can tweak the serialization / deserialization
-   you can override any operation in the CRUD operations when needed
-   you don't shoot yourself in the foot by using CRUD with some code or
    DB that is not meant to be used that way
-   you can use the power of the underlying tools without being blocked
    by the lib

  
For the latter, Ben Bangert was pointing me at [SQLAlchemy horizontal
feature][], which is basically what I wrote from scratch last year to
make the Sync server shard across databases... At this point I sense
that Firefox Sync could have been built with a CRUD lib, and be as
efficient as it is today, because when I look at the queries produced by
the code and the one a CRUD lib would produce, we are one or two tweaks
away.   
  
Anyways, here's a first attempt at such a library.   
### Defining the model

  
In SQLAlchemy, you can define the DB model using mappings, which are
simple classes containing a description of the tables.   
  
For example, if I have a class "users" with a field "id" and a field
"name", the mapping will look like this:   
   class Users(_Base):                                           

        __tablename__ = 'users'                                      

        id = Column(Integer, primary_key=True)                    

        name = Column(String(256), nullable=False)

  
What I started to do is write a meta class one can use in a class to
publish the mapping via HTTP.   
  
Here's an example:   
   from cornicesqla import MetaDBView

    from myapp import Users, DBSession



    class UsersView(object):

        __metaclass__ = MetaDBView

        mapping = Users

        path = '/users/{id}'

        collection_path = '/users'

        session = DBSession

  
What we have here is the definition of a view for the Users mapping.
The class defines an URI for the collection (collection\_path) and for
each user (path). The session attribute is an SQLAlchemy [session][]
object you usually define when you work with that tool.   
  
That's it.   
  
The model gets published, and you can GET, PUT, POST and DELETE on
*/users* and */users/someid.*   
  
The code of the prototype is [here][] and you can find [a working
example in the tests here][]. It's called **cornice-sqla**   
### Tweaking serialization & data validation

  
By default, *cornice-sqla* will serialize and deserialize using JSON
but you can tweak these steps by providing a custom serializer, or
deserializer (or both.)   
  
Let's say you want to use the [Colander libary][] to validate and
serialize the data. To do this, you just have to write your serializer
method into the view class   
   class UsersValidation(colander.MappingSchema):

        name = colander.SchemaNode(colander.String())



    class UsersView(object):

        __metaclass__ = MetaDBView



        mapping = Users

        path = '/users/{id}'

        collection_path = '/users'

        session = DBSession



        def serialize(self):

            """Unserialize the data from the request, to serialize it for the DB"""

            try:

                user = json.loads(self.request.body)

            except ValueError:

                request.errors.add('body', 'item', 'Bad Json data!')

                # let's quit

                return



            schema = UsersValidation()

            try:

                deserialized = schema.deserialize(user)

            except Invalid, e:

                # the struct is invalid

                request.errors.add('body', 'item', e.message)



            return deserialized

  
Colander is used here to validate the incoming request and create a
flat mapping we can push into the DB. Cornice's error system is in usage
here, as explained [here][1].   
  
You can tweak the data that gets back from the DB with
***unserialize()***, and for the collection URI, use
***collection\_serialize()*** and ***collection\_unserialize()***.   
### Tweaking C, R, U or D

  
cornice-sqla is based on a fresh feature Gael added into Cornice
lately: [resources][]. A resource is a class where you can define
*get()*, *post()*, *delete()* and *put()* methods for a given URI.   
  
cornice-sqla views are based on resources, meaning that you can
override anyone of those methods and do whatever you want if you don't
want the CRUD part.   
### What's next

  
I need to make sure everything you can do in Cornice (acls various
options etc) can still be done in cornice-sqla, and start to work with
more complex DB schema that include relations etc. I also need to add
basic missing features like batching and some docs.   
  
My hope at the end is that this small library will reduce considerably
the code needed in some of our projects that interact with SQL.

  [Cornice]: http://packages.python.org/cornice/
  [CRUD]: https://en.wikipedia.org/wiki/Create,_read,_update_and_delete
  [*mappings*]: http://www.sqlalchemy.org/docs/orm/mapper_config.html
  [ORMs]: https://en.wikipedia.org/wiki/Object-Relational_Mapping
  [Active Records]: https://en.wikipedia.org/wiki/Active_record
  [SQLAlchemy horizontal feature]: http://www.sqlalchemy.org/docs/orm/extensions/horizontal_shard.html
  [session]: http://www.sqlalchemy.org/docs/orm/session.html
  [here]: https://github.com/mozilla-services/cornice-sqla/blob/master/cornicesqla/views.py
  [a working example in the tests here]: https://github.com/mozilla-services/cornice-sqla/tree/master/cornicesqla/tests
  [Colander libary]: http://docs.pylonsproject.org/projects/colander/en/latest/
  [1]: http://packages.python.org/cornice/validation.html
  [resources]: https://github.com/mozilla-services/cornice/blob/master/docs/source/resources.rst
