Title: Vacations + a new job
Date: 2009-07-24 16:38
Category: python

I am officialy on vacations !   
  
I've just finished my time at Alterway / Ingeniweb, where I was CTO for
the last two years. Well CTO was a translation for "Directeur technique"
in French, which is more like "head of developments". So I was like some
kind of lead developer, but without a code project :)   
  
These two years were a great time for me. It's time for me to summarize
what I have done, what went right, and what went wrong.   
### Summary of my work at Ingeniweb

  
I won't talk about customer projects, but about what I did that served
both for our projects and for the community. Ingeniweb is a company that
does (did in fact) Plone websites.   
  
I was hired at Ingeniweb with some clear goals (I had more, but these
are the most interesting):   
1.  improve the release process
2.  help Ingeniweb get back into the community
3.  QA work

  
**Improve the release process **: when I started, Ingeniweb was not
using zc.buildout, the de-facto Plone standard, so one of the biggest
task I achieved was to make them switch to zc.buildout, and eventually
make some minor contributions in zc.buildout. That was a hard work
because the average developer was against such a big change in his
habits. I eventually succeeded.   
  
I've also worked on plone.org side to make it "pypi compatible" and
eventually became a Python commiter to improve distutils, the mother of
all packaging tools in Python. That was very positive for me and for the
community, I think. And I am now involved in Python development for the
future, trying to write some useful PEPs and so on. This is going to be
one of the major community task I'll be working on for the upcoming
years I think.   
  
**Help Ingeniweb get "back into the Plone community"**: this was quite
an interesting task. The people that hired me were frustrated because
their developers were not (besides a few exceptions) part of the Plone
community. So I worked on this by trying to understand why it happened.
It's quite simple in fact : that's because of the lack of communication
: people in our company were not talking enough with the community and
were trying to solve and work on their problems on their side. No
judgment or disrespect on this : this is mainly because of the language
barrier I think. And also because the people in charge were not sending
our developers in conferences anymore. Being part of an OSS community
requires from the company managers to send their developers in
conferences from time to time.   
  
The output of this task was not positive for Ingeniweb, but in the
meantime very positive for me : I was able to become part of the Plone
community and meet great people. Although I was unable to push my
co-workers to follow me in this, neither to make the company contribute
more on this. We organized one sprint, but given the size of the company
at that time (20+) this was not enough in my opinion.   
  
The worst part I think is were I realized that the people that asked me
to do it, didn't care much about it anymore. The boss left us, and the
"second" left right after :)   
  
**QA in customer projects** : The third main task was to raise the QA
in all projects, starting from scratch : beside a very few exceptions,
people were not making tests neither buying the Test-Driven approach.
The problem with TDD is that it cannot work if it's not done everywhere
by everyone in the company. When this is the case, someone who doesn't
practice TDD looks like he's trying to break a window of the house we
are all building together.   
  
But when you are working with developers that don't practice TDD, you
need to first convince the project managers that it's better, otherwise
it doesn't take. I have convinced some co-workers, but at the end, TDD
didn't work out because some managers were just telling their developers
to drop TDD to go "faster" in the customer projects. (faster... into
troubles for big applications)   
  
At the end, I think it's very hard to raise the QA in companies that
sells development services, because it implies a lot of commitment from
all people involved, from sells to managment. In an software editor
company it's easier because you can put some guards around your software
code base and keep the QA high.   
  
But along the way I did some interesting projects to set up continuous
integration. collective.buildbot is one of those. It allows you to set
up automatically a buildbot into a zc.buildout-based project.   
  
Don't get me wrong if you feel that this is a pessimistic summary :
everything else was just great !   
### What's next ?

  
When I am back from my vacation, I am starting a new work in a startup
in Paris, providing a [Saas][] in the cloud fully written in Python.   
  
I'll blog about it when I am back :)

  [Saas]: http://en.wikipedia.org/wiki/Software_as_a_service
