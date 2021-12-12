from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'author', 'display_categories')
    list_filter = ('published_at', 'author', 'categories')
    ordering = ['title', 'published_at', 'author']

    def display_categories(self, obj):
        """Создание строки с 3 категориями"""
        return ', '.join([category.name for category in obj.categories.all()[:3]])
    display_categories.short_description = 'Genre'
