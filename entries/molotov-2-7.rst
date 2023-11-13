gRPC support for Motolov
########################

:date: 2023-11-13
:tags: python
:author: Tarek Ziade

I am happy to share that Molotov is getting gRPC support.

Molotov is a tool for testing HTTP services, see https://molotov.readthedocs.io/en/stable/

I've cut a few releases in the past few years that were mostly bug fixes and
dependencies upgrades -- thanks to contributors.
The tool has been stable for years and I did not
expect any new features.

But gRPC support is there!

Background
----------

One feature I often use is `auto sizing <https://molotov.readthedocs.io/en/stable/tutorial/#autosizing>`_.
Molotov ramps up the load
gradually and stops the test when the errors ratio is past a threshold.

That is quite useful to determine how much your service can handle and
what resource gets exhausted first. Typically memory or CPU.

We've used it recently against the `Nuclia Database <https://github.com/nuclia/nucliadb>`_
to track its performances and bottlenecks -- but there was one tool
missing in our armada: the ability to run the same kind of tests
against gRPC endpoints.

Molotov is an HTTP load tester and each scenario gets an HTTP session.
So it was a bit hackish to use it for some of the gRPC endpoints NucliaDB uses.

We had to create ad-hoc gRPC scripts but then lose the ability to run
automatic ramp-up tests.


Introducing gRPC support
------------------------

But adding gRPC support to Molotov was quite easy. When you create a
gRPC channel using `grpc.aio.insecure_channel`, you get back an object that
acts like a session and can be used a bit like an HTTP client session.

To make its integration as simple as possible, I've used a similar trick than
Pytest does for its fixtures: declare the kind of session the test needs
via the test arguments.

In practice, here's a full example:

.. code-block:: python

  from molotov import scenario
  from molotov.tests._grpc import helloworld_pb2, helloworld_pb2_grpc

  @scenario(weight=40)
  async def grpc_scenario(
      session,
      session_factory="grpc",
      grpc_url="ipv4:///127.0.0.1:50051"
      ):

      stub = helloworld_pb2_grpc.GreeterStub(session)
      response = await stub.SayHello(helloworld_pb2.HelloRequest(name="Alice"))
      assert response.message == "Hello, Alice!", response.message


The scenario gets its usual `session` argument, and a `session_factory`
argument that can be either `grpc` or `http` (the default). Molotov will read
the signature and pick the right session factory to create it. For `grpc` the
`grpc_url` argument is the URL of the gRPC server.


I've implemented a new `session_factory` API to make this pluggable. The
full implementation for the `grpc` factory is:


.. code-block:: python

  from grpc import aio
  from molotov.api import session_factory

  @session_factory("grpc")
  def grpc_session(loop, console, verbose, statsd, trace_config, **kw):
      url = kw["grpc_url"]
      channel = aio.insecure_channel(url)
      channel._trace_configs = [trace_config]
      return channel

Which means you can implement your own factory if you want. The returned
object will be passed to the test as `session` and will be created once
for each Molotov worker.

The only requirement is that this object implements a `close` async function
that will be called when the worker has finished its work.

I hope that new feature will be useful out there.

You can try it out by installing the current `main` branch:


.. code-block:: python

  pip install git+https://github.com/tarekziade/molotov



Happy hacking!

