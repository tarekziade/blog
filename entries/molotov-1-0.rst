Load Testing at Mozilla
#######################

:date: 2017-03-23
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

After a stabilization phase, I am happy to announce that
`Molotov 1.0 <http://molotov.readthedocs.io/>`_ has been
released!

.. image:: http://molotov.readthedocs.io/en/latest/_static/logo.png

(Logo by Juan Pablo Bravo)

This release is an excellent opportunity to explain a little bit how we
do load testing at Mozilla, and what we're planning to do
in 2017 to improve the process.

I am talking here specifically about load testing our HTTP
services, and when this blog post mentions what Mozilla
is doing there, it refers mainly to the Mozilla QA team,
helped with Services developers team that works on some of our
web services.


What's Molotov?
---------------

**Molotov is a simple load testing tool**

Molotov is a minimalist load testing tool you can use to load test
an HTTP API using Python. Molotov leverages Python 3.5+ asyncio
and uses aiohttp to send some HTTP requests.

Writing load tests with Molotov is done by decorating asynchronous
Python functions with the @scenario function::

    from molotov import scenario

    @scenario(100)
    async def my_test(session):
        async with session.get('http://localhost:8080') as resp:
            assert resp.status == 200

When this script is executed with the **molotov** command, the
**my_test** function is going to be repeatedly called to perform
the load test.

Molotov tries to be as transparent as possible and just hands
over session objects from the aiohttp.client module.

The full documentation is here: http://molotov.readthedocs.io

Using Molotov is the first step to load test our services. From
our laptops, we can run that script and hammer a service to
make sure it can hold some minimal charge.


What Molotov is not
-------------------

**Molotov is not a fully-featured load testing solution**

Load testing application usually comes with high-level features to understand
how the tested app is performing. Things like performance metrics are displayed
when you run a test, like what Apache Bench does by displaying how many
requests it was able to perform and their average response time.

But when you are testing web services stacks, the metrics you are
going to collect from each client attacking your service will
include a lot of variation because of the network and clients
CPU overhead. In other words, you cannot guarantee reproducibility
from one test to the other to track precisely how your app
evolves over time.

Adding metrics directly in the tested application itself is much
more reliable, and that's what we're doing these days at Mozilla.

That's also why I have not included any client-side metrics in Molotov,
besides a very simple StatsD integration. When we run Molotov at Mozilla,
we mostly watch our centralized metrics dashboards and see how the tested
app behaves regarding CPU, RAM, Requests-Per-Second, etc.

Of course, running a load test from a laptop is less than ideal.
We want to avoid the hassle of asking people to install Molotov & all the
dependencies a test requires everytime they want to load test a deployment --
and run something from their desktop. Doing load tests occasionally from your
laptop is fine, but it's not a sustainable process.

And even though a single laptop can generate a lot of loads (in one project,
we're generating around 30k requests per second from one laptop, and happily
killing the service), we also want to do some distributed load.

We want to run Molotov from the cloud. And that's what we do,
thanks to Docker and Loads.


Molotov & Docker
----------------

Since running the Molotov command mostly consists of using the right
command-line options and passing a test script, we've added in Molotov
a second command-line utility called **moloslave**.

Moloslave takes the URL of a git repository and will clone it and
run the molotov test that's in it by reading a configuration file.
The configuration file is a simple JSON file that needs to be at the
root of the repo, like how you would do with Travis-CI or other tools.

See http://molotov.readthedocs.io/en/latest/slave

From there, running in a Docker can be done with a generic image that
has Molotov preinstalled and picks the test by cloning a repo.

See http://molotov.readthedocs.io/en/latest/docker

Having Molotov running in Docker solves all the dependencies issues you
can have when you are running a Python app. We can specify all the
requirements in the configuration file and have moloslave installs
them. The generic Docker image I have pushed in the Docker Hub is
a standard Python 3 environment that works in most case, but
it's easy to create another Docker image when a very specific environment
is required.

But the bottom line is that anyone from any OS can "docker run" a load
test by simply passing the load test Git URL into an environment
variable.


Molotov & Loads
---------------

Once you can run load tests using Docker images, you can use
specialized Linux distributions like **CoreOS** to run them.

Thanks to **boto**, you can script the Amazon Cloud and deploy hundreds
of CoreOS boxes and run Docker images in them.

That's what the Loads project is -- an orchestrator that will run hundreds
of CoreOS EC2 instances to perform a massively distributed load test.

Someone that wants to run such a test has to pass to a **Loads Broker**
that's running in the Amazon Cloud a configuration that tells
where is the Docker that runs the Molotov test, and says for how long the
test needs to run.

That allows us to run hours-long tests without having to depend on a
laptop to orchestrate it.

But the Loads orchestrator has been suffering from reliability issues.
Sometimes, EC2 instances on AWS are not responsive anymore, and
Loads don't know anymore what's happening in a load test.
We've suffered from that and had to create specific code to clean up
boxes and avoid keeping hundreds of zombie instances sticking around.

But even with these issues, we're able to perform massive load tests
distributed across hundreds of boxes.


Next Steps
----------

At Mozilla, we are in the process of gradually switching all our load
testing scripts to Molotov. Using a single tool everywhere will allow us
to simplify the whole process that takes that script and performs
a distributed load test.

I am also investigating on improving metrics. One idea is to
automatically collect all the metrics that are generated during a load
test and pushing them in a specialized **performance trend** dashboard.

We're also looking at switching from Loads to Ardere. Ardere is a new
project that aims at leveraging Amazon ECS. ECS is an orchestrator we
can use to create and manage EC2 instances. We've tried ECS in the past, but it
was not suited to run hundreds of boxes rapidly for a load test. But ECS has
improved a lot, and we started a prototype that leverages it and it looks
promising.

For everything related to our Load testing effort at Mozilla, you can
look at https://github.com/loads/

And of course, everything is open source and open to contributions.
