Title: How to receive email alerts when someone talks about something - 6 steps tutorial using Atomisator
Date: 2008-11-08 12:38
Category: plone, python, zope

I like Google Alert, the idea of receiving a mail every day that
summarizes all articles related to a given topic is really helpfull when
you need to focus on a specific subject for a while.   
  
But this is not enough. I want to receive a mail that points me to any
mailing list or planet feed or blogs out there as well, that talks about
the topic.   
  
You can't do it with Google Alerts as far as I know.   
  
Let's take an example:   
  
**I want to receive a daily mail that points me to any mail thread or
blog entry, that is related to the word "buildout" or to the word
"pycon".**   
  
Basically, to do it manually, I need to read Planet Python, Planet
Zope, then take a look at the Python, Zope and Plone mailing lists. It
takes at least 10 minutes, and more if you want to read all entries to
make sure you won't miss anything.   
  
Since online systems like [Nabble][] provides RSS feed for mailing
lists (don't find yours ? just add it there !), it is easy to read them
as they where regular feeds.   
  
From there, a script that reads all the selected feeds and sends a mail
pointing to the entries that match the selected words is simple to write
as well, and fill the need.   
  
But don't code it : [Atomisator][] will let you do this with a few
lines of configuration.   
  
Here's a step-by-step tutorial.   
  
**Step 1 - install easy\_install**   
-   download ez\_setup :
    [http://peak.telecommunity.com/dist/ez\_setup.py][]
-   run it with your Python interpreter

  
**Step 2 - install Atomisator and SQLite   
**   
-   run the command : *easy\_install Atomisator*
-   make sure SQLite is installed on your system. If not, install it:
    [http://www.sqlite.org/download.html][]*   
    *

  
**Step 3 - create an "atomisator.cfg" file**   
  
The content of the file has to be:   
   [atomisator]

    store-entries = false



    sources =

      rss http://www.nabble.com/Python---python-list-f2962.xml

      rss http://n2.nabble.com/Plone-f293351.xml

      rss http://www.nabble.com/Zope---General-f6715.xml

      rss http://planet.python.org/rss10.xml

      rss http://www.zope.org/Planet/planet_rss10.xml

  
   filters =

      buzzwords words.txt

  
   outputs =

      email email.cfg

  
This file will look into Planet Python, Planet Zope and various mailing
lists (Python, Plone, Zope). Of course you can add or remove feeds in
the **sources** option.   
  
**Step 4 - Create the words.txt file**   
  
This file contains regular expressions, one per line, that will be used
to match the entries. The file has to be saved besides* atomisator.cfg*.
  
  
For our example:   
   buildout

    pycon

  
You can put any expression you want in this file, as long as you have
one matching expression per line.   
  
**Step 5 - add an email.cfg configuration file. **   
  
This is where you define the target emails that will receive the alerts
(**tos** option). You can also specify the **from** email, or the smtp
server location. The file has to be saved besides* atomisator.cfg*.   
  
In our case it can be:   
   [email]

    tos = tarek@ziade.org

    from = tarek@ziade.org

    smtp_server = smtp.neuf.fr

  
**Step 6 - Run it !**   
  
The command to be called is **atomisator** (installed by easy\_install)
followed by the configuration file:   
   $ atomisator atomisator.cfg

    Reading data.

    Launching worker for rss - ('http://www.nabble.com/Python---python-list-f2962.xml',)

    Launching worker for rss - ('http://n2.nabble.com/Plone-f293351.xml',)

    Launching worker for rss - ('http://www.nabble.com/Zope---General-f6715.xml',)

    Launching worker for rss - ('http://planet.python.org/rss10.xml',)

    Launching worker for rss - ('http://www.zope.org/Planet/planet_rss10.xml',)

    Retrieving from rss - ('http://www.nabble.com/Python---python-list-f2962.xml',)

    Retrieving from rss - ('http://www.nabble.com/Zope---General-f6715.xml',)

    Retrieving from rss - ('http://n2.nabble.com/Plone-f293351.xml',)

    Retrieving from rss - ('http://planet.python.org/rss10.xml',)

    Retrieving from rss - ('http://www.zope.org/Planet/planet_rss10.xml',)

    .................................................................................................................................................

    Writing outputs.

    Data ready.

  
Check your mails. This call can be put in a daily cron.   
  
Tested under Mac OS X and Linux.

  [Nabble]: http://www.nabble.com/
  [Atomisator]: http://atomisator.ziade.org
  [http://peak.telecommunity.com/dist/ez\_setup.py]: http://peak.telecommunity.com/dist/ez_setup.py
  [http://www.sqlite.org/download.html]: http://www.sqlite.org/download.html
