from django.shortcuts import render

# Create your views here.
def blog_index(request):
    context={
        
    }
    return render(request,'blog/blogIndex.html',context)