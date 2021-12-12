from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Post


@registry.register_document
class PostDocument(Document):
    class Index:
        name = 'post'

    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }

    categories = fields.ObjectField(properties={
        'name': fields.TextField(),
    })

    author = fields.ObjectField(properties={
        'username': fields.TextField(),
    })

    class Django:
        model = Post
        fields = [
            'id',
            'title',
            'description',
            'content',
        ]