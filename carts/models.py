from django.db import models

from cars.models import Products
from users.models import User

class CartQuerySet(models.QuerySet): 
    
    def total_price(self):
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        return self.count()

class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Автомобиль')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = "Корзину"
        verbose_name_plural = "Корзины"

    objects = CartQuerySet().as_manager()
    
    def product_price(self):
        return self.product.sell_price()

    def __str__(self):
        return f'Корзина {self.user.username} | Автомобиль {self.product.name}'


class FavoriteQuerySet(models.QuerySet):

    def total_price(self):
        return sum(favorite.product_price() for favorite in self)

    def total_quantity(self):
        return self.count()

class Favorite(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Автомобиль')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'favorite'
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"

    objects = FavoriteQuerySet().as_manager()
    
    def product_price(self):
        return self.product.sell_price()

    def __str__(self):
        return f'Корзина {self.user.username} | Автомобиль {self.product.name}'

