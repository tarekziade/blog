Title: Python standard lib : give me more withs !
Date: 2009-01-20 22:11
Category: python

I used to write in files like this :   
   open('somefile', 'w').write(content)

  
It's ugly for sure, and a more proper way is :   
   f = open('somefile', 'w')

    try:

        f.write(content)

    finally:

        f.close()

  
But since Python 2.6, the **with** statement is superior for this code
pattern:   
   with open('somefile', 'w') as f:

        f.write(content)

  
This is so natural in fact that I am always thinking about **with**
when I work with classes that have a start/stop or open/close behavior.
  
  
So, what about adding this behavior into imaplib.IMAP4, ftplib.FTP and
smtplib.SMTP ?   
  
So we can write things like this :   
       >>> from ftplib import FTP

        >>> with FTP('ftp.somewhere.com') as ftp:

        ...     ftp.login('someone', 'pass')

        ...     (some code)

        ...

  
I am working on a [series of patches][] for this, and wondering if some
other classes in the standard library could benefit from this as well..

  [series of patches]: http://bugs.python.org/issue4972
