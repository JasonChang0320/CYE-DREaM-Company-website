from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Service)
class Service_Admin(admin.ModelAdmin):
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

@admin.register(Service_Title_EN)
class Service_EN_Title_Admin(admin.ModelAdmin):
    list_display = ('name',"title1","title2")

@admin.register(Experience)
class Experience_Admin(admin.ModelAdmin):
    list_display = ('title',"content")
    search_fields = ('title',)
    ordering = ("id",)

@admin.register(Experience_EN)
class Experience_EN_Admin(admin.ModelAdmin):
    list_display = ('title',"content")
    search_fields = ('title',)
    ordering = ("id",)

@admin.register(NSTC_project)
class NSTC_project_Admin(admin.ModelAdmin):
    list_display = ('project',"content")
    search_fields = ('project',)
    ordering = ("id",)

@admin.register(NSTC_project_EN)
class NSTC_project_EN_Admin(admin.ModelAdmin):
    list_display = ('project',"content")
    search_fields = ('project',)
    ordering = ("id",)