from django.shortcuts import render


def catalog(request):
    return render(request, 'cars/catalog.html')


def product(request):
    return render(request, 'cars/product.html')
