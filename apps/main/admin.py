from django.contrib import admin
from .models import Voluntary, Organization, Event, Voluntary_Events

# Register your models here.
admin.site.register(Voluntary)
admin.site.register(Organization)
admin.site.register(Event)
admin.site.register(Voluntary_Events)