Title: &quot;packaging&quot; has landed in the stdlib
Date: 2011-05-22 23:02
Category: python

I've pushed in the standard library the new version of Distutils !   
  
This new version, initially known as **distutils2** was renamed to
***packaging*** (Tres Seaver came up with this name during the last
Summit), and contains all the improvement we have been working on during
the last 2 years or so on the distutils codebase.   
  
There are still a lot of thing to do until Python 3.3 is out, but
having packaging back in the standard library makes our work easier, and
will boost its polishing for the upcoming release.   
  
This work is still not very useful to the community since we need to
backport it to Python 2. The plan is to run 3to2 and have a standalone
version released under the Distutils2 name.   
  
This tool has countless improvements I will explain later, whenever we
push the documentation in the coming days.   
  
Just to whet your appetite:   
-   for **end-users** Python gains a **pysetup** script you can use to
    install, uninstall projects, browse installed projects, browse PyPI,
    and many other things.
-   for **developers**, no more setup.py file. You just define
    everything in new setup.cfg sections. You can also define your data
    files in details.
-   for **os packagers**, you can relocate data files where they should
    be installed, without breaking the code.

  
~~nb : the push busted all the buildbots in the process, and I've been
busy in the last days to fix them. I still have cryptic issues under BSD
and Solaris, but most problems have been fixed. Thanks a lot to Victor,
Ezio, Antoine, Ned, David and many more people that helped me there~~
*Buildbot is now back to normal, everything was fixed \\o/*   
  
nb 2: the commands and compiler parts are not really different from
distutils, but we have numerous things to change before 3.3, and I'll
try to get more people involved in that part because I don't know what's
a compiler :). If you're doing sci stuff w/ Python, know compilers, and
want to help us, let me know.
