# Generated by Django 3.2.9 on 2021-12-02 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('img', models.ImageField(upload_to='ingredients/', verbose_name='Изображение')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Список продуктов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='IngredientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteapp.ingredientitem', verbose_name='Ингредиент')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Персональная информация о продуктах',
            },
        ),
        migrations.CreateModel(
            name='DishItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('img', models.ImageField(upload_to='dishes/', verbose_name='Изображение')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('ingredients', models.ManyToManyField(to='siteapp.IngredientItem')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Список блюд',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DishInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteapp.dishitem', verbose_name='Блюдо')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Персональная информация о Блюдах',
            },
        ),
    ]
