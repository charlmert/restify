import os, sys 
# module/ must contain __init__.py
# sys.path.append('/path/to/your/module/')
import django

print "::ModuleFinder::"
# use modulefinder to ensure import
from modulefinder import ModuleFinder

finder = ModuleFinder()

print 'Loaded modules:'
for name, mod in finder.modules.iteritems():
    print '%s: ' % name,
    print ','.join(mod.globalnames.keys()[:3])

print '-'*50
print 'Modules not imported:'
print '\n'.join(finder.badmodules.iterkeys())
