Title: Semantic Search in the Browser History
Date: 2023-05-24
Category: python

Semantic Search and LLMs are all the rage right now since the release of
OpenAI's ChatGPT -- there are new AI apps appearing every day and the rate of
innovation is quite amazing.

What I like the most about what is happening since a few months are two things:

1. you can explore ideas without having to spend money on cloud services
2. Python is king in the AI/ML field

For 1., no need to get a subscription or deploy large VMs. You can do some
amazing things with a modern laptop and a few Hugging Face pre-trained models
you can use offline.

For 2. I am astonished by the number of open source projects that are available
in Python to do state-of-the art AI/ML. It's not even funny how simple
it is to build an application once you know what you want to do.

It might have been like that since a few years but it's accelerating.

Searching for similarities in your documents using
HNSW? just use that lib to vectorize your text, it'll clean it for you and
output nice vectors, a summary and then you can use that other lib or vector
database to perform the search. It's a piece of cake to play and scratch an itch.

I am a noob in ML/IA. I understand how things work from a very high-level
overview, I did a few Andrew NG trainings and that's about it.

But I am a Python developer, and I want to play with the new toys!

## Bookmarks, History and the Awesome Bar

One problem I want to solve is to find back content I've previously browsed
on the internet using Firefox. Numerous times, I *know* I have seen an info
I am looking for and I am struggling to get it back. It's there, in one of
the pages I've browsed before. I cannot remember the exact search query I used
and the tools in the browser are pretty limited -- they only scan for the
url and title of pages.

If I could do a semantic search against my browsing history I could find things
back for sure. I want this search engine to work offline, just an extra agent
on my laptop.

But wait! I can build this! We have all the toys!

What I want to do is:

- extract the text from the pages I visited
- convert the text sentences into vectors
- store the vectors into a DB
- build a small web page to query that DB
- make that page my home page in Firefox

## extract the text

Building a search index with your visited pages should be done as a plugin in
Firefox. Once the page is loaded (or a file is downloaded), you can grab the
rendered content and index it -- and eventually reindex pages when they get updated
in a small indexing agent.

But for now I'll do something way easier. Firefox comes with a sqlite database
(places.sqlite) for all the pages you visit in the browser.

I can grab the list there:

```sh
% sqlite3 places.sqlite "select url from moz_places limit 3"
https://www.mozilla.org/privacy/firefox/
https://www.mozilla.org/en-US/privacy/firefox/
https://support.mozilla.org/en-US/products/firefox

% sqlite3 places.sqlite "select count(url) from moz_places"
103784
```

Wow! 100k pages in the last couple of years!

Visiting and rendering pages from outside the browser brings some other issues:
- if you want the page to be fully rendered, you need a tool like Selenium
- you lose the authentication context so you can't visit pages that require auth

But the obvious benefit is that you can get fresh version of the pages, by
running a indexing agent that checks for fresh versions. That comes with another
issue: if you have a lot of pages on the same domain, you are trying to scrape
all at once, you will get throttled and you might index a lot of
"Come back later" pages.

There are also redirects to login pages, that are using 200 codes so
it's hard to tell you are indexing a login page instead of the content.

For now, I will ignore all those problems and focus on indexing only HTML pages.
This brings me down to ~30k pages.

I'll use BeautifulSoup to make it simple. The simplified pseudo-code is:

```python
from bs4 import BeautifulSoup
import aiohttp


async with aiohttp.ClientSession() as client:
    async with client.head(url) as resp:
        if resp.content_type != 'text/html':
            return    # nope
    async with client.get(url):
        text = await resp.text()
        return BeautifulSoup(text, parser="html.parser")
```

## from text to vectors

Once you have the text, you can convert it to vectors.

I will use [sentence_transformers](https://github.com/UKPLab/sentence-transformers), 
and [txtai](https://github.com/neuml/txtai) for this and perform the following operations:

- create a summary out of my text
- split that summary in sentences
- convert those sentences into vectors

I am pretty sure I can do better to get the most out of my index, but that'll do.

In pseudo-code:

```python
from sentence_transformers import SentenceTransformer
from txtai.pipeline import Summary
from txtai.pipeline.data import Segmentation


model = SentenceTransformer("all-MiniLM-L6-v2")
summary = Summary("sshleifer/distilbart-cnn-12-6")
segmentation = Segmentation(sentences=True)


def get_vectors(text):
    sentences = segmentation(summary(text))
    return model.encode(sentences)
```

So much science in that function. I am socked! word2vec is so 2010!
I am BERT-powered! :)


## Storing in a DB

My browsing history is not something I want to send to a cloud service,
for privacy reasons. I trust Mozilla with it because I built the Firefox
Sync service and I know how it works. It's encrypted on the client side
and nothing in clear is stored on Mozilla's servers.

The day we can store and search vectors in fully encrypted storage
I'll use that system. 
[I've asked my LinkedIn network about this by the way](https://www.linkedin.com/posts/tarekziade_ml-privacy-activity-7066894583862870017-MvVG?utm_source=share&utm_medium=member_desktop)

Until then, everything will stay in my laptop.

I could store the vectors in a file but using a dedicated vector database
system gives nice features for free, like similarity search based on HWSN.

Elasticsearch has all the modules to do this now, as Lucene can store vectors.
But running a Java app takes quite a lot of memory, and the whole Elasticsearch
stack is overkill for just storing/searching vectors locally. I always want to
spare every MiB of RAM I can because my daily job usually involves running a
lot of big VMs.

And since I work at Elastic, it's a great way for me to check what others
are doing in our field.

They are numerous systems out there that focus on vectors, so I picked one
that was simple to run and query from Python (no specific reason): [Qdrant](https://qdrant.tech)

Built in Rust, turns out this database takes only a few MiB in RSS when it's running,
pretty slim and exactly what I would be ok running as a local service.

pseudo-code to upsert vectors in Qdrant

```python
from uuid import uuid4
import numpy
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams


client = QdrantClient(host="localhost", port=6333)
client.recreate_collection(
    collection_name='pages',
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

def upsert(url, sentences, vectors):

    for vec, sentence in zip(vectors, sentences):
        points.append(
            PointStruct(
                id=str(uuid4()),
                vector=list(numpy.asfarray(vec)),
                payload={"url": url, "sentence": sentence},
            )
        )

    client.upsert(collection_name='pages', points=points)

```


The `payload` part is metadata added to each point so when we search the database,
we can get back the corresponding url and sentence that matched.

That payload could be in another relational database, but QDrant has nice features
around filtering using them.

## small web page

Everytime I build small web app prototypes I love using [Bottle.py](https://bottlepy.org/docs/dev/). 
It's a brilliant tool when you don't need async stuff or complex features.

Building a search page for my ue case is done by vectorizing the search query
and running a similarity search on the DB.

pseudo-code

```python
from bottle import request, route

client = QdrantClient(host="localhost", port=6333)


def query(sentence):
    embedding = model.encode([sentence])
    vector = numpy.asfarray(embedding[0])
    vector = list(vector)
    return client.search(collection_name='pages', query_vector=vector, limit=3)


@route("/search")
def search():
    q = request.query["q"]
    hits = query(q)
    template = environment.get_template("index.html")   # jinja2 stuff
    args = {
        "args": {"title": "Private Search"},
        "description": "Search Your History",
        "hits": hits,
        "query": q,
    }
    content = template.render(**args)
    return content
```

And that's it!

See a screenshot. And it works well... I was trying to find back a page about
running training zones, and I found it!

![Private Search](https://ziade.org/zones.png)


## What's next

There's a lot of tweaking to do, and it would be better to send pages in Firefox
out of a plugin, instead of scraping after the fact.

I did not index downloaded files, that would be a killer feature to search
for something that is deep inside a downloaded invoice for example.

I am also not making any distinction between history and bookmarks and could
be smarter about how I filter out pages

I have not published the code, but I could if someone is interested and
wants to contribute. Ping me on LinkedIn or Mastodon!
