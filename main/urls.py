from django.contrib import admin
from django.urls import path
from main.views import index, about, post_create, posts, delete_post

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('posts/post-create/', post_create, name='post_create'),
    path('posts/', posts, name='posts'),
    path('posts/remove_post/<int:post_id>/', delete_post, name='remove_post'),
]