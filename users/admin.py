from django.contrib import admin

from carts.admin import CartTabAdmin, FavoriteTabAdmin
from orders.admin import OrderTabulareAdmin
from users.models import Consult, User

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name', 'last_name', 'email']
    search_fields = ['username','first_name', 'last_name', 'email']

    inlines = [CartTabAdmin, FavoriteTabAdmin, OrderTabulareAdmin]

@admin.register(Consult)
class ConsultAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'name', 'phone', 'created_timestamp']
    search_fields = ('user__username', 'name', 'phone', 'created_timestamp',)
    fields = ['user', 'name', 'phone', 'session_key', 'created_timestamp']
    readonly_fields = ('session_key', 'created_timestamp')

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        else:
            # Присваиваем "Анонимный пользователь" в качестве имени пользователя
            return "Анонимный пользователь"