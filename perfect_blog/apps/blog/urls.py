from django.urls import path

from .views import BlogHome, BlogCategory, ShowMyPosts, BestOfTheDay, BestOfTheWeek, BestOfTheMonth, ShowPost, \
    upvote_post, downvote_post, AddPost, EditPost, DeletePost, About, login

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('category/<slug:category_slug>', BlogCategory.as_view(), name='category'),
    path('myposts/', ShowMyPosts.as_view(), name='myposts'),
    path('bestoftheday/', BestOfTheDay.as_view(), name='bestoftheday'),
    path('bestoftheweek/', BestOfTheWeek.as_view(), name='bestoftheweek'),
    path('bestofthemonth/', BestOfTheMonth.as_view(), name='bestofthemonth'),
    path('editpost/<slug:post_slug>', EditPost.as_view(), name='editpost'),
    path('deletepost/<slug:post_slug>', DeletePost.as_view(), name='deletepost'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('upvote/<slug:post_slug>', upvote_post, name='upvote_post'),
    path('downvote/<slug:post_slug>', downvote_post, name='downvote_post'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('about/', About.as_view(), name='about'),

    path('login/', login, name='login')

]
