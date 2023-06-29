from django.contrib.auth.forms import AuthenticationForm
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

