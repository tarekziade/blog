Title: Snow sprint report #2 : benchmarking
Date: 2008-01-21 14:22
Category: plone, python, zope

*EDIT: The chomsky was somehow limited, and was creating very similar
documents. Dokai worked on another text generator that generates more
various document. It is based on various file and combine random texts
that are quite nice, check it out ! (same place, but the method is
called random\_text() (I have updated the code extract as well))*   
  
Dokai and Tom are working hard on the best way to hook the regular
catalog with the Solr utility. I was a bit aside on this task so I
didn't catch up with it yet.   
  
Anyway, I have prepared the field in order to compare a pure plone 3
with a solr-enabled one. I wanted to generate a Plone instance with many
documents, which content would look realistic.   
  
I found on ASPN a great recipe for a Chomsky-based random text
generator:
[http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/440546][]   
  
So I have just bundled it in a script that can be used to generate
Plone folders with documents in it. When Dokai and Tom work will be
ready, we will use this script to load several thoushands of documents
in the catalogs, to start a few benchmarks.   
  
Here's the script (used in an Extension, but straight forward to bundle
in a class), you can also download it from [here][]   

    """ Generates documents with realistic content,

        with a Chomsky random generator

        taken here : http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/440546

    """

    from Products.CMFCore.utils import getToolByName

    import logging

    import transaction



    leadins = """bunch of lines"""

    subjects = """bunch of lines"""

    verbs = """bunch of lines""" objects = """bunch of lines"""

    import textwrap, random

    from itertools import chain, islice, izip



    def chomsky(times=1):

        """Chomsky method of generating random text."""

        return ' '.join(chain(random.choice(part).strip()

                              for part

                              in (leadins, subjects, verbs, objects)

                              for i in xrange(times)))

    def gen_documents(context, folder, numdocs=10, root_name='doc_'):



        wftool = getToolByName(context, 'portal_workflow')

        for i in range(numdocs):

            root = i

            id_ = root_name + str(root)

            while id_ in folder.objectIds():

                root += 1

                id_ = root_name + str(root)

            desc = chomsky(5)

            title = chomsky(2)

            sub = chomsky(1)

            context.invokeFactory('Document', id_, description=desc, title=title,

                                  subject=sub)

            obj = context[id_]

            wftool.doActionFor(obj, 'publish')

            logging.info('created document #%d' % i)

            if i % 100 == 0:

                transaction.savepoint()



    def gen_folders(context, numfolders=10, numdocs=1000, root_folder_name='folder_',

                    root_name='doc_'):

        wftool = getToolByName(context, 'portal_workflow')

        for i in range(numfolders):

            root = i

            id_ = root_folder_name + str(root)

            while id_ in context.objectIds():

                root += 1

                id_ = root_folder_name + str(root)

            context.invokeFactory('Folder', id_)

            obj = context[id_]

            wftool.doActionFor(obj, 'publish')

            logging.info('created folder #%d' % i)

            gen_documents(obj, obj, numdocs, root_name)

            transaction.savepoint()



    def gen_sample(portal):

        gen_folders(portal)      def random_text(data, num_words=100):

        """Source: http://www.physics.cornell.edu/sethna/StatMech/ComputerExercises/RandText"""

        # Read in the file and create a prefix mapping

        words = data.split()

        prefix = {}

        for i in xrange(len(words)-2):

            prefix.setdefault((words[i], words[i+1]), []).append(words[i+2])



        current_pair = random.choice(prefix.keys())

        random_text = current_pair[0] + ' ' + current_pair[1]

        for i in xrange(num_words-2):

            # last two words in document may not have a suffix

            if current_pair not in prefix:

                break

            next = random.choice(prefix[current_pair])

            random_text = random_text + ' ' + next

            current_pair = (current_pair[1], next)



        return random_text

  [http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/440546]: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/440546
  [here]: https://svn.enfoldsystems.com/browse/*checkout*/public/enfold.solr/branches/snowsprint08-buildout/SolrIntegration/Extensions/gen.py?content-type=text/plain&rev=1806
