from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import User

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request: HttpRequest):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # Создаем форму и передаем в нее дату, для дальнейшей обработки
        if form.is_valid():  # Проверяем валидность
            username = request.POST['username']
            password = request.POST['password']  # Берем значения из формы
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)  # Если такой юзер есть, то авторизуем
                return HttpResponseRedirect(reverse('index'))
        else:
            context = {'form': form}
    else:
        context = {'form': UserLoginForm()}
    return render(request, 'users/login.html', context=context)


def register(request: HttpRequest):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            # Если данные валидные то сохранить юзера
            form.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            # Если не прошла валидация вернем форму с ошибками
            context = {'form': form}
    # Если метод GET передать форму
    else:
        context = {'form': UserRegistrationForm()}
    return render(request, 'users/register.html', context=context)


def user_profile(req: HttpRequest, username):
    user_in_db = User.objects.filter(username=username)
    if user_in_db:
        if req.user.is_authenticated:
            current_user = req.user.get_username()
        else:
            current_user = None
        context = {'user': username}
        if current_user and current_user == username:
            return render(req, 'users/user_profile.html', context)
        else:
            return render(req, 'users/public_user_profile.html', context)
    else:
        return render(req, 'users/not_user.html')


def logout(req: HttpRequest):
    """
    Представление для выхода из профиля пользователя
    """
    auth.logout(req)
    return HttpResponseRedirect(reverse('index'))


def user_settings(req: HttpRequest):
    """
    Представление для настроек профиля пользователя
    """
    form = UserProfileForm()
    if req.user.is_authenticated:
        user = req.user.get_username()
        context = {'user': user, 'profile_form': form}
        return render(req, 'users/user_settings.html', context=context)
    else:
        return HttpResponseRedirect(reverse('index'))
