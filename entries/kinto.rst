Kinto Work Week Recap
#####################

:date: 2016-02-22
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade


We just had a work-week in London on `Kinto <http://kinto.readthedocs.org/>`_ our
JSON storage project, and while heading back to France in the Eurostar, I figured
I'd give a summary of where we're at in the project and what's next.

.. image:: http://ziade.org/team-selfie.jpg

If you are not familiar with Kinto, it's an HTTP API that'll let you store
(not so) arbitrary JSON content. Data is organized in *collections*, which are
basically a list of timestamped records. As a client, you can query Kinto
to get records filtered by dates or other fields. Kinto also provides neat
features like a diff-based API to grab only the newest data, like how you
would with a git client.

**Kinto is the project designed to serve collections of data to Firefox in
real-time, such as configurations.**


*Kinto stores arbitrary JSON* because like some other storage
systems, you don't really have to describe the data you are pushing in it like
in a classical Database (you can if you want Kinto to control inputs).

*Kinto stores not so arbitrary JSON* because we're using some of the cool features
Postgres has to index in specific fields the JSON mappings - and we are
making the assumption that your data does follow a schema.

We were featured in Hackernews a couple of times already, and as you would
expect, it sparked a lot of comparisons with other systems that exist. Things
like "Are you the Parse killer?" "Why don't you use CouchDB already?" "You
don't have everything Firebase provides!"

But frankly, for a HN thread, most of the feedback was really positive and useful
for us. In particular it gave us a good hindsight on what things should be improved
in the documentation. For instance, making it crystal clear that we are not
building a product with a tight integration with the clients and the server API
and a **service** we'd provide (our comparison table right now is a mixed bag
of products and server-side frameworks, so that's confusing.)

We're building an HTTP API and we provide a JS client and working on some other
clients -- that's it for now.

That said, we're sure hoping products and services will be built by the community with this "toolkit"
at some point in the future.

But as far as 2016 is concerned, our main goal is to develop Kinto for our needs
in Firefox.


Kinto & Firefox
===============

For our daily work, the goal of Kinto is to be used in Firefox as the go-to
service to grab data continuously from our servers without having to wait for the
next release.

That's the `Go Faster <https://wiki.mozilla.org/Firefox/Go_Faster>`_ umbrella project.

We're going to use Kinto for:

- the **OneCRL** client in Firefox, that is syncing the list of certificate revocations in
  Firefox. The plan is to offer the security team the ability to deploy a change
  to all our users as fast as possible.

- the **AMO blocklist** client in Firefox, to get an up-to-date list of add-ons that should
  be blocked.

- **Fennec Assets** : static files needed by Fennec (Firefox for Android), like font files,
  hypenation dictionaries and so on. The goal here is to reduce the APK file size as much
  as possible and to limit the amount of data exchanged between mobile phones and
  our servers as well.

OneCRL
------

Mark is driving the development of the client on behalf of the Firefox Security
Team, and besides the obvious benefit of getting certificate revocations changes
on-the-fly as diffs, he started to work with my team, Julien and Franziskus
on a signing protocol that will allow the Kinto client to verify that the data
that was sent by the server was not tampered with.

That work started a few months ago and the work week was a perfect time
to give it a boost.

On the server-side, the signing is done with a micro-service Julien started,
called **autograph** that will let a Kinto administrator sign the data before
it's pushed into Kinto.

See https://github.com/mozilla-services/autograph

Kinto is interacting with the signer through a specialized plugin, that triggers
the signing whenever some data is changed into Kinto, and that makes
sure the data is published to clients once properly signed.

See https://github.com/mozilla-services/kinto-signer

The storage itself is pretty passive about this, as it just stores signed
hashes of collections and let any client get them back.

The Kinto client can grab that signature and ask Firefox to verify it before
applying data changes. The verification logic uses a custom PKI that Mark and
Franziskus and building on top of NSS in the client.

Obviously, we should do this for all the data Kinto ever sends to Firefox,
so going forward, all our Kinto deployments will integrate by default signatures
capabilities.

.. image:: http://ziade.org/kinto-ww.jpg


AMO Blocklist
-------------

The existing AMO blocklist client is already doing most of what we do in Kinto:
it performs daily download of an XML file and applies changes in Firefox.

So what are the benefits of moving to Kinto for this ?

The biggest one will be the signing of the data, since this is not something
the current client has. The second one will be to separate the feature from
the current AMO Django website. Instead of having a dashboard within the Django
admin to push data, the Addons administrator will be able to manage
the whole dataset in a dedicated web admin.

We've built an admin app for Kinto that will be used for this.

See https://github.com/Kinto/kinto-admin

It's a static React-based app, and we're providing now a **Kinto Distribution**
to let you have a full Kinto service that include among other things that
web admin hooked into an **/admin** endpoint.

See https://github.com/Kinto/kinto-dist/


The last benefit is mostly a side-benefit, but quite important. Right now,
the daily ping done by Firefox for the AMO blocklist is used for some metrics
work. This is not related to the blocklist feature itself, but happened for historical reasons.

The plan (ongoing dicussion though) is to separate the two features in
Firefox as they should, and make sure we have a dedicated ping mechanism for the metrics.

We'll end up with two clearly separated and identified features, that can
be maintained and evolve separately.


Fennec Assets
-------------

Sebastian, from the Fennec team, has been working on the Fennec client
to sync a list of assets into Kinto. The goal is to reduce the size of the Android
package, and download those extra files in the background.

We've built for this a plugin to Kinto, to extend our API so files
could be uploaded and downloaded.

Kinto stores files on disk or on Amazon S3 (or whatever backend you
write the class for) and their metadata in a Kinto collection.

See https://github.com/Kinto/kinto-attachment/


From a client point of view, what you get is a MANIFEST you can browse
and sync locally, of what files are available on the server.

Fennec is going to use this to let admins manage static file lists
that will be made available to the mobile browser, and downloaded
if they really need them.

Next Steps
==========

They are tons and tons of other stuff happening in Kinto right now,
but I wanted to give you an overview of the three major use cases
we currently have for it at Mozilla.

If all goes according to ours plans, these are the Firefox versions
they will land in:

- OneCRL: Firefox 47 - June 7th
- Fennec: Firefox 48 - July 18th
- AMO: Firefox 49 - August 8th

Good times!
