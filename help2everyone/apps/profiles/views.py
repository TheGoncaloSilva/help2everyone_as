from django.shortcuts import redirect, render # Render html code
from django.http import HttpResponse
from django.contrib.auth import logout
from ..main.models import Voluntary, Organization, Event

# Create your views here.
def say_hello(request):
    # pull data from db, transform, send emil...
    return HttpResponse('Hello World')

def org_profile(request):
    org_email = request.GET.get('org_email')
    org = Organization.objects.filter(email=org_email)
    context = {}
    if not org:
        return redirect('index')
    context.update({'profile_org': org})
    #print(getattr(org[0], 'orgName'))

    # Associated events
    events = Event.objects.filter(idOrganization = org[0])
    print(getattr(events[0], 'eventName'))
    if events:
        context.update({'events': events})

    



    return render(request, 'profile_org.html', context)

def vol_profile(request):
    return HttpResponse('Voluntary Profile')
