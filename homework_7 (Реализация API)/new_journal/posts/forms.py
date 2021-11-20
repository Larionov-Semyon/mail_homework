from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    """Форма для создания нового поста"""
    class Meta:
        model = Post
        fields = ('categories', 'title', 'author', 'content')
