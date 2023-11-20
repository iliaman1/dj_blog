from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView
from .models import Profile
from .forms import RegistrationForm, LoginForm, EditProfileForm
from core.utils import BaseDataMixin

from apps.blog.models import Post


class ShowProfile(BaseDataMixin, DetailView):
    model = Profile
    template_name = 'user/user_profile.html'
    extra_context = {
        'title': 'Профиль'
    }

    def get_context_data(self, *args, **kwargs):
        page_user = get_object_or_404(Profile, name=self.kwargs['name'])
        context = super().get_context_data()
        context['page_user'] = page_user
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, name=self.kwargs['name'])


class ShowUserPosts(BaseDataMixin, DetailView):
    model = Profile
    template_name = 'user/user_profile.html'
    extra_context = {
        'title': 'Профиль'
    }

    def get_context_data(self, *args, **kwargs):
        page_user = get_object_or_404(Profile, name=self.kwargs['name'])
        context = super().get_context_data()
        context['page_user'] = page_user
        context['posts'] = Post.objects.filter(author__profile__name=self.kwargs['name'])
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, name=self.kwargs['name'])


class ShowUserComments(BaseDataMixin, DetailView):
    model = Profile
    template_name = 'user/user_profile.html'
    extra_context = {
        'title': 'Профиль'
    }

    def get_context_data(self, *args, **kwargs):
        page_user = get_object_or_404(Profile, name=self.kwargs['name'])
        context = super().get_context_data()
        context['page_user'] = page_user
        context['posts'] = Post.objects.filter(comments__owner__profile__name=self.kwargs['name'])
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, name=self.kwargs['name'])


class ShowUserVotes(BaseDataMixin, DetailView):
    model = Profile
    template_name = 'user/user_profile.html'
    extra_context = {
        'title': 'Профиль'
    }

    def get_context_data(self, *args, **kwargs):
        page_user = get_object_or_404(Profile, name=self.kwargs['name'])
        context = super().get_context_data()
        context['page_user'] = page_user
        context['posts'] = Post.objects.filter(vote__user__profile__name=self.kwargs['name'])
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, name=self.kwargs['name'])


class EditProfile(LoginRequiredMixin, BaseDataMixin, UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'user/edit_profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)


class Registration(BaseDataMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'user/registration.html'
    # success_url = reverse_lazy('home')
    raise_exception = False
    extra_context = {
        'title': 'Регистрация'
    }

    def form_valid(self, form):
        user = form.save()
        profile = Profile.objects.create(user=user, name=user)
        login(self.request, user)
        return redirect('home')


class Login(BaseDataMixin, LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'
    extra_context = {
        'title': 'Авторизация'
    }

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
