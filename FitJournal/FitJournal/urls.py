"""
URL configuration for FitJournal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from trainings.views import index
from articles.views import about
from users.views import login, register, user_profile, logout, user_settings
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('about/', about, name='about'),
    path('articles/', include('articles.urls', namespace='articles')),
    path('tools/', include('tools.urls', namespace='tools')),
    path('profile/<username>/', user_profile, name='profile'),
    path('profile/settings', user_settings, name='profile_settings'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    # Добавляем локальный путь для медиа файлов если локальная отладка, но можно добавлять и на основном
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
