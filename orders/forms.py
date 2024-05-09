from django import forms
from django.http import request

from orders.models import Order
from users.models import User


class CreateOrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateOrderForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'requires_delivery', 'delivery_address', 'delivery_price', 'requires_installment', 'installment', 'payment_on_get']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'requires_delivery': 'Требуется доставка',
            'delivery_address': 'Адрес доставки',
            'delivery_price': 'Стоимость доставки',
            'requires_installment': 'Требуется кредит',
            'installment': 'Вариант кредита',
            'payment_on_get': 'Оплата при получении',
        }
        widgets = {
            'installment': forms.RadioSelect(choices=Order.INSTALLMENT_OPTIONS),
            'requires_delivery': forms.RadioSelect(choices=Order.REQUIRES_DELIVERY_OPTIONS),
            'requires_installment': forms.RadioSelect(choices=Order.REQUIRES_INSTALLMENT_OPTIONS),
            'payment_on_get': forms.RadioSelect(choices=Order.PAYMENT_OPTIONS),
        }
    
        
    # Проверка если выбрана доставка, но не выбран адрес доставки
    def clean(self):
        cleaned_data = super().clean()
        requires_delivery = cleaned_data.get('requires_delivery')
        delivery_address = cleaned_data.get('delivery_address')

        if requires_delivery == 1:
            if not delivery_address:
                self.add_error(None, 'Выберите точку доставки на карте.')
        
        self.installment_choice()
        self.clean_delivery()

        return cleaned_data
    
     # Проверка если выбран кредит, но не выбран срок кредита
    def installment_choice(self):
        cleaned_data = super().clean()
        
        requires_installment = cleaned_data.get('requires_installment')
        installment = cleaned_data.get('installment')

        if requires_installment == 1:
            if installment == 0:
                self.add_error(None, 'Выберите срок кредита или откажитесь от него.')
                return cleaned_data
            else:
                return cleaned_data
        # Если кредит не выбран, но выбран срок кредита, в заказе кредит тоже будет не выбран
        elif requires_installment == 0:
            cleaned_data['installment'] = 0
            return cleaned_data
        
    def clean_delivery(self):
        cleaned_data = super().clean()
        requires_delivery = cleaned_data.get('requires_delivery')
        # Если доставка не требуется, очищаем адрес и цену доставки
        if requires_delivery == 0:
            cleaned_data['delivery_address'] = 'Доставка не требуется'
            cleaned_data['delivery_price'] = 0
            return cleaned_data


