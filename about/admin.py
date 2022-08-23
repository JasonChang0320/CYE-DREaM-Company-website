from django.contrib import admin
from .models import AboutContent,Member,AboutContent_EN,Member_EN

# Register your models here.
@admin.register(AboutContent)
class Contact_Admin(admin.ModelAdmin):
    list_display = ( 'name', 'title',"content","member_title")

@admin.register(Member)
class Contact_Admin(admin.ModelAdmin):
    list_display = ( 'name', 'experience1','experience2',"phone","introduce")
    ordering = ("id",)

@admin.register(AboutContent_EN)
class Contact_EN_Admin(admin.ModelAdmin):
    list_display = ( 'name', 'title',"content","member_title")

@admin.register(Member_EN)
class Contact_EN_Admin(admin.ModelAdmin):
    list_display = ( 'name', 'experience1','experience2',"phone","introduce")
    ordering = ("id",)