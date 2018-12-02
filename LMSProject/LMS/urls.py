from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('TheSeekers/', views.index, name='index'),
    #path('TheSeekers/getprofile', views.profile, name='profile'),
    #path('TheSeekers/', views.index, name='index'),
    #url('^$', views.index),
    url('login/', views.login),
    #url(r'^test', views.test),
    url('complete/auth0', views.auth0),
    url(r'^profile', views.profile),
    url(r'^logout', views.logout, name='logout'),
]