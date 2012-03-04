Title: Indexation service with Xapian
Date: 2007-06-12 15:39
Category: django

In a previous [post][] on my french Blog, I was explaining how to use
[Xapian][] from its Python binding, to index text content for documents.
The idea was to use the indexing part of Xapian and not to store any
data in the documents.When I started to hook my code into my Django
application, I realized it was not very robust, because I had to open
only one Xapian connector to index content. This was not easy to do and
depends a lot on how the web framework loads the code. Furthermore, the
website had to take care of launching threads to avoid waiting for the
indexation to be finished.   
  
I rewrote the tool to avoid these issues, by decoupling indexation and
queries: when the website needs an indexation, it writes the data into a
special table in a SQL database. On the other side, a thread in a
separated process (eg a worker) reads this table and launch indexations
when it finds lines in it. This producers-consumer pattern makes the
solution very fast and simple.   
  
It is better to perform this kind of pattern than a solution like a
live server, based for example on XML-RPC, because it is more robust:   
-   if any part of the application crashes, the work in process is not
    lost in the SQL database;
-   if the indexer program crashes, the website can still query the
    Xapian database.

  
Queries are made with read-only Xapian connectors, which can be used
concurrently with no problems.   
  
These were the changes I made:   
-   A sqlite database is used to store indexation queries in a table
    (since it's based on [SQLALchemy][], postgres or mysql can be used
    as well);
-   a thread scans the table to pick its work and delete rows when its
    done;
-   the search API launches standalone and read-only Xapian connectors
    to perform each search.

  
When documents are modified and added on the website, a query is made
on the database. This is done through the Django event framework wich
allows to hook code on events like "A document was created". (explained
here: [http://www.mercurytide.com/whitepapers/django-signals/][])   
  
The package I wrote can be used this way:   
-   The thread in charge of indexations is launched via the *run.py*
    script
-   the *searcher* and *indexer* modules can be used to work with the
    API

  
Here's the complete doctest of my package, which provide examples on
how to use these API:   
~~~~
{style="border:1px solid black;background-color:#efefef;font-size:10pt;padding:4px;"}

=======

indexer

=======



The indexer provides:



- client-side modules : API for client to ask for indexations and query the

Xapian database. When an indexation is asked, it is stored in a sql

database;



- server-side application: a standalone thread that indexes what has been

asked by reading the sql database.



Let's import the modules used by the client-side::



>>> import indexer

>>> import searcher



Let's reset the SQL DB first::



>>> indexer.reset()



Let's also reset the Xapian DB::



>>> from xapindexer import force_reset

>>> force_reset()



The Xapian DB should be empty now::



>>> searcher.corpus_size()

0



Indexation

==========



Each indexable content has a unique id, and a text to index::



>>> uid = '1'

>>> text = 'my taylor is not rich anymore'



Let's index it::



>>> indexer.index_document(uid, text)



Another one::



>>> indexer.index_document('2', 'pluto is a dog')



Let's start the worker that is in charge of asynchronous indexation::



>>> from xapindexer import start_server

>>> start_server()



Let's wait a bit so the worker has the time to read the SQL Database

and do the work::



>>> import time

>>> while indexer.is_working():

...     time.sleep(0.2)



`is_working` looks in the SQL DB if there is some work left.



The Xapian DB has two documents now::



>>> searcher.corpus_size()

2



Searching

=========



Let's search now, with `searcher`. Operator is AND by default::



>>> res = searcher.search('rich')

>>> list(res)

['1']

>>> res = searcher.search('pluto')

>>> list(res)

['2']

>>> res = searcher.search('dog')

>>> list(res)

['2']

>>> res = searcher.search('rich dog')

>>> list(res)

[]



Or operator::



>>> res = searcher.search('rich dog', or_=True)

>>> res = list(res)

>>> res.sort()

>>> res

['1', '2']



We have an API to detect if a document is present::



>>> searcher.document_exists('2')

True

>>> searcher.document_exists('ttt')

False



And another one to retrieve indexed terms::



>>> list(searcher.document_terms('2'))

['dog', 'is', 'pluto']



Reindexation

============



The document can also be reindexed::



>>> indexer.index_document('2', 'pluto is a cat')

>>> indexer.work_in_process()

([2], [])



Let's wait a bit::



>>> while indexer.is_working():

...     time.sleep(0.2)



Let's make sure the document has been reindexed::



>>> list(searcher.document_terms('2'))

['cat', 'is', 'pluto']



Then check the indexation has changed::



>>> res = searcher.search('rich dog', or_=True)

>>> list(res)

['1']



Or deleted::



>>> res = searcher.search('pluto')

>>> list(res)

['2']

>>> indexer.delete_document('2')

>>> while indexer.is_working():

...     time.sleep(0.2)

>>> res = searcher.search('pluto')

>>> list(res)

[]
~~~~

  
The complete code is here :
[http://hg.programmation-python.org/browser/xap][][][]   
  
It is not packaged yet, but can be used to provide an indexation
service for a website or any other application.

  [post]: http://programmation-python.org/sections/blog/2007_06_07_indexation-facile-rapide
  [Xapian]: http://xapian.org
  [SQLALchemy]: http://www.sqlalchemy.org/
  [http://www.mercurytide.com/whitepapers/django-signals/]: http://www.mercurytide.com/whitepapers/django-signals/
  [http://hg.programmation-python.org/browser/xap]: http://hg.programmation-python.org/browser/xap
  []: http://hg.programmation-python.org/repositories/public/
