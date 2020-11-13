from django.shortcuts import render, get_object_or_404
from .models import Question,Choice
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    # get_object_or_404 해석 : 특정한 객체를 가져와라(Try:) 오류가난다면 404에러를 발생시켜라(except:)
        # try : instance_detail_question = Question.obejcts.get(pk=question_id)
        # except : Question.DoesNotExist: Raise http404('question does not exist')
    # get_object_or_404 사용 : 첫번째 인자는 사용하고자 하는 Model.py의 클래스(또는 함수) 명칭(Question)[=데이터베이스의 테이블명]이고, 두번째 인자값은 검색조건을 의미함.
    # get_object_or_404 역활 : 모델(테이블명)과 그 조건에 따라 검색한 결과(객체, Row)를 할당하라
    instance_detail_question = get_object_or_404(Question, pk=question_id)

    # 실제 값이 할당된 객체 instance_detail_question를 // template에서 사용할 teamplate_detail_question에 매핑(매칭)하고 // detail.html로 이동하라
    return render(request, 'polls/detail.html', {'template_detail_question':instance_detail_question})

def vote(request, question_id):
    instance_detail_question = get_object_or_404(Question, pk=question_id)

    try:
        # instance_detail_question이 대상 테이블(이 경우 choice)이 연결(Foreignkey)되어 있는 테이블(choice)에 설정된 DB값을(_set)을 검색하여 가져와라(.get). 검색조건은 Post 제출된 choice의 id에 해당하는 값(Row)
        selected_choice = instance_detail_question.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'poll/detail.html', {'template_detail_question':instance_detail_question})

    else:
        selected_choice.votes += 1
        selected_choice.save()

        # reverse() 함수 : 첫번쨰 인자값 URL 패턴(polls/results) / 두번째 인자값 해당 URL 패턴에서 사용되는 인자값(instance_detail_question.id)
        # reverse() 활용 : 함수에 활용된 URL 스트링으로 사용하여 url로 이동하라
        return HttpResponseRedirect(reverse('polls:results', args=(instance_detail_question.id,)))


def results(request, question_id):
    instance_detail_question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'template_detail_question':instance_detail_question})
