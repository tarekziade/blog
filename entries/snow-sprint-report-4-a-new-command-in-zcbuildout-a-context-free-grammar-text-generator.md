Title: Snow sprint report #4 : a new command in zc.buildout + a context-free grammar text generator
Date: 2008-01-27 11:06
Category: plone, python, zope

So this was the last sprint day here at the snowsprint, and a lot of
work was done to wrap-up some of the tasks. On my side I worked on two
topics:   
-   adding a new describe command to [zc.buildout][]
-   coding a random-text generator library

  
### Adding a "describe" command to zc.buildout

  
Godefroid came up with a nice idea about buildouts: when you are
working with a recipe, it's sometimes hard to figure out what are the
options it takes, which ones are optionals, what are the default, etc.   
  
It means that you have to digg into the code, or get to the PyPI page.
Hopefully this page will give you the infos, if the long\_description
variable was hooked into some reSTructuredText. (see [iw.recipe.pound][]
for example).   
  
That make a lot of context changes for the developer, so basically, the
idea of the new describe command is to be able to query for a given
recipe help. This help will be displayed online as long as the recipe
creator fills the Recipe class docstring. We checked with Jim that this
would be a good idea, since he wants (and that's good) to keep the
recipe as simple as possible (basically, any class with an install and
an update commands). Since he liked the idea, we started to code it.   
  
So basically, the command is called like this:   
       $ bin/buildout describe my.recipes

        my.recipes

            The coolest recipe on Earth.

            Ever.

  
It deals with recipe versions and takes care of multiple entry points:
  
       $ bin/buildout describe my.recipes:default my.recipes:second

        my.recipes:default

            The coolest recipe on Earth.

            Ever.

        my.recipes:second

            No description available

  
This feature looks quite simple, but was a bit tricky to implement,
since we had to parse the working set of the current buildout to extract
the infos. The version section is also taken care of.   
  
All that work we did together with Godefroid and Dokai is in a branch,
waiting for Jim's feedback.   
### Coding a random-text generator

  
When we worked on benchmarking Solr versus Plain catalog on the
indexing task, we created a small script to generate random text, based
on a chomsky algorithm. We were really excited about going deeper in
this topic. Both Dokai and I worked on some generators. I have written
on my side a Python port of [nonsense][], and the results were pretty
interesting.   
  
Anyway, we started a fun task for the last day with Dokai and Ethan:
write a random-text generator library and a grok-based web app on the
top of it. I worked on the core part, and we came up with this cool
command line scripts that would generate som random text, given a file
that would provide structure of sentences, and for each part of the
sentence a list of choices.   
  
The command is building the sentences picking the choices randomly. For
example this file adapted from nonsense (extract):   
   [gibberish]



    default =

        ${course}



    name = college



    annoucement =

        The ${university} class "${course}" has been cancelled due to lack of interest.

        Starting next year, incoming freshman at ${university} will be required to take "${course}."

        "${course}" will no longer be offered at ${university} due to lack of interest.

        Due to overwhelming popularity, an additional section of "${course}" will be offered at ${university} next semester.

        Not one single student signed up for ${university}'s "${course}" last semester.



    course =

        ${adjective} ${noun} ${suffix}

        ${adjective} ${noun}: ${ending}

        ${adjective} ${noun} And ${adjective} ${noun} ${suffix}

        ${noun} & ${noun} ${suffix}

        ${group1} ${group2} ${life} ${suffix}

        ${group2} ${noun} ${life} ${suffix}

        ${group1} ${group2} ${life} Since {#1800-1970}

        ${group2} ${life}: ${ending}

     event =

        The African Diaspora

        The Harlem Renaissance

        The Civil Rights Movement

        The Italian Renaissance

        Westward Expansion

        Manifest Destiny

        Women's Suffrage

        World War I

        World War II

        The War Of 1812

        The American Revolution

        The French Revolution

        The Russian Revolution

        The American Civil War

        The Spanish-American War

        The Franco-Prussian War

        The JFK Assasination



    action =

        Basketweaving

        Aquatic Ballet

        Synchronized Swimming

        Professional Sports

        The ${adjective} Pottery Experience

        Home Economics

        Cardplaying

        Birdwatching



    noun =

        Diversity

        Globalism

     ...

  
will generate random, domain-specific text. A Grok application has been
built on the top on this, allowing dynamic creation of such files, and
online text generation. Check out [Dokai's blog][] about this during the
week, as he will present the Grok part. The code is in a Git repo here:
[http://repo.or.cz/w/gibberis.ch.git][]   
### Thank you Lovely Systems

  
Thanks to the Lovely team for this sprint !

  [zc.buildout]: http://pypi.python.org/pypi/zc.buildout
  [iw.recipe.pound]: https://tarekziade.wordpress.com/wp-admin/So%20this%20was%20the%20last%20sprint%20day%20here%20at%20the%20snowsprint,%20and%20a%20lot%20of%20work%20was%20done%20to%20wrapup%20some%20of%20the%20tasks.%20On%20my%20side%20I%20worked%20on%20two%20topics:
  [nonsense]: http://nonsense.sourceforge.net/
  [Dokai's blog]: http://blogs.hexagonit.fi/kai/
  [http://repo.or.cz/w/gibberis.ch.git]: http://repo.or.cz/w/gibberis.ch.git
