from django.db import models
from django.utils import timezone
# Create your models here.
class ChiefEditor(models.Model):
    name=models.CharField(max_length=50,verbose_name='نام')
    family=models.CharField(max_length=50,verbose_name='نام خانوادگی')

    def __str__(self) -> str:
        return f"{self.name} {self.family}"

    class Meta:
        verbose_name='سردبیر'
        verbose_name_plural='سردبیر ها'

class Publication(models.Model):
    title=models.CharField(max_length=100,verbose_name='نام انتشارات')
    cheifEditor=models.OneToOneField(ChiefEditor,on_delete=models.CASCADE,primary_key=True,verbose_name='سردبیر')
    
    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name='نشریه'
        verbose_name_plural='نشریات'


class Auther(models.Model):
    name=models.CharField(max_length=30,verbose_name='نام')
    family=models.CharField(max_length=30,verbose_name='نام خانوادگی')
    sulg=models.SlugField(max_length=100,verbose_name='url آدرس')
    age=models.IntegerField(default=0,verbose_name='سن')
    is_active=models.BooleanField(default=True,verbose_name='فعال/غیرفعال')
    register_date=models.DateTimeField(default=timezone.now,verbose_name='تاریخ ثبت نام')
    email=models.EmailField(max_length=100,verbose_name='ایمیل')
    image_name=models.CharField(max_length=200,default='nophoto.jpg',verbose_name='نام تصویر')
    
    def __str__(self) -> str:
        return f"{self.name} {self.family} {self.age} {self.email} {self.register_date}"

    class Meta:
        verbose_name='نویسنده'
        verbose_name_plural='نویسندگان'

class Article(models.Model):
    article_title=models.CharField(max_length=300,verbose_name='عنوان مقاله')
    slug=models.SlugField(max_length=100,verbose_name='url آدرس')
    article_text=models.TextField(verbose_name='عنوان اصلی')
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    published_at=models.DateTimeField(default=timezone.now,verbose_name='تاریخ انتشار')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='تاریخ بروزرسانی')
    is_active=models.BooleanField(default=False,verbose_name='فعال/غیر فعال')
    ARTICLE_STATUS=[
        ('Draft','پیش نویس'),
        ('Publish','منتشر شده')
    ]
    status=models.CharField(max_length=40,choices=ARTICLE_STATUS,verbose_name='وضعیت')
    # ------- relation
    auther=models.ForeignKey(Auther,null=True,on_delete=models.CASCADE,verbose_name='نوسینده')
    publication=models.ManyToManyField(Publication, verbose_name=("انتشارات/سردبیر"))

    class Meta:
        verbose_name='مقاله'
        verbose_name_plural='مقالات'