from carts.models import Favorite, Cart


def get_user_favorites(request):
    if request.user.is_authenticated:
        return Favorite.objects.filter(user=request.user)
    
def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)