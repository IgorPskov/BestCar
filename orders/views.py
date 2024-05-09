from email import message
from gettext import install
from unicodedata import category
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from traitlets import default

from carts.models import  Cart, CartQuerySet 
from cars.utils import calculate_installment

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem, OrderItemQueryset

@login_required
def create_order(request):

   # Получаем все заказы пользователя
    user_carts = Cart.objects.filter(user=request.user)

    # Вызываем метод total_price для получения общей суммы заказов пользователя
    total_price = user_carts.total_price()
    total_price = float(total_price)

    installment_24 = calculate_installment(total_price, 24)
    installment_36 = calculate_installment(total_price, 36)
    installment_60 = calculate_installment(total_price, 60)

    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST, request=request)
        

        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)
                        
                    #Создать заказ
                    order = Order.objects.create(
                        user=user,
                        first_name=form.cleaned_data.get('first_name'),
                        last_name=form.cleaned_data.get('last_name'),
                        phone=form.cleaned_data.get('phone'),
                        total_price=total_price,
                        requires_delivery=form.cleaned_data.get('requires_delivery'),
                        delivery_address=form.cleaned_data.get('delivery_address'),
                        delivery_price=form.cleaned_data.get('delivery_price'),
                        requires_installment=form.cleaned_data.get('requires_installment'),
                        installment=form.cleaned_data.get('installment'),
                        monthly_payment = 0,
                        payment_on_get=form.cleaned_data.get('payment_on_get'),
                    )

                    # Вычисляем ежемесячный платеж
                    if order.requires_installment == 1:
                        if order.installment == 1:
                            order.monthly_payment = installment_24
                        elif order.installment == 2:
                            order.monthly_payment = installment_36
                        elif order.installment == 3:
                            order.monthly_payment = installment_60
                    else:
                        order.monthly_payment = 0

                    order.save()

                    #Создать заказанные авто
                    for cart_item in cart_items:
                        product = cart_item.product
                        category = cart_item.product.category
                        name = cart_item.product.name
                        price = cart_item.product.sell_price()

                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            category=category,
                            name=name,
                            price=price,
                        )

                    #Очистить корзину пользователя после создания заказа
                    cart_items.delete()

                    messages.success(request, 'Заказ оформлен!')
                    return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('cart:order')
        else:
            print(form.errors)
                        

    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'phone': request.user.phone,
        }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'BestCar - Оформление заказа',
        'form': form,
        'total_price': total_price,
        'installment_24': installment_24,
        'installment_36': installment_36,
        'installment_60': installment_60,
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
