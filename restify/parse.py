import re
import pprint
import logging
logging.basicConfig(filename='/tmp/test.log', level=logging.DEBUG)

# Types.method_int
#argspec_str = "ArgSpec(args=['self', 'number'], varargs=None, keywords=None, defaults=None)"

# Types.method_kwargs
argspec_str = "ArgSpec(args=['self', 'var1'], varargs='args', keywords='kwargs', defaults=('1',))"

# wordnet.morphy
#argspec_str = "ArgSpec(args=['self', 'form', 'pos'], varargs=None, keywords=None, defaults=(None,))"

# takes "'self', 'var1'", stripped "args=['self', 'var1'],"
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
        keys.append(part)
        
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
    argspec_ret['defaults'] = defaults

    return argspec_ret

if __name__ == '__main__':
    argspec = parse_argspec(argspec_str)
    if (not argspec):
        logging.error(''.join(['not a valid argspec: ', argspec]))
        print 'error: not a valid argspec:', argspec

    print pprint.pformat(argspec)
