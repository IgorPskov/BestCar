from ast import Or
from django.contrib import admin

from orders.models import OrderItem, Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'created_timestamp', 'phone', 'status')
    search_fields = ('id','user__username', 'first_name', 'last_name', 'phone')
    list_filter = ('status', 'user', 'created_timestamp')
    fields = ('user', 'first_name', 'last_name', 'created_timestamp', 'phone', 'total_price', 'requires_delivery', 'delivery_address', 'delivery_price', 'requires_installment', 'installment', 'monthly_payment', 'payment_on_get', 'is_paid', 'status')
    readonly_fields = ('created_timestamp',)
admin.site.register(OrderItem)
