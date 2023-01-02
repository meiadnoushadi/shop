from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Auther)
class AutherAdmin(admin.ModelAdmin):
    list_display=('id','name','family','age','email','register_date','is_active')
    list_filter=('family','is_active')
    search_fields=('family','name')
    ordering=['family','name']
    prepopulated_fields={'sulg':('name','family')}

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('id','article_title','create_at','published_at','updated_at','status','is_active')
    list_filter=('article_title','is_active')
    search_fields=('article_title','create_at')
    ordering=['article_title','status']

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display=('cheifEditor_id','title')

@admin.register(ChiefEditor)
class ChiefEditorAdmin(admin.ModelAdmin):
    list_display=('id','name','family','publication')

