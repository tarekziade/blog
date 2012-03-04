Title: QA script on web services
Date: 2011-12-12 11:00
Category: mozilla, python

The other task Alexis and I are going to work on this week, besides
Cornice, is a QA script for web services.   
  
The goal is simple : check that a set of web services are HTTP
compliant. For example, does your application send the proper 406 error
when an unsupported Accept is asked by the client ?   
  
If you document properly your web services, asking for an unsupported
Accept should not occur of course, but in most projects those protocol
details are often a bit vague. And someone that writes a client software
will inevitably make some assumptions based on his HTTP knowledge on how
the application is supposed to behave.   
  
Richard Newman came up with a fair list of tests we could run against a
web app already, and we've started to summarise and add more of them
here: [https://wiki.mozilla.org/Services/WALint][]   
  
The idea of the script is to print out a report of errors and warnings
it found on a web app, exactly like a lint tool would do on some code.
That's what I called it ***WALint*** (Web App Lint). Alexis doesn't like
the name but he did not find a better name yet ;)   
  
The way it works is that you describe in a configuration file the URIs
of your web services, then WALint runs tests against them, using what we
called *controllers*.   
  
Each controller is in charge of trying out something on the web app,
using a small HTTP test client (using WebTest), given a path and a
method. WALint will provide built-in controllers and will be extensible.
We will have Mozilla-specific tests, like the maximum size of a query
string, or the maximum size of the request, since those limits are
specific to the used stack.   
  
We got bitten by this is the past in Sync - one web service failed to
work properly because the client was building a super long query string,
that was truncated along the way in our stack.   
  
Our final goal with this tool is to be able to add in Jenkins these
controls for all our web apps, and catch more problems before they occur
in production.   
  
Since it's also useful while you build your code, WALint will have a
UnitTest integration, so you can run it as a functional test from within
your test suite -- In that case, it will run directly against the code.
  
  
As usual, feedback & contributions are welcome. The code is being built
here: [https://github.com/mozilla-services/walint][]

  [https://wiki.mozilla.org/Services/WALint]: https://wiki.mozilla.org/Services/WALint
  [https://github.com/mozilla-services/walint]: https://github.com/mozilla-services/walint
