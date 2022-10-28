Title: Elasticsearch - keep your streams under control
Date: 2022/10/27
Tags: python, elastic
Category: elastic
Author: Tarek Ziade


Ingesting a stream of data from a backend into Elasticsearch is pretty simple -- the service has this really
nice [bulk api](https://www.elastic.co/guide/en/elasticsearch/reference/8.4/docs-bulk.html) where you
can send in the same request for a bunch of indexing operations.

I've built a straightforward asynchronous consumer-producer system on top of our excellent [Python client](https://elasticsearch-py.readthedocs.io/).
The producer is an iterator that returns documents to send to Elastic, and the consumer is a function that
iterates on those documents and sends them in batches using the `bulk` API.

If your Elasticsearch service is nearby and you have a lot of network
bandwidth, you can send colossal bulk requests -- sending documents in batches of
500 is pretty fast.

Of course, that's only possible if you have a lot of resources available, and
that includes the RAM, where you collect the data you want to send over by
batches.

As soon as your network gets more limited (smaller bandwidth, longer
round-trips), big requests won't work anymore. Your network will get saturated
and you will start to see time-outs. Sending requests of 50MB over the network
don't make much sense in that context.

You can reduce the size of the batches, but the size of the document also matters
and they may vary from one document to the other.

And in async Python it's pretty easy to pile up data in memory when the producer
is pumping data faster than what the consumer can grab to send to Elasticsearch.

I was trying to find the most elegant way to deal with this in various network conditions,
with a few goals in mind.

- making it as fast as possible
- have a configurable maximum memory Resident Set Size for the app
- have a configurable maximum bulk request size
- a way to throttle calls done in the producer when limits are reached

The program initially used an `asyncio.Queue` but that queue is not aware of its
size in memory -- it just allows you to define a maximum number of items before
`put` blocks on the next insertion.

But that class is easy to override!


You can use [Pympler](https://pympler.readthedocs.io) to get the real memory size of a
Python object -- this is different from `sys.getsizeof` because Pympler recursively look
at all objects attached to the object you measure. For simple data structures like
lists or dicts, it's pretty accurate -- and our docs are simple mappings:

```python
from pympler import asizeof

def get_size(ob):
    """Returns size in MiB"""
    return round(asizeof.asizeof(ob) / (1024 * 1024), 2)
```

Using that function, I've created a `MemQueue` class that will block any
attempt to put new data into the queue if it reaches a specific size in memory:

```python
import asyncio


class MemQueue(asyncio.Queue):
    def __init__(self, maxsize=0, maxmemsize=0):
        super().__init__(maxsize)
        self.maxmemsize = maxmemsize
        self._current_memsize = 0

    def _get(self):
        item = self._queue.popleft()
        self._current_memsize -= get_size(item)
        return item

    def _put(self, item):
        self._queue.append(item)
        self._current_memsize += get_size(item)

    def mem_full(self):
        if self.maxmemsize == 0:
            return False
        return self.qmemsize() >= self.maxmemsize

    def qmemsize(self):
        return self._current_memsize

    async def put(self, item):
        while self.mem_full():
            await asyncio.sleep(1.0)
        return await super().put(item)
```


That's it for the queue! Producers can use it to put new documents for the bulk consumer.

A simplified version of the producer:

```python
MAX_QUEUE_SIZE = 100

queue = MemQueue(maxmemsize=MAX_QUEUE_SIZE)     # the queue can hold 100MB

async def producer(queue):
    for doc in some_source:
        queue.put(make_it_an_operation(doc))
    queue.put('END')
```

`put` will block if `queue` has reached 100MB. The function will get unblocked 
once the consumer grabbed enough data so the queue is down to 100MB.

A simplified version of the consumer:

```python

MAX_OPS = 500   # 500 docs per call at the max
MAX_REQUEST_SIZE = 5   # 5MB

async def consumer(queue):
    batch = []
    self.bulk_time = 0
    self.bulking = True
    while True:
        operation = await queue.get()
        if operation == "END":
            break
        batch.extend(operation)
        if len(batch) >= MAX_OPS or get_size(batch) > MAX_REQUEST_SIZE:
            await batch_bulk(batch)
            batch.clear()

        await asyncio.sleep(0)

    if len(batch) > 0:
        await batch_bulk(batch)
```

The consumer will pile up to 500 operations and sends them to Elasticsearch.
If `batch` reaches 5MB before it has a chance to aggregate 500 operations, it
will stop there and send it out.

That's it! with these memory guards, I know that the app will not exceed
~250M in memory and will emit bulk requests of 5MB maximum.
Python 3.10 is doing a pretty decent job at garbage collecting data that streams
through.

`MAX_QUEUE_SIZE`, `MAX_OPS` and `MAX_REQUEST_SIZE` can be used to make sure the
application stays under control whatever data flows through it.
