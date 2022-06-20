from django.shortcuts import redirect, render # Render html code
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import Event
from .models import Voluntary, Organization

# Create your views here.
def say_hello(request):
    # pull data from db, transform, send emil...
    return HttpResponse('Hello World')

def test(request):
    # pull data from db, transform, send emil...
    context = {'value' : ['good', 'meh', 'bad']}
    return render(request, 'test.html', context)

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        context = {'authentication' : 'true'}
        vol = Voluntary.objects.filter(email=request.user)
        org = Organization.objects.filter(email=request.user)
        if vol:
            context.update({'session_vol': vol})
        if org:
            context.update({'session_org': org})

        return render(request, 'index.html', context)

def about(request):
    if not request.user.is_authenticated:
        return render(request, 'about.html')
    else:
        context = {'authentication' : 'true'}
        vol = Voluntary.objects.filter(email=request.user)
        org = Organization.objects.filter(email=request.user)
        if vol:
            context.update({'session_vol': vol})
        if org:
            context.update({'session_org': org})

        return render(request, 'about.html', context)

def blog(request):
    if not request.user.is_authenticated:
        return render(request, 'blog.html')
    else:
        context = {'authentication' : 'true'}
        vol = Voluntary.objects.filter(email=request.user)
        org = Organization.objects.filter(email=request.user)
        if vol:
            context.update({'session_vol': vol})
        if org:
            context.update({'session_org': org})

        return render(request, 'blog.html', context)

def events(request):
    context = {}
    if request.user.is_authenticated:
        context = {'authentication' : 'true'}
        vol = Voluntary.objects.filter(email=request.user)
        org = Organization.objects.filter(email=request.user)
        if vol:
            context.update({'session_vol': vol})
        if org:
            context.update({'session_org': org})
    if request.method == 'POST':
        text = request.POST['filtnome']
        select = request.POST['filt_select']
        if select == '1':
            events = Event.objects.filter(eventName=text)
        elif select == '2':
            events = Event.objects.filter(country=text)
        elif select == '3':
            events = Event.objects.filter(district=text)
        elif select == '4':
            events = Event.objects.filter(county=text)
        elif select == '5':
            events = Event.objects.filter(parish=text)
        elif select == '6':
            events = Event.objects.filter(totalVoluntarys=text)
        elif select == '7':
            events = Event.objects.filter(hours=text)
        else:
            events = None

    else:
        events = Event.objects.all()

    if events:
        context.update({'events' : events})
    return render(request, 'events.html', context)

def contact(request):
    if not request.user.is_authenticated:
        return render(request, 'contact.html')
    else:
        context = {'authentication' : 'true'}
        vol = Voluntary.objects.filter(email=request.user)
        org = Organization.objects.filter(email=request.user)
        if vol:
            context.update({'session_vol': vol})
        if org:
            context.update({'session_org': org})
            
        return render(request, 'contact.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')
