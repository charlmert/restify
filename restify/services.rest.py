# generating the restify definitions for the wordnet service
# everything is a string unless a type is specified
# types can be objects or native types
import json

service = ()
methods = []

# abspaths ( fileids, include_encoding, include_fileid )
method = (
      {'method':'abspaths'}, 
      {'parameters':
        {
         '':'fileids', 
         'bool':'include_encoding', 
         'bool':'include_fileid'
        }
      },
      {'defaults':
        [
         'None', 
         'False', 
         'False'
        ]
      }
    )

methods.append(method)

# notice type pos!
# all_lemma_names ( pos )
method = (
      {'method':'all_lemma_names'}, 
      {'parameters':
        {
         'pos':'pos'
        }
      },
      {'defaults':
        [
         'None'
        ]
      }
    )

methods.append(method)

# ic ( corpus, weight_senses_equally, smoothing )
method = (
      {'method':'ic'}, 
      {'parameters':
        {
         'corpus':'corpus',
         'bool':'weight_senses_equally',
         'float':'smoothing'
        }
      },
      {'defaults':
        [
         'None', 
         '0.1'
        ]
      }
    )

methods.append(method)

# wordnet.lin_similarity ( synset1, synset2, ic, verbose )
method = (
      {'method':'lin_similarity'}, 
      {'parameters':
        {
         'synset':'synset1',
         'synset':'synset2',
         'ic':'ic',
         'bool':'verbose'
        }
      },
      {'defaults':
        [
         'False'
        ]
      }
    )

methods.append(method)

service = (
            {'service':'wordnet'},
            {'namespace':'nltk/wordnet'},
            {'methods': methods}
          )

print json.dumps(service, sort_keys=True, indent=4)
