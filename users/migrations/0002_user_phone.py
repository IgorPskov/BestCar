# Generated by Django 4.2.7 on 2024-05-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, null=True, verbose_name='Номер телефона'),
        ),
    ]
