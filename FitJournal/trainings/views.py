from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from users.models import UserTraining


def index(request):
    context = {
        'title': "FitJournal"
    }
    return render(request, 'trainings/index.html', context=context)


@login_required
def trainings_list(req: HttpRequest):
    """
    Представление дает информацию о тренировках пользователя
    """
    # Определяем пользователя и делаем запрос его тренировок
    user = req.user
    training_data = UserTraining.objects.filter(user=user).order_by('-training_date')

    # Собираем контекст
    context = {"training_data": training_data}
    return render(req, 'trainings/trainings_list.html', context=context)
