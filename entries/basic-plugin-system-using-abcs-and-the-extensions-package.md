Title: Basic plugin system using ABCs and the &quot;extensions&quot; package
Date: 2009-05-01 20:59
Category: python

I need a very simple plugin system for one of my projects. The project
is a small WSGI application called **mysysadmin** that allows you to
launch some commands on your system to manage some applications. It also
allows you to view log files in your web browser.   
  
It's similar in some ways to [WebMin][],   
  
So in my application, every tab is a plugin that manages one
application. I have a plugin for Apache, another one for MySQL, and so
one.   
  
Back to my plugin system. So every plugin that is registered becomes a
tab in the WSGI application, as long as it provides all the methods my
web application needs to interact with it. So I want to check that each
plugin **strictly** provides the API needed by the main program.   
  
The first tools that came in mind were :   
-   [zope.interface][], to be able to provide that each plugin meets the
    requirements.
-   [setuptools entry points][], so it's easy for a third party code to
    implement a plugin.

  
But I find both projects a bit complex to implement such a simple
plugin system.I could use the standalone Plugins package Phillip
provides instead of setuptools, but it still does too much things imho.
That's someting I am currently learning by working on packaging matters
: one library should not provide too many features.   
### Extensions : a simple plugin system

  
So I have started to implement a light-weight plugin system called
[extensions][], which reuses setuptools entry points principles but is
more simple to use. The goal of this project is to provide very simple
APIs to handle plugins, and to make it work without introducing a new
argument into the setup.py *setup* method, like setuptools does.   
  
For instance, if you want to define an **apache** function in your
**modules** module, in your **myapp** package, you just call the
**register** function :   
~~~~ {.literal-block}
from extensions import register



register('mysysadmin.modules', 'apache', 'myapp.modules:apache')
~~~~

  
That's it !   
  
And to use it, the **mysysadmin** application can use a simple API
called **get**, that iterates over all plugins defined for
*"mysysadmin.modules"* :   
~~~~ {.literal-block}
from extensions import get



for plugin in get(group='mysysadmin.modules'):

    # do something with the plugin
~~~~

  
The magic is done by writing in the *.egg-info* directory installed for
the package that contains each plugin, a *PLUGIN* file that contains the
list of registered elements. It's an idea borrowed from setuptoools
entry points. So *get* iterates over all *.egg-info* directories in your
path and load the *PLUGIN* files it finds. Nothing new here. That's how
setuptools does, and that's perfect.   
  
If you have any feedback on [extensions][], let me know !   
### Strict plugins

  
The other need is to strictly check that every plugin provides the API
needed, e.g. fulfill the requirements. This is what we could call
[Design by contract][].   
  
You can provide a base class for this, and ask the plugins to inherit
from it. Or you can ask the Plugin to provide a marker to specify it
implements a given behavior. *zope.interface* can do a nice job for the
latter,and let you check that a given object implements an interface.   
  
But I wanted to give a shot to the brand new Python ABCs and make sure
anyone can write a plugin in plain Python, without having to rely on any
kind of marker system. ABCs will let you check that a class implements
some methods without requiring it to inherit from a specific class, to
implement a specific interface or provide a custom marker. Pure duck
typing !   
  
So let's define for our application a **Plugin** class, that gives the
signature every plugin will need to provide. It uses **ABCMeta** as its
meta class, and the **abstractmethod** for every method that should be
implemented by every plugin.   
  
Here's an extract :   
   from abc import ABCMeta, abstractmethod



    class Plugin(object):

  
       __metaclass__ = ABCMeta

  
       @abstractmethod

        def get_command_list(self):

            return []



        @abstractmethod

        def run_command(self, name):

            pass



        @classmethod

        def __subclasshook__(cls, klass):

            if cls is Plugin:

                for method in cls.__abstractmethods__:

                    if any(method in base.__dict__ for base in klass.__mro__):

                        continue

                    return NotImplemented

                return True

            return NotImplemented

  
The **\_\_subclasshook\_\_** method is a class method that will be
called everytime a class is tested using **issubclass(klass, Plugin)**.
In that case, it will check that every method marked with the
**abstractmethod** decorator is provided by the class.   
  
So basically, the application can discover and use the plugins, with:   
~~~~ {.literal-block}
from extensions import get



for plugin in get(group='mysysadmin.modules'):

    klass = plugin.load()

    if not issubclass(klass, Plugin):

        logging.info('sorry, not a suitable plugin')

        continue

    # do something with the plugin

    xxx
~~~~

  
Abstract Base Classes are one honking great idea -- let's do more of
those!

  [WebMin]: http://www.webmin.com/
  [zope.interface]: http://pypi.python.org/pypi/zope.interface
  [setuptools entry points]: http://peak.telecommunity.com/DevCenter/setuptools#extensible-applications-and-frameworks
  [extensions]: http://pypi.python.org/pypi/extensions
  [Design by contract]: http://en.wikipedia.org/wiki/Design_by_contract
