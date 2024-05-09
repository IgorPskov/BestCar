# Generated by Django 4.2.7 on 2024-05-09 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_products_options'),
        ('orders', '0028_alter_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='name',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='cars.products', verbose_name='Модель'),
        ),
    ]
