import os
from django.shortcuts import render # Render html code
from django.http import HttpResponse
from django.contrib.staticfiles import finders

from help2everyone.settings import BASE_DIR, MEDIA_ROOT, PROJECT_ROOT, STATIC_ROOT, STATIC_URL

# Create your views here.
def say_hello(request):
    # pull data from db, transform, send emil...
    return HttpResponse('Hello World')

def test(request):
    # pull data from db, transform, send emil...
    context = {'value' : ['good', 'meh', 'bad']}
    return render(request, 'test.html', context)

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def events(request):
    return render(request, 'events.html')

def contact(request):
    return render(request, 'contact.html')
