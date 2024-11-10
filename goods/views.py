from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.template.loader import render_to_string
from goods.utils1 import get_user_likes
from .models import Products
from django.core.paginator import Paginator
from .utils import q_search
from django.contrib import messages

# Create your views here.
def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        products = Products.objects.all()
    elif query:
        products = q_search(query)
    else:
        products = Products.objects.filter(category__slug=category_slug)
        if not products.exists():
            raise Http404()

    if on_sale:
        if on_sale and order_by == 'is_liked' or order_by == 'is_disliked' or order_by == 'out' or order_by == 'in':
            messages.warning(request, 'Такая сортировка невозможна')
        elif on_sale and order_by != 'default':
            messages.success(request, 'Выбраны только товары по скидке и сортировка')
            products = products.filter(discount__gt=0)
        else:
            messages.success(request, 'Выбраны только товары по скидке')
            products = products.filter(discount__gt=0)
    elif order_by and order_by == 'out':
        messages.success(request, 'Сортировка по количеству')
        products = products.filter(is_little=True)
    elif order_by and order_by == 'in':
        messages.success(request, 'Сортировка по количеству')
        products = products.filter(is_little=False)
    elif order_by and order_by == 'is_liked':
        messages.success(request, 'Сортировка по оценённым')
        products = products.filter(is_liked=True)
    elif order_by and order_by == 'is_disliked':
        messages.success(request, 'Сортировка по неоценённым')
        products = products.filter(is_disliked=True)
    elif order_by and order_by != 'default':
        if not on_sale:
            messages.success(request, 'Сортировка по цене')
        products = products.order_by(order_by)
    elif order_by and order_by == 'default':
        messages.success(request, 'Все товары')
    
    

    paginator = Paginator(products, 3)
    current_page = paginator.page(int(page))
    context = {
        'products': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    if product.quantity < 10:
        product.is_little = True
        product.save()
    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context)


def like(request, product_id=None):
    products = Products.objects.get(id=product_id)
    if products.is_liked == False:
        products.likes += 1
        products.is_liked = True
        products.save()
        messages.success(request, f'Вы оценили товар {products.name}, количество лайков: {products.likes}')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        messages.warning(request, f'Вы уже оценивали продукт {products.name}')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
def remove_like(request, product_id=None):
    products = Products.objects.get(id=product_id)
    if products.is_liked:
        products.is_liked = False
        products.likes -= 1
        products.save()
        messages.success(request, 'Оценка отменена')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        messages.warning(request, 'Вы не оценивали данный товар')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
def remove_dislike(request, product_id=None):
    products = Products.objects.get(id=product_id)
    if products.is_disliked:
        products.is_disliked = False
        products.dislikes -= 1
        products.save()
        messages.success(request, 'Оценка отменена')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        messages.warning(request, 'Вы не оценивали данный товар')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

def dislike(request, product_id):
    products = Products.objects.get(id=product_id)
    if products.is_disliked == False:
        products.dislikes += 1
        products.is_disliked = True
        products.save()
        messages.success(request, f'Вы оценили товар {products.name}, количество дизлайков: {products.dislikes}')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        messages.warning(request, f'Вы уже оценивали продукт {products.name}')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
