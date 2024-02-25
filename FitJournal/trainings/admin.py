from django.contrib import admin

from trainings.models import Exercise, TypeExercise, Activity

# Регистрируем наши модели в админке
for item in [Exercise, TypeExercise, Activity]:
    admin.site.register(item)
