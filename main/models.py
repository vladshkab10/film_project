from django.db import models

# Create your models here.
class Post(models.Model):
    good = models.CharField(max_length=100, null=True)
    bad = models.CharField(max_length=100, null=True)
    text = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Получен новый отзыв от {self.title}'