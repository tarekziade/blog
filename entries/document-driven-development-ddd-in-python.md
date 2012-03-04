Title: Document-Driven Development (DDD) in Python
Date: 2007-01-06 23:04
Category: pycon, python, quality

Test-Driven Development is widely used in the Python community to create
quality software. The benefits of such approach is not to be proved
anymore. It creates better software by :   
-   preventing *regression*
-   making the developers actually *think* about what they write
-   providing a real help for newcomers : unit and functional tests are
    showing how the code was made and how it has to be used.
-   ...

  
Python has brought a real enhancement to test-driven developement with
doctests. They allow developer to write documentation with embed code
examples that can be run for real. This allows a team to integrate
documentation in the development cycle and to replace most of their
tests with documents that are always up to date: documents become tests.
  
  
In the meantime, documentation has always been the black beast of
developers. They hate writing it and most of the time, a software
project website is never up to date if there's no one dedicated to this
task. For open source projects, the website is the most important media
and should always reflect to what is happening in the code base.   
  
**doctests can resolve this problem by automating documentation
creation at all level **   
  
I have used this principle to create a *Document-Driven Developpement*
(DDD) approach, which provides to a project team a way to automate the
update the project website : each commit on the code base calls a script
that generates on the fly html pages for:   
-   the api
-   the glossary for the project
-   documents for all important modules
-   tutorials
-   recipes
-   ...

  
This method will be fully explained at my [PyCon Tutorial (February,
22th)][].   
  
I will published by then the script that automates the creation of the
website, using a subversion repository that follows a few guidelines (in
its content and structure).   
  
Can't wait to be there !

  [PyCon Tutorial (February, 22th)]: http://us.pycon.org/TX2007/TutorialsAM#AM6
    "pycon"
