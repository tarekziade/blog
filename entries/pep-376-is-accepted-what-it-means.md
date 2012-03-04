Title: PEP 376 is accepted -- What it means 
Date: 2010-04-26 12:30
Category: python

[PEP 376][] has just been accepted. This is a very important step in the
packaging work we have been doing during the last year.   
  
This PEP introduces a database of installed distributions, and
therefore a standard that allows interoperability among all tools.   
  
To summarize, a distribution that gets installed will have to create a
***.dist-info*** directory in Python, containing these files:   
-   **METADATA**: contains the project metadata, as described in [PEP
    345][], [PEP 314][] and [PEP 241][].
-   **RECORD**: records the list of installed files
-   **INSTALLER**: records the name of the tool used to install the
    project
-   **REQUESTED**: the presence of this file indicates that the project
    installation was explicitly requested (i.e., not installed as a
    dependency).

  
Python will provide in the ***pkgutil*** module, [a set of APIs][]that
can be used to query installed projects. This ressembles a lot to what
the Setuptools project currently provides with its **pkg\_resources**
module.   
  
An interesting side-effect of the ***RECORD*** file is that package
managers will be able to uininstall projects. As a matter of fact
Distutils2 will provide a basic uninstall feature on the top of the
***pkgutil*** APIs, and I hope tools like Pip (that already provide this
feature) will adopt the new standard.   
  
This small PEP is the basis to a new PEP that is coming next, which
will define a standard to describe and consume resource files in Python
projects. The ultimate goal will be to be able to get rid of
***setup.py*** and describe everything in static configuration files in
your project. But this is another story ;)   
  
Thanks to all people involved in this PEP, and in particular, thanks to
Philip J. Eby for his help (PEP 376 is massively based on what he has
created in Setuptools.)

  [PEP 376]: http://www.python.org/dev/peps/pep-0376
  [PEP 345]: http://www.python.org/dev/peps/pep-0345
  [PEP 314]: http://www.python.org/dev/peps/pep-0314
  [PEP 241]: http://www.python.org/dev/peps/pep-0241
  [a set of APIs]: http://www.python.org/dev/peps/pep-0376/#new-functions-and-classes-in-pkgutil
