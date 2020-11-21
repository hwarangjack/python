from django.shortcuts import render, HttpResponse
from .forms import post_form
from .models import post

def blog_home(request):
    post_all = post.objects.all()
    img = post.picture
    context = {
        'post_all':post_all,
        'img':img
    }
    return render(request, 'blog/home.html', context)


def blog_postform(request):
    form = post_form()
    context = {
        'form':form,
    }
    return render(request, 'blog/form.html', context)



def blog_postcreate(request):
    if request.method == 'POST':
        form = post_form(request.POST, request.FILES)  # 단순 Post 가 아닌 FIles 도 포함하는 POST의 경우에는 request.FILES 필요한 듯
        if form.is_valid():
            post.objects.create(**form.cleaned_data)
            
    context = {
        'form':form,
    }
    return render(request, 'blog/create.html', context)
