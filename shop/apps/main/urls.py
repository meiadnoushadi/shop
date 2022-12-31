from django.urls import path
import apps.main.views as views

urlpatterns = [
    path('',views.index,name='home'),
]


