Title: Random notes on Mercurial queues
Date: 2010-06-30 17:21
Category: python

Working on the various parts of the Mozilla project requires some patch
fu.   
  
Basically, everything happens in [bugzilla.mozilla.org][], where you
upload a patch and ask for a review. Once you have started to work on
several patches, maintaining several mercurial clones can be tedious.
That's where queues are helping a lot.   
  
Mozilla has a [nice document about queues][]. I've also found this
[Sympy tutorial][]quite useful.   
  
Here are my random notes about queues so far:   
-   a queue is a directory of patch files (in .hg/patches). You can
    qpush or qpull them in your local repo. qpush will apply the current
    patch and add an entry in the commit log. qpop undoes it. pushing
    and poping will move you up or down in the stack.
-   I enabled 'color' in mercurial and use "hg qseries" to know where I
    am in the stack
-   I reorder patches by editing .hg/patches/series. Pretty rough but
    good enough. how come there are no q\* command for that ?
-   to delete a patch, I make sure there are no pending changes, then I
    do "hg qpop -a; hg qdelete the\_patch"
-   to import a patch from bugzilla, I use "hg qimport -n xxxx.patch
    https://bugzilla.mozilla.org/attachment.cgi?id=xxxx" where xxxx is
    the bug number

  
How do *you* work with queues ?

  [bugzilla.mozilla.org]: http://bugzilla.mozilla.org
  [nice document about queues]: https://developer.mozilla.org/en/Mercurial_queues
  [Sympy tutorial]: http://docs.sympy.org/spt-printable.html
