from django.contrib import admin
from .models import Service, Experience,Service_Title
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
