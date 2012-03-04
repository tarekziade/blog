Title: shutil.copytree small improvement
Date: 2008-07-08 08:11
Category: plone, python, zope

When you have to work with directories and files, there's a very common
pattern: copying a directory into another, but filtering out a few files
and directories.   
  
For instance, if you want to copy a directory that contains source
code, you will probably remove .pyc files and .svn directories if you
work with Subversion. In that case, *shutil.copytree* cannot be used, so
*os.walk* is the usual way to go (rough example):   
   import os

    from os.path import join, splitext, split, exists

    from shutil import copyfile



    def copy_directory(source, target):

        if not os.path.exists(target):

            os.mkdir(target)

        for root, dirs, files in os.walk(source):

            if '.svn' in dirs:

                dirs.remove('.svn')  # don't visit .svn directories           

            for file in files:

                if splitext(file)[-1] in ('.pyc', '.pyo', '.fs'):

                    continue

                from_ = join(root, file)           

                to_ = from_.replace(source, target, 1)

                to_directory = split(to_)[0]

                if not exists(to_directory):

                    os.makedirs(to_directory)

                copyfile(from_, to_)

  
This is a lot of boiler-plate code, so I usually create a small
function that accepts more arguments to filter out files and directory.
But Python should provide this pattern in the standard library.   
  
I have proposed a patch for shutil.copytree, to integrate filtering
capability. It has been reviewed and commited in the trunk this week, so
we will have it in Python 2.6. Now copytree comes with an ignore
argument that has to be a callable. If given it will be called on each
visited directory to decide what is copied and what is not.   
  
There's a default callable in shutil called ignore\_patterns, that can
be used to filter out files with glob-style patterns. I have added this
example to Python doc:   
   from shutil import copytree, ignore_patterns

    copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))

  
Pretty straight forward ! :D   
More info and examples here :
[http://docs.python.org/dev/library/shutil.html\#shutil.copytree][]

  [http://docs.python.org/dev/library/shutil.html\#shutil.copytree]: http://docs.python.org/dev/library/shutil.html#shutil.copytree
