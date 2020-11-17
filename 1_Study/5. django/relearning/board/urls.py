from django.urls import path

# 해당 App에서의 url은 Views.py로 연결하므로, Views 파일을 임포트

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.board, name='index_page'),
    path('create/', views.create, name='create'),
    path('create/raw', views.Rawcreate, name='rawcreate'),
]
