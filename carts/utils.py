from .models import Cart
from .models import Chosens

def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
    
    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key)


def get_user_chosens(request):
    if request.user.is_authenticated:
        return Chosens.objects.filter(user=request.user)
    
    if not request.session.session_key:
        request.session.create()
    return Chosens.objects.filter(session_key=request.session.session_key)
