from django.urls import path
from apps.blog.views import *


urlpatterns = [
    path('',blog_index,name='blog'),
    path('auther/',auther_list,name='auther_list')
]
