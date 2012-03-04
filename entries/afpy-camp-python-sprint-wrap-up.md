Title: Afpy Camp - Python Sprint Wrap-up
Date: 2010-09-22 21:39
Category: python

The Afpy Computer Camp was great as usual. We were fifteen of us
sprinting at my house and we had a lot of fun watching zombies movies
(Shawn of the Dead. Zombie Land) and eating that suckling Pig I bought.
  
  
[caption id="" align="alignright" width="315" caption="The packaging
pig is dead "]![image][][/caption]   
  
On the coding side I must admit I did not do as much as I wanted, which
is a shame since I had around me great folks to work on testing,
packaging etc. I had to take care of the catering and the train station
shuttling.   
  
I did find some time to brainstorm with Michael on plugins and some
code should follow this week. The idea is to provide a entry-point like
set of API in the version of pkgutil we have in distutils2, which
complements PEP 376 and is supposed to update the module we have in the
stdlib. Michael will use it for unittest2 once I ship a working version.
  
  
I also did quite some work with Holger, who helped me with is Tox tool
to set up a Continuous Integration server for Distutils2 that tests
multiple Python version. Yay! Its up and running but I need to add some
ACLs before I publish it.   
  
Next we talked about the best approach for people to start using
Distutils2 amd Holger came up with great ideas.   
  
We will provide as planned an alpha version that has a run module that
can be run to execute distutils2 on a project. No more setup.py here,
the script will just read the setup.cfg and read all options from there,
including a section where all metadata are described.   
   $ python -m distutils2.run install

  
That's already committed and I have one more feature to add before I
released Distutils2 1.0a3 : a small hook to allow people to run
arbitrary code in the process. This hook won't be able to change the
metadata so we don't break the "static metadata" paradigm we want to
provide -- see PEP 345 --. It will be useful though to work on build
options etc.![image][1]   
  
Projects will be able to keep their setup,py file for Distutils1 and
Setuptools (that's the new idea :D) , and add sections in their
setup.cfg to make the project Distutils2 compatible in the same time.
IOW each Distutils version will not step on the other version toes. I am
more concerned about the adoption of distutils2 in the various
installers like Pip or easy\_install but that's a good complement to
have.   
  
I had a great time with great folks, thanks to the PSF / Jesse Noller
for the $250 grant we are going to use for paying part of the travel
expenses for Michael and Holger. Thanks also to Logilab who sent us
Pierres-Yves.   
  
I am looking forward to read other people wrap-up, and also to next
year Camp !   
  
[More Pictures][]

  [image]: http://farm5.static.flickr.com/4109/5000775607_c8b6f9673d.jpg
    "Packaging Pig"
  [1]: http://farm5.static.flickr.com/4152/5005266723_3f9db72e71.jpg
    "Debian FTW"
  [More Pictures]: http://www.afpy.org/photos/afpy_barcamp_3
