from django.contrib import admin
from django.urls import path
from goods.views import catalog, product, like, dislike, remove_like, remove_dislike

app_name = 'goods'

urlpatterns = [
    path('search/', catalog, name='search'),
    path('<slug:category_slug>/', catalog, name='index'),
    path('product/<slug:product_slug>/', product, name='product'),
    path('feedback/like/<int:product_id>/', like, name='like'),
    path('feedback/remove_like/<int:product_id>/', remove_like, name='remove_like'),
    path('feedback/dislike/<int:product_id>/', dislike, name='dislike'),
    path('feedback/remove_dislike/<int:product_id>/', remove_dislike, name='remove_dislike'),
]