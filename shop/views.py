from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView
from .forms import *
from .models import Product, Shop
from django.contrib.auth.mixins import LoginRequiredMixin


def product_list(request):
    products = Product.published.all()
    return render(request, 'shop/product/products review.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id, is_published='True',)
    shop = Shop.objects.get(shop_name=product.shop_owner)
    return render(request, 'shop/product/product card.html', {'product': product, 'shop': shop})


def shop_review(request, slug):
    shop = Shop.objects.get(slug=slug)
    product = Product.objects.all().filter(shop_owner=shop.shop_name).filter(is_published='True')
    return render(request, 'shop/product/shop review.html', {'shops': shop, 'products': product})


def shops_review(request):
    shop = Shop.objects.all()
    return render(request, 'shop/product/shops review.html', {'shops': shop})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            shop = Shop.objects.get(proprietor=user)
            product = Product.objects.create(shop_owner=shop, **form.cleaned_data)
            return redirect(product.get_absolute_url())
    else:
        form = AddProductForm()
    return render(request, 'shop/product/add product.html',  {'form': form})

@login_required
def create_shop(request):
    if request.method == 'POST':
        form = CreateShopForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            shop = Shop.objects.create(proprietor=user, **form.cleaned_data)
            user.user_shop = shop
            user.save()
            shop = Shop.objects.get(slug=form.instance.slug)
            return redirect(shop)

    else:
        form = CreateShopForm()
    return render(request, 'shop/product/create shop.html', {'form': form})





