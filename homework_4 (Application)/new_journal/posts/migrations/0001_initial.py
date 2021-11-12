# Generated by Django 3.2.9 on 2021-11-12 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=32, verbose_name='Автор')),
                ('message', models.CharField(max_length=128, verbose_name='Сообщение')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_page.category', verbose_name='Категория')),
            ],
        ),
    ]