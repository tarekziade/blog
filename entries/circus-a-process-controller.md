Title: circus - a process controller
Date: 2012-02-24 16:58
Category: mozilla, python

Benoit -- from Gunicorn fame -- and myself have started to work on
Circus, a process controller.   
  
I really like this small project for several reasons:   
-   it's the first time we're building a Mozilla Services library from
    the ground with a contributor that's not for the Mozilla community
    but rather from the Python community
-   this library is the last bit we're missing in our Python server
    stack to have a full control over it

  
![image][]   
### Why a new lib ?

  
A process controller is mostly a script that manages processes, sends
signals to them, re-spawns them whenever they die. There are numerous
libraries out there that are already doing this so creating this new
library can sound like NIH.   
  
I have looked at several projects before we've started this one, like
[supervisord][], [BluePill][], and so on. But none of them met exactly
all of my requirements - here's my audacious list:   
-   can be used as a program and as a library -- so in Python
-   a way to query the system to perform live operations via a (secured)
    remote console such as   
   -   add or remove workers
    -   restart the workers, broadcast signals
    -   get some stats on what's going on

      
-   advanced process management features, like   
   -   controlled flapping - trying to restart n times a worker that
        dies on startup -- then abandon
    -   auto-grow - add workers if all workers are 100% busy n seconds
        (for CPU-bound workers)
    -   auto-shrink - remove workers if they are bored
    -   run in containment tools like cgroups

      
-   meta-controller that can drive several controller remotely, to
    manage a cluster (later)

  
BluePill looked very promising because it has most features we wanted,
but unfortunately, since we'd like to use it as a library, it's a
blocker. Also, while the DSL is quite sexy, that's not something we'd
want to use as-is because we're in a ini-file land were every tool is
configured via a new *[section]* in a config file.   
  
Supervisord is excellent -- and widely used.   
  
I have tried to extend it and I must admit I had a little hard time to
wrap my head into it. This is purely technical, but some choices made in
Supervisord make it hard for me to extend it the way we want -- like the
fact that the main class is driven by a configuration where I wanted to
completely separate these two concepts. I want to be able to create a
class and tell it to run *n* workers without having to create a
configuration object in the middle. There's also now the subprocess
module in Python, and while Supervisord is probably compatible with
older versions of Python, we want 2.6+ so we can make the code way less
verbose.   
  
Here's an example on how to run 3 workers on a given command with
Circus - KISS:   
   from circus import get_trainer



    trainer = get_trainer(cmd, 3)

    try:

        trainer.start()

    finally:

        trainer.stop()

  
Anyways -- we'll still be suffering from our choice for a bit -- we'll
encounter issues that other projects have encountered before. But I
think that's for the best, and Benoit has a lot of experience in this
area with Gunicorn - I expect both project to exchange a lot of pieces.
  
### Current status

  
We're busy polishing the tool, but it's already in a usable state. For
Mozilla, the main use case is to run Crypto Workers for Powerhose ([read
about Powerhose here][]) and we can already do this.   
  
Turns out all Powerhose does is wrapping the ***get\_trainer()*** call
into a class called *Workers*. (see
[https://github.com/mozilla-services/powerhose/blob/master/powerhose/client/workers.py)][]
and when the web application is launched, it runs a Powerhose Master and
some PowerHose Workers that way -- delegating all the process management
tasks to Circus.   
  
For our Ops, Circus provide a small console that will let them watch
the workers, add some, restart them, etc.   
  
We've reached a point where we have almost all the features we wanted
for our needs, but I suspect the project will gain many more features
with the contributions of Benoit and maybe other folks in the future.   
  
Nothing's released yet -- I'll wait for it to pass our benches, QA
tests before I cut a release. But the code is growing here if you're
curious : [https://github.com/mozilla-services/circus][].   
  
Yeah, it's under-tested because I did not come up with a nice testing
environment yet - it's hard to do this properly when you deal with
processes and signals -- and mocking this is a bit of a non-sense. I
suspect the best way will be to run functional tests with workers that
produce some content the test can check out.

  [image]: http://farm3.staticflickr.com/2602/3988814835_83f13f6d53.jpg
    "The Flying Circus official food (cc)"
  [supervisord]: http://supervisord.org/
  [BluePill]: https://github.com/arya/bluepill
  [read about Powerhose here]: http://tarekziade.wordpress.com/2012/02/06/scaling-crypto-work-in-python/
  [https://github.com/mozilla-services/powerhose/blob/master/powerhose/client/workers.py)]:
    https://github.com/mozilla-services/powerhose/blob/master/powerhose/client/workers.py)
  [https://github.com/mozilla-services/circus]: https://github.com/mozilla-services/circus
