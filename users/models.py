from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.formfields import PhoneNumberField



class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    phone = models.CharField(blank=True, null=True, verbose_name='Номер телефона')


    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username