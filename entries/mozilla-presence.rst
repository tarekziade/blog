Presence on Firefox OS
######################

:date: 2013-12-13 09:42
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

.. note::

   The topic is still in flux, this blog post represents my own thoughts,
   not Mozilla's.


Since a couple of months, we've been thinking about *presence* in my team at Mozilla,
trying to think about what it means and if we need to build something in this area
for the future of the web.

The discussion was initiated with this simple question: if you are not currently
running social application *Foo* on your phone, how hard would it be for your friends
to know if you're available and to send you an instant notification to reach you ?


A few definitions
-----------------

Before going any further, we need to define a few words - because I realized
through all the dicussions I had that everyone has its own definitions of words
like **presence**.

The word **presence** as we use it is how `XMPP defines it <http://xmpp.org/rfcs/rfc6121.html#presence-fundamentals>`_.
To summarize, it's a flag that will let you know if someone is **online** or **offline**.
This flag is updated by the user itself and made available to others by different ways.

By **device** we define any piece of hardware that may update the user presence.
It's most of the time a phone, but by extension it can also be the desktop browser.
Maybe one day we will extend this to the whole operating system on desktop,
but right now it's easier to stay in our realm: the Firefox desktop browser
and the Firefox OS.

We also make the distinction between **app-level presence** and **device-level presence**.
The first one is basically the ability for an online app to keep track of who's *currently*
connected to its service. The latter, device-level presence, is the ability to
keep track of who's active on a device - even if that user is not active in
an application - which can even be turned off.

Being active on a device depends on the kind of device. For the desktop browser,
it could simply be the fact that the browser is running and the user has toggled
an 'online' button. For the phone, there are things like the `Idle API <https://developer.mozilla.org/en-US/docs/WebAPI/Idle>`_
that could be used to determine the status. But it's still quite fuzzy
what would be the best way to use this.

Last very important point: we're keeping the notion of **contacts** out of the
picture here because we've realized it's a bit of a dream to think that we could embed
people's contacts into our service and ask all of the social apps out there to
drop their own social graphs in favor of ours. That's another fight. :)

Anyways, I've investigated a bit on what was done on iOS and Android and found out
that they both more or less provide ways for apps to reach out their users even
when they don't use the app. I am not a mobile expert at all so if I miss something
there, let me know!


Presence on iOS
---------------

In iOS >= 7.x, applications that want to provide a presence feature
can keep a socket opened in the background even if the application
is not running any more in the foreground.

The feature is called `setKeepAliveTimeout <https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/Reference/Reference.html#//apple_ref/occ/instm/UIApplication/setKeepAliveTimeout:handler:>`_ and will give the app the ability to register
a handler that will be called periodically to check on the socket connection.

The handler has a limited time to do it (max 10 seconds) but
this is enough to handle presence for the user by interacting with a
server

The Apple `Push Notification Service <https://en.wikipedia.org/wiki/Apple_Push_Notification_Service>`_
is also often used by applications to keep a connection opened on a
server to receive push notifications. That's comparable to the
`Simple Push <https://wiki.mozilla.org/WebAPI/SimplePush>`_ service Mozilla has added
in Firefox OS.

Therefore, building an application with device-level presence on an iOS device
is doable but requires the publisher to maintain one or several connections per user
opened all the time - which is draining the battery. Apple is mitigating the problem
by enforcing that the service spends at most 10 seconds to call back its server,
but it seems that they are still keeping some resources *per application* in the
background.


Presence on Android
-------------------

Like iOS, Android provides features to run some services in the background,
see http://developer.android.com/guide/components/services.html

However, the service can be killed when the memory becomes low, and
if TCP/IP is used it can be hard to have a reliable service. That's also
what currently happens in Firefox OS, you can't bet that your application
will run forever in the background.

Google also provides a "Google Cloud Messaging" `(GCM) service <http://developer.android.com/google/gcm/index.html>`_.
That provides similar features to `Simple Push <https://wiki.mozilla.org/WebAPI/SimplePush>`_,
to push notifications to users.

There's also a new feature called `GCM Cloud Connection Server - (CCS) <http://developer.android.com/google/gcm/ccs.html>`_
that allows applications to communicate with the device via XMPP and with client side "Intent Services".
The app and the devices interact with CCS, which relays the messages back and forth.

There's a full example on their documentation of a Python server interacting with the GCM service
to interact with users.

What's interesting is that the device keeps a *single* connection to a Google
service, that relays calls from application servers. So instead of keeping
one connection in every application, the phone shares the same pipe.

It's still up to the app to leverage this service to keep track of connected
devices to get device-level presence, but the idea of keeping a single service
in the background that dispatches messages to apps and eventually wakes them up,
is very appealing to optimize the life of the battery.

Plus, XMPP is a widely known protocol. Offering  app developers this standard
to interact with the devices is pretty neat.


And Firefox OS ?
----------------

If you were to build a chat application today on Firefox OS, you would
need to keep your own connection open on your own server. Once your application
is sent in the background, you cannot really control what happens when
the system decides to shut it down to free some resources.

In other words, you're blacking out and the application service will
not really know what's your status on the device. It will soon be able to
send a notification via SimplePush to wake up the app - but there's still
this grey zone when the app is sent in the background.

The goal of the **Presence project** is to improve this and provide
a better solution for app developers.

At first, we thought about running our own presence service, be it based
on `ejabberd <http://www.ejabberd.im/>`_ or whatever XMPP server out there. Since
we're hackers, we quickly dived into all the challenges of scaling such a service for
Firefox OS users. Making a presence service scaling for millions of users is not
a small task - but that's really interesting.

The problem though, is the incentive for an app publisher to use our own
presence service. Why whould they do this ? They all already solved presence
in their applications, why would they use our own thing ? They would rather
want us to provide a better story for background applications - and keep their
client-side interacting with their own servers.

But we felt that we could provide a better service for our user experience,
something that is less battery draining, and that puts back the user in the
center of the picture.

Through the discussions, Ben Bangert came up with a nice proposal that partially
answered those questions: Mozilla can keep track of the users' device status
(online/offline/available) if they agree, and every user can authorize the
applications she uses to fetch these presence updates through the Mozilla
service - via a doorhanger page.

This indirection is a bit similar to Android's GCC architecture.

Like GCC, we'd be able to tweak the battery usage if we're in control of the background
service that keeps a connection opened to one of our servers. There are several
ways to optimize the battery usage for such a service - and we're exploring
them.

One extra benefit of having a Mozilla service keep track of the presence
flag is that users will be able to stay in control: they can revoke
an application's authorization to see their online presence at anytime.

There's also a lot of potential for tweaking how and who see this information.
For example, I can decide that *BeerChat*, my favorite chat app to talk about
beer, can see my presence only between 9pm and 11pm.

And of course, like Firefox Sync, the devices could point to a custom Presence
service that's not running on a Mozilla server.


What's next ?
-------------

The Presence project is just an experiment right now, but we're trying
to reach a point where we can have a solid proposal for Firefox OS.

As usual for any Mozilla project, everything is built in the open, and
we trying to have weekly meetings to talk about the project.

The wiki page of the project is here : https://wiki.mozilla.org/CloudServices/Presence

It's a big mess right now, but it should improve over time to something
more readable.

We're also trying to have a prototype that's up-to-date at
https://github.com/mozilla-services/presence and an end user application
demo that uses it, a Chat Room at: https://github.com/mozilla-services/presence-chatroom

There's a screencast at http://vimeo.com/80780042 where you can
see the whole flow of a user authorizing an application to see her presence
and another user reaching out the first user through a notification.

The desktop prototype is based on the excellent
`Social API <https://developer.mozilla.org/en-US/docs/Social_API>`_  feature,
and we're now building the Firefox OS prototype - to see how the whole
thing looks from a mobile perspective.

There's a mailing list, if you want to get involved: https://mail.mozilla.org/listinfo/wg-presence


