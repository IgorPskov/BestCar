from django.shortcuts import render

def login(request):
    context = {
        'title': 'BestCar - Авторизация'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'BestCar - Регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'BestCar - Кабинет'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...