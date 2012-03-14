PCard - Password Card
#####################

:date: 2012-03-14 12:00
:tags: python
:category: python
:author: Tarek Ziade

.. image:: http://dl.dropbox.com/u/8617023/pcard.png

If you go to http://passwordcard.org, there's a password card generator
you can use to create a 8 x 30 card filled with random characters, like
the one you see here.

The first line is composed of icons and the idea is that you memorize
one icon per service you use, then get a pass phrase by reading the
characters on that column, or going in diagonal.

Of course that does not work if you have hundreds of passwords. But
if you have a dozen very important passwords, the great thing about
this card is that it can be printed and fit in your wallet, so you
don't depend on any computer or untrusted Internet access when you
want a password.

I am not sure to understand why passwordcard.org has the **key**
used to generate the card printed on it, since it can be easy for
someone that gives a glimpse to memorize that short sequence (8 chars) 
and regenerate the card with it. He won't get your passwords but will be 
closer to them I guess. Of course when you use that card you are not 
supposed to put you finger on it and follow a line in public ;)

Anyways, I wanted to print out a card for myself, but wanted to
run it on my own computer for more safety, and remove the key on the
printed version -- I also wanted a command line tool to print out
the card in a shell.

And you know what happens when a Python programmer tries to change a 
Java program that's quite small. He ends up coding it back in Python
after staring at it a few minutes :o

Anyways, http://pcard.ziade.org is my own version, the code is
at https://github.com/tarekziade/pcard . There's a command line tool
and a bottle-based web generator.
