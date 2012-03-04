Title: Continuous Load Testing wint Funkload
Date: 2011-06-10 13:08
Category: mozilla, python

There's one thing we're often neglect when we build applications:
**performance trending**. In other words, are things getting slower over
time because the code base grows, or because someone introduced a* O(n)*
piece of code somewhere ?   
  
In very big projects this is a major concern: the code grows and the
performances are steadily decreasing. I read somewhere that this became
a problem in the Linux Kernel at some point. Can't find a good link on
this. If you know about this story, please let me know.   
  
In smaller base code, it's still important to watch, and by following
the changes you can detect such issues. But you can't focus all the time
on everything. That's why doing it automatically and continuously is
important.   
  
For our Services at Mozilla, we're benching our APIs with stress tests,
but what we miss is a bit of automation, so we can do ***continuous load
testing*** and keep a history of our performances.   
  
Some examples:   
-   I want to see after a new feature has been introduced, if my RPS
    average on my API remains the same.
-   When some indexes are changed in the Database, what's the impact on
    the overall performances ?

  
Getting good statistics from continuous load testing requires a stable
environment with realistic data, so the trend means something, and
that's hard to keep over long periods of time. But it's manageable for
shorter periods, like weeks, I guess.   
### Funkload trending

  
I've started to work on this topic this week, to try to set up some
automation in our stress tests, and I've the tool it takes to do this
easily: [Funkload][].   
  
[caption id="" align="alignright" width="531" caption="Disclaimer:
These are not Firefox Sync performances, just a sample from Funkload
docs ;)"]![image][][/caption]   
  
Everytime you run a Funkload stress test, it produces its results in an
XML file you can store.   
  
Funkload then provides a script to generate reports for every bench
your run, but is also able to produce trend reports, using Gnuplot.   
  
So what I've started to do is:   
-   run Funkload via Jenkins against the server that has the deployed
    APIs
-   collect all produced XML files
-   refresh and publish the trend report

  
Grinder is nice, and I could do the same thing with the raw data. But
why bother, Funkload does already all the reporting needed \\o/

  [Funkload]: http://funkload.nuxeo.org
  [image]: http://funkload.nuxeo.org/report-example/trend-report/trend_spps.png
    "Trend"
