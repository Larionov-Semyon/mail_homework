from django.http.response import JsonResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods, require_GET
from django.shortcuts import render
from database import LOCAL_DATABASE


@require_GET
def show_post(request, post_id):
    """Детальная информация об объекте"""
    return JsonResponse(LOCAL_DATABASE[post_id])


@require_http_methods(["GET", "POST"])
def create_new_post(request):
    """Форма создания нового поста"""
    if request.method == 'POST':
        post_id = len(LOCAL_DATABASE) + 1
        new_post = {
            'ID': post_id,
            'TITLE': request.POST.get('title'),
            'AUTHOR': request.POST.get('author'),
            'CONTENT': request.POST.get('text')
        }
        # print(request.POST)
        LOCAL_DATABASE[post_id] = new_post
        return HttpResponseRedirect(f'/post/{post_id}')
    if request.method == 'GET' or request.method == 'PUT':
        return render(request, "add_post.html")
    return HttpResponseBadRequest()
