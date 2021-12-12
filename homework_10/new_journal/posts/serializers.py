from rest_framework import serializers

from main_page.serializers import CategorySerializer
from main_page.models import Category
from .models import Post

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import PostDocument


# # serializers.ModelSerializer
# class PostSerializer(serializers.ModelSerializer):
#     """Serializer для Постов"""
#     author = serializers.CharField(default=serializers.CurrentUserDefault())
#     categories = CategorySerializer(read_only=True, many=True)
#     category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, many=True)
#
#     class Meta:
#         model = Post
#         document = PostDocument
#         fields = '__all__'
#         read_only_fields = ['id', 'published_at']
#
#     def create(self, validated_data):
#         """POST: создание нового поста"""
#         categories = validated_data.pop('category_id')
#         posts = Post.objects.create(**validated_data)
#         for category in categories:
#             posts.categories.add(category)
#         return posts
#
#     def validate_title(self, title):
#         """Проверка, что название не число"""
#         if title.isdigit():
#             raise serializers.ValidationError("You only use numbers in the title")
#         return title
#
#     def validate_category_id(self, category_id):
#         """Проверка, что у поста есть категория"""
#         if not category_id:
#             raise serializers.ValidationError("category_id is empty !")
#         return category_id


class PostDocumentSerializer(DocumentSerializer):
    class Meta:
        document = PostDocument
        fields = (
            'title',
            'categories',
            'author',
            'description',
            'content',
            'published_at',
        )
