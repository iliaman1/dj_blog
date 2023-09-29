from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _

from .models import Post, Comment
from .forms import AddPostForm, AddCommentForm
from .utils import DataMixin
from .permissions import IsAuthorPermission


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


class ShowPost(DataMixin, DetailView, CreateView):
    model = Post
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    form_class = AddCommentForm

    def get_context_data(self, *, object_list=None, **kwargs):
        post = self.get_object()
        self.additional_context['title'] = post.title
        self.additional_context['cat_selected'] = post.category_id
        self.additional_context['comments'] = Comment.objects.filter(post=post.pk)
        self.additional_context['form_comment'] = AddCommentForm
        return super().get_context_data(**kwargs)

    # переписать пост метод для формы когда получаю данные с формы
    def form_valid(self, form):
        form.instance.post = self.get_object()
        form.instance.owner = self.request.user
        return super().form_valid(form)


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


class EditPost(LoginRequiredMixin, IsAuthorPermission, DataMixin, UpdateView):
    model = Post
    form_class = AddPostForm
    template_name = 'blog/editpost.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        post = self.get_object()
        self.additional_context['title'] = post.title
        self.additional_context['cat_selected'] = post.category_id

        return super().get_context_data(**kwargs)


class DeletePost(LoginRequiredMixin, IsAuthorPermission, DataMixin, DeleteView):
    model = Post
    slug_url_kwarg = 'post_slug'
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('myposts')


class About(DataMixin, TemplateView):
    template_name = 'blog/about.html'
    additional_context = {
        'title': 'О всяком'
    }


def login(request):
    ...
