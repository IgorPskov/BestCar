# Generated by Django 4.2.7 on 2024-05-11 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_consult_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consult',
            name='phone',
        ),
    ]
