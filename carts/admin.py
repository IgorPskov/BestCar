from django.contrib import admin

from carts.models import Cart, Favorite


admin.site.register(Cart)
admin.site.register(Favorite)