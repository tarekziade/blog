Title: Technical writing, the seven laws
Date: 2007-02-23 20:31
Category: conference, documentation, pycon, python

  
I am here at PyCon, enjoying the talks. I will blog about what I have
seen in a few days. Until then, let me drop here the **seven laws** on
how to write good technical documents.

  
These laws are the rules I have synthetized for the tutorial I gave
yesterday, and that can be followed by anyone who write for softwares.

  
They are based on advices taken from:   
-   Writing With Power (Peter Elbow)
-   Agile Documentation (Andreas Rüping)
-   My own experience on the topic.

  

  
The seven *laws* for technical writing:

  
  
-   [The Two-step writing process][]
-   [Simple style][]
-   [Targeted readership][]
-   [Focused information][]
-   [Realistic examples][]
-   ["Light but sufficient" approach][]
-   [Structured documents][]

  

  
  
### [The Two-step writing process][1]

  
Writing should be done in two stages (Elbow, 1980):   
-   a free writing where ideas are written on the paper no matter the
    shape.
-   a review stage where things are structured and reviewed.

  
Each stage should take 50% of the time.   
  
-\> Split you writing time in two phases, no one can write it right the
first time (except Mozart)   

  
  
### [Simple style][2]

  
-   Use short sentences and simple writing style.
-   Use simple vocabulary

  

  
  
### [Targeted readership][3]

  
Focus on your target when you write a document (Rüping, 2003).   
  
Assume their background knowledge to restrict the scope of the
documentation.   
  
-\> A *prerequest* section can help a lot.   

  
  
### [Focused information][4]

  
A document is about a clear focus.   
  
A precise title for each section and the document itself, and a summary
can help.   
  
-\> If you cannot easily name the document or one of its section,
there's a problem   

  
  
### [Realistic examples][5]

  
Drop the *foo* and *bar* habits. Examples must be real-life examples,
and usable as-is.   
  
Neh:   
   >>> import graph

    >>> foo = graph.calculateSquare(1, 1, 1, 1)

    >>> bar = graph.renderSquare(foo)

  
Better:   
   >>> import graph

    >>> square = graph.calculateSquare(1, 7, 1, 10)

    >>> square_view = graph.renderSquare(square)

  

  
  
### ["Light but sufficient" approach][6]

  
A working software is more important than the best documentation in the
world (Ambler, 2002).   
  
*Quality over Quantity* is the best rule.   
  
-\> Spending too much time to find something in the documentation is a
bad sign.   
  
-\> Think documents like code. Always limit the size of sections,
examples, etc. Modularized documentation is the key.   

  
  
### [Structured documents][7]

  
Use a clear document portfolio to facilitate the reading. Document
should use:   
-   an abstract with a readers guideline
-   a toc when there are more than one section
-   references
-   glossary
-   tables and diagrams

  
-\> Never write a document that doesn't have a template   
### 

  [The Two-step writing process]: #the-two-step-writing-process "id1"
  [Simple style]: #simple-style "id2"
  [Targeted readership]: #targeted-readership "id3"
  [Focused information]: #focused-information "id4"
  [Realistic examples]: #realistic-examples "id5"
  ["Light but sufficient" approach]: #light-but-sufficient-approach
    "id6"
  [Structured documents]: #structured-documents "id7"
  [1]: #id1 "the-two-step-writing-process"
  [2]: #id2 "simple-style"
  [3]: #id3 "targeted-readership"
  [4]: #id4 "focused-information"
  [5]: #id5 "realistic-examples"
  [6]: #id6 "light-but-sufficient-approach"
  [7]: #id7 "structured-documents"
