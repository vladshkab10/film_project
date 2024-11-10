from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from chat.models import Chat
from django.contrib import messages
import datetime

# Create your views here.
@login_required
def chat(request):
    if request.method == 'POST':
        message = request.POST['message']
        chat = Chat(user=request.user, message=message, is_author=True)
        if chat and message != '':
            chat.save()
            messages.success(request, 'Сообщение отправлено')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            messages.warning(request, 'Сообщение не должно быть пустым')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    chat = Chat.objects.all()
    context = {
        'title': 'Чат',
        'chats': chat
    }
    return render(request, 'chat/chat.html', context)
def delete_message(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    if chat.is_author == True:
        chat.delete()
        messages.success(request, 'Сообщение удалено')
        print(f'Пользователь {chat.user.username} удалил сообщение: {chat.message}')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        messages.success(request, 'Вы не автор сообщения')
        print(f'Пользователь {chat.user.username} не автор сообщения')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])