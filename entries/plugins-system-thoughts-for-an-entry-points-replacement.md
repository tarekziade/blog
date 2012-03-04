Title: plugins system: thoughts for an entry points replacement 
Date: 2010-07-25 02:29
Category: python

*This blog entry was inspired by the discussion I just had with Michael
on IRC, as he just added plugins in unittest2.*   
  
Setuptools' entry points feature is *hated* and *loved* by developers.
If you are not familiar with them, you can read [this post from
Armin][].   
  
**Hated** because when you install a project that contains entry points
(let's call them *plugins*), they can be used in another application
without letting you know. So basically if a plugin sucks, it can break
another application just by being installed in your Python. And it's not
easy to have an overview of what plugins are installed and potentially
active.The worst is that projects that provide entry points, usually
provide many other things. But if you want to deactivate the plugin, you
have to remove the whole project... Note that plugins are not loaded at
Python startup. What happens is that any application can iterate over
the metadata of installed projects, looking for plugins, and eventually
loading them if wanted.   
  
**Loved**, because from a developer point of view you can have a new
feature added in a program with no extra configuration at all. Take
Nose. Thanks to entry points, it's dead easy to create a plugin for this
test runner, and tell people to pip-install this new project. Zero
config. Nice. Another great thing is that it's global to Python. Any
application can consume any entry point. Entry points are **implicit
plugins** I guess.   
  
*Distutils* has a plugin system as well: you can add new commands by
adding in distutils.cfg the path to the Python package containing the
command. That's an explicit plugin system since the end-user has to
configure it manually so Distutils uses it. *Mercurial* uses the same
technique: activating a plugin is done in .hgrc. I would call these
**explicit plugins**.   
  
I think we can get the benefits of entry points without their caveats
really simply. And provide a generic plugin system for all. Let's
summarize what we want:   
-   being able to list all installed plugins for every Python
    application
-   being able to remove a plugin or deactivate it. Without being forced
    to uninstall the project that provided it
-   have a plugin automatically installed and activated when the project
    that provides it is installed

  
Here's how we can do. That's a brain dump, please give me some feedback
!   
### Global plugin registry

  
Let's have a *.python-plugins.cfg* file in the user's home *(and one
global to Python. The user cfg is merged with the global one at startup,
and overrides the values -- thanks Mongoose\_Q for mentioning this on
Twitter)*. It's a simple ini-like file like *.hgrc*, where each section
represents a python application and a group name. A group is just a
family of plugins. For instance 'commands' can be a group for the
'distutils' application. In this section, each line is a plugin,
represented by a pointer to the module or class, followed by a label as
the value.   
  
Here's an example for a distutils 'i18n' command. It's a MyClass class,
located in the foo package, in the bar module:   
     [distutils:commands]

      foo.bar:MyClass = i18n

  
The link to the code comes first because some plugins could have no
name:   
     [app:group]

      package.module:Class =

  
### Accessing the registry

  
distutils can provide an API to read the file, iterate and load the
plugins:   
       >>> from distutils2 import plugins

        >>> plugins.get('distutils', 'command')

        <iterator>

        >>> plugins.get('distutils', 'command').next()

        <Plugin "i18n" at foo.bar:MyClass>



        >>> plugin = plugins.get('distutils', 'command').next()

        >>> plugin.load()    # gets the code and loads it

        <MyClass Instance>

  
  
### Installing the plugins

  
Last, distutils could provide a mechanism to automatically register a
plugin.   
  
Projects could describe their plugins in their setup.cfg:   
     [plugins]

      distutils.commands.i18n =  foo.bar:MyClass

  
Then distutils would automatically inject them at installation time in
*.python-plugins.cfg* **only if the end user agrees**:   
     $ python setup.py install

      distutils has detected a "i18n" plugin for distutils:commands. Do you want to activate it (Y/n) ?

  [this post from Armin]: http://lucumr.pocoo.org/2006/7/30/setuptools-plugins
