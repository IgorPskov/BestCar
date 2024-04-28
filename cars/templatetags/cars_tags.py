from django.utils.http import urlencode
from django import template

from cars.models import Categories


register = template.Library()


@register.simple_tag()
def tag_categories():
    categories = Categories.objects.all().order_by('name')

    # Создаем объект "Все марки" и добавляем его в начало списка
    all_categories = Categories(name="Все марки", slug="all")
    categories = [all_categories] + list(categories)

    return categories

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)