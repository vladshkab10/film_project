from django.db import models

from users.models import User

# Create your models here.
class Chat(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_author = models.BooleanField(default=False)
    amount_of_message = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чат'

    def __str__(self):
        return f'Сообщение от {self.user.username}: {self.message}'