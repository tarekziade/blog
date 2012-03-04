Title: Pycon packaging sprint topics
Date: 2010-01-11 22:20
Category: python

Pycon is coming soon. Here's a list of possible topics I would like to
work on during the sprint:   
1.  adding the features in Distutils I've mentioned in my [earlier
    post][].
2.  work on the standalone release of Distutils, and make sure it works
    with 2.4, 2.5, etc so it can be distributed at PyPI. There are
    already [installable nightly builds][] by the way.
3.  Finish the buildbot work so Distutils is tested with more projects
    from PyPI
4.  Continue the work on Distribute, and specifically the work on 0.7:   
   1.  finish the develop command that would work with non-eggs formats
    2.  finish the configure/build/install command where all options are
        computed and saved by the configure command

      
5.  Fix plenty of issues in the tracker
6.  work on a geolocalisation feature for Pip, so the nearest mirror can
    be picked
7.  ...

  
Anyone interested in packaging sprinting at Pycon ? Let me know !

  [earlier post]: http://tarekziade.wordpress.com/2010/01/07/possible-new-features-for-distutils-2-7/
  [installable nightly builds]: http://python-distribute.org/
