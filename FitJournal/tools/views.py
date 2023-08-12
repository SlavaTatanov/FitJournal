from django.shortcuts import render
from django.http import HttpRequest


def calculator_1rm(request: HttpRequest):
    context = {'title': 'Расчет одноповторного максимума'}
    return render(request, 'tools/calculator_1rm.html', context=context)
