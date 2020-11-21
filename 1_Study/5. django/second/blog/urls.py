from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_home, name='home'),
    path('postform/', views.blog_postform, name='postform'),
    path('postform/postcreate', views.blog_postcreate, name='postcreate'),
]
