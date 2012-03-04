Title: Montreal Packaging sprint wrapup
Date: 2010-03-16 19:42
Category: python

After the Confoo.ca conference, [Yannick Gingras][] from the Montreal
Python user group organized two   
  
[caption id="" align="alignright" width="343" caption="Sprinting on
TurboGears 2"][![Les Brasseurs Numérique - Sprinting on TurboGears
2][]][][/caption]   
  
small sprints at the Brasseurs Numériques headquarters (Digital
Brewers). Yannick's company is called like that because he brews his own
beers ! As a matter of fact, he prepared a beer for the sprints, that
was really good (and quite strong.). His beer would probably beat some
good Belgium beers on a blind test.   
### Sprint \#1 : Turbogears

  
[Chris Perkins][] led a Turbogears sprint Saturday. I am not very
familiar with this framework but I am using Pylons a lot, and its the
basis of Turbogears. [Alice Bevan-McGregor][] was present, and could
confront his ideas on web frameworkery with Chris since he created his
own tool : [WebCore][]. I've heard that they worked on making the
Turbogears dispatcher a standalone library so it could be used by both
frameworks.   
  
I worked on my side on small packaging issues TG has. We fixed the
latest TG 2.x beta custom package index that was broken (it was
generating incomprehensible errors when installing TG, and I found out
that the index pages in the TG PyPI were broken)   
  
Next, I've added to easy\_install a *--no-find-links* option to prevent
links added by projects in their setup.cfg. This will prevent projects
like Pylons to implicitely add links that easy\_install reads. The
effect is that some old version of some packages like nose were
installed. This is not released yet.   
  
If you were present to the sprint, please comment to tell us what
you've done !   
  
**EDIT: Chris added more details on the TG sprint** -- [see the
comments][]   
### Sprint \#2 : Packaging

  
Monday evening we worked on packaging issues. I started the sprint by
presenting the current state of packaging on a board. That took quite a
while because it is not obvious to understand the packaging eco-system
(distutils, setuptools, distutils2 and pip.).   
  
Then I've listed possible tasks and people started to work.   
-   Yannick Gingras worked a bit on the Hitchicker's Guide to Packaging
    then worked on Distribute on Issue \#133.
-   Ahmed Al-Saadi was pretty new to packaging so he worked on the guide
    and tried to catch up with the state of packaging (that's a real
    work :) )
-   Alexandre Vassaloti worked on porting distutils2 into Python3. So
    basically, like Distribute, Distutils2 will be installable on Python
    2 and 3, using the same source tree, and a 2to3 call upon
    installation.
-   Nicolas Cadou worked on PEP 345 support. He created a sample project
    that will be used in a functional test to validate that everything
    works. He eventually fixed some code in Distutils2 so it works with
    the PEP 345 DistributionMetadata class I've built during Pycon. I
    need to merge his work asap.
-   Matthieu Leduc-Hammel worked with me on PEP 345 support for PyPI.
    I've changed the postgres database to add the new fields, and
    Matthieu worked on PyPI UI. For instance, you will have a nice box
    on the project pages now that displays links from the Project-URL
    metadata field. I need to merge his work asap.

  
As a global note: Mercurial was the perfect tool for this sprint. I am
able to merge people work in Distutils2 and other projects without all
the repository access issues we usually get when we start a sprint. I am
looking forward for a full Mercurial switch of Python, because this will
boost contributions.   
  
Thanks Yannick, Nicolas for the Sprint and the Beer ! Thanks [Ubity][]
for sponsoring the Packaging sprint with pizzas ! (they are looking for
developers btw)

  [Yannick Gingras]: http://ygingras.net/
  [Les Brasseurs Numérique - Sprinting on TurboGears 2]: http://lh5.ggpht.com/_BBU4XN71nJo/S5_Ly74ivlI/AAAAAAAAAoM/00wkIxnidaY/s512/IMGP7327.jpg
    "Les Brasseurs Numérique - Sprinting on TurboGears 2"
  [![Les Brasseurs Numérique - Sprinting on TurboGears 2][]]: http://lh5.ggpht.com/_BBU4XN71nJo/S5_Ly74ivlI/AAAAAAAAAoM/00wkIxnidaY/s512/IMGP7327.jpg
  [Chris Perkins]: http://percious.com/blog
  [Alice Bevan-McGregor]: http://www.gothcandy.com/blog
  [WebCore]: http://www.web-core.org
  [see the comments]: http://tarekziade.wordpress.com/2010/03/16/montreal-packaging-sprint-wrapup/#comment-9959
  [Ubity]: http://ubity.com
