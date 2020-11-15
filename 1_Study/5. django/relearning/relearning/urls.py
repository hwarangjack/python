from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),    # polls로 시작하는 url을 받았을 경우에는 일괄 polls App에 있는 urls에서 처리하라는 의미// Apps로의 이동은 include 함수 사용함
]
