from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('TheSeekers/', views.index, name='index'),
    path('TheSeekers/getprofile', views.profile, name='profile'),
    #path('TheSeekers/', views.index, name='index'),
    #url('^$', views.index),
    url(r'^dashboard', views.dashboard),
    url(r'^test', views.test),
    url('login/', views.login),
    url('complete/auth0', views.auth0)
    #url(r'^', include(('django.contrib.auth.urls', 'auth'), namespace='auth')),
    #url(r'^', include(('social_django.urls', 'social'), namespace='social')),
]