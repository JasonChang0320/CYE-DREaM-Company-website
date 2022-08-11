from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class Contact_Admin(admin.ModelAdmin):
    list_display = ( 'title', 'phone',"email","address","office_hour")