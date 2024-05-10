# Generated by Django 4.2.7 on 2024-05-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_alter_order_requires_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='requires_delivery',
            field=models.IntegerField(choices=[(0, 'Нужна'), (1, 'Не нужна')], default=0, verbose_name='Требуется доставка'),
        ),
    ]