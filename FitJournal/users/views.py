from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm


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
                print("Такого юзера нет")
    context = {'form': UserLoginForm()}
    return render(request, 'users/login.html', context=context)


def register(request: HttpRequest):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            # Если данные валидные то сохранить юзера
            form.save()
            return HttpResponseRedirect(reverse('login'))
    # Если метод GET передать форму
    context = {'form': UserRegistrationForm()}
    return render(request, 'users/register.html', context=context)


def user_profile(req: HttpRequest, username):
    context = {'user': username}
    return render(req, 'users/user_profile.html', context)


def logout(req: HttpRequest):
    """
    Представление для выхода из профиля пользователя
    """
    auth.logout(req)
    return HttpResponseRedirect(reverse('index'))
