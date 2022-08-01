from django.contrib import admin

# Register your models here.
from .models import Post
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'content')
#     search_fields = ('title', 'content')
#     ordering = ("id",)
# admin.site.register(Post, PostAdmin)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'content')
    search_fields = ('title', 'content')
    ordering = ("id",)
