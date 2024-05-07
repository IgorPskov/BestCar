from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string

from carts.models import Cart, Favorite
from cars.models import Products
from carts.utils import get_user_carts, get_user_favorites

def cart_add(request):
    product_id = request.POST.get("product_id")    
    product = Products.objects.get(id=product_id)

    product_category = product.category
    product_name = product.name

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            # Если товар уже в избранном, возвращаем флаг already_in_favorite=True
            response_data = {
                "already_in_cart": True,
                "warning_message": "Этот автомобиль уже добавлен к вам в корзину",
            }
        else:

            Cart.objects.create(user=request.user, product=product)
            success_message = f"Автомобиль {product_category} {product_name} добавлен в корзину"

            response_data = {
                "already_in_cart": False,
                "success_message": success_message,
            }

    else:
        carts = Cart.objects.filter(
            session_key = request.session.session_key, product = product)
        
        if carts.exists():
            # Если товар уже в избранном, возвращаем флаг already_in_favorite=True
            response_data = {
                "already_in_cart": True,
                "warning_message": "Этот автомобиль уже добавлен к вам в корзину",
            }
        else:

            Cart.objects.create(session_key=request.session.session_key, product=product)
            success_message = f"Автомобиль {product_category} {product_name} добавлен в корзину"

            response_data = {
                "already_in_cart": False,
                "success_message": success_message,
            }
    
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data["cart_items_html"] = cart_items_html

    return JsonResponse(response_data)
    

def cart_remove(request):
    cart_id = request.POST.get("cart_id")

    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, id=cart_id, user=request.user)
    else:
        cart = get_object_or_404(Cart, id=cart_id, session_key=request.session.session_key)

    product_category = cart.product.category
    product_name = cart.product.name

    if request.user.is_authenticated:
        quantity = Cart.objects.filter(user=request.user).count()
    else:
        quantity = Cart.objects.filter(session_key=request.session.session_key).count()

    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    success_message = f"Автомобиль {product_category} {product_name} удален из корзины"
    response_data = {
        "message": success_message,
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity, 
    }

    return JsonResponse(response_data)




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

    else:
        favorites = Favorite.objects.filter(
            session_key=request.session.session_key, product = product)
        
        if favorites.exists():
            # Если товар уже в избранном, возвращаем флаг already_in_favorite=True
            response_data = {
                "already_in_favorite": True,
                "warning_message": "Этот автомобиль уже добавлен к вам в избранное",
            }
        else:

            Favorite.objects.create(session_key=request.session.session_key, product=product)
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

    if request.user.is_authenticated:
        favorite = get_object_or_404(Favorite, id=favorite_id, user=request.user)
    else:
        favorite = get_object_or_404(Favorite, id=favorite_id, session_key=request.session.session_key)


    product_category = favorite.product.category
    product_name = favorite.product.name

    if request.user.is_authenticated:
        quantity = Favorite.objects.filter(user=request.user).count()
    else:
        quantity = Favorite.objects.filter(session_key=request.session.session_key).count()

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