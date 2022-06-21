# This file works in conjunction with the urls.py file in the help2everyone project folder, in order
#to handle HTTP requests
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello', views.hello , name='hello'),

    path('', views.chooselog , name='chooselog'),
    path('chooselog', views.chooselog , name='chooselog'),
    path('chooselog.html', views.chooselog , name='chooselog'),

    path('login_vol', views.login_vol , name='login_vol'),
    path('login_vol.html', views.login_vol , name='login_vol'),

    path('register_vol', views.register_vol , name='register_vol'),
    path('register_vol.html', views.register_vol , name='register_vol'),

    path('login_org', views.login_org , name='login_org'),
    path('login_org.html', views.login_org , name='login_org'),

    path('register_org', views.register_org , name='register_org'),
    path('register_org.html', views.register_org , name='register_org'),

]