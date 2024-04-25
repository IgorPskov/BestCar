from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from django.template import context

from cars.models import Products

def catalog(request, category_slug):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by_price = request.GET.get('order_by_price', None)

    if category_slug == 'all':
        cars = Products.objects.all()
    else:
        cars = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    
    if on_sale:
        cars = cars.filter(discount__gt=0)

    if order_by_price and order_by_price != "default":
        cars = cars.order_by(order_by_price)


    paginator = Paginator(cars, 6)
    current_page = paginator.page(int(page))

    context = {
        'title': 'BestCar - Каталог',
        'cars': current_page,
        'slug_url': category_slug
    }
    return render(request, 'cars/catalog.html', context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'cars/product.html', context=context)
