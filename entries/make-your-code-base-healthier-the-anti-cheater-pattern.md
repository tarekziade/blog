Title: Make your code base healthier: the anti-cheater pattern
Date: 2007-10-08 19:20
Category: plone, python, zope

I gave a few years ago some courses to college students. They had to
write some small C++ programs and send them to me before the end of the
course, so I could correct them and give some grades.   
  
They were massively cheating :)   
  
I created a anti-cheat tool to try to find the cheaters, mainly for fun
and curiosity. To make it efficient, I tried to understand how people
where cheating. They were cutting and pasting pieces of code from
various people, and where arranging them so they would look original.
They were changing the comments of course, and moving functions around
so I wouldn't recognize the class similarities when I was glancing
through the code. But when they were cheating, 80% of the code would
look similar to the programs they borrowed. When they were composing a
new program out of several sources, the atomic bloc was roughly the
function: it was most of the time coming for one source. In other words,
there were a few students zero (like patient zero in epidemics), that
where the providing a function help-yourself copy-n-paste catalog for 30
fellows.   
  
The Levenshtein distance worked great there in finding the cheaters:
given two strings, it computes the number of permutations needed to get
from one string to the other. A ratio can therefore be calculated
between the two strings. Roughly, when its value is equal or up to 0.7,
we can consider that the two are quite similar. This can be applied to
function code as well.   
  
It was quit funny to use this tool at the end of the course, as I could
point the cheaters immediatly. I hurd that some college use such
programs now to detect if students are doing plagias in their homeworks.
  
  
In software, developers acts the same: in the very same code base, as
long as there is more than one developer involved, you will always find
the same functions duplicated again and again. Sometimes, the
duplication is not done on purpose: **it's a natural use case involved
by the APIs**. In other words, a refactoring is needed to remove
duplicate code. This is done most of the time by agile developers that
smell the need: why this function is not made generic and moved into the
base class ?   
  
So it's a good practice to hunt for duplicates, to make the code
smaller, thus more robust. But it's hard to see all duplicates, as it
takes a lot of code reviewing time.   
  
**That's where the anti-cheater pattern is useful**   
  
The pattern can be applied in two steps:   
1.  Parsing the code and applying a bit of filtering.
2.  Calculating the distance, and reporting similarities.

  

  
  
# Parsing the code

  
The first step is to read the code, using the compiler module. This is
the cleanest way to extract the functions because the module parses the
code and renders an Abstract Syntax Tree (AST), that is browsable
without having to import, thus compile the code. Regular expression
could work, but would be painful to create. In the AST, each node
represents a piece of the program, with a specialized class. For
example, a function is a node of the Function class and a list of
children that represent the content of the function. compiler also
provides a visitor pattern that allows us to set some hook everytime a
function, a module, a class or anything else, gets traversed by the
parser.   
  
Below is the visitor used to parse the code for our duty:   
   registered_code = {}



    class CleanNode(object):



        def __init__(self, node):

            code = [str(el) for el in node.getChildren()

                    if el is not None and not isinstance(el, basestring)]

            # too small

            self.small = len(code) < 5

            self.code = ' '.join(code)

            self.name = node.name

            self.filename = node.filename

            self.key = node.key



            if hasattr(node, 'klass'):

                self.klass = node.klass



    class CodeSeeker(object):



        def __init__(self, filename):

            """compiles the AST"""

            self.filename = os.path.realpath(filename)

            self.node = compiler.parseFile(self.filename)

            res = compiler.walk(self.node, self)



        def _key(self, node):

            """calculates an unique key for a node"""

            if hasattr(node, 'klass'):

                return '%s %s.%s:%s' % (node.filename, node.klass,

                                        node.name, node.lineno)

            else:

                return '%s %s:%s' % (node.filename, node.name, node.lineno)



        def _clean(self, node):

            return CleanNode(node)



        def register(self, node):

            """register the node"""

            node.filename = self.filename

            node.key = self._key(node)

            node = self._clean(node)

            if not node.small:

                registered_code[node.key] = node



        #

        # compiler walker APIs

        #

        def visitFunction(self, t):

            self.register(t)



        def visitClass(self, t):

            for subnode in t.getChildren():

                if not subnode.__class__ in  (compiler.ast.Stmt, compiler.ast.Function):

                    continue

                for f in subnode.getChildren():

                    if f is None or isinstance(f, str):

                        continue

                    f.klass = t.name

                    self.visit(f)



    def register_module(filename):

        """registers a module"""

        CodeSeeker(filename)



    def register_folder(folder):

        """walk a folder and register python modules"""

        for root, dirs, files in os.walk(folder):

            if os.path.split(root)[-1] == 'tests':

                continue

            for file in files:

                if file.endswith('.py') and file != 'interface.py':

                    register_module(os.path.join(root, file))

  
Each function, inside and outside classes, are registered in
registered\_code with a few metadata. There's a few filters as you can
see. Some are Plone specific (like the omission of tests folders, and
interface.py files), and some removes very small functions (when there's
less than 5 nodes in the function, including its name, parameters, etc).
This is the playground for our Levenshtein algorithm.   

  
  
# Calculating the distance

  
Now we can compare each function to each other, and get a ratio. When
the value is up to 0.7 we can consider that the code is pretty similar.
I have used David Neca's package:
[http://trific.ath.cx/resources/python/levenshtein/][] for this, because
it's fast and real simple to use:   
   from Levenshtein import ratio



    def levenshtein(entry1, entry2):

        """returns the ratio"""

        return ratio(entry1, entry2)

  
Using it over our dictionnary will look like this:   
   def search_similarities():

        similar = []

        items = registered_code.items()

        done = []

        for key, value in items:

            done.append(key)

            code = str(value.code)

            for key2, value2 in items:

                if key2 == key or key2 in done:

                    continue

                code2 = str(value2.code)

                ratio = levenshtein(code, code2)

                if ratio > 0.7:

                    similar.append((ratio, value.key, value2.key))

        similar.sort()

        similar.reverse()

        return similar

  
Of course we could do some caching, and use an iterator to optimize the
code (the sorting is not really needed)   

  
  
# Demo in Plone and Zope

  
Let's run this pattern over Plone and Zope. I have tried it on Plone 3
lib and Zope 3 lib (within Zope 2.10).   
  
For example, addOpenIdPlugin in plone.openid.plugins.oid:   
   def addOpenIdPlugin(self, id, title='', REQUEST=None):

        """Add a OpenID plugin to a Pluggable Authentication Service.

        """

        p=OpenIdPlugin(id, title)

        self._setObject(p.getId(), p)



        if REQUEST is not None:

            REQUEST["RESPONSE"].redirect("%s/manage_workspace"

                    "?manage_tabs_message=OpenID+plugin+added." %

                    self.absolute_url())

  
was trapped to be similar to manage\_addSessionPlugin in
plone.session.plugins.session:   
   def manage_addSessionPlugin(dispatcher, id, title=None, path='/', REQUEST=None):

        """Add a session plugin."""

        sp=SessionPlugin(id, title=title, path=path)

        dispatcher._setObject(id, sp)



        if REQUEST is not None:

            REQUEST.RESPONSE.redirect('%s/manage_workspace?'

                                   'manage_tabs_message=Session+plugin+created.' %

                                   dispatcher.absolute_url())

  
This tells us that a common API could be written that way (if it
doesn't alreay exists):   
   def addPlugin(container, klass, id, REQUEST=None, **kw):

        """adds a plugin"""

        plugin = klass(id, title=title, **kw)

        container._setObject(plugin.getId(), plugin)



        if REQUEST is not None:

            REQUEST.RESPONSE.redirect(('%s/manage_workspace?manage_tabs_message'

                                       '=Plugin+created') % container.absolute_url())

  
It would avoid having to write such boiler-plate code.   
  
Another example, in Zope 2.10's zope.app folder. The class
SimpleViewClass in zope.app.pagetemplate.simpleviewclass looks very
similar to the one found in zope.app.onlinehelp.onlinehelptopic. Mmmm
**it's exactly the same in fact !** ;)   
  
Last example. In zope.app.authentication.principalfolder, in
PrincipalFolder class:   
   def search(self, query, start=None, batch_size=None):

        """Search through this principal provider."""

        search = query.get('search')

        if search is None:

            return

        search = search.lower()

        n = 1

        for i, value in enumerate(self.values()):

            if (search in value.title.lower() or

                search in value.description.lower() or

                search in value.login.lower()):

                if not ((start is not None and i < start)

                        or (batch_size is not None and n > batch_size)):

                    n += 1

                    yield self.prefix + value.__name__

  
This is very similar to GroupFolder's one in
zope.app.authentication.groupfolder:   
   def search(self, query, start=None, batch_size=None):

        """ Search for groups"""

        search = query.get('search')

        if search is not None:

            n = 0

            search = search.lower()

            for i, (id, groupinfo) in enumerate(self.items()):

                if (search in groupinfo.title.lower() or

                    (groupinfo.description and

                     search in groupinfo.description.lower())):

                    if not ((start is not None and i < start)

                            or

                            (batch_size is not None and n >= batch_size)):

                        n += 1

                        yield self.prefix + id

  
This should be a common code as well, in the base class.   

  
  
# Conclusion

  
My example is not very clean though:   
-   the distance is calculated on the string representation of the tree
    of each function, and this is probably not optimal;
-   the ratio treshold was fixed by trying out the pattern on a few
    source code;
-   the whole thing is quite slow (I'm not Lundh).

  
So it's more likely to be a base for a better implementation, or maybe
a CheeseCake addon ?   
  
But this works for me at this stage, and let me find duplicate code.
I'm thinking of hooking it in a buildbot, to analyze what developers
commit and, when a similarity is found, send a mail with a few
suggestions.

  [http://trific.ath.cx/resources/python/levenshtein/]: http://trific.ath.cx/resources/python/levenshtein/
