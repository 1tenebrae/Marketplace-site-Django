from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published='True')


class Shop(models.Model):
    proprietor = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_shop', verbose_name='')
    shop_name = models.CharField(max_length=50, primary_key=True, verbose_name='Название магазина')
    slug = models.SlugField(unique=True, verbose_name='URL')
    banner = models.ImageField(upload_to="photos", verbose_name='Баннер магазина', blank=True, default='Null')
    shop_description = models.TextField(max_length=500, verbose_name='Описание магазина')
    created = models.DateTimeField(auto_now_add=True)
    sell_services = models.BooleanField(default=False, verbose_name='Предоставление услуг')
    sell_products = models.BooleanField(default=False, verbose_name='Продажа товаров')
    objects = models.Manager()

    def __str__(self):
        return self.shop_name

    def get_absolute_url(self):
        return reverse_lazy('shop:shop_review', args=[self.slug])


class Product(models.Model):
    STATUS_CHOICES = (
        ('услуга', 'Услуга'),
        ('товар', 'Товар'),
    )
    shop_owner = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop_products')
    categor = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='Категория', blank=True)
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    price = models.CharField(max_length=50, verbose_name='Цена')
    product_description = models.TextField(max_length=500, default='', verbose_name='Описание')
    main_photo = models.ImageField(upload_to="photos", verbose_name='Главное фото', blank=True, default='Null' )
    photo1 = models.ImageField(upload_to="photos", verbose_name='Фото 1', blank=True, default='Null')
    photo2 = models.ImageField(upload_to="photos", verbose_name='Фото 2', blank=True, default='Null')
    photo3 = models.ImageField(upload_to="photos", verbose_name='Фото 3', blank=True, default='Null')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')
    status = models.CharField(max_length=10, default='Товар', choices=STATUS_CHOICES, verbose_name='Услуга или товар')
    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse_lazy('shop:product_detail', args=[self.id])


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name





