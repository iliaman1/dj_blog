from django.urls import path

from .views import index, about, addpost, login, show_post, show_category

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpost/', addpost, name='addpost'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>', show_post, name='post'),
    path('category/<slug:category_slug>', show_category, name='category')
]
