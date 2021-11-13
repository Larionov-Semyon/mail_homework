from django.views.decorators.http import require_GET
from django.shortcuts import render
# from database import LOCAL_DATABASE
from posts.models import Post
from main_page.models import Category


@require_GET
def index(request):
    """Главная страница"""
    categories = Category.objects.all()
    contents = Post.objects.all()
    return render(request, 'index.html', {'categories': categories, 'contents': contents})
