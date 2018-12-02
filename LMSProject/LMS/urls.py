from django.urls import path

from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('TheSeekers/', views.index, name='index'),
    path('TheSeekers/Home', views.Home, name='Home'),
    path('TheSeekers/profile', views.profile, name='profile'),
    path('TheSeekers/ApplyForLeave', csrf_exempt(views.ApplyForLeave), name='ApplyForLeave'),
    path('TheSeekers/ApproveLeave', views.ApproveLeave, name='ApproveLeave'),
    #path('TheSeekers/EditEmployee', views.EditEmployee, name='EditEmployee'),
    #path('TheSeekers/AddEmployee', csrf_exempt(views.EditEmployee), name='AddEmployee'),
    #path('TheSeekers/DeleteEmployee', csrf_exempt(views.EditEmployee), name='DeleteEmployee'),
]
