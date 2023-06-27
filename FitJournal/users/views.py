from django.shortcuts import render
from django.http import HttpRequest

from users.forms import AuthenticationForm


def login(request: HttpRequest):
    context = {'form': AuthenticationForm()}
    return render(request, 'users/login.html', context)
