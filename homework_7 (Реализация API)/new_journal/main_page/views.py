from django.views.decorators.http import require_GET
from django.shortcuts import render, get_object_or_404
from posts.models import Post
from .models import Category


@require_GET
def index(request):
    """Главная страница"""
    data = {
        'categories': Category.objects.all(),
        'contents': Post.objects.all(),
    }
    return render(request, 'index.html', data)


@require_GET
def filter_by_category(request, category_to_filter):
    active_category = get_object_or_404(Category, url=category_to_filter)
    categories = Category.objects.all()
    contents = Post.objects.filter(categories__url=category_to_filter)\
        .order_by('-published_at')

    data = {
        'categories': categories,
        'contents': contents,
        'active_category': active_category,
    }
    return render(request, 'index.html', data)
