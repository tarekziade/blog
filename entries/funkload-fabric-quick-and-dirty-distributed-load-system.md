Title: Funkload + Fabric = quick and dirty distributed load system 
Date: 2010-12-09 00:05
Category: mozilla, python

We're currently using [The Grinder][] for our Sync load tests at Mozilla
Services. Grinder will let you write the tests using [Jython][] and run
a distributed load test. Despite the Java and Jython environment layer
which is always painful to set up, Grinder works well.   
  
But do not expect it to produce nice reports, you're on your own for
this. You need to work on the raw results to produce nice diagrams. Do
not expect either to perform some operations on the test nodes before
and after the distributed load test is executed. Tests are driven via an
UI and while it's probably possible to script them via Java... it's
Java. And well, the feedback when the tests are running is nearly
inexistant.   
  
The distributed load system of my dreams must:   
-   let me run arbitrary commands on every node before and after it runs
    the test. And retrieve results then merge them in a consolidated
    result.
-   let me write complex unittest-based functional tests that I can also
    use to check the health of a server.
-   provide basic reporting features
-   be written in Python ;)

  
  
Oh.. hold on.. I have it : Funkload and Fabric.   
  
[Funkload][] let you write complex functional tests, does load testing
with complex cycles and produces nice reports.   
  
And then there's [Fabric][], which allows you to run commands via SSH
on a pool of servers.   
  
Funkload is not distributed but it's fairly simple to drive it via
Fabric. And when all nodes have finished the execution --whom you can
watch via the Fabric stdout-- you can get them back and merge them in a
single file.   
  
So basically, the fabric script looks like this:   
  

    from fabric.api import run, get, env



    def runtest():

        run('fl-run-bench testmodule TestClass.test_function')

        file = '/path/to/results.xml'

        get(file, env.host_string + '-results.xml')

  
  
This will run the command on the distant server, then download the xml
file. All through SSH. It can be launched on every server with:   
  

    $ fab -H the.server.org runtest

  
  
Fabric does not provide parallel execution yet, so you have to create a
batch to run the script on every server in parallel processes. But this
feature should be included in Fabric 1.1. There's a branch for this:
[https://github.com/goosemo/fabric/commits/multiprocessing][]   
  
Then you can merge the files in a single XML file like this:   
  

    from funkload.MergeResultFiles import MergeResultFiles

    import os



    def merge_results():

        files = []

        for file_ in os.listdir(HERE):

            if not file_.endswith('-results.xml'):

                continue

            files.append(file_)



        MergeResultFiles(files, 'results.xml')

  
  
And finally, create an HTML output:   
  

    $ bin/fl-build-report --html -o html results.xml

  
  
Granted, there's no control of the nodes during the tests, that feature
would require a small TCP server that drives Funkload on each server.
And that would obsoletes the need for Fabric I guess. But for setting up
a quick distributed test, I am good with SSH for now.   
  
I should also mention [Benchmaster][], which do something similar but
seems complex to configure compared to a simple Fabric script.   
  
**Funbric** ? :D   

  [The Grinder]: http://grinder.sourceforge.net/
  [Jython]: http://www.jython.org/
  [Funkload]: http://funkload.nuxeo.org
  [Fabric]: http://fabfile.org/
  [https://github.com/goosemo/fabric/commits/multiprocessing]: https://github.com/goosemo/fabric/commits/multiprocessing
  [Benchmaster]: http://pypi.python.org/pypi/benchmaster/
