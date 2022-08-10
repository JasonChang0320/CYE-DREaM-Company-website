from django.db import models
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your models here.
class OverwriteStorage(FileSystemStorage):
    #overwrite same filename image 
    # need to change storage.py: 
    # name = self.get_available_name(name, max_length=max_length) --> name = self.get_available_name(name)
    def get_available_name(self, name):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class HomePage(models.Model):
    name = models.CharField('公司名稱', max_length=20)
    big_pic_url1 = models.ImageField("圖片1 URL",storage=OverwriteStorage(),upload_to='home_image/',blank=True)
    big_pic_url2 = models.ImageField("圖片2 URL",storage=OverwriteStorage(),upload_to='home_image/',blank=True)
    big_pic_url3 = models.ImageField("圖片3 URL",storage=OverwriteStorage(),upload_to='home_image/',blank=True)
    title = models.CharField('標題', max_length=20)
    title_content=models.TextField('標題內容', max_length=200)
    sub_title1=models.CharField('子標題1', max_length=50)
    sub_title2=models.CharField('子標題2', max_length=50)
    sub_title3=models.CharField('子標題3', max_length=50)
    sub_title4=models.CharField('子標題4', max_length=50)
    content1 = models.TextField('子標題內容1', max_length=200)
    content2 = models.TextField('子標題內容2', max_length=200)
    content3 = models.TextField('子標題內容3', max_length=200)
    content4 = models.TextField('子標題內容4', max_length=200)
    pic_url1 = models.ImageField("子標題圖片1 URL",storage=OverwriteStorage(),upload_to='home_image/',blank=True)
    pic_url2 = models.ImageField("子標題圖片2 URL",storage=OverwriteStorage(),upload_to='home_image/',blank=True)
    pic_url3 = models.ImageField("子標題圖片3 URL",storage=OverwriteStorage(),upload_to='home_image/',blank=True)
    pic_url4 = models.ImageField("子標題圖片4 URL",storage=OverwriteStorage(),upload_to='home_image/',blank=True)
    def __str__(self):
        return self.name

class GoogleMap_Img(models.Model):
    image_ID = models.TextField("圖片群ID",primary_key=True, editable=False)
    pic_url1 = models.ImageField("子標題圖片1 URL",storage=OverwriteStorage(),upload_to='home_image/google_map_img',blank=True)
    pic_url2 = models.ImageField("子標題圖片2 URL",storage=OverwriteStorage(),upload_to='home_image/google_map_img',blank=True)
    pic_url3 = models.ImageField("子標題圖片3 URL",storage=OverwriteStorage(),upload_to='home_image/google_map_img',blank=True)
    pic_url4 = models.ImageField("子標題圖片4 URL",storage=OverwriteStorage(),upload_to='home_image/google_map_img',blank=True)
    pic_url5 = models.ImageField("子標題圖片5 URL",storage=OverwriteStorage(),upload_to='home_image/google_map_img',blank=True)
    pic_url6 = models.ImageField("子標題圖片6 URL",storage=OverwriteStorage(),upload_to='home_image/google_map_img',blank=True)
    pic_url7 = models.ImageField("子標題圖片7 URL",storage=OverwriteStorage(),upload_to='home_image/google_map_img',blank=True)
    pic_url8 = models.ImageField("子標題圖片8 URL",storage=OverwriteStorage(),upload_to='home_image/google_map_img',blank=True)
    pic_url9 = models.ImageField("子標題圖片9 URL",storage=OverwriteStorage(),upload_to='home_image/google_map_img',blank=True)
    pic_url0 = models.ImageField("子標題圖片10 URL",storage=OverwriteStorage(),upload_to='home_image/google_map_img',blank=True)
