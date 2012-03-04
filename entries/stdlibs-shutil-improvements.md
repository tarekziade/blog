Title: stdlib&#039;s shutil improvements
Date: 2010-04-21 13:21
Category: python

I have contributed [a small feature to **shutil** in the past][], and in
my work on distutils I used it really intensively. So I took over its
maintenance a while ago.   
  
I had some feedback from the community that shutil shouldn't be used,
because of some negative comments like this one in copytree: "*consider
this example code rather than the ultimate tool*". Well guess what ? I
removed that comment because this is a darn lie ! ;) . *copytree()* for
instance, is really powerful and avoid you to write yet-another-os-walk
loop. Use it.   
  
The only limitation of shutil APIs are related to the fact that it's
unable to copy all the file metadata when you move/copy files around.
Those are too specific to each platform and it's impossible/very hard to
come up with a portable metadata reader/writer.   
  
But for most needs you have in your Python applications, shutil is
perfect. Have a look at tools like *Distribute* or *zc.buildout*, they
are using shutil all over the place.   
  
Besides a few bug fixes I did, here's a list of major features I have
added or I am currently working on, with their Python version
availability:   
-   **make\_archive()**: this function will let you create any kind of
    archive, given a tree of files. You can create tarballs, zip files,
    or anything you want as long as you register a function that knows
    how to create one. See the [doc][] for more details.** (Python
    2.7)**

  
-   **unpack\_archive()**: this function will let you unpack any kind of
    archive. It has a registery like *make\_archive*(). It's almost
    ready but too late for 2.7 inclusion. **(Python 3.2)**
-   **copytree()**: Two new options for this one (see [doc][1]).
    **(Python 3.2)**   
   -   *copy\_function*: allows you to provide your own *copy*
        function. Used by *copytree() *it wants to copy a file.
    -   *ignore\_dangling\_symlinks*: if *copytree()* encounter a
        dangling symlink, and *symlinks* is set to False, it will ignore
        it and not raise an error anymore.

      

  
**shutil** groups *all high-level files operations*, that's why I have
added new functions to work with archives.   
  
If you have any feature suggestion, any file operation function that
you think should be included there, please let me know !

  [a small feature to **shutil** in the past]: http://tarekziade.wordpress.com/2008/07/08/shutilcopytree-small-improvement/
  [doc]: http://docs.python.org/dev/library/shutil.html#archives-operations
  [1]: http://docs.python.org/dev/py3k/library/shutil.html#shutil.copytree
