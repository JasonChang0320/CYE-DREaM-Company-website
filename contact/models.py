from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField('公司名稱', max_length=20)
    title = models.CharField('標題', max_length=20)
    phone=models.CharField("電話:", max_length=30,blank=True)
    email=models.CharField('E-mail', max_length=60,blank=True)
    address=models.TextField('地址', max_length=100,blank=True)
    office_hour=models.CharField('辦公時間', max_length=60,blank=True)
    def __str__(self):
        return self.name