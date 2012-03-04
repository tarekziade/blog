Title: Another GSOC Idea : a PyPI testing infrastructure
Date: 2010-03-21 21:38
Category: python

Last year I've proposed [a GSOC project][] that no student picked up. I
think the fact that it was titled "A Distutils Regression System" was
not really appealing. I should have called it a "PyPI testing
infrastructure" because that's what it is really. And I know today
exactly how the system should work, so I can make a clearer proposal.
The proposal page is here:
[http://wiki.python.org/moin/SummerOfCode/PyPITestingInfrastructure][]   
  
So basically, the idea is to run a service that will receive update
notifications everytime someone uploads a distribution at PyPI, to
perform a few tests on it and send a report to the author by email (or
display it on a website).   
  
The tests we want to do are quite simple:   
-   does "*python setup.py install"* works or throw out some errors ?
-   what files are modified on the system upon installation ?
-   does the tests pass ?

  
For the latter, it supposes that we are able to detect and run the
tests. They are no conventions yet (but the TIP list is working on this)
but we can try out a few things on the source tree.   
  
***EDIT: for all the tests we want to run on a distribution, we should
look at the [CheeseCake][] project (Thanks Richard for mentioning it in
the comments)***   
  
Getting update notifications is fairly simple now that Martin added a
[PubSubHubBub][] service at PyPI.   
  
The core part of the project is to make sure the commands are run on a
clean system. The easiest way to do it is to use Virtual Machines
through a service like EC2: we can run the test, then rollback the VM
state so it's back in a clean state. There are a few libs in Python to
drive systems like EC2. We also need to secure the VM so the code that
is run doesn't make network calls. If the project tests are relying on a
network resource, those are bad tests anyways.   
  
Last, but not least, if we want to get back interesting reports, we
need to probe what's going on. It's simple at Python level, but we never
know what can happen in a *setup.py* module. If a C module or an
external program is called somehow in there, it could perform operations
on the system we wouldn't be aware of. I think [SystemTap][] is a great
tool to probe for all operations at the OS level. I am not sure how to
do it under Win32 though..   
  
But having a working story under Linux would be already a great thing,
so I am not worrying about that at this point.   
  
So, I've entered the topic in the GSOC list, and I am willing to mentor
this if a student wants to do this. I know Titus is also very interested
in this topic, so we might work together on this, as co-mentors, which
would be great. That's a topic we've discussed several times in the past
and I think Titus wants a similar system. Mmm.. wait, we all do, don't
we ? ;)

  [a GSOC project]: http://wiki.python.org/moin/SummerOfCode/2009
  [http://wiki.python.org/moin/SummerOfCode/PyPITestingInfrastructure]: http://wiki.python.org/moin/SummerOfCode/PyPITestingInfrastructure
  [CheeseCake]: http://pycheesecake.org
  [PubSubHubBub]: http://en.wikipedia.org/wiki/PubSubHubbub
  [SystemTap]: http://sourceware.org/systemtap/
