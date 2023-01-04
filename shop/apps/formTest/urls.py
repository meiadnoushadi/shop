from django.urls import path,re_path
from apps.formTest.views import *

urlpatterns = [
    path('form/',form,name='sign-up'),
    path('form0/',form0,name='sign-up0'),
    path('form1/',form1,name='sign-in'),
]
