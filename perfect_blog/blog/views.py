from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .models import Post
from .forms import AddPostForm
from .utils import DataMixin


class BlogHome(DataMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        return dict(**super().get_context_data(**kwargs), **self.get_user_context(title='Все посты'))

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class BlogCategory(DataMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(
            **context,
            **self.get_user_context(title=context['posts'][0].category, cat_selected=context['posts'][0].category_id)
        )

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)


class ShowPost(DataMixin, DetailView):
    model = Post
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(
            **context,
            **self.get_user_context(title=context['post'].title, cat_selected=context['post'].category_id)
        )


class AddPost(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/addpost.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        return dict(**super().get_context_data(**kwargs), **self.get_user_context(title='Создание поста'))


class About(DataMixin, TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return dict(**super().get_context_data(**kwargs), **self.get_user_context(title='О всяком'))


def login(request):
    ...
