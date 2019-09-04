from django.contrib import admin

from .models import Comment, Article, Category

admin.site.register(Comment)
admin.site.register(Article)
admin.site.register(Category)