Circus Sprint Report
####################

:date: 2012-03-14 15:28
:tags: python
:category: python
:author: Tarek Ziade

.. image:: http://dl.dropbox.com/u/8617023/circus.png

Benoit and I organized a sprint at Pycon for Circus, the process watcher
we're building (see http://ziade.org/2012/02/24/circus-a-process-controller). 

We had quite some interest on the topic, and a few 
contributors. I was myself naviguating between the Circus sprint and the
Packaging one. On Circus we were most of the time discussing features
and adding test coverage and documentation.

Unfortunately, a few bugs prevented us from releasing the first public 
version, but that should be out there in a few days.

You can read the doc while we're building it here: 
http://circus.readthedocs.org/en/latest/index.html

And have a look at the architecture here: 
http://circus.readthedocs.org/en/latest/architecture

Stuff we did during the sprint:

- more test coverage
- hooked the project in Travis - http://travis-ci.org/#!/mozilla-services/circus
- more doc
- flapping detection
- added pub/sub channel to allow any client to watch over
  what's going on -- any event, like a process that restarts,
  is published in the pub/sub channel
- started an pub/sub client example: a web monitoring 
  page based on websockets, using
  Flask -- that app will be a subscriber of Circus. (not in the repo yet)

Stuff we need to finish / Features we're thinking about:

- factor out the flapping detector as a pub/sub plugin.
- stream the process stdout/stderr so clients can subscribe to them
- refactor how the commands are plugged in Circus -- mainly to 
  be able to produce a doc like this one : http://www.redis.io/commands
- add an encryption layer for the zmq channels
- discuss with Chris McDonough wrt Supervisord common bits.


And welcome to our new contributors, Neil Chintomby and Ori Livneh !

If you want to have a look, for us at https://github.com/mozilla-services/circus
