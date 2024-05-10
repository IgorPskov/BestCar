# Generated by Django 4.2.7 on 2024-05-10 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0036_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[(0, 'В обработке'), (1, 'Ожидает оплаты'), (2, 'Готов к выдаче'), (3, 'В доставке'), (4, 'Завершен')], default='В обработке', verbose_name='Статус заказа'),
        ),
    ]
