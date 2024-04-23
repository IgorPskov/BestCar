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


def product(request):
    return render(request, 'cars/product.html')
