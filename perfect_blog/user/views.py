from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistrationForm


class Registration(CreateView):
    form_class = RegistrationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('home')
    raise_exception = False
    additional_context = {
        'title': 'Регистрация'
    }
