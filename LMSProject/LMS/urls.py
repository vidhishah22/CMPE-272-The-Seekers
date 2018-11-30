from django.urls import path

from . import views

urlpatterns = [
    path('TheSeekers/', views.index, name='index'),
    path('TheSeekers/base', views.base, name='base'),
    path('TheSeekers/Home', views.Home, name='Home'),
    path('TheSeekers/profile', views.profile, name='profile'),
    path('TheSeekers/ApplyForLeave', views.ApplyForLeave, name='ApplyForLeave'),
    path('TheSeekers/ApproveLeave', views.ApproveLeave, name='ApproveLeave'),
    path('TheSeekers/EditEmployee', views.EditEmployee, name='EditEmployee'),
]
