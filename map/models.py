from doctest import master
from django.db import models
from home.models import OverwriteStorage

# Create your models here.

class Map_Image(models.Model):
    pic_url = models.ImageField("圖片URL",storage=OverwriteStorage(),upload_to='map_image',blank=True)

class MapPage(models.Model):
    name = models.CharField('公司名稱', max_length=20)
    logo= models.ImageField("公司logo",storage=OverwriteStorage(),upload_to='',blank=True)
    form_title=models.TextField('表單頂部內容', max_length=100,blank=True)
    form_image=models.ImageField("表單底部圖片URL",storage=OverwriteStorage(),upload_to='map_image',blank=True)
    bottom_title=models.CharField('底部標題', max_length=20,blank=True)
    bottom_content=models.TextField('底部內容', max_length=300,blank=True)
    bottom_email=models.CharField('底部email', max_length=100,blank=True)
    bottom_phone=models.CharField('底部連絡電話', max_length=50,blank=True)
    def __str__(self):
        return self.name

class MapPage_EN(models.Model):
    name = models.CharField('公司名稱', max_length=50)
    form_title=models.TextField('表單頂部內容', max_length=300,blank=True)
    bottom_title=models.CharField('底部標題', max_length=50,blank=True)
    bottom_content=models.TextField('底部內容', max_length=400,blank=True)
    bottom_email=models.CharField('底部email', max_length=100,blank=True)
    bottom_phone=models.CharField('底部連絡電話', max_length=50,blank=True)
    def __str__(self):
        return self.name

class Visitor_Info(models.Model):
    name= models.CharField("名字", max_length=50)
    email=models.EmailField("Email",max_length=100)
    job_title=models.CharField("隸屬單位",max_length=80)
    create_time = models.DateTimeField("傳送日期",auto_now_add=True)
    def __str__(self):
        return self.name