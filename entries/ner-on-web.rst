Named-Entity Recognition on web pages
=====================================

:date: 2024-02-19
:tags: js
:category: ai
:author: Tarek Ziade

In a project, I had the goal of detecting *named entities* on the web page I am looking at without calling an external service, using NER. `Named-Entity Recognition <https://en.wikipedia.org/wiki/Named-entity_recognition>`_ (NER) is a task that aims to extract entities from a text, like locations, persons, organizations, etc.

NER is an interesting task because unlike summarization, you can work at the sentence level to detect names, you don't need the context of the whole text. Which means you can iterate on large texts
without hitting a context size limit, by infering sentence by sentence. This means NER is a
great target for small specialized models.

The Hugging Face Hub has tons of models for this, the most popular one is `bert-base-NER <https://huggingface.co/dslim/bert-base-NER>`_. Another model from dslim that I have found that
is doing an excellent job is `distilbert-NER <https://huggingface.co/dslim/distilbert-NER>`_ which is a fined-tuned version of DistilBERT. The model weights 66M params, and once quantized, the weight file is down to 65MiB, which is quite small.

I've pushed an ONNX version at https://huggingface.co/tarekziade/distilbert-NER for my experiments with `Transformers.js <https://huggingface.co/docs/transformers.js/index>`_.

Detecting names on a web page
#############################

Extracting this kind of knowledge from a web page is a great way to propose some
follow-up actions. For example, if the city of Paris is mentioned in the text, you could
wrap that word with a link to its wikipedia page.

To iterate on sentences, you can use some regular expressions, but most browsers now
have implemented `Intl.Segmenter <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter>`_ which
is a standardized way to iterate on a text in Javascript. It's currently in Firefox Nightly (Desktop) and in all other browsers. It does not work as well as Python's nltk because its lists of abbreviations is imperfect. It will split the text on words like "Jr." - But I expect that it will improve over time.

I wrote the following function to iterate on sentences:

.. code-block:: js

  function sentenceIterator(text, num_sentences = 1) {
    let useSegmenter = typeof Intl.Segmenter !== "undefined";
    let sentences;

    if (useSegmenter) {
      const segmenter = new Intl.Segmenter("en", { granularity: "sentence" });
      const segments = segmenter.segment(text);
      sentences = Array.from(segments).map(segment => segment.segment);
    } else {
      // Fallback to regex-based sentence splitting
      sentences = text.match(/[^.!?]+[.!?]+/g) || [];
    }

    let current = 0;

    return {
      next() {
        if (current < sentences.length) {
          // Collect up to num_sentences
          const chunk = sentences
            .slice(current, current + num_sentences)
            .join(" ")
            .trim();
          current += num_sentences;
          return { value: chunk, done: false, numSentences: sentences.length };
        }
        // No more sentences, mark as done
        return { done: true };
      },
    };
  }


You can combine that function with `Readability.js <https://github.com/mozilla/readability>`_ to iterate on the text of a web page,
and call Transformers.js on each sentence.

Something like the following:

.. code-block:: js

  var documentClone = document.cloneNode(true);
  var article = new Readability(documentClone).parse();

  const iterator = sentenceIterator(article);
  const classifier = await pipeline('token-classification', 'tarekziade/distilbert-NER');
  let sentenceEntities;

  for (
    let s_result = iterator.next();
    !s_result.done;
    s_result = iterator.next()
  ) {
    const sentence = s_result.value;
    sentenceEntities = await classifier(s_result.value);
    console.debug(sentenceEntities);
  }


This code can run in a web worker, and using events, you can stream back entities as you find them.

I have not built a full lib for this, but if you're interested let me know.
It could come as a webextension that underlines names on the current page, and
display a popup with a definition or a wikipedia summary.
