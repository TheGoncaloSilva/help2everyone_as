from django.shortcuts import render # Render html code
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    # pull data from db, transform, send emil...
    return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html')
