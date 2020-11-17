from django.shortcuts import render
from .models import register
from .froms import resisterForm, RawResisterForm



def board(request):
    subject = register.objects.all()
    context = {
        'subject':subject,
    }
    return render(request, 'board/detail.html', context)

def create(request):
    form = resisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = resisterForm()
        
    context = {
        'form':form,
    }
    return render(request, 'board/create_board.html', context)


def Rawcreate(request):
    form = RawResisterForm()
    if request.method == "POST":
        form = RawResisterFrom(request.POST)

        if form.is_valid():
            register.objects.create(form.cleaned_data)
            form = RawResisterForm()
        else:
            print(form.errors)

    context = {
        'form':form,
    }
    return render(request, 'board/rawcreate_board.html', context)

