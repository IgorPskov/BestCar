# Generated by Django 4.2.7 on 2024-05-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0035_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[('В обработке', 0), ('Ожидает оплаты', 1), ('Готов к выдаче', 2), ('В доставке', 3), ('Завершен', 4)], default=0, verbose_name='Статус заказа'),
        ),
    ]
