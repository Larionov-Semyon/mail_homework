from django.views.decorators.http import require_http_methods, require_GET
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import Http404
from .models import Post
from .forms import PostForm
from django.core.exceptions import ValidationError

from .serializers import PostSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    View для постов
    Пользователи могут создавать, изменять, удалять посты.
    Неавторизованные только использовать методы GET.
    """
    queryset = Post.objects.order_by('-published_at')
    serializer_class = PostSerializer
    # разрешение
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


@require_GET
def show_post(request, post_id):
    """Детальная информация об объекте"""
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post.html', {'post': post})


@require_http_methods(["GET", "POST"])
def create_post(request):
    """Форма создания нового объекта"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            raise Http404
    if request.method == 'GET' or request.method == 'PUT':
        form = PostForm()
        context = {
            'form': form,
        }
        return render(request, "add_post.html", context=context)


@require_http_methods(["GET", "POST"])
def update_post(request, post_id):
    """Обновление поста"""
    old_post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=old_post)
        if form.is_valid():
            form.save()
            return redirect(f'/post/{post_id}/')
    elif request.method == 'GET':
        form = PostForm(instance=old_post)
        context = {
            'form': form
        }
        return render(request, 'update_post.html', context)


@require_http_methods(["GET", "POST"])
def delete_post(request, post_id):
    """Удаление поста"""
    # можно удалять без get_object
    data = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        if request.POST.get('delete_button_yes') == 'Yes':
            data.delete()
            return redirect('/')
        return redirect(f'/post/{post_id}/')
    elif request.method == 'GET':
        return render(request, 'delete_post.html')
