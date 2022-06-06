from django.shortcuts import render # Render html code
from django.http import HttpResponse

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
