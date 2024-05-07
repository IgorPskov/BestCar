from django.shortcuts import render

from carts.models import  Cart, CartQuerySet 
from cars.utils import calculate_installment


def create_order(request):

    #Рассрочка
    if request.user.is_authenticated:
        # Получаем объекты корзины текущего пользователя
        user_carts = Cart.objects.filter(user=request.user)

        # Вызываем метод total_price для получения общей суммы
        total_price = user_carts.total_price()
        total_price = float(total_price)

        installment_24 = calculate_installment(total_price, 24)
        installment_36 = calculate_installment(total_price, 36)
        installment_60 = calculate_installment(total_price, 60)

        context = {
            'installment_24': installment_24,
            'installment_36': installment_36,
            'installment_60': installment_60,
        }
    else:
        # Если пользователь не аутентифицирован, предоставьте пустой контекст
        context = {}
    
    return render(request, 'orders/create_order.html', context=context)



