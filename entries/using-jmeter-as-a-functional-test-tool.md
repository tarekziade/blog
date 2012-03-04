Title: Using JMeter as a functional test tool
Date: 2007-09-28 08:05
Category: plone, python, zope

Today I made an audit on some customer intranet, and I used [JMeter][]
to perform stress tests. This tool is awesome, as you can get a whole
lot of live statistics, and create a powerfull, distributed stress
campaign.   
  
There are some features to control that the output of HTTP calls are
right, with simple but sufficient patterns (the output contains, the
output doesn't contains, the header has.., etc..) and regular
expressions can be used.   
  
A high-level functional test is really nothing much more than that: it
performs a user story and check for the result. Ok, maybe some tool like
[Selenium][] have more features, but they are not essential ones, and
JMeter brings some better things.   
  
What brings JMeter beside functionnal testing are:   
-   a powerfull reporting tool
-   the ability to stress-load your application with the user stories

  
A comparable tool, less powerfull though, is [ben's funkload][].   
  
-\> Creating you app through JMeter will give you the opportunity to
tune it without extra work.   
  
It won't make me drop zope.testbrowser tests, because those are merged
within my code and explain how it works in doctests, but it will surely
make my customers feel better with JMeter reporting capabilities, and
myself calmer with its performance analysis:   
  
**"Hey, look at the screen, that's your functionality \#123 running
right now, and you can see its performance through this live performance
graph"**   
  
[![graph\_results.png][]][]

  [JMeter]: http://jakarta.apache.org/jmeter/
  [Selenium]: http://wiki.openqa.org/display/SEL/Home
  [ben's funkload]: http://funkload.nuxeo.org/
  [graph\_results.png]: http://tarekziade.files.wordpress.com/2007/09/graph_results.thumbnail.png
  [![graph\_results.png][]]: http://tarekziade.files.wordpress.com/2007/09/graph_results.png
    "graph_results.png"
