from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('標題', max_length=20)
    content = models.TextField('內容', max_length=200)
    def __str__(self):
        return self.title