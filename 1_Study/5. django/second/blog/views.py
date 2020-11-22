from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import post_form
from .models import post



def blog_home(request):
    post_all = post.objects.all()
    context = {
        'post_all':post_all,
    }
    return render(request, 'blog/home.html', context)




def blog_create(request):

    # 함수를 불러온 방식이 POST 방식이면/ POST된 내용과 파일을 변수에 담고 / 그 변수가 적절한 내용이면 / post라는 Database에 저장하고 / blog:home으로 돌아가라
    if request.method == 'POST':
        form = post_form(request.POST, request.FILES)
        if form.is_valid():
            post.objects.create(**form.cleaned_data)
        
            return redirect('blog:home')
    
    # 함수를 불러온 방식이 POST 방식이 아니라면 / form을 담아 / create.html으로 이동하라
    else:    
        form = post_form()
        context = {
            'form':form,
        }
        return render(request, 'blog/create.html', context)

import os
from django.utils.http import urlquote




def download(request, postnum):
    instance = get_object_or_404(post, pk=postnum) #인수로 넘어온 DB Row 특정
    file_path = instance.Upload_file.url[1:]  #해당 DB row에 기재된 파일경로 특정 // 문자열의 [0]에 해당하는 '/'는 제거하여 path 구성

    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f"attachment;filename*=UTF-8''{os.path.basename(file_path)}"
        return response