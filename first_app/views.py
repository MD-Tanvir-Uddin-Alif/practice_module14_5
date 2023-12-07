from django.shortcuts import render
from .forms import Account
from .import models
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = Account(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = Account()
    return render(request,"home.html",{'form':form})

def modal(request):
    student = models.student.objects.all()
    return render(request,"modal.html",{'data' : student})
