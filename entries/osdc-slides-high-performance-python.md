Title: OSDC Slides - High performance Python web apps
Date: 2011-10-04 16:15
Category: mozilla, python

We gave a talk last month with Benoit in Paris about web servers.   
  
The talk consisted of a first part were we've explained how a web
server works, and we got into details like what's a backlog etc. and
explained how the technology evolved from a single CGI process to modern
setups based on event loops or such things.   
  
We've also presented the stack I've set up for the Firefox Sync server,
and gave an overview about stress tests tools.   
  
You can grab the PDF translated in English here: [High Availability
Server Apps - benoitc + tarek][]   
  
Or watch them on SlideShare here: [High Availability Server Apps][]   
  
***The bottom line is : use Nginx, Gunicorn and Gevent***   
  
If you wonder why we have socks and shoes on our slides, it's because
"socket" sounds a lot like "chaussette" (means socks) in French, so it's
a (stupid but efficient) joke :)

  [High Availability Server Apps - benoitc + tarek]: http://ziade.org/ha_osdcfr_20110923.pdf
  [High Availability Server Apps]: http://www.slideshare.net/tarek.ziade/high-availability-server-apps
    "High Availability Server Apps"
