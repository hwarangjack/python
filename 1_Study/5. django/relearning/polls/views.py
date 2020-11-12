from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    # Polls.models.py에서 정의된 Quesition 객체(Question.objects.all())를 date라는 컬럼 5개를 정렬해서 구성하여 변수에 할당
    # Question 클래스는 Models.model 를 상속했으므로, 사실상 objects.all() 함수는 Models.model의 함수임
    instance_question_list = Question.objects.all().order_by('-date')[:5]
    
    # 실제 값이 할당된 객체 instance_Question_list를 // template에서 사용할 template_question_list에 //매핑(매칭)하라는 명령어 //를 context라는 변수에 부여
    context = {'template_question_list':instance_question_list} 
    
    #결과를 방출하되(render(request, ..), 템플릿 위치(polls\teamplate\polls\index.html에서 template 이하만 지정)를 지정하고, 그 템플릿에는 매칭(매핑)된 내용을 적용하라
    return render(request, 'polls/index.html', context) 
    


def detail(request, question_id):   #detail에 연결되기 전 url에서는 <int:question_id>로 설정하여, url 매칭시 question_id라는 인자값을 전달토록 되어 있음
    # get_object_or_404 호출 : django.shortcuts에서 render와 함께 호출 필요.
    # get_object_or_404 사용 : 첫번째 인자는 Model.py의 클래스(또는 함수) 명칭(Question)[=데이터베이스의 테이블명]이고, 두번쨰 인자값은 검색조건을 의미함.
    # get_object_or_404 역활 : 모델(테이블명)과 그 조건에 따라 검색한 결과(객체, Row)를 할당하라
    instance_detail_question = get_object_or_404(Question, pk=question_id)

    # 실제 값이 할당된 객체 instance_detail_question를 // template에서 사용할 teamplate_detail_question에 매핑(매칭)하고 // detail.html로 이동하라
    return render(request, 'polls/detail.html', {'template_detail_question':instance_detail_question})

def vote(request):
    return hello