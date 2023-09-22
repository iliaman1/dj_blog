from django.urls import path

from .views import BlogHome, BlogCategory, ShowMyPosts, ShowPost, AddPost, About, login

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('category/<slug:category_slug>', BlogCategory.as_view(), name='category'),
    path('myposts/', ShowMyPosts.as_view(), name='myposts'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('about/', About.as_view(), name='about'),

    path('login/', login, name='login')

]
