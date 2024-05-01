from django.utils.http import urlencode
from django import template

from cars.models import Categories


register = template.Library()


@register.simple_tag()
def tag_categories():
    categories = Categories.objects.all().order_by('name')

    # Создаем объект "Все марки" 
    all_categories = Categories(name="Все марки", slug="all")

    #Удаляем "Все марки" из конца списка
    categories = list(categories.exclude(slug='all'))

    # Добавляем "Все марки" в начало списка
    categories.insert(0, all_categories)

    return categories

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)