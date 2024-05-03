from carts.models import Favorite


def get_user_favorites(request):
    if request.user.is_authenticated:
        return Favorite.objects.filter(user=request.user)