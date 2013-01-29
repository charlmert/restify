import nltk
from nltk.corpus import wordnet
import pprint
import os, sys
sys.path.append('/home/charl/study/python')

from introspection import Types

# Create your views here.
from django.shortcuts import render_to_response, render # render_to_response('rest/hi')

#from django.core.handlers import wsgi
from django.http import HttpResponse

# return a direct response (without templating) which should be quicker
def raw(request):
    http = HttpResponse()
    http.write('hello')
    return http

# return a response via the template engine route
def home(request):
    return render_to_response('rest/hi.html')

# http://localhost:8000/morphy/verified
def morphy(request, word="balled"):
    http = HttpResponse()
    morphed = str(wordnet.morphy(word))
    http.write(''.join(['wordnet.morphy(', word, '): ', morphed]))
    return http

# http://localhost:8000/kwargs/content/the%20content/defaults/the%20defaults
def kwargs(request, kwargs):
    http = HttpResponse()
    parts = kwargs.split('/')
    
    # validity check (if the number of kwargs isn't even then 
    # a value has been omitted from a keyword
    if (len(parts) % 2 != 0):
        http.write("error: the amount of arguments don't amount to an even number, /value has been omitted")
        return http

    # parsing the keyword value here
    kv = {}
    for counter in range(0,len(parts)):
        if (counter % 2 == 0):
            kv[parts[counter]] = parts[counter+1]

    http.write(pprint.pformat(kv))
    return http

