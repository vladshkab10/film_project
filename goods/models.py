from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(null=True, upload_to='category_image')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return f'Новая категория {self.name}'


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)
    likes = models.SmallIntegerField(default=0)
    is_liked = models.BooleanField(default=False)
    dislikes = models.SmallIntegerField(default=0)
    is_disliked = models.BooleanField(default=0)
    is_little = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id', )

    def __str__(self):
        return f'Продукт {self.name}'
    
    def display_id(self):
        return f'{self.id:05}' 

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        elif self.is_liked:
            return round(self.price - self.price*self.discount/100 - self.price / 100 * 10, 2)
        else:
            return self.price
