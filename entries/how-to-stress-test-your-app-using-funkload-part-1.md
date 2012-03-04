Title: How to stress test your app using Funkload -- part 1
Date: 2011-07-27 13:07
Category: mozilla, python

***EDIT: [Part 2 is now published][](distributed tests and
monitoring)***   
  
[Funkload][] is a functional and stress test tool that can be used on
your web applications.   
  
It's my favorite stress tool for these reasons:   
-   stress tests are implemented as PyUnit tests, so they can also be
    used as functional tests
-   the test runner is very light, it's dead easy to run a stress test
    on your box against a local app
-   it's simple to do a distributed test with a few extra options --
    Funkload will drive the other boxes using SSH
-   Funkload provides nice reporting features out of the box: you can do
    trends and diff reports
-   You can monitor the server being tested

  
This blog post demonstrates how to use Funkload on a dummy app and
generate report. A second blog post will explain how to run the test
using several test servers, and how to monitor the server that runs the
application.   
#### The tested application

  
The dummy application we'll stress test for this demo is a very simple
WSGI application that can be run in plain Python, or using Gunicorn:   
   from wsgiref.simple_server import make_server

    import time



    def application(environ, start_response):

        status = '200 OK'

        headers = [('Content-type', 'text/plain')]

        start_response(status, headers)

        time.sleep(0.1)

        return ["Hello World"]



    if __name__ == '__main__':

        httpd = make_server('', 5000, application)

        print("Serving on port 5000")

        try:

            httpd.serve_forever()

        except KeyboardInterrupt:

            pass

  
Every time the application is called, no matter what's the request path
or method, it will sleep for 100 ms then return a Hello World.   
  
Let's run our application:   
   $ python wsgiapp.py

    Serving on port 5000

  
The application is ready to get some hits !   
### Installing Funkload

  
Let's open a new shell and create a local environment in a directory,
using [Virtualenv][], and install Funkload in it:   
   $ virtualenv --no-site-package --distribute .

    New python executable in ./bin/python2.6

    Also creating executable in ./bin/python

    Installing distribute.................................done.

    $ bin/pip install Funkload

    Downloading/unpacking Funkload

    ...

    Successfully installed docutils Funkload webunit

    Cleaning up..

  
Once everything's installed, you will get in the local **bin**
directory a few Funkload scripts:   
   $ ls bin/fl*

    bin/fl-build-report    bin/fl-install-demo 

    bin/fl-record     bin/fl-run-test

    bin/fl-credential-ctl  bin/fl-monitor-ctl  

    bin/fl-run-bench

  
The two scripts that interest us right now are ***fl-run-test*** and
***fl-run-bench***.   
### A first Funkload test

  
Let's create a **test\_simple.py** module in our directory:   
   import unittest

    from random import random

    from funkload.FunkLoadTestCase import FunkLoadTestCase



    class Simple(FunkLoadTestCase):



        def setUp(self):

            self.server_url = self.conf_get('main', 'url')



        def test_simple(self):

            server_url = self.server_url       

            res = self.get(server_url, description='Get url')

            self.assertEqual(res.code, 200)

            self.assertEqual(res.body, "Hello World")



    if __name__ in ('main', '__main__'):

        unittest.main()

  
This test simply checks that the server returns ***Hello World*** and
that the response status code is ***200***.   
  
To run this test, Funkload needs a few options to run. These options
can be placed in a configuration file. Let's create a **Simple.conf**
file with this content:   
   [main]

    title = Demo

    description = Simple demo

    url = http://localhost:5000



    [test_simple]

    description = Access our Demo app



    [ftest]

    log_to = console file

    log_path = simple-test.log

    result_path = simple-test.xml

    sleep_time_min = 0

    sleep_time_max = 0



    [bench]

    cycles = 5:10:20

    duration = 10

    startup_delay = 0.01

    sleep_time = 0.01

    cycle_time = 1

    log_to =

    log_path = simple-bench.log

    result_path = simple-bench.xml

    sleep_time_min = 0

    sleep_time_max = 0.5

  
Those are defining options Funkload will use when it's running.   
  
Now we can try out our Funkload script with the*** fl-run-test***
script, which will run the tests just once:   
   $ bin/fl-run-test test_simple.py

    .

    ----------------------------------------------------------------------

    Ran 1 test in 0.104s



    OK

  
Victory ! The test is working nicely.   
  
Let's now try a full bench, using ***fl-run-bench***. The bench script
takes an extra option which is the test method to use to run the bench:
  
   $ bin/fl-run-bench test_simple.py Simple.test_simple

    ========================================================================

    Benching Simple.test_simple

    ========================================================================

    Access our Demo app

    ------------------------------------------------------------------------



    Configuration

    =============



    * Current time: 2011-07-27T12:02:35.319172

    * Configuration file: /home/tarek/dev/hg.mozilla.org/funkload-demo/Simple.conf

    * Log xml: /home/tarek/dev/hg.mozilla.org/funkload-demo/simple-bench.xml

    * Server: http://localhost:5000

    * Cycles: [5, 10, 20]

    * Cycle duration: 10s

    * Sleeptime between request: from 0.0s to 0.5s

    * Sleeptime between test case: 0.01s

    * Startup delay between thread: 0.01s



    Benching

    ========



    * setUpBench hook: ... done.



    Cycle #0 with 5 virtual users

    -----------------------------



    * setUpCycle hook: ... done.

    * Current time: 2011-07-27T12:02:35.321906

    * Starting threads: ..... done.

    * Logging for 10s (until 2011-07-27T12:02:45.380090): .............................................................................................. done.

    * Waiting end of threads: ..... done.

    * Waiting cycle sleeptime 1s: ... done.

    * tearDownCycle hook: ... done.

    * End of cycle, 11.66s elapsed.

    * Cycle result: **SUCCESSFUL**, 94 success, 0 failure, 0 errors.



    Cycle #1 with 10 virtual users

    ------------------------------



    * setUpCycle hook: ... done.

    * Current time: 2011-07-27T12:02:46.986399

    * Starting threads: .......... done.

    * Logging for 10s (until 2011-07-27T12:02:57.117788): .............................................................................................. done.

    * Waiting end of threads: .......... done.

    * Waiting cycle sleeptime 1s: ... done.

    * tearDownCycle hook: ... done.

    * End of cycle, 12.86s elapsed.

    * Cycle result: **SUCCESSFUL**, 94 success, 0 failure, 0 errors.



    Cycle #2 with 20 virtual users

    ------------------------------



    * setUpCycle hook: ... done.

    * Current time: 2011-07-27T12:02:59.844273

    * Starting threads: .................... done.

    * Logging for 10s (until 2011-07-27T12:03:10.100680): ................................................................................................ done.

    * Waiting end of threads: .................... done.

    * Waiting cycle sleeptime 1s: ... done.

    * tearDownCycle hook: ... done.

    * End of cycle, 23.18s elapsed.

    * Cycle result: **SUCCESSFUL**, 96 success, 0 failure, 0 errors.



    * tearDownBench hook: ... done.



    Result

    ======



    * Success: 284

    * Failures: 0

    * Errors: 0



    Bench status: **SUCCESSFUL**

  
The script runs three cycles of respectively 5, 10 and 20 virtual
users, for 10 seconds each. This is configured with the **cycles** and
**duration** options in the ***[bench]*** section of the configuration
file (*cycles=5:10:20* and *duration=10*), but you can also provide
these options through the command line.   
  
Let's say you want to run 2 then 5 users for 5 seconds each:   
   $ bin/fl-run-bench --cycles=2:5 --duration=5 test_simple.py Simple.test_simple

    ========================================================================

    Benching Simple.test_simple

    ========================================================================

    Access our Demo app

    ------------------------------------------------------------------------



    Configuration

    =============



    * Current time: 2011-07-27T12:07:56.294745

    * Configuration file: /home/tarek/dev/hg.mozilla.org/funkload-demo/Simple.conf

    * Log xml: /home/tarek/dev/hg.mozilla.org/funkload-demo/simple-bench.xml

    * Server: http://localhost:5000

    * Cycles: [2, 5]

    * Cycle duration: 5s

    * Sleeptime between request: from 0.0s to 0.5s

    * Sleeptime between test case: 0.01s

    * Startup delay between thread: 0.01s



    Benching

    ========



    * setUpBench hook: ... done.



    Cycle #0 with 2 virtual users

    -----------------------------



    * setUpCycle hook: ... done.

    * Current time: 2011-07-27T12:07:56.297701

    * Starting threads: .. done.

    * Logging for 5s (until 2011-07-27T12:08:01.322419): ............................. done.

    * Waiting end of threads: .. done.

    * Waiting cycle sleeptime 1s: ... done.

    * tearDownCycle hook: ... done.

    * End of cycle, 6.28s elapsed.

    * Cycle result: **SUCCESSFUL**, 29 success, 0 failure, 0 errors.



    Cycle #1 with 5 virtual users

    -----------------------------



    * setUpCycle hook: ... done.

    * Current time: 2011-07-27T12:08:02.574411

    * Starting threads: ..... done.

    * Logging for 5s (until 2011-07-27T12:08:07.637394): ............................................. done.

    * Waiting end of threads: ..... done.

    * Waiting cycle sleeptime 1s: ... done.

    * tearDownCycle hook: ... done.

    * End of cycle, 6.60s elapsed.

    * Cycle result: **SUCCESSFUL**, 45 success, 0 failure, 0 errors.



    * tearDownBench hook: ... done.



    Result

    ======



    * Success: 74

    * Failures: 0

    * Errors: 0



    Bench status: **SUCCESSFUL**

  
Now let's check the reporting features..   
### Reporting

  
Everytime you are running a bench, an XML file is produced. In our case
it's ***simple-test.xml***   
  
The XML file contains raw results and can be used to produce reports.
fl-build-report takes these XML file and produce reports out of them.   
  
For example, you can create an HTML report with the ***html*** option.
  
  
Make sure you have **gnuplot** installed, then run:   
   $ bin/fl-build-report --html --output-directory=html simple-bench.xml

    Creating html report: ...

    done:

    /home/tarek/dev/hg.mozilla.org/funkload-demo/html/test_simple-20110727T120756/index.html

  
The result is a nice HTML page containing various diagrams, like the
number of requests per seconds depending on the number of virtual
concurrent users.   
[![image][]][]   
  
Another nice report is the diff report, which takes two already
generated reports, and build a diff one -- if you get some errors, make
sure you have the latest ***gnuplot*** installed.   
   $ bin/fl-build-report -o html --diff html/test_simple-20110727T123642 html/test_simple-20110727T123718

    Creating diff report ... done:

    /home/tarek/dev/hg.mozilla.org/funkload-demo/html/diff_simple-20110727T_123718_vs_123642/index.html

  
The diagram you get will provide a clear overview of the differences
between the two runs. This is useful if you want to check for speed
regression when you've changed some code.   
  
[![image][1]][]   
  
The trending report has the same goal, but can be built using more that
two runs:   
   $ bin/fl-build-report -o html --trend html/*

    Creating trend report ... done:

    /home/tarek/dev/hg.mozilla.org/funkload-demo/html/trend-report/index.html

  
That's useful to see how your application is doing over time.   
  
[![image][2]][]   
  
In the next post we see two extra features Funkload provides:   
-   run distributed tests
-   monitor the benched server

  
[Go to part 2][Part 2 is now published]

  [Part 2 is now published]: http://tarekziade.wordpress.com/2011/07/28/how-to-stress-test-your-app-using-funkload-part-2/
  [Funkload]: http://funkload.nuxeo.org/
  [Virtualenv]: http://pypi.python.org/pypi/virtualenv
  [image]: http://tarekziade.files.wordpress.com/2011/07/requests_rps.png
    "requests_rps"
  [![image][]]: http://tarekziade.files.wordpress.com/2011/07/requests_rps.png
  [1]: http://tarekziade.files.wordpress.com/2011/07/rps_diff.png
    "rps_diff"
  [![image][1]]: http://tarekziade.files.wordpress.com/2011/07/rps_diff.png
  [2]: http://tarekziade.files.wordpress.com/2011/07/trend_avg.png
    "trend_avg"
  [![image][2]]: http://tarekziade.files.wordpress.com/2011/07/trend_avg.png
