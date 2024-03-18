DistilVit ~ Image Captioning Model
==================================

:date: 2024-03-17
:tags: python
:category: ai
:author: Tarek Ziade

Ankur Kumar released a `popular model <https://huggingface.co/nlpconnect/vit-gpt2-image-captioning>`_ on
Hugging Face to generate captions for images and `blogged about it <https://ankur3107.github.io/blogs/the-illustrated-image-captioning-using-transformers/>`_.

This model was also published as ONNX weights by Xenova so it could be
used in Transformers.js, see https://huggingface.co/Xenova/vit-gpt2-image-captioning

The model is doing a pretty good job - even if in some cases I had better results
with https://huggingface.co/microsoft/git-base-coco - But the GIT architecture is not yet supported in ONNX converters,
and my current understanding of those different architectures is that most
of the accuracy is obtained with great and vast data. So for now I am making the bet
that I can get good results with ViT.

Ankur used the `google/vit-base-patch16-224-in21k` image encoder and the
`GPT2` text decoder and fine-tuned them using the COCO dataset, which is
a dataset of 120k labeled images.

I wanted to reduce the model size and speed it up a little bit, so I decided
to build the same one replacing `GPT2` with `DistilGPT2` -- which is
2 times faster and 33% smaller according to its documentation.

I took Ankur's code snippets and recreated a training script that is published here:
https://github.com/tarekziade/distilvit

The major differences are:

- Once tokenized, the dataset is saved so it can be reused (450GiB).

- The training resumes from the last checkpoint on failure

- Only the last 10 checkpoints are kept, because each one is 2.1GiB so it's easy to fill your disks.

- Some labels were breaking the training because they had different sizes, so I had to created a data collector to fix this. I am not sure why this is happening since the tokenizer is supposed to pad everything.

The training took 45 hours on my 2xRTX4090 GPUs, but one GPU was often idling and the other
one was underused. I assume this is because some of the image processing is done on the CPU.
I also had several crashes on GPU parallelization, which seems to be a bug somewhere in CUDA or torch,
but I could resume every time.

I published the model in https://huggingface.co/tarekziade/distilvit and
the ONNX quantized weights are down to : 87MiB for the encoder and 98MiB for the
decoder, making the whole system weight under 200MiB when used in Transformers.js.

I've noticed a 30% speedup on average on the non quantized version
on my M1, and the generated text was also properly capitalized and punctuated (see `infere.py` in my repo) compared to the
original one. I am not sure why because the COCO dataset has uncased labels with sometimes
no periods.

The metrics at the end of the training were:

- eval_loss: 0.19939416646957397
- eval_rouge1: 43.006
- eval_rouge2: 16.9939
- eval_rougeL: 38.8923
- eval_rougeLsum: 38.8877
- eval_gen_len: 11.327256736227712
- eval_runtime: 1816.5255
- eval_samples_per_second: 13.77
- eval_steps_per_second': 1.721
- train_runtime: 46263.3695
- train_samples_per_second: 38.373
- train_steps_per_second: 4.797
- train_loss: 0.05974134062104816

My interpretation is that the the delta between the eval loss and the train loss suggest there's room for
improvement if the model gets trained on more data - and maybe more epochs.
So I am going to add the Flickr30k dataset along side the COCO one, and train on both to see if it gets better.

The results are still pretty good. So it seems worth pursuing.
