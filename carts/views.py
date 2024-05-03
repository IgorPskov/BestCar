from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.template.loader import render_to_string

from carts.models import Cart, Favorite
from cars.models import Products
from carts.utils import get_user_favorites

def cart_add(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            messages.warning(request, "Этот автомобиль уже добавлен в вашу корзину")
        else:
            Cart.objects.create(user=request.user, product = product)
        
            messages.success(request, "Автомобиль добавлен в корзину")


    return redirect(request.META['HTTP_REFERER'])
    

def cart_change(request, product_slug):
    ...

def cart_remove(request, cart_id):

    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])




def favorite_add(request):
    product_id = request.POST.get("product_id")    
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(user=request.user, product=product)

        if favorites.exists():
            # Если товар уже в избранном, возвращаем флаг already_in_favorite=True
            response_data = {
                "already_in_favorite": True,
                "warning_message": "Этот автомобиль уже добавлен к вам в избранное",
            }
        else:
            Favorite.objects.create(user=request.user, product=product)
            response_data = {
                "already_in_favorite": False,
                "success_message": "Товар добавлен в избранное",
            }
    
    user_favorite = get_user_favorites(request)
    favorite_items_html = render_to_string(
        "carts/includes/included_favorite.html", {"favorites": user_favorite}, request=request)

    response_data["favorite_items_html"] = favorite_items_html

    return JsonResponse(response_data)

def favorite_remove(request, favorite_id):

    favorite = Favorite.objects.get(id=favorite_id)
    favorite.delete()

    return redirect(request.META['HTTP_REFERER'])