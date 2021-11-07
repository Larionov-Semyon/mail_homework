from django.urls import path, include
from .views import index, create_new_post

urlpatterns = [
    path('', index, name='index'),
    path('add_post/', create_new_post, name='create_new_post'),
]