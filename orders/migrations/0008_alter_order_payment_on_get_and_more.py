# Generated by Django 4.2.7 on 2024-05-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_on_get',
            field=models.BooleanField(default=True, verbose_name='Оплата при получении'),
        ),
        migrations.AlterField(
            model_name='order',
            name='requires_installment',
            field=models.BooleanField(default=True, verbose_name='Требуется кредит'),
        ),
    ]
