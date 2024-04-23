from unicodedata import category
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from decimal import Decimal

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')


    class Meta:
        db_table = 'category'
        verbose_name = 'Марку'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Марка')
    name = models.CharField(max_length=150, verbose_name='Модель')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)],
        verbose_name='Год')
    engine = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(15.0)],
        verbose_name='Объем двигателя')
    power = models.PositiveIntegerField(
        validators=[MaxValueValidator(5000)],
        verbose_name='Мощность')
    mileage = models.PositiveIntegerField(
        validators=[MaxValueValidator(10000000)],
        verbose_name='Пробег'
    )
    gearbox_choices = [
    ('manual', 'Механическая'),
    ('automatic', 'Автомат'),
    ('robotic', 'Робот'),
    ('variator', 'Вариатор'),
    ]   
    gearbox = models.CharField(
        choices=gearbox_choices,
        max_length=15,
        verbose_name='Коробка передач'
    )
    color_choices = [
        ('black', 'Черный'),
        ('white', 'Белый'),
        ('grey', 'Серый'),
        ('red', 'Красный'),
        ('blue', 'Синий'),
        ('yellow', 'Желтый'),
        ('green', 'Зеленый'),
        ('brown', 'Коричневый'),
    ]
    color = models.CharField(
        choices=color_choices,
        max_length=15,
        verbose_name='Цвет'
    )
    fuel_choices=[
        ('gasoline', 'Бензин'),
        ('diesel', 'Дизель'),
        ('electric', 'Электро'),
    ]
    fuel = models.CharField(
        choices=fuel_choices,
        max_length=15,
        verbose_name='Топливо'
    )
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='cars_images', blank=True, null=True, verbose_name='Изображение1')
    image2 = models.ImageField(upload_to='cars_images', blank=True, null=True, verbose_name='Изображение2')
    image3 = models.ImageField(upload_to='cars_images', blank=True, null=True, verbose_name='Изображение3')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    discount = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=0, verbose_name='Скидка в %')
    

    class Meta:
        db_table = 'product'
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return self.name
    
    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(Decimal(self.price) - Decimal(self.price)/100*self.discount, 0)
        
        return self.price