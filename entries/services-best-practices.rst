Web Services Best Practices
###########################

:date: 2016-10-01 09:50
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade


The other day I've stumbled on a
`reddit comment on Twitter about micro-services <https://pbs.twimg.com/media/CsbMpQ8VYAA5XLA.jpg>`_.
It really nailed down the best practices around building web services, and
I wanted to use it as a basis to write down a blog post. So all the credits go
to **rdsubhas** for this post :)

Web Services in 2016
--------------------

The notion of **micro-service** rose in the past 5 years, to describe the fact that
our applications are getting splitted into smaller pieces that need to interact
to provide the same service that what we use to do with monolothic apps.

Splitting an app in smaller micro services is not always the best design decision
in particular when you own all the pieces. Adding more interactions to serve a
request just makes things more complex and when something goes wrong you're
just dealing with a more complex system.

Peope often think that it's easier to scale an app built with smaller blocks,
but it's often not the case, and sometimes you just end up with a slower,
over-engineered solution.

So why are we building micro-services ?

What really happened I think is that most people moved their apps to cloud providers
and started to use the provider services, like centralized loggers, distributed
databases and all the fancy services that you can use in Amazon, Rackspace or
other places.

In the `LAMP <https://en.wikipedia.org/wiki/LAMP_%28software_bundle%29>`_
architecture, we're now building just one piece of the **P** and
configuring up to 20 services that interact with it.

A good chunk of our daily jobs now is to figure out how to deploy apps, and
even if some tools like Kubertenes gives us the promise of an abstraction
on the top of cloud providers, the reality is that you have to learn
how AWS or another provider works to built something that works well.

Understanding how multi-zone replication works in RDS is mandatory
to make sure you control your application behavior.

Because no matter how fancy and reliable, all those services are,
the quality of your application will be tighted to its ability
to deal with problems like network splits or timeouts etc.

That's where the shift in bests practices is: when something goes wrong,
it's harder just to tail your postgres logs and your Python app
and see what's going on. You have to deal with many parts.


Best Practices
--------------

I can't find the original post on Reddit, so I am just going to copy
it here and curate it with my own opinions and with the tools
we use at Mozilla. I've also removed what I see as redundant tips.

**Basic monitoring, instrumentation, health check**

We use statsd everywhere and services like Datadog to see what's going on
in our services.

We also have two standard heartbeat endpoints that are used to monitor
the services. One is a simple round trip where the service just sends back
a 200, and one is more of a smoke test, where the service tries to use
**all** of its own backends to make sure it can reach them and read/write
into them.

We're doing this distinction because the simple round trip
health check is being hit very often, and the one that calls all the
services the service use, less often to avoid doing too much traffic
and load.



**Distributed logging, tracing**

Most of our apps are in Python, and we use Sentry to collect tracebacks and
sometimes New Relic to detect problems we could not reproduce in a dev
environment.


**Isolation of the whole build+test+package+promote for every service.**

We use Travis-CI to trigger most of our builds, tests and packages. Having
reproducible steps made in an isolated environment like a CI gives us
good confidence on the fact that the service is not spaghetti-ed with
other services.

The bottom line is that "gill pull & make test" should work in Travis
no matter what, without calling an external service. The travis YML
file, the Makefile and all the mocks in the tests are rhoughly
our 3 gates to the outside world. That's as far as we go in term
of build standards.


**Maintain backward compatibility as much as possible**

The initial tip included forward compatibility. I've removed it,
because I don't think it's really a thing when you build web services.
Forward compatibility means that an older
version of your service can accept requests from newer version of the client
side. But I think it should just be a deployment issue and an error management on
the client side, so you don't bend your data design just so it works with
older service versions.

For backward compatibility though, I think it's mandatory to make sure that
you know how to interact with older clients, whatever happens. Depending
on your protocol, older clients could get an update triggered, partially work,
or just work fine -- but you have to get this story right even before the first
version of your service is published.

But if your design has dramatically changed, maybe you need to accept
the fact that your are building something different, and just treat it
as a new service (with all the pain that brings if you need to migrate data.)

Firefox Sync was one complex service to migrate from its first version to its
latest version because we got a new authentication service along the way.

**Ready to do more TDD**

I just want to comment on this tip. Doing **more** TDD imply that it's cool
to do less TDD when you build software that's not a service.

I think this is a bad advice. You should simply do TDD right.
Not less or more, but right.

Doing TDD right in my opinion is :

- 100% coverage unless your have something very specific you can't mock.
- Avoid over-mocking at all costs because testing mocks is often slightly different
  from testing the real stuff.
- Make sure your tests pass all the time, and are fast to pass, otherwise people
  will just start to skip them.
- Functional tests are generally superior to unit tests for testing services.
  I often drop unit tests in some services projects because everything is covered
  by my functional tests. Remember: you are not building a library.


**Have engineering methodologies and process-tools to split down features and develop/track/release them across multiple services (xp, pivotal, scrum)**

That's a good tip. Trying to reproduce what has worked when building a service,
to build the next one is a great idea.

However, this will only work if the services are built by the same team, because
the whole engineering methodology is adopted and adapted by people. You don't
stick into people's face the SCRUM methodology and make the assumption
that everyone will work as described in the book. This never happens. What
usually happens is that every member of the team brings their own recipes on
how things should be done, which tracker to use, what part of XP makes sense to them,
and the team creates its own custom methodology out of this. And it takes time.

Start a service with a new team, and that whole phase starts again.



