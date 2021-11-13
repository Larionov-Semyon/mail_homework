from django.db import models
from main_page.models import Category
from django.conf import settings


class Post(models.Model):
    # один ко многим
    categories = models.ManyToManyField(
        to=Category,
        verbose_name='Категории',
    )
    title = models.CharField(verbose_name='Название', max_length=64)
    description = models.TextField('Описание', max_length=100, blank=True)
    published_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True,
    )
    content = models.CharField(verbose_name='Контент', max_length=128)

    def get_absolute_url(self):
        # need to change
        return f'/post/{self.id}'

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-published_at',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
