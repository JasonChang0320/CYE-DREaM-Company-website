from django.contrib import admin
from .models import Service, Experience
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