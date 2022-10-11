from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'related_user', 'is_active']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'related_user', 'related_article']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)