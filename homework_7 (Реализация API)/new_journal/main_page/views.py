from django.views.decorators.http import require_GET
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from posts.decorators import authorization_check
from rest_framework import viewsets

from posts.models import Post
from .models import Category
from .serializers import CategorySerializer


def login(request):
    return render(request, 'login.html')


class CategoryViewSet(viewsets.ModelViewSet):
    """
    View для категорий
    Пользователи могут создавать, изменять, удалять категории.
    Неавторизованные только использовать методы GET.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@require_GET
# @login_required
def index(request):
    """
    Главная страница
        categories: категории в плашке выбора вверху страницы
        contents: список постов
    """
    data = {
        'categories': Category.objects.all(),
        'contents': Post.objects.all(),
    }
    return render(request, 'index.html', data)


@authorization_check
@require_GET
def filter_by_category(request, category_to_filter):
    """
    Страница фильтрации по категории
        active_category: активная категория
        categories: категории в плашке выбора вверху страницы
        contents: список постов
    """
    active_category = get_object_or_404(Category, url=category_to_filter)
    categories = Category.objects.all()
    contents = Post.objects.filter(categories__url=category_to_filter)\
        .order_by('-published_at')

    data = {
        'active_category': active_category,
        'categories': categories,
        'contents': contents,
    }
    return render(request, 'index.html', data)


@require_GET
def filter_by_user(request):
    """
    Страница фильтрации по категории для пользователя
        active_category: активная категория
        categories: категории в плашке выбора вверху страницы
        contents: список постов
    """
    categories = Category.objects.all()
    contents = Post.objects.filter(author=request.user).order_by('-published_at')
    data = {
        'categories': categories,
        'contents': contents,
    }
    return render(request, 'index.html', data)
