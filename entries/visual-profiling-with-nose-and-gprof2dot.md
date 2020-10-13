Title: Visual profiling with Nose and gprof2dot
Date: 2008-08-25 09:19
Category: plone, python, quality, zope

[Nose][] comes with a handy option to generate profiling stats.   
  
To profile your code, create a test dedicated to this purpose and run
it with the right options:   
   $ nosetests --with-profile --profile-stats-file stats.pf test_performance

  
This will run the tests that corresponds to the *test\_performance*
name and generate a stats.pf file.   
  
Nose uses [hotshot][], so if you want to generate a file that can be
read directly by the [pstats][] module and all the statistics tools out
there, you need to convert it using the [hotshot.stats][] module.   
  
From there, there is plenty of tools that can transform such a file
into a visual graph. Most of the time, they use [Graphviz][] to render a
graph, by generating a file [dot][] can read. This software is most of
the time easy to install through a binary distribution on your system.
If you need to compile it... good luck.. ;)   
  
Anyway, from there, I use [gprof2dot][], which renders a nice graph
with meaningful colors.   
  
From the author:   
  
  
  
  
[![image][]][gprof2dot]   
> *The color of the nodes and edges varies according to the total time %
> value. In the default temperature-like color-map, functions where most
> time is spent (hot-spots) are marked as saturated red, and functions
> where little time is spent are marked as dark blue.*

  
*   
*   
  
*   
*   
  
*   
*   
  
*   
*   
  
*   
*   
  
*   
*   
  
*   
*   
  
*If *you want to use it, I have created some console scripts for
conveniency, you can install using [easy\_install][]:   
   $ easy_install pbp.scripts

  
It creates a *gprof2dot* script you can use, following the author
documentation, but also a *hotshot2dot* script that will convert
automatically a statistics file and pass it to *gprof2dot*:   
   $ hotshot2dot /path/to/my/hotshot/file

  
This will print in the output a dot file, you can send to the dot
program, using a pipe:   

  $ hotshot2dot /path/to/my/hotshot/file | dot -Tpng -o output.png

  
You will get the visual result in *output.png*.

  [Nose]: http://www.somethingaboutorange.com/mrl/projects/nose/
  [hotshot]: http://docs.python.org/lib/module-hotshot.html
  [pstats]: http://docs.python.org/lib/module-profile.html
  [hotshot.stats]: http://docs.python.org/lib/module-hotshot.stats.html
  [Graphviz]: http://www.graphviz.org/
  [dot]: http://www.graphviz.org/cgi-bin/man?dot
  [gprof2dot]: http://code.google.com/p/jrfonseca/wiki/Gprof2Dot
  [image]: http://jrfonseca.googlecode.com/svn/wiki/gprof2dot.png
  [easy\_install]: http://peak.telecommunity.com/DevCenter/EasyInstall
