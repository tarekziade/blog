Title: Scaling the connectors framework
Date: 2023-06-20
Category: elastic, python

Looking back at the [ingestion framework](https://github.com/elastic/connectors-python/) 
we've built in my team in the past year, we've achieved a lot. As a tech lead,
I've focused on ensuring we deliver a service using resources efficiently and
not blowing out as we scale up the data we ingest. 

In theory, ingesting data from different sources into Elasticsearch is a simple
use case, and the Elasticsearch stack scales well and can handle a lot of data.
If you have a lot of network bandwidth and RAM, the `_bulk` API is a monster; it
can ingest much data quickly. 

In practice, a ton of issues happen as you scale up. The problem is not how
Elasticsearch handles data once it's there. It's how it accepts data. In
particular, if you can't use the data steam API.

The main ones for the Elasticsearch stack are:

- **Transport protocol** -- APIs are based on the HTTP protocol, which has its
  limits in orchestration and size. We have the `http.max_content_length` option
  to raise the size of one bulk request -- but raising it to 100MiB is non-sense.
  It will lead to problems quickly. HTTP is not meant for this, and that does not 
  scale well
- **Binary files** -- using the ingest attachment to deal with binary files
  like PDFs will blow your memory usage because Elasticsearch will start a tika
  process on the side but still load the whole memory file in its memory before
  it passes it along.

So, what now?

## Extraction on edge

For the binary files problem, I've started to look at how to improve the stack.
Jetty can implement multipart uploads and pass the data to Tika, which also
supports this. But the Elasticsearch layer in-between uses a file abstraction
that requires a whole rewrite to avoid holding the entire file in memory. If
you have some 200MiB PDFs --yes, some folks have PDFs like this-- you will get
into trouble pretty quickly unless your server or VM has a lot of RAM. And the
comparison hurts: a tool like pdfstream can stream-extract text from a very
large PDF without loading it entirely in memory -- and stay under 30MiB in RSS
usage.

In comparison, Tika will happily take 2GiB for the same job. PDFBox comes with
some sophisticated strategies to use more disk and less RAM, but it's still
hard to make it efficient. And if you take a step back, is it really
Elasticsearch job to do that extraction? It's a nice built-in feature, but
extracting binary content on edge earlier in the pipeline is a much better
idea.

This is why we've decided to process files [inside our connectors service](https://github.com/elastic/connectors-python/blob/main/connectors/utils.py#L699), 
so we can efficiently chunk-transfer data over the network and send to Elasticsearch
only the text we want to index and have dedicated resources outside that stack.


## Built-in safeguards

The transport protocol is a very large topic. Elasticsearch might, at some
point, [support gRPC](https://github.com/elastic/elasticsearch/issues/10981),
which would unlock what can be done to ingest data more efficiently. 

### Memory-aware queue

In the meantime, it's all about good queueing practices in our application and
do what we can with the available APIs. The connectors service is an I/O-bound
service that sits in-between Elasticsearch and the source of data. You can see
it as one queue of documents produced by a task that calls a third-party and
consumed by a task that sends them to Elasticsearch via the bulk query.

Since we've built a framework where anyone can create their own connector,
creating chaos in the service is pretty easy. For instance, if your connector
pulls documents way faster than they are sent to Elasticsearch, you will pile
up documents in the queue and blow up your RAM and overload the Elasticsearch
cluster.

Adding backpressure in the queue at the framework level is easy enough -- this
is what every engineer that deals with streams have to do at one point in their
projects. I've built a [memory-aware asyncio Queue](https://github.com/elastic/connectors-python/blob/main/connectors/utils.py#L200) 
for this since this is not something Python has in the standard lib. 

### Continuous performance testing

But since we're using an event loop, it's also super easy for someone to
inadvertently create a connector that blocks the loop and degrades the service.
A connector can also eat up all the RAM or CPU, there's nothing that prevents a
developer from doing it.

This is why I've created [perf8](https://github.com/elastic/perf8) which we use
in our nighty tests to verify that a connector does not block the event loop,
and behaves correctly in how it uses resources. It produces single-page html 
reports (so it can be an artifact in the CI)

You can see it running here for all our connectors : 

[https://buildkite.com/elastic/connectors-python-nightly](https://buildkite.com/elastic/connectors-python-nightly)

Click on any connector there, and click on `index.html`. You will get a static
report with a bunch of cool graphs. Perf8 can run with limits and complain if
you go over them. For instance, raise an error in the CI if your connector goes
over 250MiB of RSS when it ingests 10GiB of data, etc.

Here's one report from today on MySQL : [Flake8 report](https://ziade.org/flake8.html)

### What's next?

Our framework is providing rails to implement any new connector, you only need to
implement a class with a few functions, the main one being an iterator on 
documents you grab from the backend. [Example](https://github.com/elastic/connectors-python/blob/main/connectors/sources/directory.py)

This mechanism is used in our simple sync mechanism, that will run the service
on a regular basis against a source and make sure Elasticsearch is up-to-date.

But some sources have sophisticated APIs (like Mongo's Changes API) that allows
to get notified on changes. Same goes for some SQL databases that support
a binlog. This offers real-time updates.

Changing the service to sync on events is the next logical step, and has to be done
in a way that still offers classical syncs, because some backends will never
provide notifications.

There are also a lot of improvments we can do. The project is mature enough now 
to understand what needs to stay in RAM and what could move to disk, to reduce
our footprint. The memory-aware queue can now be converted into a 
[disk queue](https://github.com/elastic/connectors-python/issues/1031)

