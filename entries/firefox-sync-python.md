Title: Firefox Sync Server is now 100% Python
Date: 2011-07-12 12:36
Category: mozilla, python

Two weeks ago, we pushed the last bit of the Python Sync Server in
production, and there's no more PHP.   
  
For the client-side it's not changing anything, since the Python server
is just a re-write of the existing PHP server.   
### Lessons learned

  
The first push we did of the storage part on that week went really bad
and we had to rollback urgently, fix the problems and push it back a few
days later.   
  
The main problem we had in production was related to the MySQL driver
we used in conjunction with [Gunicorn][] and [GEvent][]. We picked
[PyMySQL][] because we wanted GEvent's ability to monkey patch the
socket module -- using MySQL-Python would have been useless for this
since it uses C code.   
  
When you use Gevent workers with GUnicorn, sockets become automatically
cooperative and you can handle more parallel requests that are waiting
for data from the SQL server. [Read more about this here][].   
  
And that's exactly what the Sync server is: a thin layer of web
services on the top of a database, sending requests and waiting for the
results.   
  
PyMySQL was working fine in our load tests and in staging. We were
happily pushing the load and had slightly better performances than the
PHP stack.We were not expecting a huge difference since most of the time
(I'd say around 80%) is spent waiting for the SQL server and the Python
server is using the same database.   
  
But the main difference is that the Python stack stays persistent in
memory, so we can pool connectors and avoid recreating TCP connections
for every request. I don't have any hard numbers yet, as we're
collecting them, but we've definitely reduced the time taken by our web
services in those 20% spent outside the SQL server.   
  
**But.**   
  
But as soon as we pushed in production, everything started to lock.
Some queries were just hanging and incoming requests were piling up
until we were unable to cope with the load.   
  
What happened is that PyMySQL is using ***socket.send()*** to send data
to the MySQL server, without checking that all the bytes were really
sent. And on high load, with Gevent, doing this will not work anymore
because you're not necessarily sending all bytes at once. The API to be
used is ***send.sendall()*** to make sure everything is sent.   
  
Here's an extract of the doc for **send()**:   
> `socket.send`(*string*[, *flags*])
>   ~ Send data to the socket. The socket must be connected to a remote
>     socket. The optional *flags* argument has the same meaning as for
>     [`recv()`][] above. Returns the number of bytes sent. Applications
>     are responsible for checking that all data has been sent; if only
>     some of the data was transmitted, the application needs to attempt
>     delivery of the remaining data.

  
And for **sendall()**:   
> `socket.sendall`(*string*[, *flags*])
>   ~ Send data to the socket. The socket must be connected to a remote
>     socket. The optional *flags* argument has the same meaning as for
>     [`recv()`][] above. Unlike [`send()`][], this method continues to
>     send data from *string* until either all data has been sent or an
>     error occurs. `None` is returned on success. On error, an
>     exception is raised, and there is no way to determine how much
>     data, if any, was successfully sent.

  
As soon as we've changed the code in the driver, (PyMySQL's author was
told about this, and the tip is now fixed. [Also there's the same
problem in MyConPy it seems..][].) everything went smoothly.   
  
So the question you're probably wondering is: why didn't we caught this
issue in our load test environment ? The reason is that our load test
script was not asserting all the responses the web server was returning,
and we did not detect those errors and the locked queries were basically
timing out in a mass of normal behavior. They "came back" as valid. The
load test infrastructure, while filled with hundreds of thousands of
fake users' data, has less databases than in production so this kind of
issue is not bubbling up as hard. While our load test infrastructure is
very realistic, it will never be exactly like production.   
  
The other thing is that the Grinder outputs raw data and we just used
the Query Per Second indicator. I suspect we would have caught this
issue with Funkload because it provides some results diagrams were you
can see things like min and max.   
  
So the main lessons learned here are:   
-   make sure the load test scripts assert all the responses (status +
    content)
-   make sure your load testing tools detect any abnormal behavior --
    like a very very long request, even if it's a fraction in a mass of
    normal behavior

  
I am very thankful to the Services Ops team, and in particular Pete who
drove the production push. These guys rock.   
### What's next

  
Now that everything works well, there are a few things we need to tweak
in order to have a better system:   
-   [Kill pending queries when a Gunicorn worker is restarted][]
-   See if we can cache a few LDAP calls
-   See if we can use several GUnicorn servers behind one Nginx -- the
    CPU is under-used.

  
But overall, I hereby declare the Python push as a success.

  [Gunicorn]: http://gunicorn.org/
  [GEvent]: http://gevent.org/
  [PyMySQL]: http://code.google.com/p/pymysql/
  [Read more about this here]: http://gevent.org/intro.html#monkey-patching
  [`recv()`]: http://docs.python.org/library/socket.html#socket.socket.recv
    "socket.socket.recv"
  [`send()`]: http://docs.python.org/library/socket.html#socket.socket.send
    "socket.socket.send"
  [Also there's the same problem in MyConPy it seems..]: https://bugs.launchpad.net/myconnpy/+bug/711520
  [Kill pending queries when a Gunicorn worker is restarted]: https://bugzilla.mozilla.org/show_bug.cgi?id=668664
