from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.template.loader import render_to_string

from carts.models import Cart, Favorite
from cars.models import Products
from carts.templatetags.carts_tags import user_favorites
from carts.utils import get_user_favorites

def cart_add(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        product_category = product.category
        product_name = product.name

        if carts.exists():
            messages.warning(request, "Этот автомобиль уже добавлен в вашу корзину")
        else:
            Cart.objects.create(user=request.user, product = product)
    
            success_message = f"Автомобиль {product_category} {product_name} добавлен в корзину"
            messages.success(request, success_message)

    return redirect(request.META['HTTP_REFERER'])
    

def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    
    # Получаем информацию о товаре из объекта корзины
    product_category = cart.product.category
    product_name = cart.product.name
    
    # Удаляем объект корзины
    cart.delete()

    # Формируем сообщение об успешном удалении из корзины
    success_message = f"Автомобиль {product_category} {product_name} удален из корзины"
    messages.success(request, success_message)

    return redirect(request.META['HTTP_REFERER'])




def favorite_add(request):
    product_id = request.POST.get("product_id")    
    product = Products.objects.get(id=product_id)

    product_category = product.category
    product_name = product.name

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
            success_message = f"Автомобиль {product_category} {product_name} добавлен в избранное"

            response_data = {
                "already_in_favorite": False,
                "success_message": success_message,
            }
    
    user_favorite = get_user_favorites(request)
    favorite_items_html = render_to_string(
        "carts/includes/included_favorite.html", {"favorites": user_favorite}, request=request)

    response_data["favorite_items_html"] = favorite_items_html

    return JsonResponse(response_data)

def favorite_remove(request):

    favorite_id = request.POST.get("favorite_id")

    favorite = Favorite.objects.get(id=favorite_id)

    product_category = favorite.product.category
    product_name = favorite.product.name

    quantity = Favorite.objects.filter(user=request.user).count()
    favorite.delete()

    user_favorite = get_user_favorites(request)
    favorite_items_html = render_to_string(
        "carts/includes/included_favorite.html", {"favorites": user_favorite}, request=request)

    success_message = f"Автомобиль {product_category} {product_name} удален из избранного"
    response_data = {
        "message": success_message,
        "favorite_items_html": favorite_items_html,
        "quantity_deleted": quantity, 
    }

    return JsonResponse(response_data)