from django.contrib import admin
from app_blog.models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)

class PostAdmin(SummernoteModelAdmin):
    fields = ['title','slug','content' ,'author' ,'category','image' ,'status','published_date']
    list_display = ['title' ,'author' ,'status' ,'published_date']
    list_filter = ['status', 'created_date', 'author', 'category']
    search_fields = ['title', 'author', 'content', 'category']
    summernote_fields = ['content']

admin.site.register(Post, PostAdmin)