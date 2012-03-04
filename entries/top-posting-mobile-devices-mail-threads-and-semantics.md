Title: top-posting, mobile devices, mail threads and semantics
Date: 2009-10-11 10:55
Category: python

There's an interesting discussion on python-dev about how hard it is to
follow a thread when people are starting to top-post, meaning they are
answering by quoting the whole text and putting their answers at the
top. I even got bitten by someone once because I was top-posting (don't
get me wrong, he was right about it, I was just not fully aware of the
problem)   
  
First of all, if you use a mobile device, there are good chances that
the mail application you are using doesn't give you the choice : it will
quote the text for you and will let you answer at the top. That's how it
works on my android (HTC) phone and I couldn't find a way to change it.
I am expecting mail apps on mobile devices to improve on this.   
  
But this problem reflects how hard it is to follow a thread with +100
answers. Worse, depending on the way people are quoting to provide an
answer for a specific part of a mail, some people will just stop reading
it.   
  
Gmail is doing a pretty good job to reduce this problem, because it
will automagically hide old content and you will only see new content on
every new mail in the thread.   
  
But some people are not using Gmail for good reasons.   
  
The other problem with gigantic threads at python-dev is that they
often end up in a tree of several sub-threads, making it very hard to
follow what's going on if you don't sort mails by threads in your
client. And again, this is not possible in some mail clients.   
  
I was very frustrated about this problem on gigantic threads about
Distutils because I was seeing people "lost" in a branch of the thread,
asking questions that were answered at the other end of the tree.   
  
So how could we improve on this ?   
  
Imho, mail threads are not suited for design discussions. I think a way
to improve the situation could be to link mails by keywords.   
  
Everytime you answer a mail, instead of quoting some of its text, you
provide some keywords related to the topic you want to discuss, and you
just type a plain answer. Your answer and the original mail will then be
linked through a semantical relation, like a RDF triplet. These keywords
could be new headers in the mail that is sent.   
  
Let's imagine all mail client are able to sort and browse the threads
by keywords, and to list the used keywords on the side of the thread.
Meaning that everytime you send a mail, you can pick one of the keyword
that was already used, to limit the number of keywords.   
  
Does that make any sense ?
