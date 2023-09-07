from django.urls import path

from .views import index, about, addpost, login, show_post

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpost/', addpost, name='addpost'),
    path('login/', login, name='login'),
    path('post/<int:post_id>', show_post, name='post')
]
