Title: Are Type Hints glorified unit tests?
Date: 2023/02/26
Tags: python
Author: Tarek Ziade


The Python programing language is pretty lax in the coding style. You can build
your application using just plain functions or only classes, or a mix of both.
There’s no explicit privacy model and this can be quite confusing for
developers with a Java or C++ background.

This flexibility is part of the reason why Python is so successful. My mother
which is a statistician and never learned Object-Oriented Programming (OOP) is
happily using Python with an enormous amount of small functions and could not
care less about classes and modules. She just happily uses her pile or
functions.

This freedom is also why the language is sometimes seen as not suitable for
building large applications, pointing to its lack of safeguards. But the truth
is that you can build pretty much anything as long as you have a good strategy
on how your code base is growing.

I’ve written about this 15 years ago in one of my books and I think this is
still true today. 

## Entering Type Annotations

Following an [interesting conversation on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7030601707717894144) about type annotations, I
felt the need to think about this topic again. If you don’t know what are types
annotations, you can read the official [Python documentation](https://docs.python.org/3/library/typing.html)

This feature is controversial in the community because it drastically changes
how coding in Python feels and looks. Some folks [hate it](https://dev.to/etenil/why-i-stay-away-from-python-type-annotations-2041), 
some [love it](https://medium.com/analytics-vidhya/type-annotations-in-python-3-8-3b401384403d).

Although, adding hints in your code offers some interesting features and the
promise that it will have fewer bugs if you run Mypy or pytype against your
code – or even in IDEs like PyCharm.

I’ve been building large applications in Python for a long time and never
needed them. So I tried to ask myself if using type annotations would have made
my life easier.  

**Can type annotations help build, grow, and maintain large Python applications?**

For me, it’s quite hard to measure, to be honest, because I’ve developed over
the years some software design strategies that are not using them and that
seems to work well. And when they don’t work, it’s a signal for me to drop
Python and use another language. 

Gregory Smith who works at Google and is a prominent Python dev contributor has
replied to my LinkedIn post with this:

```
Meanwhile our 100+ million line Python code base with a
significant portion of things statically analyzed by pytype
and most recent code authors including annotations by default
continues to prevent bugs and make it easier to maintain
the code.


Data from practical experience disagrees with your opinion.
```

My immediate reaction was – “I really want to see that code base! Too bad it’s
not open sourced” – my speculation is that these 100 million lines of code have
been around for over a decade, and require a lot of work for keeping its tech
debt under control. 

[Pytype](https://google.github.io/pytype/user_guide.html) can check your code
and find issues using inference I love the fact that it can work on unannotated
code as well.

But Greg’s last part about starting to include annotation to prevent bugs
strikes me because this is exactly the argument some developers use to explain
the superiority of statistically typed language where the compiler (and here
pytype) will catch some problems. The compiler would prevent a specific set of
problems similar to what [fuzz testing](https://en.wikipedia.org/wiki/Fuzzing) does.

If you push this logic to its extreme, you can use [Ada](https://ada-lang.io/).
The nature of the language and its deep compile-time checks make a program that
survives the compiling steps rock solid. Tests in this context can focus on
happy paths and make sure the application works as advertised. Today, Ada is
still used to build applications to launch rockets or control planes because
there’s so little room for bugs. Rust is also a great language for writing 
safe code, in particular memory-safe code.

But back to Python, if annotations are just used to prevent bugs, should they
be considered as a new DSL to automate a range of tests against your code? 

This is the example the project provides:

```python
def annotated(x: int, y: float = 0.0) -> int:
    return x + y
```

Pytype will detect the problem and complain that the function returns a float
instead of an int. If you don’t use type hints, the same function would look
like this and you would miss the problem for sure unless you have a specific
assertion in your tests:

```
def not_annotated(x, y=0.0): 
    return x + y 

def test_not_annotated():
    assert isinstance(not_annotated(3), int)
```

The bigger question is the reason why the developer added the type annotation
`-> int` . If there’s an incentive to make sure the function returns an int and
nothing else, there must be a very good reason and hopefully, it’s covered in
some tests that are more sophisticated than the `test_annotated` example I gave.

So for me, it begs the question: are type annotations just extra unit tests
that have migrated closer to your code?

