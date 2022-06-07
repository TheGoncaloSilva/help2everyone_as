from django.shortcuts import redirect, render # Render html code
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.http import HttpResponse
from ..main.models import Voluntary, Organization

# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

def chooselog(request):
    return render(request, 'chooselog.html')

def login_vol(request):
    if request.method == 'POST':
        email = request.POST['email']
        passw = request.POST['password']
        if(Voluntary.objects.filter(email=email, password = passw)):
            return redirect('index')
        else:
            context = {'messages': ['Email ou Password incorretos']}
            return render(request, 'login_vol.html', context)
    else:
        return render(request, 'login_vol.html')

def login_org(request):
    if request.method == 'POST':
        email = request.POST['Email']
        passw = request.POST['Password']
        if(Organization.objects.filter(email=email, password = passw)):
            return redirect('index')
        else:
            context = {'messages': ['Email ou Password incorretos']}
            return render(request, 'login_org.html', context)
    else:
        return render(request, 'login_org.html')