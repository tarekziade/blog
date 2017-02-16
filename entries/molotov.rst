Molotov, simple load testing
############################

:date: 2017-02-16
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade


I don't know why, but I am a bit obsessed with load testing tools. I've tried
dozens, I built or been involved in the creation of over ten of them in the past 15
years. I am talking about load testing HTTP services with a simple HTTP client.

Three years ago I built **Loads** at Mozilla, which is still being used to load test
our services - and it's still evolving. It was based on a few fundamental
principles:

1. A Load test is an integration test that's executed many times in parallel
   against a server.

2. Ideally, load tests should be built with vanilla Python and a simple HTTP client.
   There's no mandatory reason we have to rely on a Load Test class or things
   like this - the lighter the load test framework is, the better.

3. You should be able to run a load test from your laptop without having to
   deploy a complicated stack, like a load testing server and clients, etc.
   Because when you start building a load test against an API, step #1 is
   to start with small loads from one box - not going nuclear from AWS on day 1.

4. Doing a massively distributed load test should not happen & be driven from
   your laptop. Your load test is one brick and orchestrating a distributed
   load test is a problem that should be entirely solved by another software
   that runs in the cloud on its own.

Since Loads was built, two major things happened in our little technical word:

- Docker is everywhere
- Python 3.5 & asyncio, yay!

Python 3.5+ & asyncio just means that unlike my previous attempts at building
a tool that would generate as many concurrent requests as possible, I don't
have to worry anymore about key principle #2: we can do async code now in
vanilla Python, and I don't have to force ad-hoc async frameworks on people.

Docker means that for running a distributed test, a load test that runs
from one box can be embedded inside a Docker image, and then a tool can orchestrate
a distributed test that runs and manages Docker images in the cloud.

That's what we've built with Loads: "give me a Docker image of something that's
performing a small load test against a server, and I shall run it in hundreds
of box." This Docker-based design was a very elegant evolution of Loads
thanks to Ben Bangert who had that idea. Asking for people to embed their load
test inside a Docker image also means that they can use whatever tool they want
as long as it performs HTTP calls on the server to stress, and optionally send
some info via statsd.

But proposing a helpful,  standard tool to build the load test script that will be
embedded in Docker is still something we want to suggest. And frankly, 90% of
the load tests happen from a single box. Going nuclear is not happening that
often.

Introducing Molotov
===================

Molotov is a new tool I've been working on for the past few months - it's based
on asyncio, aiohttp and tries to be as light as possible.

Molotov scripts are coroutines to perform HTTP calls, and spawning
a lot of them in a few processes can generate a fair amount of load from a
single box.

Thanks to Richard, Chris, Matthew and others - my Mozilla QA teammates,
I had some great feedback to create the tool, and I think it's almost ready
for being used by more folks - it stills need to mature, and the docs
to improve but the design is settled, and it works well already.

I've pushed a release at PyPI and plan to push a first stable final release
this month once the test coverage is looking better & the docs are polished.

But I think it's ready for a bit of community feedback.
That's why I am blogging about it today -- if you want to try it, help building
it here are a few links:

- Docs: http://molotov.readthedocs.io
- code: https://github.com/loads/molotov/

Try it with the console mode (-c), try to see if it fits your brain and
let us know what you think.

