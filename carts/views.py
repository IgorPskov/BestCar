from django.shortcuts import redirect, render
from django.contrib import messages

from carts.models import Cart, Favorite
from cars.models import Products

def cart_add(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            messages.warning(request, "Этот автомобиль уже добавлен в вашу корзину")
        else:
            Cart.objects.create(user=request.user, product = product)

    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, product_slug):
    ...

def cart_remove(request, product_slug):
    ...

def favorite_add(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(user=request.user, product=product)

        if favorites.exists():
            messages.warning(request, "Этот автомобиль уже добавлен к вам в избранное")
        else:
            Favorite.objects.create(user=request.user, product = product)

    return redirect(request.META['HTTP_REFERER'])

def favorite_remove(request, product_slug):
    ...