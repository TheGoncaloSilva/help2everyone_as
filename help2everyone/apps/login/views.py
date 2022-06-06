from django.shortcuts import render # Render html code
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

def chooselog(request):
    return render(request, 'chooselog.html')

def login_vol(request):
    return render(request, 'login_vol.html')

def login_org(request):
    return render(request, 'login_org.html')