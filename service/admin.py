from django.contrib import admin
from .models import Service, Experience,Service_Title,Service_EN,Service_Title_EN,Experience_EN
# Register your models here.
@admin.register(Service)
class Service_Admin(admin.ModelAdmin):
    list_display = ('title',"content","pic_url")
    search_fields = ('title',)
    ordering = ("id",)

@admin.register(Experience)
class Experience_Admin(admin.ModelAdmin):
    list_display = ('title',"content","pic_url")
    search_fields = ('title',)
    ordering = ("id",)

@admin.register(Service_Title)
class Service_Title_Admin(admin.ModelAdmin):
    list_display = ('name',"logo","title1","title2")

@admin.register(Service_EN)
class Service_EN_Admin(admin.ModelAdmin):
    list_display = ('title',"content")
    search_fields = ('title',)
    ordering = ("id",)

@admin.register(Experience_EN)
class Experience_EN_Admin(admin.ModelAdmin):
    list_display = ('title',"content")
    search_fields = ('title',)
    ordering = ("id",)

@admin.register(Service_Title_EN)
class Service_EN_Title_Admin(admin.ModelAdmin):
    list_display = ('name',"title1","title2")
