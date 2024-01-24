from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile, UserWeight
from django import forms


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={
        'class': "form-control mt-2",
        'placeholder': "Введите имя пользователя"
    }))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={
        'class': "form-control mt-2",
        'placeholder': "Введите пароль"
    }))

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        """
        Кастомный метода валидации для поля
        """
        user = self.cleaned_data['username']
        if not User.objects.filter(username=user).exists():
            msg = ValidationError("Такого пользователя не существует")
            self.add_error("username", msg)
        user_pass = self.cleaned_data['password']
        if not User.objects.filter(username="SlavaTatanov")[0].check_password(user_pass):
            self.add_error("password", ValidationError("Неверный пароль"))
        return self.cleaned_data


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={
        'class': "form-control mt-2",
        'placeholder': "Имя пользователя"
    }))
    email = forms.CharField(label="e-mail", widget=forms.EmailInput(attrs={
        'class': "form-control mt-2",
        'placeholder': "Введите адрес эл. почты"
    }))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={
        'class': "form-control mt-2",
        'placeholder': "Введите пароль"
    }))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={
        'class': "form-control mt-2",
        'placeholder': "Подтвердите пароль"
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    height = forms.IntegerField(label="Рост")
    gender = forms.ChoiceField(label="Пол",
                               choices=UserProfile.Gender.choices)

    class Meta:
        model = UserProfile
        fields = ('height', 'gender')


class UserWeightForm(forms.ModelForm):
    weight_date = forms.DateField(label="Дата", widget=forms.DateInput(attrs={'type': 'date'}))
    weight = forms.FloatField(label="Вес")

    class Meta:
        model = UserWeight
        fields = ('weight_date', 'weight')
