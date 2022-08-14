from django.contrib import admin
from .models import Map_Image

# Register your models here.

@admin.register(Map_Image)
class Question_Admin(admin.ModelAdmin):
    list_display = ( "pic_url",)
