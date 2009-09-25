from mysite.blog.models import Blog
from mysite.blog.models import Comment
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    search_fields = ('author', 'title')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author','email', 'url', 'blog', 'pub_date')
    search_fields = ('author', 'email')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)