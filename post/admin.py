from django.contrib import admin
from .models import Post, Comment
# Register your models here.





@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created', 'active']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'updated', 'status', ]
    prepopulated_fields = {'slug': ('title',)}
