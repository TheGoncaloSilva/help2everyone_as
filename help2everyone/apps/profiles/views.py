from django.shortcuts import redirect, render # Render html code
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import auth, User
from ..main.models import Voluntary, Organization, Event
from .forms import RegisterEvent
import datetime
from django import forms

# Create your views here.
def say_hello(request):
    # pull data from db, transform, send emil...
    return HttpResponse('Hello World')

def org_profile(request):
    context = {}
    if request.method == 'POST':
        registerEventForm = RegisterEvent(request.POST, request.FILES)
        # check whether it's valid:
        if registerEventForm.is_valid():
            form = registerEventForm.cleaned_data
            print(form)
            org_email = form['emailOrg']
            org = Organization.objects.filter(email=org_email)
            if not org:
                return redirect('index')
            else:
                context.update({'profile_org': org})
                
                if form['eventMainImage'] is None:
                    event = Event.objects.create(eventName = form['eventName'], 
                            shortDescription = form['shortDescription'],
                            description = form['description'],
                            totalVoluntarys = form['totalVoluntarys'],
                            hours = form['hours'],
                            address = form['address'],
                            zipCode = form['zipCode'],
                            district = form['district'],
                            county = form['county'],
                            parish = form['parish'],
                            country = form['country'],
                            startDate = form['startDate'],
                            endDate = form['endDate'],
                            idOrganization = org[0]
                            )
                else:
                    event = Event.objects.create(eventMainImage = request.FILES.get('eventMainImage'),
                            eventName = form['eventName'], 
                            shortDescription = form['shortDescription'],
                            description = form['description'],
                            totalVoluntarys = form['totalVoluntarys'],
                            hours = form['hours'],
                            address = form['address'],
                            zipCode = form['zipCode'],
                            district = form['district'],
                            county = form['county'],
                            parish = form['parish'],
                            country = form['country'],
                            startDate = form['startDate'],
                            endDate = form['endDate'],
                            idOrganization = org[0]
                            )

                event.save()
                return redirect('org_profile?org_email=%s' % org_email)


        else:
            pass #-> error
    else: 
        org_email = request.GET.get('org_email')
        org = Organization.objects.filter(email=org_email)
        if not org:
            return redirect('index')
        context.update({'profile_org': org})
    #print(getattr(org[0], 'orgName'))

    # Associated events
    events = Event.objects.filter(idOrganization = org[0])
    if events:
        context.update({'events': events})

    # Create event form
    form = RegisterEvent(initial = {"emailOrg": getattr(org[0], 'email')})
    context.update({'form': form})

    return render(request, 'profile_org.html', context)

def vol_profile(request):
    return HttpResponse('Voluntary Profile')
