Web App Software Development Maturity Model
###########################################

:date: 2020-10-12
:tags: python, qa, ci, cd
:author: Tarek Ziade


The `Capability Maturity Model Integration
<https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration>`_ (CMMI)
describes different levels of maturity for the development process of any
organization in a measurable way. It offers a set of best practices
to improve all processes. It's been regularly updated, and the latest
version includes some notions of agility.

CMMI can be applied to software development, but the software industry came
up with numerous other maturity models around the same concepts.
Existing models have usually 5 to 8 levels, but it's often a bit overkill.

Below is my attempt for a simplified software development maturity model for
web apps. It works for distributed remote teams where you don't always
have the ability to perform peer programming session.

It's based on three levels only, but can be adapted depending on the
context.

- **Level 1**: code style, versioning, code reviews and TDD are consistently
  used across the org.
- **Level 2**: There's a fully automated CI and CD with actionable metrics
- **Level 3**: All processes are constantly improved, refined.

It's a bit more complex than releasing desktop apps since web applications
are deployed on servers and interact with other services.

Level 1
-------

The first level is about making sure that everyone involved with building the
software shares the same culture of quality and uses the same standards and
tools.

In practice:

- all the work is pushed into a (D)VCS, including the tests, tools, configurations.
- every change is reviewed by at least another person *or* the change is made
  through peer programming sessions
- the coding style is consistent and enforced by tools.
- the code is built through tests, both functional and unit.
- the test coverage is known and a minimal coverage is enforced (80% or higher)
- installing and running the tools is done via a standard list of makefile-like
  commands, for all platforms that supports development

To reach that level of maturity, it's important that everyone gets involved
into filling the gap and improving the tools and the processes.

Cloning the code and getting started in developing it should be a very simple
step for the three major platforms (Linux, macOS, Windows). If it takes more
than an hour setting up a development environment, something is wrong.

Level 1 sets the stage for starting to automate how you test, build and
deploy your software. It's important to think of it as the foundational
basis for the next level.

Level 2
-------

Level 2 is about automation and making sure the software never gets into a
broken state. Every change should be staged and automatically build the
software and run the tests against it. This is based on the
**Continuous Integration** (CI) and **Continuous Delivery** (CD) principles.

**CI** means that your software code is continuously updated with changes
done by developers, and that the code is always in a working state.

**CD** means that at any moment, there's a releasable software that can be
pushed as the next official release. For cloud-hosted apps, the process of
deploying the new version in a staging environment is also automated.

That **pipeline**, from a change done in the code, to a new release of the
application, comes into many steps that each produces metrics and **artifacts**
that are used for deciding whether the change qualifies for the next step or
not.

A generic pipeline can be::

    PR in DVCS
      |  |
      |  ------> Build and automated tests
      |              |
      <-------<------*------> Review
      |                         |
      <--------<---------<------*-----> Merge/Release/Deployment
      |                                      |
      <--------<-----------------<-----------*---> Full Integration
      |                                                |
      <--------------<------------------<--------------*---> OK!


A **Pull Request** (PR) is pushed in the DVCS, or in a review system, and that
triggers a series of automated tests that will validate the change. Tests are
unit, functional, performance, security, etc. The tests can also assess that
the change did not lower the test coverage and when important, did not add too
much complexity to the code base (you can use the `Cyclomatic complexity
<https://en.wikipedia.org/wiki/Cyclomatic_complexity>`_ metrics for example).

If the change passes that step, there's a manual code review done
by another person, and there's a back and forth between the developer
and the reviewer until everyone is happy with the change.

It should not be the role of the reviewer to make sure the software builds or
the automated tests all pass. The reviewer role is to make sure that both  the
code and its tests are meeting their expectation in terms of design and
quality. The coder role is to ask for a review on a patch that is not broken,
that they think can be merged (if early feedback is needed, it's a distinct
process)

Once the review is accepted they are two strategies to adopt for
the next step:

1. **PR-driven** the PR is used to build a release and test it
2. **Master-driven** the PR is merged directly, master is used to build a release and test it

The PR-Driven approach offers one advantage. In case there's an issue, you won't
need to bisect the changes to find the offending patch. However, it's resource consuming
and also requires to test once more against master once the PR is merged.

The master-driven approach consists of cutting a release every day and testing it.
All changes done in the past 24h will be tested **together**. It is less resource
consuming, but means you will need to bisect.

Starting with 2. and maybe adding 1. later if that's not good enough is usually
a good approach.

In both cases, the **candidate** release is triggered and deployed in a staging
environment that can be used to verify that the new software still works when
it's running on realistic data and interacting with other apps when applicable.
That step will be used to ensure that the new version can be smoothly deployed.
It is based on end-to-end testing, which is usually the hardest and longest
thing to fully automate.

Full automation when not running in production means that you need to have a
staging environment for everything that interacts with your application, like a
database, 3rd party services etc. Besides automation, things like data
migration, backward compatibility, proper UI tests, can be tricky to simulate
properly in a staging environment.

If something goes wrong during that step, we know something went wrong
in one of the changes included in the candidate release. Once it's identified,
we're back to step 1 to correct it. The rolllback process may include
rollback scripts, to make sure that every environment is back to its
previous state, before the patches were applied. That may include rolling
back databases. In some cases, a decision can be made not to roll back the
changes but to fix with a follow-up change.

If the tests succeed, congratulations, your candidate release is ready for prime
time. In most cases, there will be a human that pulls the trigger to deploy
to production, because some manual end-to-end tests might be required.

By extension, **Continuous Deployement** (the other CD) means that the process
of deploying new versions to production is also fully automated. I don't really
make a technical distinction between the two CDs, as I consider that automated
deployments, at least in a staging environment, should be part of the
Continuous Delivery process. Deploying in **production** automatically is only
possible if all end-to-end tests are fully automated.


Level 3
-------

If you've reached Level 3, your process is already great. A lot of teams have
some of the Level 2 elements and are happily shipping, but they get more
friction when the app grows quickly or need to do some deep refactoring.

Level 3 is all about sitting down and observing how things are working to
constantly improve them. The rule of thumb is to eliminate manual steps as much
as possible, and speed up and improve the reliability of every automated step.

Some example:

- some tests are getting slow, there's a focus on making them fast
- a customer had databases errors, how can we change the full integration
  tests to cover this?
- one service is draining the CPU. Once we've fixed the scaling issue,
  what automated performance tests can we add to be proactive ?
- more e2e automation is added, one of the microservice is now fully
  deployed in production on every change, with no human intervention.
  **Double CD FTW!**


Conclusion
----------

In my model, Level 2 is the really big step, and requires a full adoption
of the principles set in Level 1. I don't think it useful to split it in smaller
steps because building that step is a horizontal task that should be seen as
a single, full project.

Have you reached Level 3 in your organization ? Do  you have a process that's
completely different ? What are your strategies to improve your processes ?

Thanks to  Dave Hunt for some feedback on this article, and proof-reading
my Frenglish  :)
