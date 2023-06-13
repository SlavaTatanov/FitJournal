from django.db import models


class TypeExercise(models.Model):
    """
    Класс описывающий типы упражнений
    """
    name = models.CharField(max_length=128)  # Название типа упражнений
    description = models.TextField()  # Описание типа упражнений


class Exercise(models.Model):
    """
    Модель описывающая упражнение
    """
    name = models.CharField(max_length=128)  # Название упражнения
    description = models.TextField()  # Описание упражнения
    type = models.ForeignKey(to=TypeExercise, on_delete=models.PROTECT, default=0)
