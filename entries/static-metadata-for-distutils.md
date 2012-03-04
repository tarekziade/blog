Title: static metadata for distutils
Date: 2009-09-12 00:25
Category: distutils, python

In Distutils, every package has some metadata fields, defined in [PEP
314][].   
  
The *setup.py* script is the place where you provide them, by calling
the *setup* function, located in *distutils.core*. Each argument passed
to the function can be one of these metadata.   
  
So basically, you can describe your distribution in the *setup.py* file
like this:   
>   
>     from distutils.core import setup
>
>   
>     setup(name='MyDistribution', version='0.1', description='cool',
>
>           packages=['my_package'], ext_modules=[Extension('foo', 'foo.c')])
>
>   

  
Notice that *packages* and *ext\_modules* in this example are not part
of the Metadata fields. They are extra fields used by some commands.   
  
From there, various *distutils* commands can be called using this
script. They will get these options and act upon.   
  
For instance, the *sdist* command will build a source distribution and
create a static *PKG-INFO* file that contains the metadata fields. It
will extract them from the arguments you've passed to *setup.py*.   
  
The *install* command will install this *PKG-INFO* file in your Python
installation alongside your packages and modules (since Python 2.5) and
some tools like Distribute or Setuptools will let you read these
information once the distribution is installed.   
  
You can even get the metadata fields values by asking for them directly
through *setup.py*:   
>   
>     $ python setup.py --name
>
>   
>     MyDistribution
>
>   

  
Another example : the *register* command can send the metadata or your
distribution to PyPI. They will be made available on PyPI website and
also through its XML-RPC interface:   
>   
>     >>> import xmlrpclib
>
>     >>> server = xmlrpclib.Server('http://pypi.python.org/pypi')
>
>     >>> server.release_data('distribute', '0.6')['author']
>
>     'The fellowship of the packaging'
>
>     >>> server.release_data('distribute', '0.6')['keywords']
>
>     'CPAN PyPI distutils eggs package management'
>
>   

  
### Limitations of metadata

  
Metadata are pretty handy, but there are some obstructing limitations
we bumped into when we started to work on packaging matters during last
Pycon.   
#### Platform-dependant metadata

  
We wanted to extend the Metadata fields list in order to add a
"*require*s" field that can be used to list the requirements (in term
others python packages or modules).   
  
For instance, if you want to define that your project depends on
*simplejson*, you could write:   
>   
>     from distutils.core import setup
>
>
>
>     setup(name='MyDistribution', version='0.1', description='cool',
>
>           packages=['my_package'], ext_modules=[Extension('foo', 'foo.c')],
>
>           requires=['simplsjon'])
>
>   

  
This is not a new proposal. It was proposed in [PEP 345][], but never
really used.   
  
Since then, Setuptools provided a similar field, called
"*install\_requires*" together with *easy\_install *script that acts a
bit like a package manager. *easy\_install* reads the requirements and
install them when you install a distribution.   
  
But the limitation of those requirement fields is that they might be
platform-dependant. For example, you don't need to install *simplejson*
anymore under 2.6 since a json library was included in the standard
library. In other cases you might have different dependencies depending
if you run under windows or linux, and so on.   
  
So to be able to get the metadata right, you have to work a little bit
in your *setup.py *file:   
>   
>     from distutils.core import setup
>
>     import sys
>
>   
>     if sys.version_info[0] == 2 and sys.version_info[1] < 6:
>
>         requires = ['simplejson']
>
>     else:
>
>         requires = []
>
>   
>     setup(name='MyDistribution', version='0.1', description='cool',
>
>           packages=['my_package'], ext_modules=[Extension('foo', 'foo.c')],
>
>           requires=requires)
>
>   

  
But the metadata will only be available at install time, when the
*install* command will execute the code of *setup.py* on the target
system.   
#### Code-dependant metadata

  
In other words, once a field like *requires* is added in the Metadata,
you will not know for sure if it's reliable when you look at the project
page at PyPI. That's because the metadata you will see there will be the
one created by the person that called the *register* command and sent
the result. This result is tighted to his environment, not yours.   
  
To be able to get the metadata for your environment you will need to
run that code again, by downloading the package, then running a
*setup.py* command.   
  
Let's try to do it with the *lxml* source distribution. Let's try to
get the *name* field :   
>   
>     $ python setup.py --name
>
>     Building lxml version 2.2.2.
>
>     NOTE: Trying to build without Cython, pre-generated 'src/lxml/lxml.etree.c' needs to be available.
>
>     Using build configuration of libxslt 1.1.12
>
>     Building against libxml2/libxslt in the following directory: /usr/lib
>
>     lxml
>
>   

  
What happened here ? Frankly I am not sure. But asking for the name
(that appears on the last line) called a bunch of code located in the
distribution.   
  
I could probably ask the lxml team to fix this output, and make sure
*setup.py* can still be used to work with the metadata, but this was
just to demonstrate a flaw in the way Distutils works : you need to run
third party code just to get the metadata of a distribution you're not
even sure you are going to install on your system.   
### The setup.cfg file

  
Part of the problem can be resolved by putting the metadata in a static
file alongside *setup.py*. As a matter of fact, the *setup.cfg* file is
already used by distutils to store some options. There's even a *global*
section that can be used to set the metadata into the *Distribution*
object Distutils creates when you run *setup()*. Using the global
section that way is not documented and probably not intended. What's
intended is to be able to set some global options like "verbose" or such
things.   
  
See
[http://docs.python.org/install/index.html\#syntax-of-config-files][]   
  
But the code is a generic setter, that allows you to pass any field (so
the metadata). Call it a bug if you want, but I was pretty excited to
see that I could pass my metadata to Distutils through it. Unfortunately
these values are not passed to the *DistributionMetadata* subobject in
Distutils, so it doesn't work exactly like the arguments passed to
*setup()*. Too bad ;-)*   
*   
  
I could change this right away in the code, but we have better plans I
think.   
#### A new setup section

  
Instead of working in the *global* section which should stay specific
to running options, let's create a new section and put the metadata in
them.   
>   
>     [setup]
>
>   
>     name: MyDistribution
>
>   
>     version: 0.1
>
>   
>     description: cool
>
>   

  
The *setup.py* script stays, but is now not containing any metadata
field, and does only contain what I would call "working arguments". e.g.
argument used by commands that are not part of the Metadata:   
>   
>     from distutils.core import setup
>
>   

  
>   
>     setup(packages=['my_package'], ext_modules=[Extension('foo', 'foo.c')])
>
>   

  
#### What about platform-dependant fields ?

  
In order not to require any third party code to read the metadata, we
need a way to express platform-dependant fields in the* setup.cfg* file.
  
  
The proposed way is to have platform-dependant sections :   
>   
>     [setup]
>
>   
>     name: MyDistribution
>
>   
>     version: 0.1
>
>   
>     description: cool
>
>   
>     conditional-sections: py25
>
>   
>     [py25]
>
>   
>     condition: python_version == '2.5'
>
>   
>     requires: simplejson
>
>   

  
The *py25* section is read only if the expression is true.   
  
Another example:   
>   
>     [setup]
>
>   
>     name: MyDistribution
>
>   
>     version: 0.1
>
>   
>     description: cool
>
>   
>     conditional-sections: py25, py26
>
>   
>     [py25]
>
>   
>     condition: python_version == '2.5' or python_version == '2.4'
>
>   
>     requires: simplejson
>
>     [py26]
>
>     condition: python_version == '2.6' and sys_platform == 'win32'
>
>     requires: bar
>
>   
>   

  
here, "*bar*" will be installed under Python 2.6 under Windows, and
"*simpljson*" under Python 2.5 or 2.4 on any platform.   
  
Distutils will provide a new function that is able to interpret the
expressions provided in the condition, and calculate the metadata
depending on the platform.   
  
That's still some code we are running here, but:   
-   We are restricting the execution context to the bare minimum:
    *python\_version*, *sys\_platform*, *os\_name*, and all values
    returned by *os.uname()*
-   The function will be vanilla Python: you will be able to extract the
    metadata without running a third party code, and knowing that the
    execution is restricted to a few string comparisons.
-   The code can be executed at PyPI without any potential security
    issue, meaning that the XML-RPC functions will be able to send you
    back the metadata of a packages depending on your environment. In
    other word, a package manager would be able to list all the
    dependency of a distribution for the target platform without
    downloading any of these distribution.

  
#### There will always be edge cases

  
For the 1% of distributions that need more work to calculate the
metadata,* setup.py* will still be present and any option passed as an
argument will override a value provided by *setup.cfg*. They'll just
have to add a flag in the *setup.cfg* file, indicating that it does not
provides all the metadata, and that running *setup.py* is required:   
>   
>     [setup]
>
>     name: MyDistribution
>
>     version: 0.1
>
>     description: cool
>
>     static-metadata: false
>
>   

  
If this flag is present, people will now that running setup.py is
mandatory to get the full set of metadata.   
  
For example, if the web service provided at PyPI to get the metadata,
will be able to return a platform specific set if we provide the target
environment. Let's say we add in distutils an '*execution\_environment*'
that returns the environment used to interpret the *setup.cfg* file:   
   >>> import xmlrpclib

    >>> server = xmlrpclib.Server('http://pypi.python.org/pypi')

    >>> from distutils.util import execution_environment

    >>> execution_environment

    {'os_version': 'Darwin Kernel Version 9.8.0: Wed Jul 15 16:55:01 PDT 2009; root:xnu-1228.15.4~1/RELEASE_I386',

     'os_name': 'posix',

     'python_version': '2.6',

     'os_release': '9.8.0',

     'os_sysname': 'Darwin',

     'os_nodename': 'MacZiade',

     'os_machine': 'i386',

     'sys_platform': 'darwin'}



    >>> server.release_data('MyDistribution', '0.6', execution_environment)['requires']

    ['foo', 'bar']

    >>> server.release_data('MyDistribution', '0.6', execution_environment)['static-metadata']

  
True
  
PyPI will be able to generate the metadata by interpreting the
*setup.cfg* file with the *execution\_environment* info.   
#### What happens now ?

  
I won't write a PEP for this. I don't think it's necessary because this
feature is backward compatible, and if people don't use it in Python 2.7
and 3.2, it will just fade away, like other things in Distutils.   
  
But we need to reach a consensus at Distutils-SIG then inform about it
at Python-dev. I just hope we will have this consensus real quickly,
unlike most topics we are working on for a year ;)   
  
Or maybe I should be a bit of a dictator for this feature and just go
ahead and add it ? Because as [Brett][] told me several times, it's
impossible to make everyone happy about everything. And I'd like to see
Distutils move on. There's so much left to do...   
  
What do you think ? How do you like that feature ?

  [PEP 314]: http://www.python.org/dev/peps/pep-0314
  [PEP 345]: http://www.python.org/dev/peps/pep-0345/
  [http://docs.python.org/install/index.html\#syntax-of-config-files]: http://docs.python.org/install/index.html#syntax-of-config-files
  [Brett]: http://sayspy.blogspot.com/
