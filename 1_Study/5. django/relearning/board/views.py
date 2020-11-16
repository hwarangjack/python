from django.shortcuts import render
from .models import register
from .froms import resisterForm


def create(request):
    form = resisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = resisterForm()
        
    context = {
        'form':form,
    }
    return render(request, 'board/create_board.html', context)



def board(request):
    subject = register.objects.get(pk=1)
    context = {
        'subject':subject,
    }
    return render(request, 'board/detail.html', context)

