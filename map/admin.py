from django.contrib import admin
from .models import Map_Image,MapPage,MapPage_EN

# Register your models here.

@admin.register(Map_Image)
class Map_Image_Admin(admin.ModelAdmin):
    list_display = ( "pic_url",)
    ordering = ("id",)

@admin.register(MapPage)
class MapPage_Admin(admin.ModelAdmin):
    list_display = ( "name","logo","bottom_title","bottom_content","bottom_email","bottom_phone")

@admin.register(MapPage_EN)
class MapPage_EN_Admin(admin.ModelAdmin):
    list_display = ( "name","bottom_title","bottom_content","bottom_email","bottom_phone")