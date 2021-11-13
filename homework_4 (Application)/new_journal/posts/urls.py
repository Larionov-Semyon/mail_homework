from django.urls import path
from .views import show_post, create_post, update_post, delete_post

urlpatterns = [
    path('<int:post_id>/', show_post, name='show_post'),
    path('<int:post_id>/update/', update_post, name='update_post'),
    path('<int:post_id>/delete/', delete_post, name='delete_post'),
    path('add/', create_post, name='create_post'),
]