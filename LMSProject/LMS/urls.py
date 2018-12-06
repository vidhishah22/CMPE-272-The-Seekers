from django.urls import path
from django.conf.urls import url, include
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

urlpatterns = [
    path('TheSeekers/', views.index, name='index'),
    path('TheSeekers/Home', views.Home, name='Home'),
    path('TheSeekers/profile', views.profile, name='profile'),
    path('TheSeekers/ApplyForLeave', csrf_exempt(views.ApplyForLeave), name='ApplyForLeave'),
    path('TheSeekers/ApproveLeave', csrf_exempt(views.ApproveLeave), name='ApproveLeave'),
    #path('TheSeekers/EditEmployee', views.EditEmployee, name='EditEmployee'),
    #path('TheSeekers/AddEmployee', csrf_exempt(views.EditEmployee), name='AddEmployee'),
    #path('TheSeekers/DeleteEmployee', csrf_exempt(views.EditEmployee), name='DeleteEmployee'),
    url('login/', views.login),
    url('complete/auth0', views.auth0),
    url(r'^profile', views.profile),
    #url(r'^logout', views.logout, name='logout'),
    path('TheSeekers/login/Auth0', views.logout, name='logout'),
]