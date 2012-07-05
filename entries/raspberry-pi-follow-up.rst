My Raspberry Pi Juke Box (Follow up)
####################################

:date: 2012-07-04 20:11
:tags: python
:category: python
:author: Tarek Ziade

.. image:: http://blog.ziade.org/rpi-jukebox-mini.jpg
   :target: http://blog.ziade.org/rpi-jukebox.jpg


Just a follow-up on my `Raspberry Pi Juke Box project <http://blog.ziade.org/2012/07/01/a-raspberry-pi-juke-box-how-to/>`_.

I have received all the peripherals by mail today so I could finish the
project.

A few remarks:

- The `XMI Speaker <http://www.amazon.fr/gp/product/B001UEBN42/>`_ is amazing.
  You unfold it like an accordion and it has a really good sound.
  It's hard to give you an idea, but if you have a MBP or a MBA, the
  sound coming out of this tiny speaker is much better.

- The `USB Battery <http://www.amazon.fr/gp/product/B006LR6N3O>`_ delivers
  1A or 500ma, so is working perfectly well for the R-Pi.

Both peripherals were fully charged when I got them, so I could go ahead
and plug them.

The `AirLink 101 <http://www.amazon.fr/gp/product/B003X26PMO>`_ wifi dongle
on the other hand was a bit tedious to install. It's a Realtek 8188CUS but
a 8191SU driver seems to work well.

Don't plug it, it will freeze your R-PI. Edit the **etc/modprobe.d/blacklist.conf**
file and add::

    blacklist rtl8192cu

Then, before you plug it::

    $ wget http://www.electrictea.co.uk/rpi/8192cu.tar.gz
    $ tar -xzvf 8192cu.tar.gz
    $ sudo install -p -m 644 8192cu.ko /lib/modules/3.1.9+/kernel/drivers/net/wireless/
    $ sudo depmod -a
    $ sudo apt-get install firmware-realtek dhcpcd wpasupplicant

Now you can plug it and reboot your R-Pi. Things should work fine.

Tweak your **/etc/network/interfaces** if you want the dongle to autoconnect
to your wifi. Here's my relevant section for *wlan0*::


    auto wlan0

    iface wlan0 inet dhcp
        wpa-ssid Villa_Des_Mouches
        wpa-psk MyPassWord


That's all. Now when I reboot the R-Pi via the hardware, it gets an IP via the WIfi
Dongle and I can happily ssh it or get into the Juke box app.

I am really happy I did not have to add a powered USB Hub.
