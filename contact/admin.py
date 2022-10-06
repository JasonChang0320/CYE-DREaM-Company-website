from django.contrib import admin
from .models import Contact,Contact_EN

# Register your models here.
@admin.register(Contact)
class Contact_Admin(admin.ModelAdmin):
    list_display = ( 'title', 'phone',"email","address","office_hour","tax_ID_number")

@admin.register(Contact_EN)
class ContactEN_Admin(admin.ModelAdmin):
    list_display = ( 'title', 'phone',"email","address","office_hour","tax_ID_number")