# Generated by Django 4.2.7 on 2024-05-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_first_name_order_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(verbose_name='Номер телефона'),
        ),
    ]
