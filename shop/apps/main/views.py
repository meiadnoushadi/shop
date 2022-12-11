from django.shortcuts import render
from django.conf import settings
# Create your views here.
def index(request):
    context={
       'media_url':settings.MEDIA_URL 
    }
    return render(request,'main/index.html',context)