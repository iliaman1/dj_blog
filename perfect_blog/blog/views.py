from django.shortcuts import render

nav_menu = ['Создать пост', 'О всяком', 'Войти']


def index(request):
    return render(request, 'blog/index.html', {'nav_menu': nav_menu, 'title': 'Main page'})


def about(request):
    return render(request, 'blog/about.html', {'nav_menu': nav_menu, 'title': 'О всяком'})
