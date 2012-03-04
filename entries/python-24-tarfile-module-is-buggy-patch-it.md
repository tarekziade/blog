Title: Python 2.4: tarfile module is buggy, patch it !
Date: 2008-06-19 00:44
Category: plone, python, zope

I have encoutered really bad bugs in some Python 2.4 applications (Zope
based) using the *tarfile* module. For instance, the
*TarFile.getmembers* method that returns the files a tar file contains
will just fail to return all files ...   
  
Hopefully Zope will work under Python 2.5 sometimes. This is a work in
progress in GSOC if I recall it correclty, but I am not sure of the
current state.   
  
Until then I just stick Python 2.5 module in my packages. It seems to
work fine (tests pass :D) after a few changes as it is isolated from the
rest of Python.   
  
If you want to do it as well, there are only two changes to make it
work under Python 2.4, to introduce 3 new constants in *os* module and
to get rid of a syntax that does not work under 2.4:   
   $ diff /opt/local/lib/python2.5/tarfile.py tarfile.py

  
   46a47,49

    >

    > os.SEEK_SET, os.SEEK_CUR, os.SEEK_END = range(3)

    >

    1070c1073,1076

    <         self.name = os.path.abspath(name) if name else None

    ---

    >         if name:

    >             self.name = os.path.abspath(name)

    >         else:

    >             self.name = None
