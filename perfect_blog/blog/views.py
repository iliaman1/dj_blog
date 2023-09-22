from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import AddPostForm, EditPostForm
from .utils import DataMixin


class BlogHome(DataMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    additional_context = {
        'title': 'Все посты'
    }

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class BlogCategory(DataMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        self.additional_context['title'] = queryset[0].category
        self.additional_context['cat_selected'] = queryset[0].category_id

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)


class ShowMyPosts(LoginRequiredMixin, DataMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class ShowPost(DataMixin, DetailView):
    model = Post
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        post = self.get_object()
        self.additional_context['title'] = post.title
        self.additional_context['cat_selected'] = post.category_id

        return super().get_context_data(**kwargs)



class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/addpost.html'
    success_url = login_url = reverse_lazy('home')
    raise_exception = False
    additional_context = {
        'title': 'Создание поста'
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, DataMixin, UpdateView):
    form_class = EditPostForm


class About(DataMixin, TemplateView):
    template_name = 'blog/about.html'
    additional_context = {
        'title': 'О всяком'
    }


def login(request):
    ...
