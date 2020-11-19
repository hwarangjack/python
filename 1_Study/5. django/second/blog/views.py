from django.shortcuts import render, HttpResponse
from .forms import post_form
from .models import post

# Create your views here.

def blog_home(request):
    return HttpResponse('<h6>햇님이의 블로그에 오신 것을 환영합니다')


def blog_create(request):
    form = post_form()
    if request.method == 'POST':
        form = post_form(request.POST)

        if form.is_valid():
            post.objects.create(form.cleaned_data)
            form = post_form()

        else:
            print(form.errors)
    
    return render(request, 'create.html', {})

