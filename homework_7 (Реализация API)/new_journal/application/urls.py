"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet
from main_page.views import CategoryViewSet
from users.views import UserViewSet

router = DefaultRouter()
router.register(r'api/posts', PostViewSet, basename='posts')
router.register(r'api/categories', CategoryViewSet, basename='main_page')
router.register(r'api/users', UserViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls'), name='main_page'),
    path('post/', include('posts.urls'), name='posts'),
]

urlpatterns += router.urls
