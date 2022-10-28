from django.urls import path
from . import views
from .views import *

app_name = 'shop'
urlpatterns = [
    path('products', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('create_shop/', views.create_shop, name='create_shop'),
    path('shops/', views.shops_review, name='shops_review'),
    path('product_id<int:id>/', views.product_detail, name='product_detail'),
    path('shop_<slug:slug>/', views.shop_review, name='shop_review'),
]

