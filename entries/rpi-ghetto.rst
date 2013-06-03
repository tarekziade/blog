Raspberry-Pi Ghetto Blaster Suitcase
####################################

:date: 2013-06-03 22:00
:tags: python
:category: python
:author: Tarek Ziadé


tldr; I built a Ghetto blaster with a suit case. Click on the image
below to see me dancing with it.

.. image:: https://lh4.googleusercontent.com/-WsaYOOate7w/UaoqKI6guzI/AAAAAAAAD_o/iRZhFzaSlrw/w912-h604-no/balster+%25281+of+2%2529.jpg
   :target: https://plus.google.com/106436370949746015255/posts/6ZwW6wt6Rx9

After my `Raspberry Juke box <http://raspberry.io/projects/view/a-rapsberry-pi-juke-box-1/>`_
project was done, I wanted to take it to the next level and build a standalone
amplified speaker I could drive from the home wifi instead of putting $300 in a
Bose Soundlink or a Jawbone JAMBOX and get limited features compared with what
I can build with a Raspberry.

So I build a Ghetto blaster with a suit case.

Ghetto blasters are one of the coolest thing ever. It's the perfect device
to enjoy music outside - and it's so 80s.. :)

I found an old suit case in my basement that used to contain tools.
This kind of suit case is made with cardboard and covered with aluminum.
Once emptied, it's perfect as a speaker. The cardboard and aluminum
vibrate and produce excellent basses. This suitcase costs around 10 euros.

I also found 2 old car speakers in my basement, that are pretty good.
25W & 3 channels each. I suspect these would cost arount 20 euros these days.

Once the holes were made and the speakers screwed on the suitcase panel,
I bought `a small 25W amplifier on Amazon <http://www.amazon.fr/Lepai-Tripath-class-T-Amplificateur-acoustique/dp/B009US84UQ/>`_
for 27 euros. This thing is really amazing. It's small enough to fit in
the suitcase and has a small equalizer that is really handy.
I unscrewed the front panel and placed it outside on the suitcase,
and screwed back through the suitcase to hold the amplifier inside.

I started to play with my suitcase and got amazed by the sound,
it really kicks and has very good basses.

The next steps were to plug a Raspberry-Pi with an USB sound
card and a wifi dongle and run `Mopidy <http://docs.mopidy.com/en/latest/>`_
on it.  That allowed me to stream music from my Spotify account.

When the Raspberry starts, it starts Mopidy, connects to the home
Wifi and speaks out using *espeak*:

    "I am ready to play music, my IP address is 192.168.0.16"

From there I can start a MPD client like MPDroid and connect
to that IP and queue some music.


Powering
--------

Of course the big challenge was to power up the amplifier & the Raspberry
so I could actually walk around freely. I did not want to
use lead acid, so I bought this `12v lipo battery <http://www.aliexpress.com/item/1Pcs-12V-Rechargeable-Li-po-Battery-for-CCTV-Cam-6800mAh-Free-shipping-Drop-ship-3452-01/472817705.html>`_
for $20.  It comes pre-charged and has a small on/off button.

Now this battery delivers 12v but I still need 5v for my Raspberry.
You can use a voltage regulator for this, like the
`LM1117 <http://hackspark.fr/fr/ld1117-lm1117-5v-ldo-voltage-regulator-1-3a-to220.html>`_.

I built a small board you can see in the video. It
takes the 12v from the battery and outputs 5v for the Raspberry.
It has the LM1117 with a sink, and a few capacitors for
stability.

It's exactly the same design as this
one https://www.youtube.com/watch?v=CKS6zHo5T9k except
they use a L7805 in there - which has a different wiring.

That's it - my 12v LiPO powers up the amplifier & the Raspberry.
It's been playing for hours and the battery still has some juice.


Issues & next steps
-------------------

The wifi dongle loses the signal if I close the suitcase
and I am too far from the wifi router. I need to set up an external
antenna.

I am also going to add a battery level indicator, using
`this schematic <http://www.electroschematics.com/6868/12v-battery-level-indicator-circuit/>`_

One issue I have yet to solve is the ability to reconfigure
the network setup in case I use the Ghetto blaster in someone
else's house. Right now I have to plug a screen and a keyboard
or to plug a network cable and ssh on the Raspberry to change the
network config.

Maybe one way to solve this would be to have
a second wifi dongle set as an access point, and a small web interface
to configure the network.


Raspberry-Pis are so fun.
