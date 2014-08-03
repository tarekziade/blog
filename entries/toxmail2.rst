ToxMail Experiment Cont'd
#########################

:date: 2014-08-03 21:33
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

I started the other day experimenting with Tox to build a secure
e-mailing system. You can `read my last post here <http://blog.ziade.org/2014/07/26/toxmail-experiment/>`_.

To summarize what Toxmail does:

- connects to the `Tox network <https://tox.im/>`_
- runs a local SMTP and a local POP3 servers
- converts any e-mail sent to the local SMTP into a Tox message

The prototype is looking pretty good now with a web dashboard that lists all
your contacts, uses DNS lookups to find users Tox Ids,
and has a experimental relay feature I am making progress on.

See https://github.com/tarekziade/toxmail

DNS Lookups
===========

As described `here <https://github.com/Tox/Tox-STS/blob/master/STS.md#dns-discovery>`_,
Tox proposes a protocol where you can query a DNS server to find out the Tox ID
of a user as long they have registered themselves to that server.

There are two Tox DNS servers I know about: http://toxme.se and http://utox.org

If you register a nickname on one of those servers, they will add a TXT record
in their DNS database. For example, I have registered **tarek** at **toxme.se**
and people can get my Tox Id querying this DNS::

    $ nslookup -q=txt tarek._tox.toxme.se.
    Server:     212.27.40.241
    Address:    212.27.40.241#53

    Non-authoritative answer:
    tarek._tox.toxme.se text = "v=tox1\;id=545325E0B0B85B29C26BF0B6448CE12DFE0CD8D432D48D20362878C63BA4A734018C37107090\;sign=u+u+sQ516e9VKJRMiubQiRrWiVN0Nt98dSbUtsHBEwYiaQHk2T8zAq4hGprMl9lc89VXRnI+AukoqpC7vJoHDXRhcmVrVFMl4LC4WynCa/C2RIzhLf4M2NQy1I0gNih4xjukpzRwkA=="


Like other Tox clients, the Toxmail server uses this feature to convert on the
fly a recipient e-mail into a corresponding Tox ID. So if I
write an e-mail to **tarek@toxme.se**, Toxmail knows where to send the message.

That breaks anonymity of course, if the Tox Ids are published on a public server,
but that's another issue.


Offline mode
============

The biggest issue of the Toxmail project is the requirement of having both
ends connected to the network when a mail is sent.

I have added a retry loop when the recipient is offline, but the mail will
eventually make it *only* when the two sides are connected at the same time.

This is a bit of a problem when you are building an asynchronous
messaging system. We started to discuss some
`possible solutions on the tracker <https://github.com/tarekziade/toxmail/issues/1>`_
and the idea came up to have a **Supernode** that would relay e-mails
to a recipient when its back online.

In order to do it securely, the mail is encrypted using the Tox public/private
keys so the supernode don't get the message in clear text. It uses the same
**crypto_box** APIs than Tox itself, and that was really easy to add
thanks to the nice PyNaCL binding, see https://github.com/tarekziade/toxmail/blob/master/toxmail/crypto.py

However, using supernodes is adding centralization to the whole system,
and that's less appealing than a full decentralized system.

Another option is to use all your contacts as relays. A e-mail propagated
to all your contacts has probably good chances to eventually make it
to its destination.

Based on this, I have added a **relay** feature in Toxmail that will send
around the mail and ask people to relay it.

This adds another issue though: for two nodes to exchange data, they
have to be friends on Tox. So if you ask Bob to relay a message to Sarah,
Bob needs to be friend with Sarah. And maybe Bob does not want you to know
that he's friend with Sarah.

Ideally everyone should be able to relay e-mails anonymously - like other
existing systems where data is just stored around for the recipient to come
pick it.

I am not sure yet how to solve this issue, and maybe Tox is not suited to
my e-mail use case.

Maybe I am just trying to reinvent `BitMessage <https://bitmessage.org/wiki/Main_Page>`_. Still digging :)




