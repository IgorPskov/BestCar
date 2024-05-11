from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from carts.models import Cart, Favorite
from orders.models import Order, OrderItem
from users.forms import ConsultForm, ProfileForm, UserLoginForm, UserRegistrationForm
from users.models import Consult

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")


                if session_key:
                    carts = Cart.objects.filter(session_key=session_key)
                    favorites = Favorite.objects.filter(session_key=session_key)
                    
                    if carts.exists():
                        # Получаем товары из сессии и создаем их для пользователя, если их еще нет в его корзине
                        for cart in carts:
                            existing_cart = Cart.objects.filter(user=user, product=cart.product)
                            if not existing_cart.exists():
                                Cart.objects.create(user=user, product=cart.product)

                    if favorites.exists():
                        # Получаем товары из сессии и создаем их для пользователя, если их еще нет в его корзине
                        for favorite in favorites:
                            existing_favorite = Favorite.objects.filter(user=user, product=favorite.product)
                            if not existing_favorite.exists():
                                Favorite.objects.create(user=user, product=favorite.product)


                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
        
    context = {
        'title': 'BestCar - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key    

            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")

            if session_key:
                    carts = Cart.objects.filter(session_key=session_key)
                    favorites = Favorite.objects.filter(session_key=session_key)
                    
                    if carts.exists():
                        # Получаем товары из сессии и создаем их для пользователя, если их еще нет в его корзине
                        for cart in carts:
                            existing_cart = Cart.objects.filter(user=user, product=cart.product)
                            if not existing_cart.exists():
                                Cart.objects.create(user=user, product=cart.product)

                    if favorites.exists():
                        # Получаем товары из сессии и создаем их для пользователя, если их еще нет в его корзине
                        for favorite in favorites:
                            existing_favorite = Favorite.objects.filter(user=user, product=favorite.product)
                            if not existing_favorite.exists():
                                Favorite.objects.create(user=user, product=favorite.product)

            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'BestCar - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    orders = (
        Order.objects.filter(user=request.user)
            .prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            )
            .order_by("-id")
    )
    context = {
        'title': 'BestCar - Кабинет',
        'form': form,
        'orders': orders
    }
    return render(request, 'users/profile.html', context)


def users_cart(request):
    return render(request, 'users/users_cart.html')


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))


def create_consultation(request):
    if request.method == 'POST':
        form = ConsultForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваша заявка принята!")
            return HttpResponseRedirect(reverse('main:index'))
        else:
            messages.warning(request, "Пожалуйста, заполните все поля корректно.")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = ConsultForm()

    return render(request, 'main/index.html', {'form': form})