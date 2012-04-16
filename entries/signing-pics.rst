Signpic - Signing Pictures with PIL
###################################

:date: 2012-04-14 23:05
:tags: python
:category: python
:author: Tarek Ziade

.. image:: http://awesomeness.openphoto.me/custom/201204/351aa7-IMGP1722_wm_870x550.jpg
   :width: 435
   :height: 275


I am starting to really like taking pictures, thanks to the new Pentax K5 I bought.

My photo processing looks roughly like this:

- I shoot many pics and delete 90% of them
- I edit them in Adobe Lightroom 4
- I push them on my openphoto.me account
- they are stored in my Dropbox account

What I wanted to add is a way to sign my pictures by adding a small text on the bottom
right corner. Not because I want to look like some kind of pro photographer -- I am not ;)

But signing is useful when you send pics around to your family & friends: I want them
to know that they are more pics at http://tarek.openphoto.me.

I found a cool little script at http://www.turboradness.com/watermark-your-images-with-python
that provides this feature with PIL and will let you sign pictures with a signature
image.

**signpic** is a small script inspired from that blog post that adds:

- a console script you can use to sign your pics or directories of pics
  using a provided signature image, or the signature image located at
  ~/.signature.jpg

- a **--powerhose** mode that will run a Powerhose cluster to perform the
  operations. This is very useful to speed up the process when you need to sign a
  bunch of pictures - a single signing takes a few seconds....
  Powerhose is a Request-Reply Broker pattern in ZMQ, and speed up the signing
  task.

If you want to give it a shot::

    $ pip install signpic
    $ bin/signpic ~/Desktop/pics --phose
    Using signature file '/Users/tarek/.signature.jpg'
    Looking for files in '/Users/tarek/Desktop/pics'
    +++++++++++++.............Done.


