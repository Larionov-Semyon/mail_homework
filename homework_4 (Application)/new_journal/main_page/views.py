from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from database import LOCAL_DATABASE


def index(request):
    """Главная страница"""
    if request.method == 'GET':
        context = {'contents': LOCAL_DATABASE.values}
        return render(request, 'index.html', context=context)
    else:
        return HttpResponseBadRequest()


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
