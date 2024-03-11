from django.urls import path
from . import views

app_name = 'trainings'

urlpatterns = [
    path('', views.trainings_list, name='trainings_list')
]
