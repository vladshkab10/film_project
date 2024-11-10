from django.urls import path
from .views import chat, delete_message

app_name = 'chat'
urlpatterns = [
    path('main/', chat, name='chat'),
    path('delete/<int:chat_id>/', delete_message, name='delete')
]
