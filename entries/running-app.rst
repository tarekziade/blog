The Perfect Running App
########################

:date: 2014-09-14 19:05
:author: Tarek Ziade


.. note::

   Most running applications out there are good enough
   for casual runners. This blog post is my tentative
   to describe what I would like to see in a running
   app for more serious practice.


I used a few running applications to track all my runs. Mostly the
Nike+ app since this what naturally came with my Nike+ watch before
I switched to a Garmin Forerunner 310XT.

.. figure:: http://blog.ziade.org/watch.jpg
   :alt: Changing watch

   From Nike+ to Garmin...


The app was a bit frustrating for many reasons and I thought that was
because it's made for beginners, and that I was not the typical user
anymore. I was not really interested in the provided metrics and was
looking for better things.

When I switched to my new watch I though the app would be as good as
the hardware. But no. What came as a surprise is that all the
applications I have tried or looked at are not really better than
Nike+. It looks like they are all aiming at casual runners.

But when you buy a expensive watch and do 5 trainings per week,
you have some expectations.

I still wonder how come we don't have something better
in a domain where anyone can understand the basics of what a good
training session should be, by reading 2 or 3 running magazines.
Unless you are doing crazy elite training with a whole staff,
it's not rocket science.

And in my running club, even the very experienced runners use one of
these apps and get frustrated. But it seems that no one expects
these apps to be better than they are right now. The general consensus
around me is: you can analyze your runs manually, the watch and its
software will just help you get the raw data.

This is not good enough for me. I am very frustrated. I want
to see if I am making any progress by using months of data - and
this is not easy to do by hand.

`SmashRun <http://smashrun.com>`_ looks like a promising app but still
misses a lot of what I am looking for. Since it's built by runners who
seem passionate about building the right stuff, I got a pro account
to encourage them. They have a voting system for new features, people
that have a pro account can use.

However, I would like to write down in this blog post what I am
exactly looking for and what I despise in a running app.

Of course
this is what *I* want - but I am pretty sure that most seasoned runners
would want something similar. Maybe it exists ? You should let me know.



Stop comparing Apples and Oranges
=================================

I think this is the worst feature **all** running apps have: they
will tell you your average pace and your *"progression"*. Some of them
try to take a coach-like tone and tell you stuff like:

    You're getting slow!


Jeez. Of course I am getting slow. I ran an interval run yesterday with
a specific pace of 3'40/km and today I am doing a long run at a very
slow pace because this is how you train !

.. figure:: http://blog.ziade.org/nike+.png
   :alt: pace over the week

   Yeah the pace varies during the week. Nothing I can do with this
   chart here.

**Global metrics that use all your recorded runs have no sense**

You can't do this. That does not mean anything. Knowing that my yearly
average pace is 4'45 does not mean anything.

You can't either really know what will be my estimate finish on a 5k using one
of my long runs.

.. figure:: http://blog.ziade.org/smashrun-1.png
   :alt: Performance Index

   My estimated 5k finish time based on one long run. Of course
   it's completely wrong.


Also, the volume of trainings and kilometers you do really depends
on what you're aiming at. Someone that is getting ready for a marathon
will do at least 60km/week, and will take it easy the last week.

That would be a non-sense if you are getting ready for a 5k - But
in most apps, the runner that prepares for the marathon will appear
like a killer compared to the 5k runner. Tell this to the runners
that are doing 16' on a 5k...

.. figure:: http://blog.ziade.org/smashrun-2.png
   :alt: Gold Medal

   I will soon lose my Gold medal since my 5 weeks training plan
   is over.


Anyways. My point is that the software should be smarter there.
Every run needs to be classified in very specific groups to have
any useful metrics on it. The most important ones are:

- long runs
- short interval runs
- long interval runs
- races


Long Runs
=========

A long run is basically running at a lower pace for a longer time than
usual. If you are getting ready for a 10k, you usually have one or two long
runs per week, that will last for 1h to 1h30 tops.

The goal of those runs is to try to keep the same steady heart rate, and
usually if the place where you are running is flat enough, the same pace.

A long run look like this:

.. figure:: http://blog.ziade.org/chart-2.jpg
   :alt: Long run

   The red zone is the HR drift.


There are several interesting things in this chart: you don't usually
warmup when you do long runs. So the first portion of the run is a slow
raise of your pace and heart rate until you've reached the targeted zone.

The quality of a long run is your ability to stick with the same heart rate
for the whole session. Unless you are very careful and slow down a bit
over time, there will be a slow, natural increase of your heart reate
over time.

**The most interesting metric in the case of a long run is to determine
how flat your HR is, excluding the warmup section at the beginning.**

A possible variation is to add a few strikes in the middle of your long
runs. It makes it less boring. For example 2x2mn at 10k speed. It's
important that these two strikes don't confuse the software that measures
how flat your HR is.

Comparing long runs can be done by looking at;

- how good you are at keeping the desired HR over time
- how fast your heart is beating for a given pace
  *as long as the circuit is flat enough* and how this evolves over time.




Short Interval Run
===================

If I do a short interval run, this is how things will go:

- 30' warmup
- 12x (45" at max speed, 30" slow)
- 10' to cool down

.. figure:: http://blog.ziade.org/chart-1.jpg
   :alt: Long run

   The red line is the linear regression of
   the fast strikes.


We can ditch the warmup. It does not bring any interesting data besides the
volume of training.  The only interesting thing to do there is to make sure
it was long  enough. That varies between runners, but for short intervals,
it's usually roughly as long as the intervals themselves.

Now for the intervals, a quality metrics is to check if they are all done
at the same speed. It's quite common to start the series very fast and
to finish slowly, completely burnt by the first strikes. This is not good!
A good interval run is done at the same speed for all strikes (both
fast and slow segments). A great interval run is done with a slightly
faster speed for the last intervals.

A good metrics in this case is the linear regression of the pace for
the fast segments then the slow segments. It should be flat or slightly
increasing.

The ten last minutes are also very intesting: how fast your heart rate
decreases over the ten minutes ? The faster the better.

Comparing interval runs between them can be done by checking how these
metrics progress over time.

Long Interval Runs
==================

Long interval runs are like the short ones. The only difference is that
you can take into account your HR variation between strikes to see
how good you are at decreasing your HR between each strike. A linear
regression can be added there.


Race
====

A Race is a very specific run, and has its specific metrics. Usually, we
tend to start too fast with the danger of getting in the red zone
in the first kilometers.

This is the perfect 10k run:

.. figure:: http://blog.ziade.org/chart-3.jpg
   :alt: Long run

   A 10K run with a perfect negative split.


The first 5-6k are down 3-5 seconds slower than your target pace, and
the end of the run 3-5 seconds faster. This is called a negative split.
The last 500m should be as fast as you can.

So for races, what I want to find out is if I was able to do a negative
split, if I did not start too fast and if I was able to sprint to the
finish line.

This is also a set of metrics that can be compared from race to race
over time.


The Impact of Temperature
=========================

I have a friend at the racing club that trained hard for 8 weeks for a
marathon. He was aiming at 3h15mn and practiced accordingly. The day the
race was there, we had a very unusual heat wave in France - 37ºC which is
a lot for my area. He finished the marathon in 3h40 and was happy about
his performance!

The bottom line is that the heat or the cold directly impact how we
perform - and this varies a lot between individuals. In my dream running
app, I want to correlate my results with the temperature.

I want all my predictions to have a ponderation (not sure that's
how you say it in english ;)) with the temperature.


The Impact of Rest
==================

How long did you rest since the last run ? How did it impact your
performances ?

With this information and how fast your heart slows down after your
training, we can detect overtraining and undertraining.

I know Polar has a bit of this in its latest software. It tells
you how long you should rest before your next run. I wonder how
they calculate this.


The Social Part
===============

Last year I ran in San Franscisco near the bay bridge with my Nike+
watch and when I uploaded my run I was delighted to see that I did
a 1 mile segment many people did.

Unfortunately, the only thing the app was able to tell me is that
I was 365th in terms of pace and another ridiculous rank in terms
of how many runs I did there.

This is so stupid. Where am I getting with this ? Becoming the Running
Mayor of the Pier? :)

There's one thing that could be interesting in running apps when
comparing your data with other people: group users by ages and
by records.

I am 37 and my 10k record is around 38' - I don't really care to know
how I perform on a weekly basis compared to an elite runner who
does 31', or a more casual runner who does 50'.

What could be interesting though is to compare with people that are at my
level or age and that are getting ready for the same race maybe ? or a
race that's similar enough and close enough.


Conclusion
==========

This blog post is just a brain dump - some ideas are pretty vague and I
have not really talked about the UX of the Running Software.

But the bottom line is that if you don't just jog, and want to use
a running application for serious training, what I have described is
what I think is needed.

I hope Smashrun will go into that direction!

