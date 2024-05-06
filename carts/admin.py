from types import NoneType
from django.contrib import admin

from carts.models import Cart, Favorite


# admin.site.register(Cart)
# admin.site.register(Favorite)

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = 'product', 'created_timestamp'
    search_fiels =  "product", 'created_timestamp'
    readonly_fields = ('created_timestamp',)
    extra = 1

class FavoriteTabAdmin(admin.TabularInline):
    model = Favorite
    fields = 'product', 'created_timestamp'
    search_fiels =  "product", 'created_timestamp'
    readonly_fields = ('created_timestamp',)
    extra = 1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product_display', 'product', 'created_timestamp',]
    list_filter = ['created_timestamp', 'user', 'product__category', 'product' ]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
            
        return "Анонимный пользователь"
    
    def product_display(self, obj):
        return str(obj.product.category)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product_display', 'product', 'created_timestamp',]
    list_filter = ['created_timestamp', 'user', 'product__category', 'product' ]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
            
        return "Анонимный пользователь"
    
    def product_display(self, obj):
        return str(obj.product.category)


