Title: A simple self-upgrade build pattern
Date: 2011-02-10 17:21
Category: mozilla, python

Bootstrapping is useful.   
  
For example, we use it to build in-place our applications at Mozilla
Services, to develop them. When the developer runs "make build", a
Python script is invoked, and makes sure all the Python packages we are
developing are checked out locally, and tied to the execution
environment.   
  
In the Python community you have similar tools like zc.buildout
combined with [mrdeveloper][], or Pip's [requirements][]. Although, our
script does Mozilla-specific things, like allowing to update the
dependencies at specific tags via command-line options, or at the
*"latest stable tag"*.   
  
Anyways, back to bootstrapping.   
  
Having such scripts is great, but maintaining them across all projects
is painful. Since the script is the first thing the build runs, it
cannot have an external dependency so it has to be completely
independent. So you have to copy it around, in all your projects, and
that leads to maintenance hell.   
  
One solution is to add a self-upgrade feature to the script, so it
tries to get the latest version online before it is run. zc.buildout has
such a self-update feature, that will make sure it's at the latest
version. Although, the implementation of this feature is a bit odd. 1/
you cannot run the bootstrap script if you're offline. 2/ on upgrades,
zc.buildout restarts itself. I don't think 2/ a robust approach and I
recall that it had some bugs under Windows in the past (updating files
that your own program is using might fail).   
  
So, since I was working in the tools-for-Mozilla-Services area, I added
a self-upgrade feature and tried to isolate a simple mechanism for this.
A pattern that would let us publish fresh versions of some scripts in
our server and make it easy for our tools to use them.   
  
An efficient bootstrap script should:   
-   be able to run offline, so the app can be built even if it's unable
    to check for the latest online version
-   be able to upgrade itself with a newer version
-   upgrade itself without having to restart itself
-   be completely independent -- besides a vanilla Python

  
The pattern I have used is as follows:   
-   The bootstrap script is an empty shell that is just responsible to
    update a second script that contains the real bootstrapping code,
    then dynamically import it via an *\_\_import\_\_*, and run it.
-   The server that publishes the real bootstrap script returns an ETag
    header with it, and supports the If-None-Match header.
-   The bootstrap script is able to ask the server if the online version
    is newer, by using the ETag value it has from the previous update in
    the If-None-Match header. If the online version is unchanged, the
    client receives a 412 code (Precondition failed).

  
The code has no dependencies besides Python.   
  
Extract from the client-side code:   
   import os

    import sys

    import urllib2



    def main():

        # getting the file age

        if os.path.exists('._build.etag'):

            with open('._build.etag') as f:

                current_etag = f.read().strip()

            headers = {'If-None-Match': current_etag}

        else:

            headers = {}

            current_etag = None



        request = urllib2.Request('http://moz.ziade.org/_build.py',

                                  headers=headers)



        # checking the last version on our server

        try:

            url = urllib2.urlopen(request, timeout=5)

            etag = url.headers.get('ETag')

        except urllib2.HTTPError, e:

            if e.getcode() != 412:

                raise

            # we're up-to-date (precondition failed)

            etag = current_etag

        except urllib2.URLError:

            # timeout error

            etag = None



        if etag is not None and current_etag != etag:

            # we need to update our version

            _rename('_build.py')

            content = url.read()

            with open('_build.py', 'w') as f:

                f.write(content)



            with open('._build.etag', 'w') as f:

                f.write(etag)



        # we're good, let's import the file and run it

        mod = __import__('_build')

        project_name = sys.argv[1]

        deps = [dep.strip() for dep in sys.argv[2].split(',')]

        mod.main(project_name, deps)



    if __name__ == '__main__':

        main()

  
Extract from the server-side code:   
   import os

    import mimetypes

    from hashlib import md5

    from wsgiref.simple_server import make_server



    # where the served files are located ?

    _DIR = '.'



    def application(environ, start_response):

        if_none_match = environ.get('HTTP_IF_NONE_MATCH', '')

        path = environ['PATH_INFO']

        path = path.lstrip('/')



        if path.startswith('.') or '/' in path:

            # looks like a bad path -- or a potential security thread

            status = '400 Bad Request'

            headers = [('Content-type', 'text/plain')]

            start_response(status, headers)

            return "Invalid Request"



        path = os.path.join(_DIR, path)



        if not os.path.exists(path):

            # unknown file

            status = '404 Not Found'

            headers = [('Content-type', 'text/plain')]

            start_response(status, headers)

            return "File not found"



        # we're good, let's look at the file age

        etag = '"%s"' % md5(str(os.stat(path).st_mtime)).hexdigest()

        if etag == if_none_match:

            # same file

            status = '412 Precondition failed'

            headers = [('Content-type', 'text/plain')]

            start_response(status, headers)

            return ''



        content_type = mimetypes.guess_type(path)

        status = '200 OK'

        headers = [('Content-type', content_type[0]),

                   ('ETag', etag)]



        start_response(status, headers)



        with open(path) as f:

            content = f.read()



        return content



    if __name__ == '__main__':

        httpd = make_server('', 5000, application)

        print "Listening on port 5000...."

        httpd.serve_forever()

  
The server is a plain Python wsgi script that is easy to hook in Apache
or Nginx, to serve a directory of files. It should be safe enough as
long as the served directory is isolated from the rest of the system. I
did not try that hard to secure it, but it makes sure you can't leave
the directory.   
  
***EDIT**: as noted in the comments, Nginx and Apache provides such
ETag features, so you can just configure it to serve static files this
way. I did a wsgi script as an initial prototype and to demonstrate what
the server does, and I kept it because it's easy to run or hook into any
web server. And I will probably add more features next there.*   
  
Now the bootstrap script we use can live in its own repository, and get
bug fixes and features, that will be automatically propagated to all our
applications.   
  
Do you solve this issue differently ? I am curious to get some feedback
on this.

  [mrdeveloper]: http://pypi.python.org/pypi/mr.developer
  [requirements]: http://pip.openplans.org/requirement-format.html
