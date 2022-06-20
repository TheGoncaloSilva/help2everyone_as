# This file works in conjunction with the urls.py file in the help2everyone project folder, in order
#to handle HTTP requests
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('org', views.say_hello, name='hello'),
    path('', views.say_hello, name='profiles'),
    path('org_profile', views.org_profile, name='org_profile'),

    path('vol_profile', views.vol_profile, name='vol_profile'),
]
