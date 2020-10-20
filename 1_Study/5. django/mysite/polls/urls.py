from django.urls import path

from . import views

uurlpatterns = [
    path('', views.index, name='index')
]