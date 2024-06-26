from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('payment/', views.payment, name='payment'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('warranty/', views.warranty, name='warranty'),
]