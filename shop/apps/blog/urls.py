from django.urls import path
import apps.blog.views as views


urlpatterns = [
    path('',views.index)
]
