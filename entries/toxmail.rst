ToxMail experiment
##################

:date: 2014-07-26 13:22
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade


I am still looking for a good e-mail replacement that is more respectful of my privacy.

This will never happen with the existing e-mail system due to the way it works: when you
send an e-mail to someone, even if you encrypt the body of your e-mail, the metadata
will transit from server to server in clear, and the final destination will store it.

Every PGP UX I have tried is terrible anyways. It's just too painful to get things
right for someone that has no knowledge (and no desire to have some) of how things work.

What I aiming for now is a separate system to send and receive mails with my close
friends and my family. Something that my mother can use like regular e-mails, without
any extra work.

I guess some kind of "Darknet for E-mails" where they are no intermediate servers between
my mailbox and my mom's mailbox, and no way for a eavesdropper to get the content.


Ideally:

- end-to-end encryption
- direct network link between my mom's mail server and me
- based on existing protocols (SMTP/IMAP/POP3) so my mom can use Thunderbird or
  I can set her up a Zimbra server.


Project Tox
===========

The `Tox Project <https://tox.im/>`_ is a project that aims to replace Skype with
a more secured instant messaging system. You can send text, voice and even video
messages to your friends.

It's based on `NaCL <http://nacl.cr.yp.to/>`_ for the crypto bits and in particular
the `crypto_box API <http://nacl.cr.yp.to/box.html>`_ which provides high-level
functions to generate public/private key pairs and encrypt/decrypt messages with it.

The other main feature of Tox is its `Distributed Hash Table <http://en.wikipedia.org/wiki/Distributed_hash_table>`_
that contains the list of nodes that are connected to the network with their **Tox Id**.

When you run a Tox-based application, you become part of the Tox network by registering
to a few known public nodes.

To send a message to someone, you have to know their **Tox Id** and send a crypted
message using the crypto_box api and the keypair magic.

Tox was created as an instant messaging system, so it has features to add/remove/invite
friends, create groups etc. but its core capability is to let you reach out another
node given its id, and communicate with it. And that can be any kind of communication.

So e-mails could transit through Tox nodes.


Toxmail experiment
==================

Toxmail is my little experiment to build a secure e-mail system on the top of Tox.

It's a daemon that registers to the Tox network and runs an SMTP service that converts
outgoing e-mails to text messages that are sent through Tox. It also converts
incoming text messages back into e-mails and stores them in a local Maildir.

Toxmail also runs a simple POP3 server, so it's actually a full stack that can
be used through an e-mail client like Thunderbird.

You can just create a new account in Thunderbird, point it to the Toxmail SMPT and
POP3 local services, and use it like another e-mail account.

When you want to send someone an e-mail, you have to know their Tox Id, and use
**TOXID@tox** as the recipient.

For example::

    7F9C31FE850E97CEFD4C4591DF93FC757C7C12549DDD55F8EEAECC34FE76C029@tox


When the SMTP daemon sees this, it tries to send the e-mail to that Tox-ID.
What I am planning to do is to have an automatic conversion of regular e-mails
using a lookup table the user can maintain. A list of contacts where you provide
for each entry an e-mail and a tox id.

End-to-end encryption, no intermediates between the user and the recipient. Ya!


Caveats & Limitations
=====================

For ToxMail to work, it needs to be registered to the Tox network all the time.

This limitation can be partially solved by adding in the SMTP daemon a retry feature:
if the recipient's node is offline, the mail is stored and it tries to send it later.

But for the e-mail to go through, the two nodes have to be online at the same time at
some point.

Maybe a good way to solve this would be to have Toxmail run into a Raspberry-PI plugged
into the home internet box. That'd make sense actually: run your own little mail server
for all your family/friends conversations.

One major problem though is what to do with e-mails that are to be sent to recipients that
are part of your toxmail contact list, but also to recipients that are not using Toxmail.
I guess the best thing to do is to fallback to the regular routing in that case, and let
the user know.

Anyways, lots of fun playing with this on my spare time.

The prototype is being built here, using Python and the PyTox binding:

https://github.com/tarekziade/toxmail

It has reached a state where you can actually send and receive e-mails :)

I'd love to have feedback on this little project.

