from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from carts.models import  Cart, CartQuerySet 
from cars.utils import calculate_installment

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


def create_order(request):

    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)


                    if cart_items.exists():
                        #Создать заказ
                        order = Order.objects.create(
                            user=user,
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            delivery_price=form.cleaned_data['delivery_price'],
                            requires_installment=form.cleaned_data['requires_installment'],
                            installment=form.cleaned_data['installment'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )

                        #Создать заказанные авто
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                            )
                            product.save()

                        #Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен!')
                        return redirect('user:profile')
            except ValidationError as e:
                #messages.success(request, str(e))
                return redirect('cart:order')
                        

    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }

        form = CreateOrderForm(initial=initial)

    
    context = {
        'title': 'BestCar - Оформление заказа',
        'form': form,
        # 'installment_24': installment_24,
        # 'installment_36': installment_36,
        # 'installment_60': installment_60,
    }
    
    return render(request, 'orders/create_order.html', context=context)


#Рассрочка
# user_carts = Cart.objects.filter(user=request.user)

# # Вызываем метод total_price для получения общей суммы
# total_price = user_carts.total_price()
# total_price = float(total_price)

# installment_24 = calculate_installment(total_price, 24)
# installment_36 = calculate_installment(total_price, 36)
# installment_60 = calculate_installment(total_price, 60)
