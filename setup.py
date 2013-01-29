#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 John Paulett (john -at- paulett.org)
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from distutils.core import setup
import restify as _restify
import os
import sys

SETUP_ARGS = dict(
    name="restify",
    version=_restify.VERSION,
    description="Python module to produce RESTful interfaces"
                "from existing classes for a target framework e.g. django",
    long_description = _restify.__doc__,
    author="Charl Mert",
    author_email="charl.mert -at- gmail.com",
    url="http://git@github.com/charlmert/restify",
    license="BSD",
    platforms=['POSIX', 'Windows'],
    keywords=['restify', 'rest', 'introspection', 'marshal',
              'serialization', 'django'],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python"
    ],
    options={'clean': {'all': 1}},
    packages=["restify"],
)

def main():
    if sys.argv[1] in ('install', 'build'):
      os.system('cp bin/restify /usr/bin/restify')      
      os.system('chmod 775 /usr/bin/restify')

    setup(**SETUP_ARGS)
    return 0

if __name__ == '__main__':
    sys.exit(main())
