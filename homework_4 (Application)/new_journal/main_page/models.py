from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=32)
