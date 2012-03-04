Title: Distutils : improved .pypirc for Python 2.7 and 3.1
Date: 2009-01-09 08:30
Category: distutils, python

When you launch such a command:   
   $ python setup.py register sdist upload

  
There's no way to give to Distutils your PyPI password in the prompt,
so you distribution is uploaded to the server. You have to store your
password in the *.pypirc* file:   
       [distutils]

        index-servers =

            pypi



        [pypi]

        username: <username>

        password: <password>

  
The password is stored in clear text, so it can be used by Distutils to
authenticate. This is rather unsecure, since anyone who has a read
access to your home can get your password.   
  
I have detected this problem this summer while listing the possible
enhancements in Distutils. Nathan Van Gheem sent me a mail a month ago
to ask for that same feature in [collective.dist][]; which is a port of
the latest Distutils features into Python 2.4 so Zope can use them. So
before having it into collective.dist, the first step was to introduce
it into Python itself.   
  
The idea is to be able to remove from *.pypirc* the password so it's
asked at the prompt. Nothing fancy here : the Distribution object that
is created before you launch any command is the place where you can
share a context between commands.   
  
So when you launch:   
   $ python setup.py register sdist upload

  
Here's what is happening:   
1.  **register** looks into *.pypirc*, if no password is found, it asks
    it to the user using *getpass*
2.  **register** use it then store it in the Distribution instance
3.  **upload** look into the Distribution instance to see if the
    password was stored, and use it

  
This is now available in Python 2.7 and 3.1, and [heavily tested][].   
  
I'd like to go further and to think about a ssh-agent like system, so
there's no need to enter the pasword everytime you work with PyPI in the
same session.   
  
Does anyone knows what would be the way to do it properly ? I think a
ssh-agent like mechanism in Python's getpass would be a great feature
itself.

  [collective.dist]: http://pypi.python.org/pypi/collective.dist#what-is-collective-dist
  [heavily tested]: http://svn.python.org/view?rev=68415&view=rev
