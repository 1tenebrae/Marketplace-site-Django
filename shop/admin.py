from django.contrib import admin
from .models import Product, Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('proprietor', 'shop_name', 'slug', 'banner', 'shop_description', 'created', 'sell_services',
                    'sell_products')
    prepopulated_fields = {'slug': ('shop_name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'shop_owner', 'categor', 'title', 'price', 'product_description', 'main_photo', 'status',
                    'is_published')

