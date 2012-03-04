Title: Eight tips to start with Python
Date: 2007-09-24 07:56
Category: python

A friend of mine is starting Python. I tried to sum up some tips for
him, that may be useful to others. Don't hesitate to comment it if you
think something important is missing.

  
  
1.    
   **Get the best online documentation**.

      
      
    There are a few online documentation you must read:   
   -   the [official tutorial][], that gives you a quite complete
        overview of Python;
    -   the standard library [module index][]. You can download it to
        simplify the search through greps. This is the documentation you
        get through the help command in the prompt.
    -   Active State's [Python Cookbook][]. There are thousands of code
        snippets that are created, ranked, categorized and commented by
        developers.
    -   [Dive Into Python][] online book, that makes you discover Python
        features through well thought examples.

      
2.    
   **Read [PyCon][], [EuroPython][] and [Pycon UK][] wrapups and
    slides**.

      
      
    They are the three main Python events, and a lot of things are
    happening there. You'll learn a lot by reading the talks slides. If
    you can go there, it's even better: sprints, bird of feathers and
    lighting talks are organized. To convince your boss to send you
    there, you could make a talk proposal "My first steps in Python" ;)
3.    
   **Suscribe to the right feeds**.

      
      
   -   The mainstream is [Planet Python][]. It gathers most of the
        blogs out there, so it is the best place to start.
    -   [Reddit's Python][] is a great place to get the hot topics.
    -   Pythonware's [Daily Python URL][]. Human-filtered feed. It used
        to provide several dozains of links per week, but it seems to
        have slowed down, and provides a few links a week now. I think
        it's better this way.

      
4.    
   **Learn and use the rising standards**.

      
      
    There are a few libraries that have a deep impact on the way people
    write and distribute their work:   
   -   [setuptools][]: helpers to build and distribute your code
        [eggs][]. A public repository à la Perl's CPAN called
        [Cheeseshop][] is wired with this library so people can
        distribute their code there. It's one of the major innovation of
        last years in Python world in my opinion.
    -   [sqlalchemy][]: The [ORM][] that is now used by the majority of
        Python frameworks. Its flexibility is impressive. I think there
        is no equivalent tool in any other language (please let me know
        if there is);
    -   [Python paster][]. This tool allows you to create templates that
        can be used to generate skeletons for your code. It is used by
        many web frameworks to provide people a simple way to generate a
        standardized boiler-plate code canvas when they start up
        something. This is done in Java for quite a long time (you
        cannot do without it in Java, otherwise it would take you years
        to write any program ;)), and tools like [PyDev][sqlalchemy] and
        Eclipse would provide the canvas to do similar things. But the
        paster is independant from any IDE;
    -   [reStructuredText][]: learn how to use it. It's our LaTeX. Your
        code documentation should use it.

      
5.  **Ask for help**. The three places you can get some help are:   
   1.  the [mailing list][]
    2.  the irc channel \#python on freenode.
    3.  [the tutor mailing list][]. Mihai Campean says: *"This is a list
        specifically for those new to Python and those interested in
        helping people learn the language, and the atmosphere is very
        friendly. It’s probably a better place to start than
        python-list, in my opinion"*

      
    There are some talented guys that dedicate their free time to help
    newcomers.
6.    
   **Try to adapt your successfull code patterns**.

      
      
    When I started Python, I tried to adapt what I used to do with the
    tool I mastered then (Delphi). Since There should be one-- and
    preferably only one --obvious way to do it. (try import this in a
    prompt), that helped me a lot to learn and understand all the
    subtles of Python on use cases I mastered.   
    The most pleasant thing about it is that you quickly drop all
    Python books and guide to work with the language, unlike Java for
    example, where you need to keep many reference books on your desk.
7.    
   **Share on your experience and participate !**.

      
      
    A newcomer (yeah! fresh blood!) experience is a highly valuable
    material for the language advocacy: the discovering state of mind
    sometime reveals weaknesses or absurdities experienced users don't
    see anymore. Furthermore, fresh new ideas are often brought by
    people that comes from other communities. If you feel that something
    is absurd, unclear or wrong, you should start a thread on the
    language mailing list. If you have an idea onany kind of
    enhancement, maybe it worth a [Python Enhancement Proposal][].
8.    
   **Watch what is being done in Python 3, PyPy and web frameworks**

      
      
    [Python 3][] is the next version of Python, [PyPy][] is Python
    written in Python. Web frameworks like [Django][] or [Zope][] are
    large Python codebases. These three sub-communities have something
    in common: they form the R&D of the language.   
    Zope for example, has enhanced a lot setuptools and doctest through
    a massive feedback. Keeping an eye on them even if you don't use
    them will make you live and understand what rises in the language.   
    PyPy is an amazing project. Even if you don't understand everything
    (Python in Python ? what the... ;)), seeing one of Armin Ringo talks
    will give you an instructive high level view of Python. Now for
    Python 3, even if you cannot read and understand all threads in the
    dedicated mailing list, keeping an eye of Guido's wrapups and thread
    subjects will help you to do the jump on P3k, and probably make your
    Python 2 code look nicer.

  [official tutorial]: http://docs.python.org/tut/tut.html
  [module index]: http://docs.python.org/modindex.html
  [Python Cookbook]: http://aspn.activestate.com/ASPN/Python/Cookbook/
  [Dive Into Python]: http://www.diveintopython.org
  [PyCon]: http://us.pycon.org/2008/about
  [EuroPython]: http://europython.org/
  [Pycon UK]: http://www.pyconuk.org
  [Planet Python]: http://planet.python.org/
  [Reddit's Python]: http://www.reddit.com/r/Python/
  [Daily Python URL]: http://www.pythonware.com/daily
  [setuptools]: http://peak.telecommunity.com/DevCenter/setuptools
  [eggs]: http://peak.telecommunity.com/DevCenter/PythonEggs
  [Cheeseshop]: http://cheeseshop.python.org/pypi/
  [sqlalchemy]: http://sqlalchemy.org
  [ORM]: http://en.wikipedia.org/wiki/Object-relational_mapping
  [Python paster]: http://pythonpaste.org/
  [reStructuredText]: http://docutils.sourceforge.net/rst.html
  [mailing list]: http://mail.python.org/mailman/listinfo/python-list
  [the tutor mailing list]: http://www.python.org/mailman/listinfo/tutor
  [Python Enhancement Proposal]: http://www.python.org/dev/peps/
  [Python 3]: http://en.wikipedia.org/wiki/Python_3
  [PyPy]: http://codespeak.net/pypy/dist/pypy/doc/news.html
  [Django]: http://djangoproject.org
  [Zope]: http://zope.org
