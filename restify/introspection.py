import inspect
import re
import pprint
"""Class to assist with evaluating classes to find out:
    - What the immediate members are (minus defaults and builtins)
    - What the immediate methods are
    - What the arguments to those methods are
    - What is required to reconstruct calling this from code 
    - What the documentation for members and methods are

      >>> import restify.introspection as introspection
          from restify.services import RestInterface
          introspection.get_callables('RestInterface', '^_')

"""

def get_methods(obj):
    # fetch the methods
    ret_method = []
    for method in inspect.getmembers(obj, predicate=inspect.ismethod):
        ret_method.append(method[0])

    return ret_method

def get_args(method):
    if (not inspect.ismethod(method)):
        raise Exception(''.join([str(method), ' is not a method']))
    # fetch the argspec
    argspec_str = str(inspect.getargspec(method))
    argspec = parse_argspec(argspec_str)

    return argspec

# method to parse the argument spec into a dict
# takes an argspec from inspect e.g. for inspect.get_argspec(wordnet.morphy)
# "ArgSpec(args=['self', 'form', 'pos'], varargs=None, keywords=None, defaults=(None,))"

def parse_argspec(argspec):

    # checking for validity of argspec
    is_valid = re.match('.*args=.*?\]\,', argspec)
    if (not is_valid):
        return False

    argspec_ret = {}

    # cleaning up the argspec
    argspec = argspec.replace('ArgSpec(', '')
    argspec = str(re.sub('\)$', '', argspec))

    # cleaning up args
    args = re.search('args=.*?\]\,', argspec)
    args = str(args.group(0))
    args = args.replace("args=[", '')
    args = args.replace("],", '')

    parts = args.split(',')
    keys = []
    for part in parts:
        part = re.sub("('|\")", '', part)
        keys.append(part.strip())
        
    # removing 'self'
    keys.reverse()
    if keys[len(keys)-1] == 'self':
      keys.pop() 
    keys.reverse()

    argspec_ret['args'] = keys

    # cleaning up varargs
    # keyword args handled by all other key/value pairs in the url
    varargs = re.search('varargs=.*?\,', argspec)
    varargs = str(varargs.group(0))
    varargs = varargs.replace("varargs='", '')
    varargs = varargs.replace("',", '')
    argspec_ret['varargs'] = varargs

    # cleaning up keywords
    # those key value pairs will translate into the keyword=value
    # in the actual function call
    keywords = re.search('keywords=.*?\,', argspec)
    keywords = str(keywords.group(0))
    keywords = keywords.replace("keywords='", '')
    keywords = keywords.replace("',", '')
    argspec_ret['keywords'] = keywords

    # cleaning up defaults (not used for now as purpose is automatic REST)
    # might not have to deal with defaults as it gets used when the argument is
    # missing
    defaults = re.search('defaults=.*$', argspec)
    defaults = str(defaults.group(0))

    if (defaults == "defaults=None"):
      defaults = None
    else:
      defaults = defaults.replace('defaults=(', '')
      defaults = re.sub('\)$', '', defaults)
      defaults = re.sub(',$', '', defaults)
      defaults = defaults.split(',')
      items = []
      for item in defaults:
        items.append(item.strip())
      defaults = items

    argspec_ret['defaults'] = defaults

    return argspec_ret

# return method strings as callables
# something that can be eval'd to return a response
# research> some arguments can be populated via dropdown
#           e.g. wordnet.morphy(form, pos)
#           pos must be a wordnet.ADV, wordnet.NOUN, wordnet define etc.
# have to parse in a prefix due to proxy classes not resolving to object class
# i.e. obj = str(wordnet) 
#      obj = '<WordNetCorpusReader in '/home/charl/nltk_data/corpora/wordnet'>'
#      should or looking for a way to just retrieve 'wordnet'
def get_callables(input_class_str, skip = '^__'):
    # fetch the methods
    for method in get_methods(eval(input_class_str)):
        if (not re.match(skip, str(method))):
            full_input_class_str_str = str(''.join([input_class_str,'.', method]))
            #full_input_class_str_str = full_input_class_str_str.replace('__main__.', '')
            full_input_class_str = eval(full_input_class_str_str)
            argspec = get_args(full_input_class_str)
            # defaults are going to have to be assisgned in the generated callable
            # as functions are always going to specify full parameter sets
            if (argspec['defaults']):
              print full_input_class_str_str, '(', ', '.join(argspec['args']), ')', ' :', argspec['defaults']
            else:
              print full_input_class_str_str, '(', ', '.join(argspec['args']), ')'



