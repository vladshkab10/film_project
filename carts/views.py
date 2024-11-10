from django.shortcuts import render
from carts.utils import get_user_carts, get_user_chosens
from .models import Cart
from goods.models import Products
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Chosens

# Create your views here.

def cart_add(request):

    product_id = request.POST.get("product_id")

    product = Products.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    
    else:
        carts = Cart.objects.filter(session_key=request.session.session_key, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)
    

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string( 
        "includes/includes.html", {"carts": user_cart}, request=request)

    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)

def chosens_add(request):
    product_id = request.POST.get("product_id")
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        chosens = Chosens.objects.filter(user=request.user, product=product)
        if chosens.exists():
            chosen = chosens.first()
            chosen.quantity += 1
            chosen.save()
        else:
            Chosens.objects.create(user=request.user, product=product)

    else:
        chosens = Chosens.objects.filter(session_key=request.session.session_key, product=product)
        if chosens.exists():
            chosen = chosens.first()
            chosen.quantity += 1
            chosen.save()
        else:
            Chosens.objects.create(session_key=request.session.session_key, product=product)

    user_chosen = get_user_chosens(request)
    chosen_items_html = render_to_string(
        "includes/chosens_include.html", {'chosens': user_chosen}, request=request)
    response_data = {
        'message': 'Товар добавлен в избранное',
        'chosen_items_html': chosen_items_html,
    }
    return JsonResponse(response_data)

def chosens_remove(request):

    chosen_id = request.POST.get("chosen_id")

    chosen = Chosens.objects.get(id=chosen_id)
    chosen.delete()

    user_chosen = get_user_chosens(request)

    chosen_items_html = render_to_string(
        "includes/chosens_include.html", {"chosens": user_chosen}, request=request)

    response_data = {
        "message": "Товар удален",
        "chosen_items_html": chosen_items_html,
    }

    return JsonResponse(response_data)

def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity

    user_cart = get_user_carts(request)

    context = {"carts": user_cart}

    # if referer page is create_order add key orders: True to context

    cart_items_html = render_to_string(
        "includes/includes.html", context, request=request)

    response_data = {
        "message": "Количество изменено",
        "cart_items_html": cart_items_html,
        "quantity": updated_quantity,
    }

    return JsonResponse(response_data)


def cart_remove(request):
    
    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)

    cart_items_html = render_to_string(
        "includes/includes.html", {"carts": user_cart}, request=request)

    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)


def chosens(request):
    return render(request, 'chosens.html')