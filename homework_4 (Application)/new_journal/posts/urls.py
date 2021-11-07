from django.urls import path
from .views import show_post

urlpatterns = [
    path('<int:post_id>/', show_post, name='show_post'),
]