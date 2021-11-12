from django.db import models
from main_page.models import Category


class Post(models.Model):
    # один ко многим
    category_id = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    author = models.CharField(verbose_name='Автор', max_length=32, blank=False)
    date = models.DateField(verbose_name='Дата', auto_now_add=True)
    content = models.CharField(verbose_name='Контент', max_length=128)
