from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from orders.models import Order, OrderItem
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from carts.models import Cart
from django.db.models import Prefetch

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        session_key = request.session.session_key

        if user:
            auth.login(request, user)
            messages.success(request, f'{username}, Вы усшпешно вошли в аккант!')

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            redirect_page = request.POST.get('next', None)
            if redirect_page and redirect_page != reverse('users:logout'):
                return HttpResponseRedirect(request.POST.get('next'))

            return HttpResponseRedirect(reverse('main:index'))
        
    else:
        form = UserLoginForm()
    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            session_key = request.session.session_key

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            
            auth.login(request, user)
            messages.success(request, f'{user.username}, Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'Home - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлён')
            return HttpResponseRedirect(reverse('users:profile'))
            
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title': 'Home - Кабинет',
        'form': form,
    }
    orders = Order.objects.filter(user=request.user).prefetch_related(
        Prefetch(
            "orderitem_set",
            queryset=OrderItem.objects.select_related("product"),
        )
    ).order_by("-id")

    context = {
        'form': form,
        'orders': orders
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'Вы успешно вышли из аккаунта!')
    return redirect(reverse('main:index'))

def users_cart(request):
    return render(request, 'users/users_cart.html')