DNS-Based soft releases
#######################

:date: 2014-12-06 06:30
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade


`Firefox Hello <http://mzl.la/1p3JqIy>`_ is this cool WebRTC app we've landed in Firefox
to let you video chat with friends. You should try it, it's amazing.

My team was in charge of the server side of this project - which consists of a few
APIs that keep track of some session information like the list of the rooms
and such things.

The project was not hard to scale since the real work is done in the background
by Tokbox - who provide all the firewall traversal infrastructure. If you are curious
about the reasons we need all those server-side bits for a peer-2-peer technology,
this article is great to get the whole picture:
http://www.html5rocks.com/en/tutorials/webrtc/infrastructure/

One thing we wanted to avoid is a huge peak of load on our servers on Firefox release day.
While we've done a lot of load testing, there are so many interacting services that it's
quite hard to be 100% confident. Potentially going from 0 to millions of users
in a single day is... scary ? :)

So right now only 10% of our user base sees the Hello button. You can bypass
this by tweaking a few prefs, as explained in many places on the web.

This percent is going to be gradually increased so our whole user base can
use Hello.

How does it work ?
==================

When you start Firefox, a random number is generated. Then Firefox ask our service
for another number. If the generated number is inferior to the number sent by
the server, the Hello button is displayed. If is superior, the button is hidden.

Adam Roach proposed to set up an HTTP endpoint on our server to send back the number
and after a team meeting I suggested to use a DNS lookup instead.

The reason I wanted to use a DNS server was to rely on a system that's highly available
and freaking fast. On the server side all we had to do is to add a new DNS entry
and let Firefox do a DNS lookup - yeah you can do DNS lookups in Javascript as
long as you are within Gecko.

Due to a DNS limitation we had to move from a TXT field to an A field - which returns
an IP field. But converting IP to integer values is not a problem, so that worked out.

See https://wiki.mozilla.org/Loop/Load_Handling#Service_Soft_Start for all the details.


Generalizing the idea
=====================

I think using DNS as a distributed database for simple values like this is an awesome
idea. I am happy I thought of this one :)

Based on the same technique, you can also set up some A/B testing based on the DNS
server ability to send back a different value depending on things like a user location for
example.

For example, we could activate a feature in Firefox only for people in Connecticut, or
France or Europe.

We had a work week in Portland and we started to brainstorm on how such a service could
look like, and if it would be practical from a client-side point of view.

The general feedback I had so far on this is: Hell yeah we want this!

To be continued...

