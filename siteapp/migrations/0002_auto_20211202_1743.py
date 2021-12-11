# Generated by Django 3.2.9 on 2021-12-02 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории блюд',
            },
        ),
        migrations.CreateModel(
            name='IngredientCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории продуктов',
            },
        ),
        migrations.AlterField(
            model_name='dishitem',
            name='img',
            field=models.ImageField(height_field=512, upload_to='dishes/', verbose_name='Изображение', width_field=512),
        ),
        migrations.AlterField(
            model_name='ingredientitem',
            name='img',
            field=models.ImageField(height_field=512, upload_to='ingredients/', verbose_name='Изображение', width_field=512),
        ),
        migrations.AddField(
            model_name='dishitem',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='siteapp.dishcategory', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='ingredientitem',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='siteapp.ingredientcategory', verbose_name='Категория'),
        ),
    ]
