# Generated by Django 4.2.7 on 2024-05-11 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_consult_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consult',
            name='phone',
        ),
    ]
