from django.shortcuts import redirect, render # Render html code
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.http import HttpResponse
from ..main.models import Voluntary, Organization, Event, Voluntary_Events

# Create your views here.
def loadView(request):
    context = {}
    if request.user.is_authenticated:
        context = {'authentication' : 'true'}
    
    event_id = request.GET.get('event_id')
    event = Event.objects.filter(id=event_id)
    if not event:
        return redirect('index')
    context.update({'event': event})

    if request.method == 'POST':
        user = Voluntary.objects.get(email=request.user)
        event2 = Event.objects.get(id=event_id)
        if Voluntary_Events.objects.filter(voluntaryId=user, eventId = event2).count() == 0:
            volEvent = Voluntary_Events.objects.create(eventId = event2, voluntaryId = user)
            volEvent.save()
        else:
            Voluntary_Events.objects.filter(voluntaryId=user, eventId = event2).delete()
            context.update({'messages': 'success', 'message_info': 'Operação concluída com sucesso'})

    # User is a voluntary
    if Voluntary.objects.filter(email=request.user):
        user = Voluntary.objects.get(email=request.user).id
        event2 = Event.objects.get(id=event_id)
        if Voluntary_Events.objects.filter(voluntaryId=user, eventId = event2).count() == 0:
            context.update({'can_register': 'yes'})
        else: 
            context.update({'can_register': 'no'})
            context.update({'messages': 'success', 'message_info': 'Já se encontra inscrito neste evento'})
    else:
        context.update({'can_register': 'no'})
        context.update({'messages': 'warning', 'message_info': 'Não está registado como voluntário'})

    # Vacancy
    vacancy = Event.objects.get(id=event_id).totalVoluntarys - Voluntary_Events.objects.filter(eventId=event_id).count()
    context.update({'vacancy': vacancy})

    #context.update({'messages': 'success', 'message_info': 'Já se encontra inscrito neste evento'})
    #context.update({'messages': 'error', 'message_info': 'Ocorreu um erro ao efetuar a operação'})
    #context.update({'messages': 'warning', 'message_info': 'Não está registado como voluntário'})
    return render(request, 'event.html', context)
    