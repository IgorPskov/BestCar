# Generated by Django 4.2.7 on 2024-05-10 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0031_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'В обрботке'), (1, 'Ожидает оплаты'), (2, 'Готов к выдаче'), (3, 'В доставке'), (4, 'Завершен')], default=0, verbose_name='Статус заказа'),
        ),
    ]
