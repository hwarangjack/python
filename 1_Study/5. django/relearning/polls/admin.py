from django.contrib import admin


# 어드민과 관련하여 테이블도 임포트 사전에 임포트 해야, 어드민에서 사용 가능함
# from 폴더.파일명 import 클래스명/함수명(=테이블명)

from polls.models import Question, Choice

# Admin.site.resiger(테이블명)을 사용하여 어드민 홈페이지에 DB에 등록된 테이블을 등록시킨다. 
admin.site.register(Question)
admin.site.register(Choice)