from django.db import models
from home.models import OverwriteStorage

# Create your models here.
class AboutContent(models.Model):
    name = models.CharField('公司名稱', max_length=20)
    title = models.CharField('標題', max_length=20)
    content=models.TextField("內容", max_length=200,blank=True)
    member_title=models.CharField('成員標題', max_length=20)
    def __str__(self):
        return self.name

class Member(models.Model):
    name= models.CharField('成員名稱', max_length=20)
    pic_url = models.ImageField("成員照片URL",storage=OverwriteStorage(),upload_to='AboutUs_image/',blank=True)
    experience1= models.CharField('經歷1', max_length=30,blank=True)
    experience2= models.CharField('經歷2', max_length=30,blank=True)
    experience3= models.CharField('經歷3', max_length=30,blank=True)
    experience4= models.CharField('經歷4', max_length=30,blank=True)
    phone= models.CharField('連絡電話', max_length=30,blank=True)
    introduce = models.TextField('成員介紹', max_length=500,blank=True)