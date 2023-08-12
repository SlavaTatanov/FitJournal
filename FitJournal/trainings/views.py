from django.shortcuts import render


def index(request):
    context = {
        'title': "FitJournal"
    }
    return render(request, 'trainings/index.html', context=context)


