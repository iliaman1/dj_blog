from django.shortcuts import render

from .models import Post, Category

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
        'title': 'Все посты',
        'cat_selected': 0,
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


def show_category(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    if len(posts) == 0:
        return about(request)
    context = {
        'posts': posts,
        'nav_menu': nav_menu,
        'title': f'категория {Category.objects.get(pk=category_id)}',
        'cat_selected': category_id,
    }
    return render(request, 'blog/index.html', context=context)
