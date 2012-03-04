Title: Is __ prefix considered unpythonic ? 
Date: 2007-12-26 17:19
Category: python, quality

**EDIT**: Justus provided in the comments a great link where Jim Fulton
argues that \_\_ should be marked deprecated, folllowed by Neal Norwiz
and Tim Peters answers. This helps a lot understanding what \_\_ should
be used for:
[http://mail.python.org/pipermail/python-dev/2005-December/058555.html][]
  
  
I am writing on Python OOP best practices and I was wondering what are
the best ways to name attributes in classes. My main concern is about
the distinction between private and protected attributes.   
-   **private attributes** are attributes that cannot be seen or used
    outside of the class, even buy subclasses. The Python parser calls
    the name mangling algorithm when it finds them to prevent name
    collision;
-   **protected attributes** are attributes that can be used and seen in
    subclasses and *should not be used* outside. Nothing is done on them
    and they can be used like public attributes.

  
### When should we use them ?

  
If you read [PEP8][], it's clearly said that name mangling (using a
'\_\_' prefix) is the best way to protect an attribute from beeing
accessed or overriden. So it should be used for all class internals that
is not intended to be overriden.   
  
But in the biggest open source code bases like Zope or Plone, '\_\_'
usage is very uncommon. The simple '\_' prefix is often used instead, to
mark attributes that are private to the class or to the module. So there
are no real distinction between private and protected attributes. It
seems that the 'private' concept is not even used, and people often cut
their class code in two parts: public and protected.   
  
In other languages (like Delphi) that define protected and private
levels though, protected attributes are not used a lot, and people tend
to cut their code in private and public parts and make the protected
layer as slim as possible.   
### Practical rules

  
Based on these remarks, here's a tentative of '\_\_' and '\_' prefixes
best usages in Python, for the use cases I know :   
-   **use \_\_ with property**. since properties cannot use overriden
    methods and are tied to the class, the methods used with it should
    always be private;
-   **use \_\_ for methods that works with private attributes**. If your
    methods works for private attributes, make them private too;
-   **use \_ on methods when they are clearly intended to be
    overriden;**
-   **use \_\_ for all module functions and variables that are
    private**. A protected level is not needed since a module cannot be
    overriden.

  
Following these rules would probably make 90% of class attributes
private instead of protected, and change all base code conventions. So I
am wondering: am I a bit unpythonic if I try to follow this standard in
attribute naming ? My guess is that most base code are not clean enough
in that matter. For instance, many of them use both new-style and
old-style classes under Python 2.5, which lead to a MRO algorithm that
differs depending on the classes !   
  
I would love to hear how you people deal with these conventions.

  [http://mail.python.org/pipermail/python-dev/2005-December/058555.html]:
    http://mail.python.org/pipermail/python-dev/2005-December/058555.html%20
  [PEP8]: http://www.python.org/dev/peps/pep-0008/
