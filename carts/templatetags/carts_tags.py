from django import template
from carts.utils import get_user_carts, get_user_chosens
from carts.models import Cart

register = template.Library()

@register.simple_tag()
def user_carts(request):
    return get_user_carts(request)

@register.simple_tag()
def user_chosens(request):
    return get_user_chosens(request)