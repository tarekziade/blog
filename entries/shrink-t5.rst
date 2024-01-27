Compressing T5 models for summarization
=======================================

:date: 2024-01-27
:tags: python
:category: ai
:author: Tarek Ziade

My quest to create a summarizer model that is as small as possible,
yet produce good results, is still going on.

I've stumbled on the https://github.com/JulesBelveze/bert-squeeze project which
is a pretty cool project that applies different strategies to compress models
and wanted to try it on a long-t5 model -- the model I want to use for summarization
because it allows large documents (16k tokens).

Unfortunately, the project does not support seq2seq models yet. But Jules is
a very nice guy and is willing to take my contributions. He helped me understand
a few things around models.

He pointed me to a research paper about the "Shrink and Fine-tune" strategy,
(see https://arxiv.org/pdf/2010.13002.pdf) which consists of pruning some decoder
layers from the original model and then fine-tuning it again with the data
that was used to train the original model.

So it's not a distillation per se, it's a fine-tuning on a model that has some
of the initial layers removed.

So I told Jules I would try it and if it works, come back to contribute
a first patch to his project for seq2seq models.

I gave up on the idea of training long-t5 models on my Apple M1 because the 32GiB
memory that is shared between the GPU and the CPU dies pretty quickly given
the size of the data. longt5 accepts 16k tokens instead of 512, which blows my
memory. PyTorch's GPU backend is also three times slower than the CPU for me,
which I realized after some experiments.

To summarize, training models on an Apple laptop is not great.
This is why I've ordered 2 RTX-4090 - I can't wait to play with bigger models.


Shrinking
#########


Until then, I tried the SFT strategy on a smaller model. I took Jule's tldr model
https://huggingface.co/JulesBelveze/t5-small-headline-generator and applied the shrinking.

I tried to shrink just the decoder layers and also both the encoder and decoder.
The former reduces the size from 60.6M params to 47.9M and the latter to 38.5M.

This is the gist of the code used to shrink layers using transformers:

.. code-block:: python

  def shrink_layer(model, layer_name, new_size=None):
    if layer_name == "encoder":
        config_name = "num_layers"
    else:
        config_name = f"num_{layer_name}_layers"

    current_size = getattr(model.config, config_name)

    if new_size is None:
        new_size = int(current_size / 2)

    if current_size != new_size:
        layers_to_remove = [i for i in range(1, new_size * 2, 2)]

        for i in reversed(layers_to_remove):
            del getattr(model, layer_name).block[i]

        setattr(model.config, config_name, new_size)


  def load_and_shrink_t5_model(
      model_name, num_decoder_layers=None, num_encoder_layers=None
  ):
      model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)
      print("Shrinking model...")
      shrink_layer(model, "decoder", num_decoder_layers)
      shrink_layer(model, "encoder", num_encoder_layers)
      return model


  # creating one with 6 encoder and 3 decoder layers
  load_and_shrink_t5_model("JulesBelveze/t5-small-headline-generator", 3, 6)

  # creating one with 3 encoders and 3 decoder layers
  load_and_shrink_t5_model("JulesBelveze/t5-small-headline-generator", 3, 3)


Training
########

Once the model was shrunk, I fined tuned it on the same dataset. I tried
many different configurations and found that a single epoch was as good as
running many. The loss convergence happened pretty quickly and the training
lasts for less than 10 minutes.

You can find the train script here : https://github.com/tarekziade/distill-t5/blob/main/sft.py


.. image:: /theme/images/loss.png
  :alt: Show the loss chart. The loss goes down to 0.2 quickly and then stays there.


Once saved and quantized, the smallest model is down to 50MiB (as opposed to 250MiB) !

Using the demo script, from Jules' model card, I took the demo text:

  US FCC commissioner Brendan Carr has asked Apple and Google to remove TikTok from their app stores.
  The video app is owned by Chinese company ByteDance.
  Carr claims that TikTok functions as a surveillance tool that harvests extensive amounts of personal and sensitive data from US citizens.
  TikTok says its data access approval process is overseen by a US-based security team and
  that data is only accessed on an as-needed basis under strict controls.


I get those summaries:

**Original model** US FCC commissioner asks Apple and Google to remove TikTok from app stores

**50% decoder layers** Apple and Google to remove TikTok from their app stores

**50% encoder and decoder layers** China’s TikTok says it can harvest data from U.S. citizens

This is just a human evaluation though, we need some metrics.

Evaluation
##########

I used the standard ROUGE metrics to evaluate the model and compare to the original model's ROUGE score,
to get an idea of how accurate the new model is.

You can find the script here: https://github.com/tarekziade/distill-t5/blob/main/evaluate.py
it runs on the non quantized versions.

These are the results for the most agressive shrinking (3-3):

**Rouge-1**

- F1 Accuracy: 92.27%
- Precision Accuracy: 91.83%
- Recall Accuracy: 93.95%

**Rouge-2**

- F1 Accuracy: 94.48%
- Precision Accuracy: 95.40%
- Recall Accuracy: 92.01%

**Rouge-l**

- F1 Accuracy: 92.53%
- Precision Accuracy: 92.11%
- Recall Accuracy: 94.17%


This is amazingly good! Maybe because the model is doing tiny summaries.

I will try this recipe on larger summarizers and see what happens.

To recap:

**Shrinking encoder and decoder layers shaved off 40% of the model size and kept over 90% of accuracy**

And if we quantize it, we are shaving off 80% of the size!


