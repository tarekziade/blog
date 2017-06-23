Advanced Molotov example
########################

:date: 2017-06-23
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

Last week, I blogged about how to drive Firefox from a Molotov script using
`Arsenic <https://github.com/HDE/arsenic>`_.

It is pretty straightforward if you are doing some isolated interactions
with Firefox and if each worker in Molotov lives its own life.

However, if you need to have several "users" (==workers in Molotov) running
in a coordinated way on the same web page, it gets a little bit tricky.

Each worker is its coroutine and triggers the execution of one
scenario by calling the coroutine that was decorated with @scenario.

Let's consider this simple use case: we want to run five workers in
parallel that all visit the same etherpad lite page with their
own Firefox instance through Arsenic.

One of them is adding some content in the pad and all the
others are waiting on the page to check that it is updated
with that content.

So we want four workers to wait on a condition (=pad written) before
they make sure and check that they can see it.

Moreover, since Molotov can call a scenario many times in a row, we
need to make sure that everything was done in the previous round
before changing the pad content again. That is, four workers did check
the content of the pad.

To do all that synchronization, Python's asyncio offers
primitives that are similar to the one you would
use with threads. **asyncio.Event** can be used for instance
to have readers waiting for the writer and vice-versa.

In the example below, a class wraps two Events and exposes
simple methods to do the syncing by making sure readers
and writer are waiting for each other::


    class Notifier(object):
        def __init__(self, readers=5):
            self._current = 1
            self._until = readers
            self._readers = asyncio.Event()
            self._writer = asyncio.Event()

        def _is_set(self):
            return self._current == self._until

        async def wait_for_writer(self):
            await self._writer.wait()

        async def one_read(self):
            if self._is_set():
                return
            self._current += 1
            if self._current == self._until:
                self._readers.set()

        def written(self):
            self._writer.set()

        async def wait_for_readers(self):
            await self._readers.wait()


Using this class, the writer can call **written()** once it has
filled the pad and the readers can wait for that event by calling
**wait_for_writer()** which blocks until the write event is set.

**one_read()** is then called for each read. This second event is
used by the next writer to make sure it can change the pad content
after every reader did read it.

So how do we use this class in a Molotov test? There are
several options and the simplest one is to create
one Notifier instance per run and set it in a variable::


    @molotov.scenario(1)
    async def example(session):
        get_var = molotov.get_var
        notifier = get_var('notifier' + str(session.step),
                           factory=Notifier)
        wid = session.worker_id

        if wid != 4:
            # I am NOT worker 4! I read the pad

            # wait for worker #4 to edit the pad
            await notifier.wait_for_writer()

            # <.. pad reading here...>

            # notify that we've read it
            await notifier.one_read()
        else:
            # I am worker 4! I write in the pad
            if session.step > 1:
                # waiting for the previous readers to have finished
                # before we start a new round
                previous_notifier = get_var('notifier' + str(session.step))
                await previous_notifier.wait_for_readers()

            # <... writes in the pad...>

            # informs that the write task was done
            notifier.written()

A lot is going on in this scenario. Let's look at each part in detail.
First of all, the notifier is created as a var via set_var().
Its name contains the **session step**.

The **step** value is incremented by Molotov every time a worker is
running a scenario, and we can use that value to create one distinct
Notifier instance per run. It starts at 1.

Next, the **session.worker_id** value gives each distinct worker
a unique id. If you run molotov with 5 workers, you will get values
from 0 to 4.

We are making the last worker (worker id== 4) the one that will be
in charge of writing in the pad.

For the other workers (=readers), they just use wait_for_writer()
to sit and wait for worker 4 to write the pad. worker 4
notifies them with a call to written().

The last part of the script allows Molotov to run the script
several times in a row using the same workers. When the writer
starts its work, if the step value is superior to one, it means
that we have already run the test at least one time.

The writer, in that case, gets back the Notifier from the **previous**
run and verifies that all the readers did their job before changing
the pad.

All of this syncing work sound complicated, but once you understand
the pattern, it let you run advanced scenario in Molotov where
several concurrent "users" need to collaborate.

You can find the full script at https://github.com/tarekziade/molosonic/blob/master/loadtest.py



