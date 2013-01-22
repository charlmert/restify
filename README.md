restify
=======

using python/inspect to produce restful interfaces to any classes methods as a django project skeleton.

depends on nltk for exposing wordnet.* methods for now
see (http://nltk.org/install.html)

to see a list of callable methods in wordnet.* run:
- python introspection.py

e.g. output:
- wordnet.abspath ( fileid )
- wordnet.abspaths ( fileids, include_encoding, include_fileid )
- wordnet.all_lemma_names ( pos )
- wordnet.all_synsets ( pos )
- wordnet.encoding ( file )
- wordnet.fileids (  )
- wordnet.get_version (  )
- wordnet.ic ( corpus, weight_senses_equally, smoothing )
- wordnet.jcn_similarity ( synset1, synset2, ic, verbose )
- wordnet.lch_similarity ( synset1, synset2, verbose, simulate_root )
- wordnet.lemma ( name )
- wordnet.lemma_count ( lemma )
- ...

todo (see nltkws django project)
====
- wsgi apache
  -> using dev server for now

- django response [done]
  -> yo world [done]

- nltk data structs as json

- django json response
  -> ["yo world"]

- rest api front end
  - manually wrap code around nltk.wordnet.morphy, expose as rest [65]
    - deal with kwargs key0/val0/key1/val1
    - use admin.autodiscover() for template location

    - determin argument types and provide interface for
      constructing json objects to pass to functions.
      i.e. wordnet.lin_similarity(synset_obj, synset_obj ...
           synset as an object comes from a return of wordnet.synset

  - learn introspection to wrap frontend code around nltk functions [49]
  - inputs, namespace, button click to call and render ajax response
