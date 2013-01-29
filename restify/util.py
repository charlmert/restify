#!/usr/bin/env python

import json
import jsonpickle
from nltk.corpus import wordnet

"""Dump a pretty printed JSON object to a file
   >>> from restify import util
       obj = {'one':1, 'two':2}
       util.dump(obj, '/tmp/obj.json')
"""

def dump(obj, filename):
  objson = jsonpickle.encode(obj)
  pj = json.loads(objson)
  f = open(filename, 'w')
  f.write(json.dumps(pj, sort_keys=True, indent=4))
  f.close()

def dumps(obj):
  objson = jsonpickle.encode(obj)
  pj = json.loads(objson)
  return json.dumps(pj, sort_keys=True, indent=4)
