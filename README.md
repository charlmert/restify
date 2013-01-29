restify
=======

using python/inspect to produce restful interfaces to any classes methods as a django project skeleton.

sudo python setup.py install

restify -i services.py -t django -p proj -a rest
//restify -i services.py -t django.xml
//restify -i services.thrift

#todo: (see nltkws django project)
- wsgi apache
  -> using dev server for now

- rest api front end
  - manually wrap code around nltk.wordnet.morphy, expose as rest [65]
    - deal with kwargs key0/val0/key1/val1 [done]
    - use admin.autodiscover() for template location

    - create a code template for django skeleton generation

    - create an interface definition language specific to restify 
      - namespace
      - methods
        - json parameters as strings or json objects
        - result as string or json objects
      - consider http and streaming/chunking
      - see how thrift does this

    - determine argument types and provide interface for
      constructing json/serialized objects to pass to functions.
      i.e. wordnet.lin_similarity(synset_obj, synset_obj ...
           synset as an object comes from a return of wordnet.synset

  - inputs, namespace, button click to call and render ajax response

transport
=========
Sets up libraries, modules or classes to be transportable accross languages
by wrapping them in executable scripts that know how to accept and pass
string or serialized parameters as well as to return string or serialized results.

#todo:
- use jsonpickle to serialize/deserialize objects in python [done]
- create wrapper that understands json parameters
  - must return string or json

- use introspection to inspect runtime objects and create serialized representations
  for use in the interface description.

- the restify IDL must produce executable transport wrappers aswell

- consume the nltk library directly from cakephp
  - i.e. json_result = exec('wrapper.py json_params')

- also build a cakephp ajax frontend to the django rest services
