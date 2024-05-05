from django import template

from carts.models import Cart, Favorite
from carts.utils import get_user_carts, get_user_favorites


register = template.Library()


@register.simple_tag()
def user_carts(request):
        return get_user_carts(request)
    
@register.simple_tag()
def user_favorites(request):
    return get_user_favorites(request)