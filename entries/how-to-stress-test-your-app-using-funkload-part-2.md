Title: How to stress test your app using Funkload -- part 2
Date: 2011-07-28 14:52
Category: mozilla, python

The first part of this blog post is [here][].   
  
I've initially split it in two parts because I've encountered a few
problems with the distributed feature, so I thought it was going to take
Ben a few days to fix them. But he did fix them within the hour... \\o/
  
  
So **Hurra for Ben** and here's the second part of my small tutorial.   
### Running a distributed test

  
If you want to hammer a server, you cannot run all the virtual
concurrent users from a single box. You will end up eating all your
resources and will not be able to simulate a very big load. If you need
to run a couple of hundreds of concurrent users, one box is enough. But
you'll need more boxes to get more load, obviously. Depending on the
complexity of the tests, I usually end up having at the most 200 CU
(Concurrent Users) per node.   
  
In the past, I was using Fabric to do distributed tests for Funkload,
see [here][1]. But this is not needed anymore because Funkload has now a
built-in support to distribute the charge amongst several nodes. It uses
a similar technique that I used in Fabric, by driving the nodes via SSH
using [Paramiko][]. The benefit though, is that it does all the heavy
lifting for you: your test suite gets deployed on the nodes, and the XML
result files gets downloaded for you on the master.   
  
All you have to do once the test is over, is to merge the XML files and
generate reports. And the merging is taken care of by a Funkload script
so... Let's do this !   
  
First of all, you need to install Paramiko in your environment:   
   $ bin/pip install paramiko

  
Also, move to a trunk snapshot version of Funkload, since there are a
couple of fixes there for this feature:   
   $ bin/pip install -U -f http://funkload.nuxeo.org/snapshots Funkload

  
Next, select a few boxes that will be your nodes to run the tests, and
make sure they have Python and virtualenv installed, and that you can
access via SSH to them without having to type anything. The simplest way
to do this is to copy over an ssh key with an empty passphrase. [See
this article if you don't know how to do it.][]   
  
***Notice: having a ssh key that does not require a passphrase is a
potential security hole, so make sure these key are used only for this
purpose, and safe.***   
  
The next step is to add a ***[distribute]*** section in the Simple.conf
file:   
   [distribute]

    log_path = distributed-simple-test.log

    funkload_location=http://pypi.python.org/packages/source/f/funkload/funkload-1.16.0.tar.gz

  
These options tell Funkload which Funkload release should be used on
the node, and where to put the logs. The script will install it in a
virtualenv on every node, prior to running the tests.   
  
Once everything is set up, you can run the test using all your nodes
with the ***--distribute*** flag and the ***--distribute-workers***
option, that gives a list of the nodes. The script deploy the tests into
the nodes, run them, and grab back the XML files.   
  
In my environment I have a master, and two nodes (node1 and node2)   
   $ bin/fl-run-bench --distribute --distribute-workers=node1,node2 test_simple.py Simple.test_simple

    ========================================================================

    Benching Simple.test_simple

    ========================================================================

    Access our Demo app

    ------------------------------------------------------------------------



    Configuration

    =============



    * Current time: 2011-07-28T14:11:47.720959

    * Configuration file: /home/tarek/dev/hg.mozilla.org/funkload-demo/Simple.conf

    * Distributed output: distributed-simple-test.log

    * Server: http://master:5000

    * Cycles: [5, 10, 20]

    * Cycle duration: 10s

    * Sleeptime between request: from 0.0s to 0.5s

    * Sleeptime between test case: 0.01s

    * Startup delay between thread: 0.01s

    * Workers :node1,node2



    * Preparing sandboxes for 2 workers...

    * Starting 2 workers..



    * [node1] returned



    * [node2] returned



    * Received bench log from [node1] into distributed-simple-test.log/node1-simple-bench.xml

    * Received bench log from [node2] into distributed-simple-test.log/node2-simple-bench.xml

  
Once the test is over, you will find two XML files on your master, you
can merge to produce an HTML report:   
   $ bin/fl-build-report --html -o html distributed-simple-test.log/node1-simple-bench.xml distributed-simple-test.log/node1-simple-bench.xml

    Merging results files: ..

    nodes: tarek-laptop, tarek-laptop

    cycles for a node:    [5, 10, 20]

    cycles for all nodes: [10, 20, 40]

    Results merged in tmp file: /tmp/fl-mrg-JL62Bi.xml

    Creating html report: .../home/tarek/dev/hg.mozilla.org/funkload-demo/html/

    done:

    /home/tarek/dev/hg.mozilla.org/funkload-demo/html/test_simple-20110728T141152/index.html

  
Congrats, you're now able to run distributed tests !   
### Monitoring the server

  
The last feature I want to show is the monitoring. Funkload with let
you monitor:   
-   the network traffic on a given interface
-   the CPU load average
-   the memory usage
-   the number of concurrent users the server is handling over time

  
This is very useful to detect memory leaks or abnormal consumption of
memory.   
  
To do this, you need to run a monitor server provided by Funkload on
the server you want to watch. Once Funkload is installed there, create a
***monitor.conf*** file.   
   [server]

    host = server

    port = 8008

    interval = .5

    interface = eth0



    [client]

    host = master

    port = 8008

  
Here ***server*** is the server I am benching, and the monitor server
will run on the port 8008. The interface parameter will just tell
Funkload which one to watch. The client section tells the monitor server
which server will call it, so our bench master.   
  
Once this is saved, simply run the monitor server with:   
   $ fl-monitor-ctl monitor.conf start

    Starting monitor server at http://localhost:8008/ as daemon.

  
use stop to stop it, obviously.   
  
Last but not least, back to our master bench server, open Simple.conf
and add these sections:   
   [monitor]

    hosts = localhost



    [localhost]

    description = The application server

    port = 8008

  
You're all set ! Simply run the benches as usual, and you should see a
new section in the reports you're generating, with four new graphs.   
  
[![image][]][]   
  
[![image][2]][]   
  
That's all. I hope you found this mini-tutorial interesting, and that
you'll give Funkload a shot. I've tried many tools, like The Grinder,
Apache JMeter, and some proprietary things from Mercury etc. And
Funkload, out of the box, beats them all because it let me create my own
stress tests without any crazy interface of framework.   
  
Thanks for all the work Ben.

  [here]: http://tarekziade.wordpress.com/2011/07/27/how-to-stress-test-your-app-using-funkload-part-1/
  [1]: http://tarekziade.wordpress.com/2010/12/09/funkload-fabric-quick-and-dirty-distributed-load-system/
  [Paramiko]: http://www.lag.net/paramiko/
  [See this article if you don't know how to do it.]: http://linuxproblem.org/art_9.html
  [image]: http://tarekziade.files.wordpress.com/2011/07/localhost_monitorcpu.png
    "localhost_MonitorCPU"
  [![image][]]: http://tarekziade.files.wordpress.com/2011/07/localhost_monitorcpu.png
  [2]: http://tarekziade.files.wordpress.com/2011/07/localhost_monitormemfree.png
    "localhost_MonitorMemFree"
  [![image][2]]: http://tarekziade.files.wordpress.com/2011/07/localhost_monitormemfree.png
