from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required


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
    return render(req, 'trainings/trainings_list.html')
