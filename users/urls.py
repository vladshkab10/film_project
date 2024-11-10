from django.contrib import admin
from django.urls import path
from .views import login, registration, profile, logout
from users import views
app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('users-cart/', views.users_cart, name='users-cart')
]