from django.urls import path

from .views import index, about, addpost, login, show_post, show_category

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpost/', addpost, name='addpost'),
    path('login/', login, name='login'),
    path('post/<int:post_id>', show_post, name='post'),
    path('category/<int:category_id>', show_category, name='category')
]
