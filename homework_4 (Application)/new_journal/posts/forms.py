from .models import Post
from django.forms import ModelForm, Form, TypedChoiceField


class PostForm(ModelForm):
    """Форма для создания нового поста"""
    class Meta:
        model = Post
        fields = ('categories', 'title', 'author', 'content')
