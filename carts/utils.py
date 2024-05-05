from carts.models import Favorite, Cart


def get_user_favorites(request):
    if request.user.is_authenticated:
        return Favorite.objects.filter(user=request.user)
    
    if not request.session.session_key:
        request.session.create()
    return Favorite.objects.filter(session_key=request.session.session_key)

    
def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
    
    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key)