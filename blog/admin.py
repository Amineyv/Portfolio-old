from django.contrib import admin
from blog.models import Category, Comment, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment, CommentAdmin)