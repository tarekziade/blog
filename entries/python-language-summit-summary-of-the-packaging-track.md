Title: Python Language Summit -- Summary of the packaging track 
Date: 2010-02-18 19:03
Category: python

Here are quick wrapup on what has been said during the packaging session
in the language summit that is happening today at Pycon.   
  
The four major points are:   
1.  The implementation of the accepted PEPs that have been done lately
    will not happen in Distutils but in a new package in the Distribute
    project (so logically in a "distribute" package). This resolves
    backward compatibility issues: new features will be under the
    "distribute" namespace.
2.  Distribute will stay a third-party package and will be integrated in
    the standard library once it has enough support and feedback from
    the community. So this could happen in 3.3 (or 2.8 ;) ). Some part
    that are useful for the existing distutils package might be added in
    the stdlib today. But the idea is to stop adding features in
    distutils and focus on distribute.
3.  The Hitchhicker's guide to packaging is going to be moved into the
    Python repository, so it becomes part of docs.python.org. It's not
    finished yet but it'll grow there.
4.  Ian threw the idea to have virtualenv as a core feature, but he's
    not sure how yet. Some brainstroming on this should happen during
    Pycon.

