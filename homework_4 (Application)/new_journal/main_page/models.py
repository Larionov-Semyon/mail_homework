from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=32, unique=True)
    url = models.CharField(verbose_name='URL', max_length=32, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
