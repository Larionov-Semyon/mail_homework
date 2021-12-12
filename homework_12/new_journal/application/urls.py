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
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet
from main_page.views import CategoryViewSet, login
from users.views import UserViewSet

# import social_django

router = DefaultRouter()
router.register(r'api/posts', PostViewSet, basename='posts')
router.register(r'api/categories', CategoryViewSet, basename='main_page')
router.register(r'api/users', UserViewSet, basename='users')
# router.register(r'api/search', SearchViewSet, basename='search')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social_auth/', include('social_django.urls', namespace='social')),
    path('post/', include('posts.urls'), name='posts'),
    path('user/', include('users.urls'), name='users'),
    path('', include('main_page.urls'), name='main_page'),
]

urlpatterns += router.urls
