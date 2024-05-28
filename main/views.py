from django.http import HttpResponse
from django.shortcuts import render

from cars.models import Categories, Products

products = Products.objects.all()

def index(request):

    context: dict[str, str] = {
        'title': 'BestCar - Главная',
        'content': 'Онлайн-автосалон BestCar',
        'products': products
    }

    return render(request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': 'BestCar - О нас',
        'content': 'О нас',
        'text_on_page': 'BestCar - ваш надежный партнер в мире автомобилей. Мы специализируемся на продаже качественных автомобилей с прозрачной и удобной системой покупки. Наша команда состоит из опытных профессионалов, готовых помочь вам выбрать идеальный автомобиль, соответствующий вашим потребностям и бюджету. Мы стремимся предоставить нашим клиентам лучший сервис, гарантированное качество и уверенность в каждой сделке. Доверьтесь нам при выборе вашего следующего автомобиля и ощутите разницу с BestCar.',
        'image': '../static/deps/images/cars.jpg'
    }

    return render(request, 'main/about.html', context)

def payment(request):
    context: dict[str, str] = {
        'title': 'BestCar - Доставка и оплата',
        'content': 'Доставка и оплата',
        'text_on_page': 'Условия доставки у нас просты и удобны: мы доставим ваш автомобиль в любую точку России, в которую можно добраться по дорогам. Стоимость доставки составляет 20 рублей за каждый километр, при этом минимальная стоимость доставки - 500 рублей. Оплата осуществляется онлайн при оформлении заказа, либо при получении автомобиля наличными или по выставленному счету. Также имеется возможность оформления автокредита на выгодных условиях, заемщиком выступает сам автосалон без участия банков! При условии, что оформлена доставка и выбрана оплата при получении автомобиля взимается полная предоплата стоимости доставки. Наша цель - ваше удовлетворение и комфорт!',
        'image': '../static/deps/images/dostavka.jpg'
    }

    return render(request, 'main/payment.html', context)

def warranty(request):
    context: dict[str, str] = {
        'title': 'BestCar - Гарантия и возврат',
        'content': 'Гарантия и возврат',
        'text_on_page': 'В нашем интернет-магазине автомобилей мы предоставляем гарантию на все приобретенные автомобили сроком на 3 месяца. Гарантия покрывает любые дефекты и неисправности автомобилей, возникшие не по вине покупателя. Для возврата автомобиля необходимо связаться с нашей службой поддержки и предоставить все необходимые документы и доказательства дефекта. Мы гарантируем высокое качество обслуживания и оперативное решение всех ваших проблем.',
        'image': '../static/deps/images/warranty.jpg'
    }

    return render(request, 'main/payment.html', context)

def contact(request):
    context: dict[str, str] = {
        'title': 'BestCar - Контакты',
        'content': 'Контакты',
    }

    return render(request, 'main/contact.html', context)