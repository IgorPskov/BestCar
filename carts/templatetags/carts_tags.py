from django import template

from carts.models import Cart, Favorite


register = template.Library()


@register.simple_tag()
def user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
    
@register.simple_tag()
def user_favorites(request):
    if request.user.is_authenticated:
        return Favorite.objects.filter(user=request.user)