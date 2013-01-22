import inspect
import re
import pprint

import logging
logging.basicConfig(filename='/tmp/introspection.log', level=logging.DEBUG)

# input, introspection takes imported modules/classes as input
import nltk
from nltk.corpus import wordnet

__doc__ = """
    Uses eval and inspect to assist the developer with evaluating methods for whilst
    building django REST interfaces to given classes or object's methods.
"""

class Types:
    member_int = 32
    def method_int(self, number):
        self.member_int += number
        return self.member_int

    def method_kwargs(self, var1='1', *args, **kwargs):
        self.member_int += number
        return self.member_int

# introspect any object/class to find out
# - What the immediate members are (minus defaults and builtins)
# - What the immediate methods are
# - What the arguments to those methods are
# - Whats required to reconstruct calling this from code 
# - What the documentation for members and methods are


# method to parse the argument spec
# takes an argspec e.g. for wordnet.morphy
# argspec = "ArgSpec(args=['self', 'form', 'pos'], varargs=None, keywords=None, defaults=(None,))"

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
    defaults = defaults.replace(",))", '')
    defaults = defaults.replace("(", '')
    defaults = defaults.split(",")
    argspec_ret['defaults'] = defaults

    return argspec_ret

def getmethods(obj):
    # fetch the methods
    for method in inspect.getmembers(obj, predicate=inspect.ismethod):
        print method[0]

# return method strings as callables
# something that can be eval'd to return a response
# research> some arguments can be populated via dropdown
#           e.g. wordnet.morphy(form, pos)
#           pos must be a wordnet.ADV, wordnet.NOUN, wordnet define etc.
# have to parse in a prefix due to proxy classes not resolving to object class
# i.e. obj = str(wordnet) 
#      obj = '<WordNetCorpusReader in '/home/charl/nltk_data/corpora/wordnet'>'
#      should or looking for a way to just retrieve 'wordnet'
def getcallables(obj, prefix_str, skip = '^__'):
    # fetch the methods
    for method in inspect.getmembers(obj, predicate=inspect.ismethod):
        if (not re.match(skip, str(method[0]))):
            full_obj_str = str(''.join([prefix_str,'.', method[0]]))
            #full_obj_str = full_obj_str.replace('__main__.', '')
            full_obj = eval(full_obj_str)
            argspec = getargs(full_obj)
            args = argspec['args']
            args.reverse()
            args.pop() # removing self
            args.reverse()

            # defaults are going to have to be assisgned in the generated callable
            # as functions are always going to specify full parameter sets
            print full_obj_str, '(', ', '.join(args), ')'

def getargs(method):
    if (not inspect.ismethod(method)):
        raise Exception(''.join([method, ' is not a method']))
    # fetch the argspec
    argspec_str = str(inspect.getargspec(method))
    argspec = parse_argspec(argspec_str)

    return argspec

# not all objects have a name but those that do store it in the __name__ attribute.
def main():

    # retrieving methods and their arguments as callables
    #getmethods(Types, 'Types')
    #getcallables(Types, 'Types')
    #getmethods(wordnet)
    getcallables(wordnet, 'wordnet', '^_')

    # demo the argspec parser
    args = getargs(Types.method_int)
    if (args == False):
        logging.error(''.join(['not a valid argspec: ', argspec]))
        print 'error: not a valid argspec:', argspec

    #print pprint.pformat(args)

    args = getargs(Types.method_kwargs)
    if (args == False):
        logging.error(''.join(['not a valid argspec: ', argspec]))
        print 'error: not a valid argspec:', argspec

    #print pprint.pformat(args)

    args = getargs(wordnet.morphy)
    if (args == False):
        logging.error(''.join(['not a valid argspec: ', argspec]))
        print 'error: not a valid argspec:', argspec

    #print pprint.pformat(args)

# splitting runnable from module behavior
# e.g. 
# python introspection.py will run main()
#     VS
# import introspection will bypass main()

if __name__ == '__main__':
    main()

# id(object) -> integer\n\nReturn the identity of an object.  This is guaranteed to be unique among\nsimultaneously existing objects.  (Hint: it's the object's memory address.)

# hasattr(object, name) -> bool\n\nReturn whether the object has an attribute with the given name.\n(This is done by calling getattr(object, name) and catching exceptions.)

# getattr(object, name[, default]) -> value\n\nGet a named attribute from an object; getattr(x, 'y') is equivalent to x.y.\nWhen a default argument is given, it is returned when the attribute doesn't\nexist; without it, an exception is raised in that case.

# callable(object) -> bool\n\nReturn whether the object is callable (i.e., some kind of function).\nNote that classes are callable, as are instances with a __call__() method.

# isinstance(object, class-or-type-or-tuple) -> bool\n\nReturn whether an object is an instance of a class or of a subclass thereof.\nWith a type as second argument, return whether that is the object's type.\nThe form using a tuple, isinstance(x, (A, B, ...)), is a shortcut for\nisinstance(x, A) or isinstance(x, B) or ... (etc.).

# issubclass(C, B) -> bool

# Return whether class C is a subclass (i.e., a derived class) of class B.
# When using a tuple as the second argument issubclass(X, (A, B, ...)),
# is a shortcut for issubclass(X, A) or issubclass(X, B) or ... (etc.).


