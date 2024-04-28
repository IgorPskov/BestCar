from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, redirect, render
from django.template import context
from django.db.models import Q

from cars.models import Products

def catalog(request, category_slug):

    #Страница
    page = request.GET.get('page', 1)
    #Скидка
    on_sale = request.GET.get('on_sale', None)
    #Коробка передач
    gearbox_manual = request.GET.get('gearbox_manual', None)
    gearbox_automatic = request.GET.get('gearbox_automatic', None)
    gearbox_robotic = request.GET.get('gearbox_robotic', None)
    gearbox_variator = request.GET.get('gearbox_variator', None)
    #Топливо
    fuel_gasoline = request.GET.get('fuel_gasoline', None)
    fuel_diesel = request.GET.get('fuel_diesel', None)
    fuel_electricity = request.GET.get('fuel_electricity', None)
    #Тип сортировки
    sort_type = request.GET.get('sort_type')

    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)

    min_year = request.GET.get('min_year', None)
    max_year = request.GET.get('max_year', None)

    min_power = request.GET.get('min_power', None)
    max_power = request.GET.get('max_power', None)

    min_mileage = request.GET.get('min_mileage', None)
    max_mileage = request.GET.get('max_mileage', None)


    if category_slug == 'all':
        cars = Products.objects.all()
    else:
        cars = get_list_or_404(Products.objects.filter(category__slug=category_slug))


    #Создаем 2 пустых Q списка
    gearbox_objects = Q()
    fuel_objects = Q()

    #Совмещение фильтров в Q списках
    if gearbox_manual:
        gearbox_objects |= Q(gearbox='Механическая')
    if gearbox_automatic:
        gearbox_objects |= Q(gearbox='Автомат')
    if gearbox_robotic:
        gearbox_objects |= Q(gearbox='Робот')
    if gearbox_variator:
        gearbox_objects |= Q(gearbox='Вариатор')


    if fuel_gasoline:
        fuel_objects |= Q(fuel='Бензин')
    if fuel_diesel:
        fuel_objects |= Q(fuel='Дизель')
    if fuel_electricity:
        fuel_objects |= Q(fuel='Электро')


    #Присваимаем cars отфильтрованный список
    cars = cars.filter(gearbox_objects).filter(fuel_objects)

    # Сортировка
    if sort_type == 'brand_asc':
        cars = cars.order_by('category')
    if sort_type == 'brand_asc':
        cars = cars.order_by('category__name')
    if sort_type == 'price_asc':
        cars = cars.order_by('price')
    elif sort_type == 'price_desc':
        cars = cars.order_by('-price')
    elif sort_type == 'year_asc':
        cars = cars.order_by('year')
    elif sort_type == 'year_desc':
        cars = cars.order_by('-year')
    elif sort_type == 'power_asc':
        cars = cars.order_by('power')
    elif sort_type == 'power_desc':
        cars = cars.order_by('-power')
    elif sort_type == 'mileage_asc':
        cars = cars.order_by('mileage')
    elif sort_type == 'mileage_desc':
        cars = cars.order_by('-mileage')

    
    # Чекбоксы
    if on_sale:
        cars = cars.filter(discount__gt=0)

    


    # Цена Проверяем, являются ли значения числами или пустыми строками
    try:
        if min_price:
            min_price = min_price
        else:
            min_price = None

        if max_price:
            max_price = max_price
        else:
            max_price = None
    except ValueError:
        # Если значения не являются числами, устанавливаем их в None
        min_price = None
        max_price = None

     # Фильтрация по цене, если указаны минимальная и/или максимальная цена
    if min_price is not None:
        cars = cars.filter(price__gte=min_price)
    if max_price is not None:
        cars = cars.filter(price__lte=max_price)


    # Год
    try:
        if min_year:
            min_year = min_year
        else:
            min_year = None

        if max_year:
            max_year = max_year
        else:
            max_year = None
    except ValueError:
        # Если значения не являются числами, устанавливаем их в None
        min_year = None
        max_year = None

    if min_year is not None:
        cars = cars.filter(year__gte=min_year)
    if max_year is not None:
        cars = cars.filter(year__lte=max_year)

    
    # Мощность
    try:
        if min_power:
            min_power = min_power
        else:
            min_power = None

        if max_power:
            max_power = max_power
        else:
            max_power = None
    except ValueError:
        # Если значения не являются числами, устанавливаем их в None
        min_power = None
        max_power = None

    if min_power is not None:
        cars = cars.filter(power__gte=min_power)
    if max_power is not None:
        cars = cars.filter(power__lte=max_power)
    

    # Пробег
    try:
        if min_mileage:
            min_mileage = min_mileage
        else:
            min_mileage = None

        if max_mileage:
            max_mileage = max_mileage
        else:
            max_mileage = None
    except ValueError:
        # Если значения не являются числами, устанавливаем их в None
        min_mileage = None
        max_mileage = None

    if min_mileage is not None:
        cars = cars.filter(mileage__gte=min_mileage)
    if max_mileage is not None:
        cars = cars.filter(mileage__lte=max_mileage)

    if 'reset_filters' in request.GET:
        # Очищаем GET-параметры фильтров и перенаправляем на страницу каталога
        return redirect('catalog:index', category_slug=category_slug)

    paginator = Paginator(cars, 6)
    current_page = paginator.page(int(page))

    context = {
        'title': 'BestCar - Каталог',
        'cars': current_page,
        'slug_url': category_slug,
        'order_by': sort_type,
    }
    return render(request, 'cars/catalog.html', context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'cars/product.html', context=context)




