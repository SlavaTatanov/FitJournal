from django.shortcuts import render


def index(request):
    context = {
        'title': 'test title from context'
    }
    return render(request, 'trainings/index.html', context=context)
