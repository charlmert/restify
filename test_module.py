#!/bin/env python

import os, sys
sys.path.append('/home/charl/study/python/test_module')
import test_module

# sys.path.append('/usr/local/django/grammar/grammar/') # not loading here for some reason
sys.path.append('/home/charl/study/python/grammar/')
import grammar
from grammar import settings

print 'loaded grammar :Y'
print grammar.settings.TIME_ZONE
from test_module import settings
from test_module.settings import the_settings
print "settings.the_settings" # specific
print settings.the_settings
print "the_settings" # vague
print the_settings
