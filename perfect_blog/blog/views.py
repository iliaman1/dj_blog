from django.shortcuts import render

from .models import Post

nav_menu = [
    {'title': 'Создать пост', 'url_name': 'addpost'},
    {'title': 'О всяком', 'url_name': 'about'},
    {'title': 'Войти', 'url_name': 'login'}
]


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'nav_menu': nav_menu,
        'title': 'Main page'
    }
    return render(request, 'blog/index.html', context=context)


def about(request):
    return render(request, 'blog/about.html', {'nav_menu': nav_menu, 'title': 'О всяком'})


def addpost(request):
    ...


def login(request):
    ...

def show_post(request, post_id):
    ...
