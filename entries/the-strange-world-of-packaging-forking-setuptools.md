Title: The strange world of packaging - forking setuptools
Date: 2009-07-19 09:59
Category: packaging, python

Again, like a year ago, people had enough of the fact that the
setuptools project is not maintained since 9 months.   
  
Phillip Eby explained that he doesn't have time to do it unless someone
would pay him for that. But in the meantime, he doesn't bless anyone to
do it. Well, he has blessed some people to do it (Ian Bicking and Jim
Fulton), but unfortunately these people are not willing to do it because
they have a lot of other projects going on. Other people that could
maintain it, including me, fail in his "unqualified people" category :)
  
  
So we are all locked in a strange situation where tons of patches are
ready to be commited in the setuptools tracker but are not making it.
Several non-public forks have started to appear around of course.   
  
So again, I decided with some other people to create a fork called
"Distribute". It's a real fork located here :
[http://bitbucket.org/tarek/distribute][].   
  
By *real* I mean that this fork was not created with the purpose of
forcing Phillip to do a release like we did last year for the 0.6c9
release, but with the intention to free us from that strange situation
where we all depend on his wills and (lack of) time.   
  
The plan is to release a first version next week, that corresponds to
the setuptools 0.6 branch, with some patches applied.   
  
Next, we are planning to start a 0.7 version where the code will be
splitted in several distributions:   
-   a distribution for pkg\_resources
-   a distribution for the setuptools package itself
-   a distribution for easy\_install

  
A little bit of bikeshedding is going on to pick a name for that fork,
and we ended up running a [poll][]. (vote!)   
  
Now, right after [I have announced this plan on Distutils-SIG][],
Phillip reacted by annoucing a similar plan, e.g. splitting the
setuptools project in several distributions. But since he previously
said that he didn't have the time to do it, I doubt that it'll work out
unless he's opening its development to a wider range of developers and
maintainers.   
  
That's the strange world of packaging...

  [http://bitbucket.org/tarek/distribute]: http://bitbucket.org/tarek/distribute
  [poll]: http://doodle.com/4eyxzrwgwq4a6t9s
  [I have announced this plan on Distutils-SIG]: http://mail.python.org/pipermail/distutils-sig/2009-July/012665.html
