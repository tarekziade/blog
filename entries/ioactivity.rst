IOActivityMonitor in Gecko
##########################

:date: 2018-06-18
:tags: gecko, c++, mozilla
:category: mozilla
:author: Tarek Ziade

This is a first blog post of a series on Gecko, since I am
doing a lot of C++ work in Firefox these days. My current focus
is on adding tools in Firefox to try to detect what's going
on when something goes rogue in the browser and starts to drain
your battery life.

We have many ideas on how to do this at the developer/user level,
but in order to do it properly, we need to have accurate ways to
measure what's going on when the browser runs.

One thing is I/O activity.

For instance, a WebExtension worker that performs a lot of disk
writes is something we want to find out about, and we had nothing
to track all I/O activities in Firefox, without running the profiler.

When Firefox OS was developed, a small feature was added in the Gecko network
lib, called NetworkActivityMonitor.

That class was hooked as an NSPR layer to send notifications whenever something was
sent or received on a socket, and was used to blink the small icon phones
usually have to signal that something is being transferred.

After the Firefox OS project discontinued in Gecko, that class was left in the
Gecko tree but not used anymore, even though the option was still there.

Since I needed a way to track all I/O activity (sockets and files), I have
refactored that class into a generalised version that can be used to get
notified every time data is sent or received in any file or socket.

The way it works is pretty simple: when a file or a socket is created, a new
NSPR layer is added so every read or write is recorded and eventually dumped
into an XPCOM array that is notified via a timer.

This design makes it possible to track along sockets, any disk file that is
accessed by Firefox. For SQLite databases, since there's no way to
get all FD handles (theses are kept internal to the sqlite lib), the
IOActivityMonitor class provides manual methods to notify when
a read or a write happens. And our custom SQLite wrapper in Firefox
allowed me to add calls like I would do in NSPR.

It’s landed in Nightly :

- https://searchfox.org/mozilla-central/source/netwerk/base/IOActivityMonitor.h
- https://searchfox.org/mozilla-central/source/netwerk/base/IOActivityMonitor.cpp

And you can see how to use it in its Mochitest

- https://searchfox.org/mozilla-central/source/netwerk/test/browser/browser_test_io_activity.js

