from django.urls import path
from .views import show_post, create_new_post

urlpatterns = [
    path('<int:post_id>/', show_post, name='show_post'),
    path('add/', create_new_post, name='create_new_post'),
]