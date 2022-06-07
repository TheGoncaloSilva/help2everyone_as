#to handle HTTP requests
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.loadView , name='event'),
]