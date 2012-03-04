Title: Testing code that calls third party servers
Date: 2007-10-05 10:03
Category: plone, python, quality, zope

One of the fundamentals of unit testing is that **the unit test should
never depend on any external resource**. This is true for all data that
might be needed to run the tests, but also for third party servers like
LDAP or SQL: they have to be faked.   
-   **LDAP** is quite painful to fake. The simplest way is to create all
    tests with a real LDAP server, then replace it with a class that
    returns explicit responses for each explicit request. This is
    managable when the LDAP layer is well done, and easy to patch.
-   **Mailhost** is also quite easy to patch in the test fixture, and
    printing back the mail sent instead of calling the smtplib will
    allow you to write doctests and unittest without depending on a smtp
    server through telnet.
-   For **SQL**, the simplest way, as long as you use a library that
    knows how to call different DBs through [DBAPI][], is to use a flat
    file DB system. I use [sqlalchemy][], and patching it in my test
    fixtures is easy as patching one line: the sqluri. For example,
    *'**mysql://user:pass/server/base'*** will become
    **'*****pysqlite:///path/to/package/tests/data/test.db'**. *The
    tests then interact with a [SQLite][] file, and as long as your code
    uses sqlalchemy APIs, everything should work like if the DB was
    MySQL or Postgres. The only difference I can think of is the DB
    unicode settings, that might be different in the production server,
    so be careful in your doctest when you test strings.
-   For other third party elements, [Mocking][] can help !

  [DBAPI]: http://www.python.org/dev/peps/pep-0249/
  [sqlalchemy]: http://www.sqlalchemy.org/
  [SQLite]: http://www.sqlite.org/
  [Mocking]: http://theblobshop.com/pymock/
