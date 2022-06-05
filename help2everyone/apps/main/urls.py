# This file works in conjunction with the urls.py file in the help2everyone project folder, in order
#to handle HTTP requests
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello', views.say_hello, name='hello'),
    path('test', views.test, name='test'),

    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('index.html', views.index, name='index'),

    path('about', views.about, name='about'),
    path('about.html', views.about, name='about'),

    path('blog', views.blog, name='blog'),
    path('blog.html', views.blog, name='blog'),

    path('events', views.events, name='events'),
    path('events.html', views.events, name='events'),

    path('contact', views.contact, name='contact'),
    path('contact.html', views.contact, name='contact'),
]
