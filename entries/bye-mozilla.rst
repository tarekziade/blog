My journey at Mozilla
#####################

:date: 2020/12/14
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade


During the spring of 2010, I applied for a job at Mozilla Labs. They were
looking for a Python developer to re-write the Firefox Sync service (called
Weave back then) into Python. They wanted to move all of their web services
from PHP to Python, and looked for a Python expert to help them.

The interviews went very well, and they were planning to fly me over for an
onsite day, and then everything went to a full stop because the Eyjafjallajökull
volcano blocked all transatlantic flights. I was really worried I would miss
that opportunity. But I was eventually able to fly there, on Castro street, at
the Mozilla Office that used to be the Netscape office back in the old days.

I got the job and embarked on an adventure that lasted for over a decade.
It was an amazing journey. It started with the Mozilla Summit in Whistler in
July 2010. In the picture below, I am the first guy on the bottom right corner,
a few meters behind Mitchell Baker.

.. image:: /theme/images/Mozilla-Summit-2010.jpg

I was blown away. After this summit, I had many more all hands. The craziest
one was in Las Vegas when they flew the whole company in two Mozillians-only
planes and organized a private party at the Envie Hotel night club to celebrate
Firefox 4.

From 30% to 5%
==============

The Firefox 4 release happened when we were over 30% in desktop market share.
But right at the same time, the new kid in town, Chrome, tripled its user base
in a single year! It was obvious we would have to fight hard
against them. And at the same time, Google was our biggest source of revenue.

.. image:: /theme/images/desktop-share.png

There's a recent article about the relation between Mozilla and Google
on `Bloomberg <https://www.bloomberg.com/news/articles/2020-11-24/deals-with-apple-aapl-mozilla-show-how-google-googl-discourages-competition>`_ that's
quite captivating.

Circa 2013, the market was getting more and more driven by tablets and phones.
I guess building Firefox OS then was the right move, to try to exist in that
space. But phones are very hard. It's quite amazing what Mozilla was able to
build for Firefox OS, and a lot of cool techs got out of it. But the OS failed
to get traction. We do have the browser available on mainstream mobile OSes,
but if you look at the global market share today, including phones, it's just
Chrome vs Safari (read, Android vs iOS), and everyone else is under 5%.

.. image:: /theme/images/browser-share.png


I think the reason is quite simple. If you buy a phone and you can browse the
Internet, what would be your incentive to install another
browser? The speed of the browser? I don't think there's one mobile browser
that's crushing others in that respect. Privacy? That's a big incentive for
me, but for the average user, they don't care that much, unfortunately. They spend
more time online using another app than a browser anyway... (FB, TikTok, Insta,
etc).

And if you are a phone maker and you are not Apple, you want to give your users
the basic Android features and that means Google Apps and its Playstore. It's a
bit of a tied sale -- I find it outrageous. And maybe someday, there will be an
antitrust policy that forces phone makers to ask the user what browser they
want to use on first start? I think that's the only way Firefox can compete
fairly.

That does not mean Mozilla is dead -- it just means Firefox is not going to be
one of the main browsers anymore. And I can't see how the trend can be reversed
unless something happens in the mobile space between Android and iOS. Mozilla
still plays a super important role for the web, and will probably be around for
very long. It's so much more than a browser. But it needs to adapt to that new
reality, and that's been on the agenda for a few years now -- and currently
happening.

In any case, I was so lucky to be part of that whole cycle. I won't write a
long article about all the tech stuff I've done during my tenure at Mozilla, but
just say that this job was an amazing adventure and explain how I grew in it.

From Engineer to Senior Staff
=============================

The first years were very hard because I went from being "a big fish in a small pond"
(to paraphrase Connor) to one of the dumbest guys in the room. I had to grow a lot
to be able to have the impact I wanted to have, in an environment packed with
world-class engineers. It took me a year to get fluent enough to understand
English spoken in a wide variety of accents, so I would not use 50% of my
brainpower just to follow engineer's conversations. One funny anecdote is that I was
not the only one struggling with this sometimes. I remember working with one
British guy from East London and could not understand everything he was saying.
When I told that to some U.S. colleagues, they laughed because they could not
either.

It also took a couple of years to get back to a decent working schedule. For a
while, I was the only European in the team, so it was easy for everyone to
forget that it was 2 a.m. for me in some of the meetings -- and I did not want to
be annoying about it, I was just too happy to be part of it. And again, I was
not the only one in that situation. Looking at you Ryan in Australia ;)

But eventually Mozilla grew a lot in Europe and I hanged on and grew with it,
and got involved in some amazing projects. I've also had a few amazing managers
along the way -- Connor, Stuart, Vicky, Thank you! (Interesting, they all are
Canadians... ;) ) and tons of amazing colleagues. I don't want to name them
here, I would be too worried to forget one.

.. image:: /theme/images/badge.png

Fast forward 2020, I grew from Software Engineer to Senior Staff Engineer and
worked lately on some pretty cool stuff for the Performance team in Patricia's
org. But after a decade, I felt like I reached the end of my cycle at
Mozilla. 10+ years is a long time, and all the recent events (COVID, layoffs)
accelerated that feeling. I felt like I needed to take a step back and think
about what I wanted to do next, and what topics excite me the most and
look for a new challenge elsewhere.

What's next for me
==================

The work I was involved with in the past 3/4 years was focused on tracking the
browser performance and that involved building tools from within the CI/CD. I
realized how crucial this is in the software cycle. Building an application
that works is within the reach of most developers team -- they are good at it.
What makes a difference is automation. Once the
application starts to grow beyond a few developers, good automation is what
will make every change easy, secure, and fast. I have seen a lot of projects
grow uncontrollably until they were replaced with something else.

There is no silver bullet when building automation. A good CI/CD pipeline is
built over time, through feedback from people and the right metrics. It
also relies on a QA culture, which needs to be created by and shared amongst
all people involved in building the software. It also helps in building the
right software architecture. A software that's hard to automate is often a sign
of bad architecture or overdue refactoring.

Driving this kind of work is something I am excited about, and that's why I've
accepted an offer to work on this topic in a new company, starting next January
-- Yeah, doing a bit of teasing, I will blog about it very soon!

Thanks, Mozilla, this was an amazing journey. I have so many memories.
Thanks Richard and Jean-Yves for reading my drafts :)
