import email
import profile
from django.shortcuts import redirect, render # Render html code
from django.contrib.auth.models import auth, User
from django.contrib.auth import logout, login as auth_login, authenticate
from django.contrib import messages
from django.http import HttpResponse
from ..main.models import Voluntary, Organization
from .forms import RegisterVol, RegisterOrg
import datetime
from django import forms

# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

def chooselog(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'chooselog.html')

def login_vol(request):
    if request.method == 'POST':
        email = request.POST['email']
        passw = request.POST['password']
        user = auth.authenticate(username = email, password = passw)
        if(Voluntary.objects.filter(email=email) and user is not None):
            auth.login(request, user)
            return redirect('index')
        else:
            context = {'messages': ['Email ou Password incorretos']}
            return render(request, 'login_vol.html', context)
    else:
        if request.user.is_authenticated:
            logout(request)
        return render(request, 'login_vol.html')

def login_org(request):
    if request.method == 'POST':
        email = request.POST['Email']
        passw = request.POST['Password']
        user = auth.authenticate(username = email, password = passw)
        if(Organization.objects.filter(email=email) and user is not None):
            auth.login(request, user)
            return redirect('index')
        else:
            context = {'messages': ['Email ou Password incorretos']}
            return render(request, 'login_org.html', context)
    else:
        if request.user.is_authenticated:
            logout(request)
        return render(request, 'login_org.html')

def register_vol(request):
    """errors = ["Utilizador já registado!!!",	"Email já registado!!!"
        "Palavra-Passe fraca!!!", "As Palavras-Passe não coincidem, por favor tente novamente!!!", 
        "Ocorreu um erro ao criar a conta, por favor tente novamente!!!"]"""
    context = {}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        registerVolForm = RegisterVol(request.POST, request.FILES)
        # check whether it's valid:
        if registerVolForm.is_valid() or form['image'] is None:
            form = registerVolForm.cleaned_data
            print(form)
            if User.objects.filter(email=form['email']).exists():
                context.update({'messages': "Email já registado"})
                context.update({'form': RegisterVol(request.POST)})
            elif form['password'] != form['confirmPassword']:
                context.update({'messages': "As Palavras-Passe não coincidem, por favor tente novamente"})
                context.update({'form': RegisterVol(request.POST)})
            elif len(form['password']) < 4:
                context.update({'messages': "Palavra-Passe fraca"})
                context.update({'form': RegisterVol(request.POST)})
            else:
                user = User.objects.create_user(username = form['email'], 
                                            email = form['email'],
                                            first_name = form['firstName'], 
                                            last_name = form['lastName'], 
                                            password = form['password']
                                            )
                user.save()
                if form['image'] is None:
                    vol = Voluntary.objects.create(email = form['email'],
                        firstName = form['firstName'], 
                        lastName = form['lastName'], 
                        registryDate = datetime.date.today(),
                        phoneNumber = form['phoneNumber'],
                        ageOfBirth = form['ageOfBirth']
                        )
                else:
                    vol = Voluntary.objects.create(email = form['email'],
                            profileImg = request.FILES.get('image'),
                            firstName = form['firstName'], 
                            lastName = form['lastName'], 
                            registryDate = datetime.date.today(),
                            phoneNumber = form['phoneNumber'],
                            ageOfBirth = form['ageOfBirth']
                            )

                vol.save()
                return redirect('login_vol')
        
        else:
            print(registerVolForm)
            context.update({'messages': "Ocorreu um erro ao criar a conta, por favor tente novamente"})
    else:
        form = RegisterVol()
        context.update({'form': form})

    return render(request, 'register_vol.html', context)


def register_org(request):
    """errors = ["Utilizador já registado!!!",	"Email já registado!!!"
        "Palavra-Passe fraca!!!", "As Palavras-Passe não coincidem, por favor tente novamente!!!", 
        "Ocorreu um erro ao criar a conta, por favor tente novamente!!!"]"""
    context = {}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        registerOrgForm = RegisterOrg(request.POST, request.FILES)
        # check whether it's valid:
        if registerOrgForm.is_valid() or form['image'] is None:
            form = registerOrgForm.cleaned_data
            print(form)
            if User.objects.filter(email=form['email']).exists():
                context.update({'messages': "Email já registado"})
                context.update({'form': RegisterOrg(request.POST)})
            elif form['password'] != form['confirmPassword']:
                context.update({'messages': "As Palavras-Passe não coincidem, por favor tente novamente"})
                context.update({'form': RegisterOrg(request.POST)})
            elif len(form['password']) < 4:
                context.update({'messages': "Palavra-Passe fraca"})
                context.update({'form': RegisterOrg(request.POST)})
            else:
                user = User.objects.create_user(username = form['email'], 
                                            email = form['email'],
                                            first_name = form['name'], 
                                            password = form['password']
                                            )
                user.save()
                if form['image'] is None:
                    org = Organization.objects.create(orgName = form['name'],
                            email = form['email'],
                            contactNumber = form['contactNumber'],
                            websiteAddress = form['websiteAddress'],
                            foundationDate = form['foundationDate'],
                            registryDate = datetime.date.today(),
                        )
                else:
                    org = Organization.objects.create(orgImg = request.FILES.get('image'),
                            orgName = form['name'],
                            email = form['email'],
                            contactNumber = form['contactNumber'],
                            websiteAddress = form['websiteAddress'],
                            foundationDate = form['foundationDate'],
                            registryDate = datetime.date.today(),
                        )

                org.save()
                return redirect('login_org')

        else:
            print(registerOrgForm)
            context.update({'messages': "Ocorreu um erro ao criar a conta, por favor tente novamente"})
    else:
        form = RegisterOrg()
        context.update({'form': form})

    return render(request, 'register_org.html', context)