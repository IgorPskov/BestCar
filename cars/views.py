from django.shortcuts import render
from django.template import context

from cars.models import Products

def catalog(request):

    cars = Products.objects.all()

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
