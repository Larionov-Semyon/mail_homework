from django.urls import path, include
from .views import index, filter_by_category


urlpatterns = [
    path('', index, name='index'),
    path('<str:category_to_filter>/', filter_by_category, name='filter_by_category'),
]