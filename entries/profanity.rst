PardonMyAI ~ Profanity Detection Model
======================================

:date: 2024-03-15
:tags: python
:category: ai
:author: Tarek Ziade


When working with Generative AI there's this fear in some contexts, that the model you are using
will generate content with curse words or hate speech. Detecting hate speech is also
useful when you want to moderate a forum or a chat room.

I was looking for some tooling to do this and stumbled on that `blog post <https://victorzhou.com/blog/better-profanity-detection-with-scikit-learn/>`_.
Victor's rationale is that all the tooling he found for this was based on a list of stop words,
which were often incomplete. He found one lib that was based on machine learning
but was very slow, so he created his own lib.

He used Linear Support Vector Machine (SVM) and trained a model against a dataset he created
by combining some Twitter and Wikipedia comments labeled data.

The results of his library are:

- Accuracy: 95%
- Precision: 86.1%
- Recall: 89.6%
- F1 Score: 0.88


That was back in February 2019. Fast-forward 2024, we now have a mature transformers architecture
with a plethora of base models that could be used to do the same work.

So I took back Victor's dataset and fined tuned a distil-bert-uncased model to do the same
detection work.

Turns out it's doing a better job. Here are my scores:

- Accuracy: 0.9748
- Precision: 0.9331
- Recall: 0.9416
- F1 Score: 0.9373
- AUC-ROC: 0.9955

You can find the model here: https://huggingface.co/tarekziade/pardonmyai
All the code used to fine-tune and evaluate here: https://github.com/tarekziade/pardonmyai

Usage example with Python:

.. code-block:: python

  from transformers import pipeline

  classifier = pipeline("sentiment-analysis", model="tarekziade/pardonmyai")

  print(classifier("These are beautiful flowers"))


Usage example with Transformers.js:

.. code-block:: javascript

  import { pipeline } from '@xenova/transformers';

  let pipe = await pipeline('sentiment-analysis', model='tarekziade/pardonmyai');

  let out = await pipe('These are beautiful flowers');


And it's fast (I am not providing numbers because I don't know against what hardware it was tested back then)

I've also created a "tiny" version based on TinyBert that is only 19M params and keeps a pretty
good accuracy. For that flavor, the ONNX quantized model weight less than 20MiB and infers really fast.

See https://huggingface.co/tarekziade/pardonmyai-tiny

I should add that the models suffers from the same limitations than Victor's one, as the training
dataset does not contains a lot of trick words. e.g. people using `f3ck` to evade a filter.
And a human will always be able to bypass the filtering by being imaginative.

But for detecting that a model has produced profanity, I think it should work fairly ok.

Thanks Victor for this great work, and inspiration.
