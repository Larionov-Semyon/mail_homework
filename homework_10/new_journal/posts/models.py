from django.db import models
from django.conf import settings
from django.shortcuts import reverse

from main_page.models import Category


class Post(models.Model):
    # один ко многим
    categories = models.ManyToManyField(
        to=Category,
        verbose_name='Категории',
    )
    title = models.CharField(verbose_name='Название', max_length=64)
    description = models.TextField('Описание', max_length=100, blank=True)
    published_at = models.DateField(verbose_name='Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True,
    )
    content = models.CharField(verbose_name='Контент', max_length=128)

    class Meta:
        ordering = ('-published_at',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('show_post', kwargs={'post_id': self.id})

    def __str__(self):
        return self.title
