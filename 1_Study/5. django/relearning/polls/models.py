from django.db import models

# 모델에서는 Database에 등록시킬 테이블을 생성한다
# 테이블은 함수 또는 클래스로 생성한다

class Question(models.Model):   # 클래스로 생성한 테이블
                                                      # 사용자 정의가 없어도 Primary key(id)는 자동 생성되고 기본값(1)으로된다(panda에서 index 역활)
    question_text = models.CharField(max_length=200)  # 변수는 컬럼명이 된다
    date = models.DateTimeField('when you register this question')  #사이트에 보이는 문자는 기본적으로 변수(칼럼명)로 하되, 별도 문자입력시 해당내용으로 적용

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

