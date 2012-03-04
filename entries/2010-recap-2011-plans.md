Title: 2010 recap, 2011 plans
Date: 2011-01-02 11:53
Category: mozilla, python

Instead of the weekly recap I've been doing lately, I will do a year
recap and list my plans for 2011. Happy new year to all of you !   
  
tldr: 2010 was quite an important year for me. The most important event
was [Suki][] of course, six months ago ! In Python I am still working on
packaging matters and I've joined Mozilla 6 months ago, working in the
Services team. 2011 should be the *Year of Packaging* and more fun at
Mozilla !   
### 2010 recap

  
**January**: My work on PEP 386 and 345 is waiting for the final
approval from Guido and [I am back at work on PEP 376 and Distribute][].
PEP work involves politics and time. It also means making sure the
solutions are good enough for a smooth evolution of the existing
ecosystem. It was frustrating at first but after a while I got used to
it. A PEP will eventually gets accepted when there's a clear need for
it.   
  
In **February** [I gave a talk at PyCon][] and [sprinted there][]. My
talk was well received (it made the top \#5 of all talks at PyCon with
the token voting system). I think it was both because I was passionate
about it, and because part of the audience followed the work we did in
the last months. The[language summit][] was held there as well, and was
both frustrating and great. *Frustrating* because I was told to revert
all changes to Distutils and do the work outside the stdlib for a while.
That was the right decision but was a bit hard to accept at first.
*Great* because Packaging was yet one of the main focus of the summit.
In February, [some of my PEPs were accepted][], which was a very
important milestone.   
  
In **March** [we started to develop Distutils2][], which was basically
the trunk of Distutils right before the Big Revert. Yannick and other
fine folks from Montreal became [regular contributors][] to the project.
I've also started in March to think hard about my future, and found out
I was really happy [working remotely][]. I also started to focus on GSOC
and build proposals for [Distutils2][] and other [topics][].   
  
In **April** I was[nominated at the PSF][]. I also started to get some
interest in Mozilla and in particular [Sync][] (formely Weave). Beta
versions of Distutils2 started [to hit the shelve][]. I also added [new
features in shutil][]. Next, [PEP 376 was accepted][]. That's the master
piece for packaging interoperability ! Last, [my GSOC proposal was
accepted][] and we got no less than 5 students for Distutils2 alone !   
  
In **May**, I [tried and failed][] to merge Pip and Distutils2 efforts
;)   
  
In **June**, [Suki was born and I got a new job at Mozilla][]. Those
events considerably slowed down my work on Packaging and my blogging of
course.   
  
The [GSOC ended][] in **August**. We managed to keep a few
contributors, which is the whole point.   
  
In **September** I [worked hard on Firefox Sync][], and we had[our
annual sprint][] at my house.   
  
In **October**, while everything which is not related to work was
slowed down because of the new-born baby, I was still finding a bit of
time to [work on Distutils2][]. But compared to Q1 and Q2, the activity
on the project was very low. I was just hoping then that it wouldn't
kill the momentum on Packaging.   
  
**November** and **December** were mainly focused on work. See my
[weekly][] reports.   
### 2011 plans

  
2011 will be the Year of Packaging, I am telling you ! Pycon will be a
milestone because Distutils2 should be in a state where it's pretty much
usable. The next tasks will be to promote it and try to gain
contributors. I am also planning move it back to the stdlib once Python
3.2 final is out.   
  
2011 will also be the *Year of Python* for Mozilla Services !   
  
Firefox Sync will be running using my Python implementation in Q1, and
Firefox 4 betas are already using the J-Pake server I've designed with
the help of my favorite client developers Stefan and Phillip. I wrote it
using the same stack than Sync. Other projects written in Python are
coming in the pipe and we are building a set of reusable tools for this
purpose.   
  
I'll also try to pursue the MoPy (Mozilla in Python) effort. That is,
sharing Python knowledge, tools etc between Mozilla projects.   
  
All in all, the work I am doing in packaging for Python is helping us a
lot at Mozilla: Distutils2 tools are now used to automatically create
RPM releases of all our dependencies by fetching them at PyPI. I hope my
Pycon talk about Firefox Sync will be accepted so I can explain how I
built it !

  [Suki]: http://picasaweb.google.com/ziade.tarek/Christmas2010Turcey#5555816919628036034
  [I am back at work on PEP 376 and Distribute]: http://tarekziade.wordpress.com/2010/01/07/possible-new-features-for-distutils-2-7/
  [I gave a talk at PyCon]: http://tarekziade.wordpress.com/2010/02/20/pycon-slides-answers-to-gm-questions/
  [sprinted there]: http://tarekziade.wordpress.com/2010/01/11/pycon-packaging-sprint-topics/
  [language summit]: http://tarekziade.wordpress.com/2010/02/18/python-language-summit-summary-of-the-packaging-track/
  [some of my PEPs were accepted]: http://tarekziade.wordpress.com/2010/02/10/pep-345-and-386-accepted-summary-of-changes/
  [we started to develop Distutils2]: http://tarekziade.wordpress.com/2010/03/03/the-fate-of-distutils-pycon-summit-packaging-sprint-detailed-report/
  [regular contributors]: http://tarekziade.wordpress.com/2010/03/16/montreal-packaging-sprint-wrapup/
  [working remotely]: http://tarekziade.wordpress.com/2010/03/18/4-simple-tips-for-wannabe-remote-workers/
  [Distutils2]: http://tarekziade.wordpress.com/2010/03/18/distutils2-proposal-for-gsoc/
  [topics]: http://tarekziade.wordpress.com/2010/03/21/another-gsoc-idea-a-pypi-testing-infrastructure/
  [nominated at the PSF]: http://tarekziade.wordpress.com/2010/04/06/hello-psf/
  [Sync]: http://tarekziade.wordpress.com/2010/04/06/python-weave-released/
  [to hit the shelve]: http://tarekziade.wordpress.com/2010/04/08/a-small-distutils2-foretaste/
  [new features in shutil]: http://tarekziade.wordpress.com/2010/04/21/stdlibs-shutil-improvements/
  [PEP 376 was accepted]: http://tarekziade.wordpress.com/2010/04/26/pep-376-is-accepted-what-it-means/
  [my GSOC proposal was accepted]: http://tarekziade.wordpress.com/2010/04/26/a-distutils2-google-summer-of-code/
  [tried and failed]: http://tarekziade.wordpress.com/2010/05/31/distutils2-vs-pip/
  [Suki was born and I got a new job at Mozilla]: http://tarekziade.wordpress.com/2010/06/19/suki-mozilla-and-japanese-book/
  [GSOC ended]: http://tarekziade.wordpress.com/2010/08/19/distutils-2-summary-of-the-gsoc/
  [worked hard on Firefox Sync]: http://tarekziade.wordpress.com/2010/09/21/firefox-sync-server-in-python-take-2/
  [our annual sprint]: http://tarekziade.wordpress.com/2010/09/22/afpy-camp-python-sprint-wrap-up/
  [work on Distutils2]: http://tarekziade.wordpress.com/2010/10/03/a-quick-glimpse-at-distutils2-alpha3-part-2/
  [weekly]: http://tarekziade.wordpress.com/2010/11/30/rsync-mozillaservices-community-week-47/
