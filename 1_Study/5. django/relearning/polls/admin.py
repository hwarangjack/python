from django.contrib import admin
# 어드민과 관련하여 테이블도 임포트 사전에 임포트 해야, 어드민에서 사용 가능함
# from 폴더.파일명 import 클래스명/함수명(=테이블명)

from polls.models import Question, Choice

# class choice_in_line(admin.StackedInline):
#     model=Choice
#     extra=2

class choice_in_line(admin.TabularInline):
    model=Choice
    extra=2

class questionadmin(admin.ModelAdmin):
    fieldsets = [
        ('question state', {'fields':['question_text']}),
        ('date information', {'fields':['date'], 'classes':['collapse']}),
    ]

    # admin 사이트에서 칼럼명을 보이도록 하기
    list_display = ('question_text','date')

    # admin 사이트 우측에 옵션제공
    list_filter = ['date']

    # admin 사이트에 검색어 입력하기 (검색기준 칼럼)
    search_fields = ['question_text']

    # admin 사이트에서 choice 모델도 함께보기
    inlines=[choice_in_line]

    


# Admin.site.resiger(테이블명)을 사용하여 어드민 홈페이지에 DB에 등록된 테이블을 등록시킨다. 
admin.site.register(Question, questionadmin)
admin.site.register(Choice)