from django.shortcuts import render
from django.http import HttpRequest


def calculator_1rm(request: HttpRequest):
    return render(request, 'tools/calculator_1rm.html')
