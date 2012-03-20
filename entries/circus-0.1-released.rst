Circus 0.1 released
###################

:date: 2012-03-20 21:55
:tags: python, mozilla
:category: python
:author: Tarek Ziade

.. image:: http://dl.dropbox.com/u/8617023/circus.png

.. note:: 

   Circus is a program that will let you run and watch multiple processes.
   Like Supervisord, BluePill and Daemontools.

We wanted to release a first version of Circus *before* Pycon
originally. Then Pycon was here, so we decided we would release
it before Pycon would end. And Pycon ended. And we had a few bugs
to fix.

But today it's happening !

Circus 0.1 is an alpha release, don't use it in production yet !

But this first release contains a lot of stuff already:

- a pub/sub channel so you can monitor what's going on.
- *circusctl* : an amazing console script that let you interact
  with the system.
- a full documentation for the *circusctl* CLI.
- an API that's simple enough in most cases.
- ... many more things really. I had to stop Benoit from adding
  features ;) -- did I mention that Benoit is amazing ?

I also added a section on how Circus is different from other tools here:
http://circus.readthedocs.org/en/latest/index.html#why-should-i-use-circus-instead-of-x ,
since a lot of people asked about it.

One very important feature for me is to be able to use Circus with 
a few lines of Python in a program that needs to spawn workers. The use case
for me is to run **Powerhose**, a library that let you dispatch some tasks
across several workers, no matter what language they're built with.

This is all it takes to run and maintain 4 workers::

    from circus import get_arbiter

    arbiter = get_arbiter("worker", 4)
    try:
        arbiter.start()
    finally:
        arbiter.stop()


Links:

- the doc: http://circus.readthedocs.org/en/latest/index.html
- the release: http://pypi.python.org/pypi/circus/0.1
- the repo: https://github.com/mozilla-services/circus

Please let us know what you think !
