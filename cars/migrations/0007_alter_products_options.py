# Generated by Django 4.2.7 on 2024-04-26 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_products_color_alter_products_fuel_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
    ]
