Title: Unobtrusive benchmark and debug of Python applications
Date: 2007-10-18 21:00
Category: plone, python, quality, zope

  
There are many tools available for Python to perform benchmarks and
debugging. For example:

  
  
-   [Hotshot][] is bundled in the standard library and provide useful
    data. Maybe you have to install an extra package on some linux
    distribution if I recall it correctly, because it's not GPL;
-   [iPython][] provides a nice interface to perform live debugging,
    like automatic invocation of pdb on exceptions;
-   the standard module test provides pystone, that let you benchmark
    the computer in use before the timed tests. This is helpfull to
    bench the code on several computers: the measurements can be
    expressed in in pystones. In other words, you are able to have a
    reproducable measure of a piece of code and work on the code
    complexity to make it faster. In reality, any interference can
    change the results, but this is true as well for time measures.
-   all big python frameworks are using the logging module, so it's easy
    to hook in it if extra logging is needed.

  
But when trying to equip an application in order to find out why some
functionalities are slow, or why something goes wrong, it's not always
easy to set up precisely what you want to log if something is slow or
what your want to hook if a bug appears. The simplest way is to call out
all the mentioned tool from the code, but it too obtrusive. Another way
is to use decorators.   
  
To perform it, you'll have to:   
-   get and install [iw.quality][]
-   create the benchmarking or debugging module

  
# Get and install iw.quality

  
iw.quality gathers helpers for QA. It has an implementation of the
Levenshtein distance [discussed earlier][], and now a decorator used for
benchmarking and debugging purpose. Since it's available in PyPi, you
should be able to install it like this:   
  
  
   $ easy_install iw.quality

  
  
  
See [setuptools informations][] if you need to install easy\_install
itself.   
# Preparing the benchmark or the debugging

  
Whether you are about to benchmark or debug your program, you need to
list all the places in your code where you need to hook a log or a pdb.
Then you can create a specialized python module that can be used when
needed. This module will simply decorate the functions you want to work
with.   
## Benchmarking

  
Here's an example, let's equip sqlalchemy for benchmarking.   
  
benchmarking.py file:   

    #

    # benchmarking queries

    #

    from iw.quality.decorators import log_time

    import sqlalchemy



    def logger(msg):

        print msg



    simple_logger = log_time(logger=logger)



    sqlalchemy.create_engine = simple_logger(sqlalchemy.create_engine)

    sqlalchemy.engine.Engine.execute = simple_logger(sqlalchemy.engine.Engine.execute)

  
  
The log\_time decorator comes with a few parameters, like logger wich
is called with the log message. By default it uses logging.info, but you
can use your own like in the example. The chosen functions are then
decorated.   
  
Let's use it:   

    >>> import benchmarking      # applies the decorators

    >>>from sqlalchemy import *



    >>> db = create_engine('sqlite:///:memory:')

    log_time::2007-10-18T21:50:52.352037::0.013::function 'create_engine',args: ('sqlite:///:memory:',), kw: {}

    >>> db.execute('create table TEST(id int)')log_time::2007-10-18T21:52:13.761085::0.104::function 'execute', args:

    (<sqlalchemy.engine.base.Engine object at 0x12e6e90>, 'create tableTEST(id int)'), kw: {}

    <sqlalchemy.engine.base.ResultProxy object at 0x12e6ff0> 

    >>> db.execute('insert into TEST (id) values (1)')

    log_time::2007-10-18T21:52:50.265860::0.000::function 'execute', args:(<sqlalchemy.engine.base.Engine object at 0x12e6e90>, 'insert into TEST

    (id) values (1)'), kw: {}<sqlalchemy.engine.base.ResultProxy object at 0x12f50d0>

  
  
  
If you need to display more infos on the call, you can use your own
formatter instead of the provoded one. Let's extend the benchmark file:
  
  
  

    def formatter(execution_time, function, args, kw):     

        return '%s = %.3f ms' % (function, execution_time)



    simple_logger = log_time(logger=logger, formatter=formatter)

  
  
  
And rerun some code:   
  
  

    >>> from sqlalchemy import *

    >>> db = create_engine('sqlite:///:memory:')

    <function create_engine at 0x12328b0> = 0.014 ms

  
  
  
You can add a treshold on the function timing, to log only functions
that are up to this treshold. This is useful to filter a bit.

  
  
## Debugging

  
For debugging purpose, you can use the debug parameter:   
  

    def debug(e):    

        import pdb

        pdb.set_trace()



    simple_logger = log_time(logger=logger, formatter=formatter,

                             debugger=debug)

  
  
It will be called in case of an Exception:   

    from sqlalchemy import *



    db = create_engine('gcckc')

    --Return--

    /Users/tziade/tests/benchmarking.py(14)debug()

    (Pdb) c

    /Users/tziade/tests/banchmarking.py(10)logger()

    (Pdb) c

    function create_engine at 0x12328f0> = 3.544 ms



    Traceback (most recent call last):...



    raise esqlalchemy.exceptions.ArgumentError: Could not parse rfc1738 URL from string 'gcckc'

  
  
# Conclusion

  
By using this simple decorator, it's easy to group benchmarking and
debugging in a specialized module, and generate custom reports. The best
practice is to create a module per each use case. I didn't hook it on
Hotshot or other utilities to let people use the tools they like.   

  [Hotshot]: http://docs.python.org/lib/module-hotshot.html
  [iPython]: http://ipython.scipy.org/
  [iw.quality]: http://pypi.python.org/pypi/iw.quality
  [discussed earlier]: http://tarekziade.wordpress.com/2007/10/08/make-your-code-base-healthier-the-anti-cheater-pattern/
  [setuptools informations]: http://peak.telecommunity.com/DevCenter/setuptools
