from django.shortcuts import render

from .models import Post

nav_menu = ['Создать пост', 'О всяком', 'Войти']


def index(request):
    posts = Post.objects.all()
    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
            'nav_menu': nav_menu,
            'title': 'Main page'
        }
    )


def about(request):
    return render(request, 'blog/about.html', {'nav_menu': nav_menu, 'title': 'О всяком'})
