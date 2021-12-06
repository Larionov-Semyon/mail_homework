import logging

from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
# from application.celery import app
from application import celery_app
from application.settings import EMAIL_HOST_USER
from celery import shared_task
from posts.models import Post
from datetime import datetime


@celery_app.task
def send_verification_email(user_id):
    UserModel = get_user_model()
    try:
        # print('SEND EMAIL !!!')
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            'Follow this link to verify your account: '
            'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
            EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
    except UserModel.DoesNotExist:
        print("No-existing user '%s'" % user_id)


@shared_task
def count_users_posts():
    UserModel = get_user_model()
    users = UserModel.objects.filter(is_active=True)
    posts = Post.objects.all()
    file = open("out.txt", "a")
    file.write(f'Date-time: {datetime.now()}  active users: {len(users)}  posts: {len(posts)}\n')
    file.close()
