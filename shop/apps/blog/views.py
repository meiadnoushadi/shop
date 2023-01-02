from django.shortcuts import render
from django.conf import settings
from django.http import Http404
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

def autherDetail(request,auther_id):
    try:
        auther=Auther.objects.get(id=auther_id)
    except:
        raise Http404("صفحه مورد نظر شما یافت نشد")
    context={
        'media_url':settings.MEDIA_URL,
        'auther':auther
    }
    return render(request,'blog/autherDetial.html',context)