from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer для категорий"""
    class Meta:
        model = Category
        fields = ['id', 'name']

