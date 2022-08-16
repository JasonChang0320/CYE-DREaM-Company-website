from django.db import models
from home.models import OverwriteStorage

# Create your models here.
class Contact(models.Model):
    name = models.CharField('公司名稱', max_length=20)
    logo= models.ImageField("公司logo",storage=OverwriteStorage(),upload_to='',blank=True)
    title = models.CharField('標題', max_length=20)
    phone=models.CharField("電話:", max_length=30,blank=True)
    email=models.CharField('E-mail', max_length=60,blank=True)
    address=models.TextField('地址', max_length=100,blank=True)
    office_hour=models.CharField('辦公時間', max_length=60,blank=True)
    bottom_title=models.CharField('底部標題', max_length=20,blank=True)
    bottom_content=models.TextField('底部內容', max_length=300,blank=True)
    bottom_email=models.CharField('底部email', max_length=100,blank=True)
    bottom_phone=models.CharField('底部連絡電話', max_length=50,blank=True)
    def __str__(self):
        return self.name