from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_home, name='home'),
    path('create/', views.blog_create, name='create')
]
