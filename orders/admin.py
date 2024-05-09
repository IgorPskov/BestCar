from ast import Or
from django.contrib import admin

from orders.models import OrderItem, Order

class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "category", "name", "price"
    search_fields = (
        "product",
        "category",
    )
    extra = 0

class OrderTabulareAdmin(admin.TabularInline):
    model=Order
    fields = (
        "total_price",
        "requires_delivery",
        "requires_installment",
        "payment_on_get",
        'is_paid',
        'created_timestamp'
    )
    search_fields = (
        "requires_delivery",
        "requires_installment",
        'is_paid',
        'created_timestamp',
    )
    readonly_fields = ("created_timestamp",)
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'status', 'requires_delivery', 'requires_installment', 'is_paid', 'created_timestamp')
    search_fields = ('id','user__username', 'first_name', 'last_name', 'phone')
    list_filter = ('status', 'user', 'requires_delivery', 'requires_installment', 'total_price', 'created_timestamp')
    fields = ('user', 'first_name', 'last_name', 'created_timestamp', 'phone', 'total_price', 'requires_delivery', 'delivery_address', 'delivery_price', 'requires_installment', 'installment', 'monthly_payment', 'payment_on_get', 'is_paid', 'status')
    readonly_fields = ('created_timestamp',)
    inlines = (OrderItemTabulareAdmin,)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "category", "price"
    search_fields = (
        "order__id",
        "category",
        "product__name",
    )
    fields = "order", "product", "category", "price"
