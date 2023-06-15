from django.shortcuts import render


def index(request):
    context = {
        'title': "title"
    }
    return render(request, 'trainings/index.html', context=context)


