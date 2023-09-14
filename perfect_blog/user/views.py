from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm, LoginForm


class Registration(CreateView):
    form_class = RegistrationForm
    template_name = 'user/registration.html'
    # success_url = reverse_lazy('home')
    raise_exception = False
    extra_context = {
        'title': 'Регистрация'
    }

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class Login(LoginView):
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
