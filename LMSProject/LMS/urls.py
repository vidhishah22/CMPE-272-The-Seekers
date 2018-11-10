from django.urls import path

from . import views

urlpatterns = [
    path('TheSeekers/', views.index, name='index'),
]