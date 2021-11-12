from django.views.decorators.http import require_GET
from django.shortcuts import render
from database import LOCAL_DATABASE


@require_GET
def index(request):
    """Главная страница"""
    context = {'contents': LOCAL_DATABASE.values}
    return render(request, 'index.html', context=context)
