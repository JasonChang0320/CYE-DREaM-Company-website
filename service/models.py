from django.db import models
from home.models import OverwriteStorage


# Create your models here.
class Service(models.Model):
    title = models.CharField('標題', max_length=50)
    content=models.TextField("內容", max_length=200,blank=True)
    pic_url = models.ImageField("照片",storage=OverwriteStorage(),upload_to='Service/service_image',blank=True)
    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField('標題', max_length=50)
    content=models.TextField("內容", max_length=200,blank=True)
    pic_url = models.ImageField("照片",storage=OverwriteStorage(),upload_to='Service/experience_image',blank=True)
    def __str__(self):
        return self.title