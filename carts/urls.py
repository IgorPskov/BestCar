from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart_add/', views.cart_add, name='cart_add'),
    path('cart_remove/', views.cart_remove, name='cart_remove'),
    path('favorite_add/', views.favorite_add, name='favorite_add'),
    path('favorite_remove/', views.favorite_remove, name='favorite_remove'),   
]