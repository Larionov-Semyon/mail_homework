from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class MyUser(AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    bio = models.TextField(verbose_name='Биография', max_length=500, blank=True)
    location = models.CharField(verbose_name='Город', max_length=30, blank=True)
    birthday = models.DateField(verbose_name='День рождения', null=True, blank=True)
    rating = models.IntegerField(verbose_name='Рейтинг', default=0,
                                 validators=[
                                     MaxValueValidator(100),
                                     MinValueValidator(0)
                                 ])
