from django.db import models
from users.models import User
from goods.models import Products
# Create your models here.

class CartQuerySet(models.QuerySet):
    
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(to=User, blank=True, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины покупателей'
    
    objects = CartQuerySet().as_manager()
    
    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}'
        else:
            return f'Корзина для анонимного пользователя | {self.product.name} | {self.quantity}'

class Chosens(models.Model):
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, blank=True, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return f'Избранное {self.product.name}'