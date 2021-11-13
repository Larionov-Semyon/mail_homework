from django.views.decorators.http import require_http_methods, require_GET
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.http import Http404


@require_GET
def show_post(request, post_id):
    """Детальная информация об объекте"""
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404('Пост не существует')
    return render(request, 'post.html', {'post': post})


@require_http_methods(["GET", "POST"])
def create_post(request):
    """Форма создания нового объекта"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        # нужен ли else ?
        if form.is_valid():
            form.save()
            return redirect('/')
    if request.method == 'GET' or request.method == 'PUT':
        form = PostForm()
        context = {
            'form': form
        }
        return render(request, "add_post.html", context=context)


@require_http_methods(["GET", "POST"])
def update_post(request, post_id):
    try:
        old_post = get_object_or_404(Post, id=post_id)
    except Exception:
        raise Http404('Пост не существует')

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
    try:
        data = get_object_or_404(Post, id=post_id)
    except Exception:
        raise Http404('Пост не существует')

    if request.method == 'POST':
        if request.POST.get('delete_button_yes') == 'Yes':
            data.delete()
            return redirect('/')
        return redirect(f'/post/{post_id}/')
    elif request.method == 'GET':
        return render(request, 'delete_post.html')
