from django.contrib import admin

# Register your models here.
from .models import HomePage

@admin.register(HomePage)
class HomePage_Admin(admin.ModelAdmin):
    list_display = ( 'name', 'title',"sub_title1","sub_title2","sub_title3","sub_title4")
    search_fields = ( 'name', 'title',"sub_title1","sub_title2","sub_title3","sub_title4")
    ordering = ("id",)

# @admin.register(GoogleMap_Img)
# class GoogleMap_Img_Admin(admin.ModelAdmin):
#     list_display = ( "image_ID",)
#     search_fields = ( "image_ID",)
#     ordering = ("image_ID",)