from django.urls import include, path
from . import views

urlpatterns = [
    #/TwitterApi/TheSeekers/
    path('TheSeekers/', views.getusertweets, name='getusertweets'),
    ]