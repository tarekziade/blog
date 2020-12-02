Salvo - my Apache Bench replacer
################################

:date: 2020-12-02
:tags: python
:author: Tarek Ziade

When I wrote `Boom <https://github.com/tarekziade/boom>`_ a few years ago, to
replace Apache Bench (ab) in my work, Python was still maturing its async
mechanisms, and `gevent <http://www.gevent.org/>`_ was a popular way to build
an asynchronous HTTP client.

Fast forward 2020, asynchronous programming is now quite simple in Python and can
be done natively, using `async` and `await` directives.
I wrote `Molotov <https://molotov.readthedocs.io/en/stable/>`_, a load testing
framework based on Python's asyncio and on the `aiohttp <https://aiohttp.readthedocs.io/>`_
client, and always wanted to rewrite Boom using Molotov, since it's just a very simple
Molotov load test scenario: hitting a single HTTP(s) endpoint.

Instead of refactoring Boom, which is Python 2 compatible, I started a new tool called
Salvo, which is Python 3 only. Salvo takes back Boom's command line interface and
runs a Molotov script under the hood, and prints results the same way Boom is doing.

It's using a single process and runs as many concurrent "workers" as you want,
which is enough to smoke test one endpoint. The philosophy is that anything more
complex should be done using a full Molotov script.

To use Salvo, install it using `pip` and then send some load to an endpoint.
Running with no option will perform a single hit ::

    $ pip install salvo
    $ salvo https://example.com
    -------- Server info --------

    Server Software: ECS (bsa/EB12)

    -------- Running 1 queries - concurrency 1 --------

    [=================================================================>] 100%

    -------- Results --------

    Successful calls    		1
    Total time          		0.4430 s
    Average             		0.4430 s
    Fastest             		0.4430 s
    Slowest             		0.4430 s
    Amplitude           		0.0000 s
    Standard deviation  		0.000000
    Requests Per Second 		2.26
    Requests Per Minute 		135.44

    -------- Status codes --------
    Code 200          		1 times.

    Want to build a more powerful load test ? Try Molotov !
    Bye!


You can then try to run more load. In the example below, we run 100 requests, across
10 concurrent workers::

    $ salvo https://example.com -n 10 -c 10
    -------- Server info --------

    Server Software: ECS (bsa/EB12)

    -------- Running 10 queries - concurrency 10 --------

    [=================================================================>] 100%

    -------- Results --------

    Successful calls    		100
    Total time          		14.7801 s
    Average             		0.1478 s
    Fastest             		0.1049 s
    Slowest             		0.5314 s
    Amplitude           		0.4265 s
    Standard deviation  		0.115398
    Requests Per Second 		6.77
    Requests Per Minute 		405.95

    -------- Status codes --------
    Code 200          		100 times.

    Want to build a more powerful load test ? Try Molotov !
    Bye!

You can also use `--duration` to run the test for a given number of seconds, and
use `--json` if you want to get the results in a JSON output.

In the example below, we also use `--quiet` to get only the JSON output, of a 10 seconds
run using 10 workers::

    $ salvo https://example.com -d 10 -c 10 --json --quiet
    {"count": 774, "total_time": 102.28760695457458, "rps": 7.566899090167683,
     "avg": 0.13215453094906277, "min": 0.10414314270019531,
     "max": 0.8381381034851074, "amp": 0.7339949607849121,
     "stdev": 0.09841954760413639,
     "rpm": 454.013945410061, "server": {"software": "ECS (bsa/EB18)"}}

Salvo has a few basic customization features (see `--help`) but I won't extend them,
the plan is to keep it as simple as possible and invite developers that need more
features to use Molotov.

I hope this tool will be useful. The repo is here: https://github.com/tarekziade/salvo

Happy breaking!
