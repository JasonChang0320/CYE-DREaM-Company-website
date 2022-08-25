from django.contrib import admin
from .models import Map_Image,MapPage,MapPage_EN,Visitor_Info

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

@admin.register(Visitor_Info)
class Visitor_Info_Admin(admin.ModelAdmin):
    list_display = ( "name","email","job_title")
    ordering = ("id",)