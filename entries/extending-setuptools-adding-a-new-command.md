Title: Extending setuptools: adding a new command
Date: 2007-09-30 01:51
Category: python, quality

Before deploying a package with *python setup.py install*, it's a good
idea to launch the tests with *python setup.py test*.   
  
This command can be used as well to quickly launch tests within a
package that is being developed. Since *setuptools* can be extended,
other commands can be added to be launched from the *setup* script,
while you work in your package.   
  
I have created for example a *qa* command that launches [*pyflakes*][]
over the package code, to make sure I don't leave unused import. I could
have used a direct *pyflakes* call, but my QAs test are going to grow so
keeping the QA script details under a *python setup.py qa* call is a
good practice. This will also make buildbot integration easier, as I can
check for package QA through an unified serie of calls, that plays with
the package *setup.py* script.   
  
Commands are simple class that derives from *setuptools.Command*, and
define some minimum elements, which are:   
-   description: describe the command
-   user\_options: a list of options
-   initialize\_options(): called at startup
-   finalize\_options(): called at the end
-   run(): called to run the command

  
The [*setuptools* doc][] is still empty about subclassing *Command*,
but a minimal class will look like this:   

     class MyCommand(Command):

         """setuptools Command"""

         description = "run my command"

         user_options = tuple()

  
        def initialize_options(self):

             """init options"""

             pass



         def finalize_options(self):

             """finalize options"""

             pass



         def run(self):

             """runner"""

             XXX DO THE JOB HERE

  
The class can then be hook as a command, using an entry point in its
*setup.py* file:   

     setup(

         # ...

         entry_points = {

         "distutils.commands": [

         "my_command = mypackage.some_module:MyCommand"]}

     )

  
This will add an entry point when the package is installed, so you can
run your new command this way:   

     python setup.py my_command

  
You can give a try of my *qa* example by installing my *eggchecker*
package:   

     easy_install http://programmation-python.org/pycommunity/eggchecker-0.1.tgz

  
That's merely a draft, but will show you how *pyflakes* is launched
within the *setup.py* script.

  [*pyflakes*]: http://divmod.org/trac/wiki/DivmodPyflakes
  [*setuptools* doc]: http://peak.telecommunity.com/DevCenter/setuptools#adding-commands
