from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('articles-list/', views.articles_list, name='articles-list')
]
