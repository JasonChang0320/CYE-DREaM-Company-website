from django.db import models
from home.models import OverwriteStorage

# Create your models here.

class Map_Image(models.Model):
    pic_url = models.ImageField("子標題圖片1 URL",storage=OverwriteStorage(),upload_to='map_image',blank=True)