from django.urls import path

from .views import BlogHome, BlogCategory, ShowMyPosts, ShowPost, like_post, dislike_post, AddPost, EditPost, \
    DeletePost, About, login

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('category/<slug:category_slug>', BlogCategory.as_view(), name='category'),
    path('myposts/', ShowMyPosts.as_view(), name='myposts'),
    path('editpost/<slug:post_slug>', EditPost.as_view(), name='editpost'),
    path('deletepost/<slug:post_slug>', DeletePost.as_view(), name='deletepost'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('like/<slug:post_slug>', like_post, name='like_post'),
    path('dislike/<slug:post_slug>', dislike_post, name='dislike_post'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('about/', About.as_view(), name='about'),

    path('login/', login, name='login')

]
