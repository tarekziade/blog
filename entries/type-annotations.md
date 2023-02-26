Title: Are Types Annotations Pythonic?
Date: 2023-02-23
Category: python, essay

Granted, the title of this blog post is a bit provocative, this topic sparks a
lot of emotional responses. I posted [a message on
LinkedIn](https://www.linkedin.com/posts/tarekziade_opinion-activity-7030601707717894144-qhYv)
and got two type of comments:

- developers that think type annotations improves readablity, adds self-documentation and make the code more robust
- developers that think they make the code harder to read and are unecessary constructs if you are writing *Pythonic* code

I am part of the latter choir, I find type-annoted code harder to read and I
wonder why devs building applications using them are not switching to Rust or
another statically type language to be honest. I find myself building good code
by carefully crafting functions and methods signatures so there's no ambiguity
on how the code works and how the data is passed around. I try to have a good
testing and QA hygiene, and I am not convinced mypy would be a game changer for
me there.

I have yet to see data about type annotation making a Python code base better.
Maybe there's a way to collect metrics on GitHub to measure the number of issues
fixed on projects using them or not, but that would be complex to do right.

The only use case I have in mind for type annotation would be for serializing and
deserializing data where I would use annotation to build a schema. But even for this,
I am in general better off using something like JSONSchema.

I wanted to expand on all the other reasons I dislike type annotations, but I've found this [blog
post](https://dev.to/etenil/why-i-stay-away-from-python-type-annotations-2041)
that nails it in my opinion.

But maybe it's just because my definition of *Pythonic* is deeply rooted in how
I've learned how to build applications in the past 15+ years and I am just became an
old grumpy coder now.

But no one can argue that using type annotations does change the look and feel of a Python 
application, and how you code in it.

It's not *my* Python anymore, it's not a few functions that explicitly get a
boost with Cython, it's a different language to me.

