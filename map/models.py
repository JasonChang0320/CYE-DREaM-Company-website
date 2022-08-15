from django.db import models
from home.models import OverwriteStorage

# Create your models here.

class Map_Image(models.Model):
    pic_url = models.ImageField("圖片URL",storage=OverwriteStorage(),upload_to='map_image',blank=True)