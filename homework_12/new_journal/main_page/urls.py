from django.urls import path, include
from .views import index, filter_by_category, filter_by_user, search


urlpatterns = [
    path('', index, name='index'),
    path('user/', filter_by_user, name='filter_by_user'),
    path('search/', search, name='search'),
    path('<str:category_to_filter>/', filter_by_category, name='filter_by_category'),
]