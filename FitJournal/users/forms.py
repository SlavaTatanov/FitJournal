from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control mt-2",
        'placeholder': "Введите имя пользователя"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control mt-2",
        'placeholder': "Введите пароль"
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control mt-2",
        'placeholder': "Имя пользователя"
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form-control mt-2",
        'placeholder': "Введите адрес эл. почты"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control mt-2",
        'placeholder': "Введите пароль"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control mt-2",
        'placeholder': "Подтвердите пароль"
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
