from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.formfields import PhoneNumberField

from app import settings



class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    phone = models.CharField(blank=True, null=True, verbose_name='Номер телефона')


    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
    


class Consult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пользователь')
    name = models.CharField(max_length=150, verbose_name='Имя')
    phone = models.CharField(verbose_name='Номер телефона')
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа")

    class Meta:
        db_table = 'consult'
        verbose_name = ('Консультацию')
        verbose_name_plural = ('Консультации')

    def __str__(self):
        return f"{self.name} - {self.phone}"


