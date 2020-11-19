from django.shortcuts import render, HttpResponse
from .forms import post_form
from .models import post

# Create your views here.

def blog_home(request):
    post_all = post.objects.all()
    context = {
        'post_all':post_all
    }
    return render(request, 'blog/home.html', context)


def blog_create(request):
    form = post_form()

    if request.method == 'POST':
        form = post_form(request.POST)
        if form.is_valid():
            post.objects.create(**form.cleaned_data)
            form = post_form()
            
    context = {
        'form':form,
    }
    return render(request, 'blog/create.html', context)

