from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile, UserWeight

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserWeightForm


def login(request: HttpRequest):
    context = {'form': UserLoginForm()}
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # Создаем форму и передаем в нее дату, для дальнейшей обработки
        if form.is_valid():  # Проверяем валидность
            username = request.POST['username']
            password = request.POST['password']  # Берем значения из формы
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)  # Если такой юзер есть, то авторизуем
                next_page = request.POST['next']  # Если был параметр next перенаправляем туда
                if next_page:
                    return HttpResponseRedirect(next_page)
                return HttpResponseRedirect(reverse('index'))
        else:
            context = {'form': form}
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


@login_required
def user_settings(req: HttpRequest):
    """
    Представление для настроек профиля пользователя
    """
    if req.method == "POST":
        if req.user.is_authenticated:
            instance_profile = UserProfile.objects.get(user=req.user)
            form = UserProfileForm(data=req.POST, instance=instance_profile)
            if form.is_valid():
                form.save()
                response = redirect("users:profile_settings")
                messages.success(req, "Профиль успешно сохранен!")
                return response
    elif req.method == "GET":
        # Если метод запроса GET, то мы делаем запрос к базе данных и заполняем форму.
        # Если данных нет, то вернем пустую форму, если есть - заполненную.
        try:
            profile = UserProfile.objects.get(user=req.user)
        except UserProfile.DoesNotExist:
            profile = None
        form = UserProfileForm(instance=profile)
        user = req.user.get_username()

        # Получаем данные по весу пользователя
        try:
            user_weight_profile = UserWeight.objects.filter(user=req.user).order_by("-weight_date")[0]
            user_weight = user_weight_profile.weight
        except UserWeight.DoesNotExist:
            user_weight = "Нет данных"

        # Собираем контекст и отправляем страницу
        context = {'user': user, 'profile_form': form, 'user_weight': user_weight}
        return render(req, 'users/user_settings.html', context=context)


@login_required
def test_view(req: HttpRequest):
    return render(req, 'test.html', {'msg': 'Это тестовое сообщение'})


@login_required
def weight_journal(req: HttpRequest):
    return render(req, 'users/weight_journal.html')


@login_required
def add_weight(req: HttpRequest):
    if req.method == "POST":
        form = UserWeightForm(data=req.POST)
        if form.is_valid():
            # Сохраняем форму, прицепляем к ней экземпляр пользователя и сохраняем в базу данных.
            form.save(commit=False)
            form.instance.user = req.user
            form.save()
            messages.success(req, "Вес успешно добавлен")
    else:
        form = UserWeightForm()
    return render(req, 'users/add_weight.html', {'form': form})
