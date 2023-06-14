from django.contrib import admin

from trainings.models import Exercise, TypeExercise

# Регистрируем наши модели в админке
for item in [Exercise, TypeExercise]:
    admin.site.register(item)
