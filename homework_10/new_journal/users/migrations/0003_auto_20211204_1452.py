# Generated by Django 3.2.9 on 2021-12-04 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211204_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_verified',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='verification_uuid',
        ),
    ]
