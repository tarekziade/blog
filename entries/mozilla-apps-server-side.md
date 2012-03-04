Title: Mozilla Apps -- server side
Date: 2011-12-14 14:43
Category: mozilla, python

Yesterday, we've launched the ***Developer Preview*** for Apps, you can
play with at [https://apps-preview.mozilla.org][]   
  
The server side is composed of many pieces, and while they are subject
to change since this is just a preview, I think it's quite interesting
to describe some of them already -- and maybe get more contributors in
the process, since everything is open source and contributors are
welcome.   
  
Here's an overview of the system -- we used:   
-   **Django** for the App MarketPlace
-   **Cornice** for the Sync APIs
-   **Node.js** for the Sauropod APIs
-   **HBase** for the Sauropod DB

  
### The App MarketPlace - Django

  
The App MarketPlace located at [https://apps-preview.mozilla.org][1] is
where you can upload your own Apps, or install some. There's a payment
process for non-free Apps, and you can see which one you have bought in
your profile.   
  
The development is driven by the WebDev team, and is based on Django --
see [https://github.com/mozilla/zamboni/tree/master/apps/webapps][]   
  
I can't really describe this part, as I did not follow it closely. But
basically, the Market Place keeps track of your apps and payment
receipts, for other parts of the system to interact with.   
### The Dashboard - HTML + JS

  
Once you start to install Open Web Applications, you are redirected to
a *Dashboard* at [https://myapps.mozillalabs.com][]. This Dashboard is
an HTML application that lists your installed Apps associated to your
Browser ID.   
  
What's pretty cool is that no matter where you've installed a given App
-- Firefox on your Desktop, your Phone, it will appear on this
dashboard, and synced across devices.This is done via a Sync service
called ***AppSync***.   
  
Code pointers for the Dashboard:   
-   [https://github.com/mozilla/openwebapps/tree/develop/site][]
-   [https://github.com/mozilla/openwebapps/blob/develop/addons/jetpack/lib/sync.js][]

  
### AppSync

  
AppSync is the part I worked on. Its design was mainly done by Ian
Bicking, who then worked on the client side implementation while I was
working on the server side one.   
  
It's quite similar to what we did for Firefox Sync, except that:   
-   AppSync supports BrowserID
-   The data is stored in Sauropod

  
Securing this data is part of a much larger ongoing project called
[Sauropod][]. The idea is that any database access has to be done with
credentials, and that Sauropod is in charge of controlling them and
dealing with the storage.   
  
In the long term, depending how Sauropod evolves with respect to
encryption, and how Firefox Sync itself evolves with respect to Browser
ID and Sauropod access, we might merge both projects.   
  
Or maybe Sauropod will provide APIs one day that are good enough for
direct clients interactions, turning AppSync into a simple proxy ?   
  
Time will tell !   
  
Anyway, here's an overview below of the AppSync system we've set up for
this preview.   
  
We have the AppSync server itself, that's built using [Cornice][]. It
provides the synchronisation APIs described in this document:
[https://wiki.mozilla.org/Apps/Sync/Spec][]   
  
Every time a client wants to write new data, we call the ***Sauropod***
server which is a very simple GET/SET api built with Node.js.   
  
The flow is:   
-   AppSync server asks for a new Sauropod session, using Browser ID
    credentials
-   Sauropod verifies the Browser ID credentials then create a DB token
    into a session
-   AppSync uses this token until its not valid anymore
-   Sauropod calls in turn an HBase cluster to access the data
-   Every write is mirrored in a MySQL database in AppSync. This
    mirroring was set so we can turn off Sauropod if we need to, and
    still have a working system. This will eventually go away later.

  
![image][]   
  
Find the code here:   
-   Server [https://github.com/mozilla/appsync][]
-   Client [https://github.com/mozilla/openwebapps/tree/develop/sync][]

  
### What's Next

  
I am really excited by this project. There are a lot of people involved
in the Mozilla community, and seeing all the moving pieces assembled to
build an ***Open*** App environement is pretty cool.   
  
We're going to work in the upcoming months on consolidating the whole
system, making sure it scales well and correct the design as the
feedback comes back.   
  
If you want to get involved, you can install the preview, play with the
available Apps and even maybe write your own Apps for the Market Place,
or help us in the coding.   
  
We're hanging in \#openwebapps on Mozilla's IRC   
  
**EDIT : [Anant wrote a very nice blog post on the topic][]**   
  

  [https://apps-preview.mozilla.org]: https://apps-preview.mozilla.org/
  [1]: https://apps-preview.mozilla.org
  [https://github.com/mozilla/zamboni/tree/master/apps/webapps]: https://github.com/mozilla/zamboni/tree/master/apps/webapps
  [https://myapps.mozillalabs.com]: https://myapps.mozillalabs.com
  [https://github.com/mozilla/openwebapps/tree/develop/site]: https://github.com/mozilla/openwebapps/tree/develop/site
  [https://github.com/mozilla/openwebapps/blob/develop/addons/jetpack/lib/sync.js]:
    https://github.com/mozilla/openwebapps/blob/develop/addons/jetpack/lib/sync.js
  [Sauropod]: https://wiki.mozilla.org/Sauropod
  [Cornice]: http://packages.python.org/cornice/
  [https://wiki.mozilla.org/Apps/Sync/Spec]: https://wiki.mozilla.org/Apps/Sync/Spec
  [image]: http://ziade.org/appsync.png "AppSync Cluster"
  [https://github.com/mozilla/appsync]: https://github.com/mozilla/appsync
  [https://github.com/mozilla/openwebapps/tree/develop/sync]: https://github.com/mozilla/openwebapps/tree/develop/sync
  [Anant wrote a very nice blog post on the topic]: http://kix.in/2011/12/15/behind-the-mozilla-apps-developer-preview/
