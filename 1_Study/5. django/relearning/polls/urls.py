from django.urls import path

# 해당 App에서의 url은 Views.py로 연결하므로, Views 파일을 임포트

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create/question', views.CreateQuestion, name='createquestion'),
    path('create/choice', views.CreateChoice, name='createchoice'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
]
