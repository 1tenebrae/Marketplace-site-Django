# Generated by Django 2.0.5 on 2022-05-21 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('price', models.CharField(max_length=50, verbose_name='Цена')),
                ('product_description', models.TextField(default='', max_length=500, verbose_name='Описание')),
                ('main_photo', models.ImageField(upload_to='photos', verbose_name='Главное фото')),
                ('photo1', models.ImageField(upload_to='photos', verbose_name='Фото 1')),
                ('photo2', models.ImageField(upload_to='photos', verbose_name='Фото 2')),
                ('photo3', models.ImageField(upload_to='photos', verbose_name='Фото 3')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('status', models.CharField(choices=[('услуга', 'Услуга'), ('товар', 'Товар')], default='Товар', max_length=10, verbose_name='Услуга или товар')),
                ('categor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Название магазина')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('banner', models.ImageField(upload_to='photos', verbose_name='Баннер магазина')),
                ('shop_description', models.TextField(max_length=500, verbose_name='Описание магазина')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sell_services', models.BooleanField(default=False, verbose_name='Предоставление услуг')),
                ('sell_products', models.BooleanField(default=False, verbose_name='Продажа товаров')),
                ('proprietor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_shop', to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='shop_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_products', to='shop.Shop'),
        ),
    ]