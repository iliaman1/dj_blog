from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'avatar', 'bio', 'email']


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'password']
