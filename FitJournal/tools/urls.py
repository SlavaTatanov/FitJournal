from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('calculator_1rm', views.calculator_1rm, name='calculator_1rm')
]
