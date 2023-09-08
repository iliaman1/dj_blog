from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import AddPostForm

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
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    context = {'form': form, 'nav_menu': nav_menu, 'title': 'Добавить пост'}
    return render(request, 'blog/addpost.html', context=context)


def login(request):
    ...


def show_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    context = {
        'post': post,
        'nav_menu': nav_menu,
        'title': post.title,
        'cat_selected': post.category_id,
    }
    return render(request, 'blog/post.html', context=context)


def show_category(request, category_slug):
    posts = Post.objects.filter(slug=category_slug)
    category = Category.objects.get(slug=category_slug)
    context = {
        'posts': posts,
        'nav_menu': nav_menu,
        'title': f'категория {category}',
        'cat_selected': category.pk,
    }
    return render(request, 'blog/index.html', context=context)
