import nltk
from nltk.corpus import wordnet

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

def morphy(request, word="balled"):
    http = HttpResponse()
    morphed = str(wordnet.morphy(word))
    http.write(''.join(['wordnet.morphy(', word, '): ', morphed]))
    return http
