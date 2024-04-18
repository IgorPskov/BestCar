from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context: dict[str, str] = {
        'title': 'BestCar - Главная',
        'content': 'Онлайн-автосалон BestCar'
    }

    return render(request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': 'BestCar - О нас',
        'content': 'О нас',
        'text_on_page': 'BestCar - ваш надежный партнер в мире автомобилей. Мы специализируемся на продаже качественных автомобилей с прозрачной и удобной системой покупки. Наша команда состоит из опытных профессионалов, готовых помочь вам выбрать идеальный автомобиль, соответствующий вашим потребностям и бюджету. Мы стремимся предоставить нашим клиентам лучший сервис, гарантированное качество и уверенность в каждой сделке. Доверьтесь нам при выборе вашего следующего автомобиля и ощутите разницу с BestCar.'
    }

    return render(request, 'main/about.html', context)

def payment(request):
    context: dict[str, str] = {
        'title': 'BestCar - Доставка и оплата',
        'content': 'Доставка и оплата',
        'text_on_page': 'Быстрая и дешевая доставка'
    }

    return render(request, 'main/payment.html', context)

def contact(request):
    context: dict[str, str] = {
        'title': 'BestCar - Контакты',
        'content': 'Контакты',
        'text_on_page': 'Телефон: 8-911-378-52-08; Почта: kovil22@mail.ru'
    }

    return render(request, 'main/contact.html', context)