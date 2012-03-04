Title: QA portal ideas
Date: 2011-02-21 11:25
Category: mozilla, python

GSOC is coming back. We'll soon have to select some projects for
CPython, and I'll probably suggest a few Distutils2 topics -- it's an
endless project ;).   
  
There's a project I want to start, a QA portal. I am not sure how this
could fit in a GSOC proposal, but I think there could be some interest
in the community.   
  
I could definitely use such a tool for our Mozilla Services projects.   
  
But let's face it: I have no time, and this is far too ambitious. But
let me dream a bit...   
### Level 1 - PyPI Watcher

  
For level 1, the idea is to create a portal that subscribes to all PyPI
events (registering or uploading of new releases) and creates a QA
report on specific projects I want to watch. The idea is not new, and we
had a student on this last year -- But the project was not finished.   
  
Basically I want a website like [PyPants][], but with more ambitious
features. Maybe a good idea would be to approach the PyPants creators
and see if the project could be extended.   
  
Some tests I'd like the portal to perform:   
-   run a real install of the project in a VM, and returns a report on
    how the system was impacted with a tool like SystemTap. The VM part
    is mainly to avoid any security issue when running third-party code.
    While I supposedly trust the projects I select, you never know.
-   try to detect and run the tests, along with a coverage report.
-   run the usual metrics (pep8, maccabe, pylint, etc)

  
Difficulties:   
-   The VM part is not that easy to set up and scale, but feasible with
    Amazon for instance
-   What about Windows ? -- dropping its support for now seems a good
    idea :D

  
### Level 2 - Clone detection

  
The next stage I would like to see the project take is **clone
detection**. Tools like [CloneDigger][] allows to detect similarities in
code. It will tell you for instance that function A is very similar to
function B.   
  
What I would want to see is an global index of clones. The users select
a project as being the master project, and a list of dependencies or
other projects. Then the portal will report any similar functions,
methods or modules it found.   
  
Difficulties:   
-   Set up the right thresholds in the algorithm that detects the
    clones. There could be a lot of back and forth here before the
    results make any sense.
-   Scaling it. For instance, while it would be easy with CloneDigger to
    keep for each project the cluster of statements ([see
    doc][CloneDigger]), so you don't have to rebuild everything every
    time, we are still doing a comparison work that grows at a
    logarithmic speed. I am not sure how to deal with it but that's an
    interesting issue to solve.

  
### Level 3 - ~~Hudson~~ Jenkins integration

  
Once we have a shiny Level 1+2 QA Portal, I'd like to see it integrated
in Hudson somehow.   
  
One idea would be to create two web services in the QA Portal, a Hudson
plugin can call. One to ask for a fresh report generation, and one to
get the result and display it in a dashboard etc.   
  
I am not sure how Hudson deals with running tasks asynchronously
though, but I am pretty sure this is doable.   
  
Ok let's stop dreaming -- back to work ;)

  [PyPants]: http://pypants.org/
  [CloneDigger]: http://clonedigger.sourceforge.net/documentation.html
