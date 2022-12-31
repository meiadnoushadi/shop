from django.db import models
from django.utils import timezone
# Create your models here.
class Auther(models.Model):
    name=models.CharField(max_length=30)
    family=models.CharField(max_length=30)
    sulg=models.SlugField(max_length=100)
    age=models.IntegerField(default=0)
    is_active=models.BooleanField(default=True)
    register_date=models.DateTimeField(default=timezone.now)
    email=models.EmailField(max_length=100)