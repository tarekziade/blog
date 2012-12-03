What The Feuille ?
##################

:date: 2012-12-03 12:27
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

.. image:: http://blog.ziade.org/whatthefeuille.png
   :align: right
   :target: http://whatthefeuille.com

This week-end I went to the `AngelHack <http://angelhack.com/>`_ hackaton in Paris with
`Olivier <https://twitter.com/ogrisel>`_
& `Ronan <https://twitter.com/amicel>`_. We teamed up to build a web
application from scratch in 24 hours,
from Saturday 12 am to Sunday 12 am. Ronan had to go home at some
point but Olivier and I stayed up all night... :)

http://whatthefeuille.com is a web app we created to let you find
out from what tree or plant a leaf is.

You take a snapshot, indicate the bottom and top of the leaf, and
the server does a bit of machine learning to make suggestions.

We are not sure yet how good it is, because we need to tweak the
algorithm we're using, and we need more data! That's Olivier's
part since he's an expert in this field.

The application is a website that works indifferently on mobile
phones or desktop, using the responsive design provided by Twitter's
bootstrap kit.

It's based on :

* Pyramid - the Python web framework - http://www.pylonsproject.org/
* Elastic Search - the Lucene-based server - to store all datas except the pictures - http://www.elasticsearch.org/
* Numpy, Scipy, scikit-image & scikit-learn for all the smart beats - http://scikit-learn.org
* Mozilla Persona - for the login - http://www.mozilla.org/persona

It was very fun to build, and the Angelhack organizers did a good job
at keeping us alive with food and support during the 24h :)

We did not win anything of course, because we were not trying to
sell something or pitch any business plan, etc. But it seems that the
idea was well received, we had positive feedback.

The code is ugly, buggy and untested - that's what happen when you rush
to finish it after a night with no sleep :) - but it works and we'll eventually
clean it up, it's not a big app.

If I have time I'll try to add the bits needed to make it an open
web app for the `Mozilla Marketplace <http://marketplace.mozilla.org/>`_.

If you like the idea, join the fun here: https://github.com/whatthefeuille/whatthefeuille
or maybe add plants and leaves on the websites.

