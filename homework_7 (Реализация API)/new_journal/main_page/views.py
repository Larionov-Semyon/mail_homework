from django.views.decorators.http import require_GET
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from posts.models import Post
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    View для категорий
    Пользователи могут создавать, изменять, удалять категории.
    Неавторизованные только использовать методы GET.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


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
    """Фильтрация для категории"""
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
