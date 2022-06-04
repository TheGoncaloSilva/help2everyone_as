# This file works in conjunction with the urls.py file in the help2everyone project folder, in order
#to handle HTTP requests
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello', views.say_hello),
    path('', views.index),
]
