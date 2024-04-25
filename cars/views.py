from django.shortcuts import get_list_or_404, render
from django.template import context

from cars.models import Products

def catalog(request, category_slug):

    if category_slug == 'all':
        cars = Products.objects.all()
    else:
        cars = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    context = {
        'title': 'BestCar - Каталог',
        'cars': cars,
    }
    return render(request, 'cars/catalog.html', context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'cars/product.html', context=context)
