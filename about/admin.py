from django.contrib import admin
from .models import AboutContent,Member

# Register your models here.
@admin.register(AboutContent)
class Contact_Admin(admin.ModelAdmin):
    list_display = ( 'name', 'title',"content","member_title")

@admin.register(Member)
class Contact_Admin(admin.ModelAdmin):
    list_display = ( 'name', 'experience1','experience2',"phone","introduce")