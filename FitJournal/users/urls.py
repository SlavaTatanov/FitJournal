from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'),
         name='password_change')
]
