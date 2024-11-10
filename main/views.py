from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from goods.models import Categories
from main.models import Post
from django.contrib import messages
# Create your views here.
def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'Home - главная',
        'content': 'Магазин мебели Home',
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - о нас',
        'content': 'О нас',
        'text_on_page': 'Текст о магазине.',
    }
    return render(request, 'main/about.html', context)

def post_create(request):
    if request.method == 'POST':
        good = request.POST['good']
        bad = request.POST['bad']
        text =  request.POST['text']
        post = Post(good=good, bad=bad, text=text)
        if post and good != '' and bad != '' and text != '':
            post.save()
            messages.success(request, 'Ваш отзыв был успешно создан!')
            return HttpResponseRedirect(reverse('main:index'))
        else:
            messages.warning(request, 'Сообщение не должно быть пустым')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return render(request, 'main/post-create.html')

def posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'main/posts.html', context)

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    messages.success(request, 'Отзыв удалён')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])