from unicodedata import category
from django.db import models

from cars.models import Products
from users.models import User


class OrderItemQueryset(models.QuerySet):

    def total_price(self):
        return sum(order_item.price for order_item in self)

    def total_quantity(self):
        return self.count()


class Order(models.Model):

    REQUIRES_DELIVERY_OPTIONS = [
        (0, 'Нет'),
        (1, 'Да')
    ]

    REQUIRES_INSTALLMENT_OPTIONS = [
        (0, 'Нет'),
        (1, 'Да')
    ]

    INSTALLMENT_OPTIONS = [
            (0, 'Не выбран'),
            (1, '24 месяца'),
            (2, '36 месяцев'),
            (3, '60 месяцев'),
        ]
    
    PAYMENT_OPTIONS = [
        (0, 'Нет'),
        (1, 'Да')
    ]

    STATUS_OPTIONS = [
        (0, 'В обработке'),
        (1, 'Ожидает оплаты'),
        (2, 'Готов к выдаче'),
        (3, 'В доставке'),
        (4, 'Завершен')
    ]


    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="Пользователь", default=None)
    first_name = models.CharField(max_length=100, verbose_name="Имя") 
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    phone = models.CharField(verbose_name='Номер телефона')
    total_price = models.PositiveBigIntegerField(default=0, verbose_name='Общая стоимость заказа')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа")
    requires_delivery = models.IntegerField(choices=REQUIRES_DELIVERY_OPTIONS, default=0, verbose_name="Требуется доставка")
    delivery_address = models.TextField(null=True, blank=True, verbose_name="Адрес доставки")
    delivery_price = models.TextField(null=True, blank=True, verbose_name="Стоимость доставки")
    requires_installment = models.IntegerField(choices=REQUIRES_INSTALLMENT_OPTIONS, default=0, verbose_name="Требуется кредит")
    installment = models.IntegerField(choices=INSTALLMENT_OPTIONS, default=0, verbose_name="Вариант кредита")
    monthly_payment = models.IntegerField(default=0, verbose_name="Ежемесячный платеж")
    payment_on_get = models.IntegerField(choices=PAYMENT_OPTIONS,  verbose_name="Оплата при получении")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    status = models.IntegerField(choices=STATUS_OPTIONS, default=0, verbose_name="Статус заказа")

    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.user.first_name} {self.user.last_name}"



class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, null=True, verbose_name="Модель", default=None)
    category = models.CharField(max_length=150, verbose_name='Марка')
    price = models.PositiveIntegerField(default=0, verbose_name="Цена")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданный автомобиль"
        verbose_name_plural = "Проданные автомобили"

    objects = OrderItemQueryset.as_manager()

    def product_price(self):
        return self.price()
    
    def __str__(self):
        return f"Автомобиль {self.category} {self.product} | Заказ № {self.order.pk}"
    
