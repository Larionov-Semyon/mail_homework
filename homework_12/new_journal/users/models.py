from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from django.urls import reverse
from django.db.models import signals
from .tasks import send_verification_email
from django.db.models import signals
from django.core.mail import send_mail


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
    is_verified = models.BooleanField(verbose_name='verified', default=False, editable=True) # Add the `is_verified` flag
    verification_uuid = models.UUIDField(verbose_name='Unique Verification UUID', default=uuid.uuid4, editable=True)


def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        # Send verification email
        send_verification_email.delay(instance.id)


signals.post_save.connect(user_post_save, sender=MyUser)

