Title: Pycon: detailed outline for documenting projects
Date: 2007-01-18 10:13
Category: documentation, pycon, python, quality, zope

There's only a few days remaining before tutorial cancellation at Pycon,
if you have interest in some of them, it's time to register !   
  
I have completed my outline for the tutorial I'll be giving. If you
consider to attend, you should bring your laptop and have this elements
installed on it, to maximize your pleasure ;) :   
-   Python 2.4 or 2.5
-   [docutils][]
-   [setuptools][]
-   [pylint][]
-   [cheesecake][]
-   subversion, client and server (optional)

  
(PyCommunity will be provided at tutorial day).   
  
Updated outline:   

    - writing a document



      - mastering reStructuredText

        - presentation of reStructuredText

        - distribution of cheatsheet

        - exercises



      - writing techniques and tips

        - presentation of the ten laws, with examples

        - exercise in binomial



      - team writing

        - presentation: bad writer, good designer VS good writer, bad designer

        - exercise: doc review



    - writing documents in Python



      - documenting a module

        - presentation : which module to document, how to split content into docs ?

        - exercise (on an existing package)



      - documenting a package

        - presentation: README.txt and friends

        - exercise: writing the minimum files, testing with cheesecake



    - using documents for test-driven developement



      - mastering doctests



        - presentation: unittests ain't doctests

        - exercise: spliting tests between doctests and unittests



      - continuous documentation

        - presentation: designing through doctests

        - exercise: creating a module with its doctest



    BREAK



    - writing documents in a Python Project



      - writing tutorials

        - presentation: what's a tutorial

        - presentation: how to write a tutorial

        - exercice: write a mini-tutorial



      - writing cookbook and recipes

        - presentation: what's a cookbook

        - presentation: how to write a recipe



        - exercice: write a recipe



      - writing a project glossary

        - exercise: write a glossary



      - crosslinking everything

        - exercice: link the recipe, tutorial and glossary



    - website autogeneration with pycommunity   



      - presentation: pycommunity

      - exercise: setting up a subversion structure

      - exercise: setting up a hook for website autogeneration

      - customize pycommunity for an existing website



    - conclusions

  [docutils]: http://docutils.sourceforge.net
  [setuptools]: http://peak.telecommunity.com/DevCenter/setuptools
  [pylint]: www.logilab.org/857
  [cheesecake]: http://pycheesecake.org/
