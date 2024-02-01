from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    # urls для смены пароля
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='users/password_change.html',
                                               success_url=reverse_lazy('users:password_change_done')),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name='password_change_done'),

    # urls для просмотра и добавления веса пользователя
    path('add_weight/', views.add_weight, name='add_weight'),
    path('user_weight/', views.weight_journal, name='user_weight'),

    # Настройки пользователя
    path('settings/', views.user_settings, name='profile_settings'),

    # urls для сброса пароля
    path("password_reset/", auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('users:password_reset_done')
    ), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password_reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('users:password_reset_complete')
    ),
         name="password_reset_confirm"),
    path("password_reset/complete", auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
    path('<username>/', views.user_profile, name='profile')
]
