from django.shortcuts import render
from django.conf import settings
from .models import Auther
# Create your views here.
def blog_index(request):
    context={
    }
    return render(request,'blog/blogIndex.html',context)

def auther_list(request):
    auhterAll=Auther.objects.all()
    context={
        'autherAll':auhterAll,
        'media_url':settings.MEDIA_URL,
    }
    return render(request,'blog/autherList.html',context)