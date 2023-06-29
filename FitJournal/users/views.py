from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm


def login(request: HttpRequest):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # Создаем форму и передаем в нее дату, для дальнейшей обработки
        if form.is_valid():  # Проверяем валидность
            username = request.POST['username']
            password = request.POST['password']  # Берем значения из формы
            user = auth.authenticate(username=username, password=password)
            if user:
                print("Авторизуем")
                auth.login(request, user)  # Если такой юзер есть, то авторизуем
                return HttpResponseRedirect(reverse('index'))
            else:
                print("Такого юзера нет")
    context = {'form': UserLoginForm()}
    return render(request, 'users/login.html', context)


