Title: How to handle large files in Plone ?
Date: 2007-09-10 08:42
Category: plone, python, zope

The first time I had to help out a customer (a fifty year old lady that
had no interest whatsoever about computers) on a Plone-based intranet, I
had to explain to her why she couldn't upload really big files.   
  
That was really tough, as she couldn't understand why the system had
such a limitation. I think she was right. If we drop the technical point
of view, a sophisticated system such as Plone should provide a
transparent way to upload big files and handle them smoothly on the
server side, so the user doesn't feel any difference. Think about it:
what's the functional difference between a big file and a small file ?
Merely none, except that it's longer to put or to get.   

  
  
# Uploading

  
The first problem when we deal with big files is the upload time.
Browser doesn't provide any feedback, unless you install some Firefox
extension or you use a dedicated protocol, such as FTP. In a web
interface, there's nothing but an animated logo that is moving around
just to say: "Hey, I am not dead !". Ruby On Rails guys came up with a
great feature on this topic: they added in their publiser a few apis
that would let client-side Javascript:   
-   display a progress bar;
-   cancel the upload at anytime.

  
I am not a technical guru on HTTP protocols but I am really wondering
why this is not already available in Gmail... I tried myself to
implement it a while ago on Zope 3 publisher, and came up with something
that was working, but never had the time to polish it.   
  
The idea is to maintain on server-side, for each ongoing uploads, some
infos that can be read by the client, and a cancel API. The only
important point is to provide a secure mechanism so no other client can
read the infos of another client. The client-side JS code then can call
asynchronously the server to display feedback, and provide a cancel
button.   
  
At this point, we may consider that it is better to use other piece of
software, like [Tramline][], or some dedicated Apache plugin. But in a
marketing point of view, I think it's really important to be able to
provide this feature with an out-of-the-box Plone.   

  
  
# Server-side handling

  
OK, so our file is uploaded. My lady at the office now complains that
the system is getting very slow. No wonder, her ZODB weights now several
gigas... Again, functionaly speaking, that's a non-sense. Plone should
be able to work with these big files without making the ZODB so heavy.
The ZODB is a great thing for light objects, but was not meant to hold
big chunk of data. A specific thing has to be done. In Java world, they
have an advanced data storage for Content Managment System, called
[JSR-170][], and implemented by the [JCR][]. In this system, a tree of
folders is maintained and big files are stored in blobs (Binar Large
OBjectS), keeping the whole thing scalable, no matter what the users
store in it.   
  
In Zope, we don't have a lot of solutions, there's the File System
Storage ([FSS][]) product (and a few similar products) in the Plone
Collective, and that's about it. The FSS provides a smart proxy over the
file system, that let the ZODB breathe and the user handle his big
files. But this is an extra product, created to provide a really missing
core feature.   
  
The [3.8 version of ZODB][] though, providen this feature now, through
blobs. On Plone side, it seems that the latest [Plone4Artists sprint][]
in Boston has boosted the work in the topic and blobs will be available
in Plone through [ATBlobField][].   
  
This is great news, and I hope we will soon be able to make all files
uses this feature transparently (big file, small file, what the
difference ? they should all be stored out of the ZODB)   

  
  
# Downloading

  
One of my colleague had a tough issue last week on big files. The File
System Storage was not acting right when the user was downloading PDF
files from the Adobe Browser plugin: the file iterator internally
provided by the Zope publisher was not acting right because it doesn't
support the range feature. This HTTP feature used by the plugin make it
possible to get pieces of files in non-sequential orders. Though, it's
not possible with an iterator to provide pieces of files without having
to rewind. So iterating is of no use there. The solution would be to
provide a smart system that knows who asked the file and how, to smartly
instanciate an iterator or a regular accessor, maybe with a cache system
for called ranges. I need to dig on ZODB blobs, maybe they already
provide such a feature. If you read this and know the answer, please let
me know...   

  
  
# Conclusion

  
There's still a lot of work in the topic, and I think the Plone4Artists
project is doing a great job to enhance things. The three topics to work
on are:   
-   cancelable upload with live feedback;
-   transparent use of blobs to store files;
-   smart downloading capabilities.

  
This could make a great sprint I guess, to create some kind of
Plone-FSS-NG, so my Lady can upload her movies in her Plone.

  [Tramline]: http://infrae.com/products/tramline
  [JSR-170]: http://jcp.org/en/jsr/detail?id=170
  [JCR]: http://en.wikipedia.org/wiki/JSR-170
  [FSS]: http://ingeniweb.sourceforge.net/Products/FileSystemStorage
  [3.8 version of ZODB]: http://www.nabble.com/ZODB-3.8.0b1-is-released-t3903510.html
  [Plone4Artists sprint]: http://plone.org/news/plone4artists-sprint-in-boston-a-success
  [ATBlobField]: http://dev.plone.org/collective/browser/ATBlobField
