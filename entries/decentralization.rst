Data decentralization & Mozilla
###############################

:date: 2014-05-23 17:00
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

The fine folks at the Mozilla Paris office took the opportunity of our presence
(Alexis/Remy/myself) to organize a "Meet the Cloud Services French Team" event yesterday
night. Among all the discussions we had, one topic came back several times during the evening.

**How do we let people using our services, host their data anywhere they want**

I built the first Python version of the Firefox Sync server, so I had an answer
already - **you can tweak your browser configuration to point to your own
server**.

But self-hosting your Sync server requires quite some knowledge.
I provided a Makefile to build the server back in the days, but the amount
of work to set everything up was quite important.

And it got bigger with the new Sync version, because we've added dependencies
to other services for authentication purposes. Our overall architecture is
getting better but self-hosting Firefox Sync is getting harder.

Alexis is quite excited about trying to improve this situation, and suggested
building debian packages to make the process easy as in "apt-get install firefox-sync".

There were also discussion around `remoteStorage <http://remotestorage.io/>`_
and the more I look at it, the more I feel like a product like Firefox Sync
could rely on a remoteStorage server. That would make self-hosting straightforward.

The only thing that's unclear to me yet is if remoteStorage is heavily tied
to OAuth or if we can plug our own authentication process.
(e.g. Firefox Account tokens)

Another problem I see: it's easy to build client-side applications that directly
interacts with a remoteStorage, but sometimes you do have to provide server-side
APIs. In that case, I am wondering how convenient it would be for a web service
to interact with a 3rd party remoteStorage server on behalf of a user.
If both parts are different entities, it's a recipe for technical nightmares.

It feels in any case that those topics are going to be very important for
the web in the upcoming months, and that Mozilla needs to play an important role there.

Looking forward to see what we'll do in this area.

Tristan Nitot, who came by during the meeting, has sparkled this discussion and
is planning to organize recurrent meetings on the topic at the Paris community space
- helped by Claire and Axel. They are also zillions of other cool stuff happening
at the Paris space this summer. Like, several meetings per week. I'll try to update
this blog post whenever I find a good link to the events list.
