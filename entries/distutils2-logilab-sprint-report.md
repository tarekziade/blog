Title: Distutils2 - Logilab Sprint Report
Date: 2011-02-07 01:43
Category: python

We had a great sprint at [Logilab][] the other week-end, and this was by
far the most productive sprint on Distutils ever. That's partially
because all the core work we did in the last year starts to surface !
That's also because we had a good team of hackers, focused on specific
tasks. I did not merge all the work yet but it should be done this week
and an alpha released right after.   
  
Now to the list of goodness..   
### Data files

  
We can now express data files in *setup.cfg*, and use a specific API to
work with them. The goal is to let OS Packagers configure where those
files should land at installation time, without breaking the code that
uses them. The brainstorming we did last year at Pycon is here :
[http://hg.python.org/distutils2/file/tip/docs/design/wiki.rst][] and
it's now a reality. This is a good step torwards a cleaner packaging
system.   
### Setup.cfg completion

  
*setup.cfg* lacked a few things to be able to fully replace a
*setup.py*, like defining extensions to be compiled. This is now done
and we're going to maintain a page were we list all projects that were
successfully converted. The page lives here for now:
[https://bitbucket.org/tarek/distutils2/wiki/Deployments\_using\_setup.cfg][]
and I will announce it widely once the alpha is released, so people can
start to convert their own projects. We did convert more projects, and I
need to update that page later this week.   
### Installer / Uninstaller

  
A first version that installs a project and its dependencies, as well
as an uninstaller, was completed. Among other things, it will rollback
the installation in case it encounters any issue. This tool exists
mainly as a implementation reference to exercise all the tools that are
provided in Distutils2 to browse an installation, build a depgraph or
query PyPI. There's still a bit of backward compatibility work to do in
order to deal with Setuptools-based installations and projects, but most
things are done. I expect this to be finished and included in the alpha.
  
### From Distutils1 to Distutils2 and vice-versa

  
Since* setup.cfg* completely replaces *setup.py* -- which is ignored by
Distutils2, you can make your project compatible with both. This implies
that you have to maintain two files that contain duplicate information,
like the project name or the version. We created a tool during the
sprint to avoid this: a simple function that you can use in your
*setup.py* file to convert *setup.cfg* options into Distutils1 options.
  
  
Of course, to avoid adding a Distutils2 dependency into that setup.py
file, we inject that function into the module, and we'll provide a
command in *pysetup*. to generate it:   
   $ pysetup createD1setup

    setup.py successfully created.

  
And if you want to do it the other way around, we offer a new feature
in the wizard that will run your *setup.py* file and generate a
*setup.cfg*. This is the tool we'll promote in order to make it easy for
people to add Distutils2 support.   
### Stuff left to do

  
Besides the merges, before I release the next alpha there's one big
task I need to do: remove the *fancygetopt.py* file, a layer on the top
of *getopt*, and add a simpler, isolated module to process the command
line. This will clean up a lot the code base, and make the *dist.py*
module stop dealing directly with this. It will only implement the
*Distribution* class, and consume command line options without having to
be the one that generates them.   
  
I am not sure yet what I'll use, since both *optparse* and *argparse*
are unable to meet my requirements here. A custom command-line parser is
not the best thing to maintain though..   
### Thank you Logilab & Bearstech

  
Logilab is awesome. We had many people from their teams sprinting with
us, and they paid our meals every day and covered Alexis' travel costs.
Bearstech was awesome as well, as they covered several snacks expenses.
  
  
Thanks to all sprinters that made it there, or worked online. We should
do these more often.

  [Logilab]: http://www.logilab.org/
  [http://hg.python.org/distutils2/file/tip/docs/design/wiki.rst]: http://hg.python.org/distutils2/file/tip/docs/design/wiki.rst
  [https://bitbucket.org/tarek/distutils2/wiki/Deployments\_using\_setup.cfg]:
    https://bitbucket.org/tarek/distutils2/wiki/Deployments_using_setup.cfg
