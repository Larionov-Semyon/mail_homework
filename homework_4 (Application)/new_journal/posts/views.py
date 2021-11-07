from django.http.response import JsonResponse
# from django.shortcuts import render
from database import LOCAL_DATABASE


def show_post(request, post_id):
    """Детальная информация об объекте"""
    return JsonResponse(LOCAL_DATABASE[post_id])
