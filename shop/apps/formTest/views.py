from django.shortcuts import render
from .forms import *

# Create your views here.
def form(request):
    return render(request,'formTest/form.html')

def form0(request):
    form=InputForm0()
    context={
        'form':form
    }
    return render(request,'formTest/form0.html',context)


def form1(request):
    form=InputForm1()
    context={
        'form':form
    }
    return render(request,'formTest/form1.html',context)