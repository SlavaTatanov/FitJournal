from django.db import models


class BaseNamedModel(models.Model):
    """
    Базовая абстрактная модель которая содержит имя сущности
    """
    name = models.CharField(max_length=128)

    def __str__(self):
        """
        Дружелюбная реализация строкового представления
        """
        return self.name

    class Meta:
        abstract = True


class BaseNamedDescriptionModel(BaseNamedModel):
    """
    Базовая абстрактная модель которая содержит имя и описание сущности
    """
    description = models.TextField()

    class Meta:
        abstract = True


class TypeExercise(BaseNamedDescriptionModel):
    """
    Класс описывающий типы упражнений
    """
    pass


class Exercise(BaseNamedDescriptionModel):
    """
    Модель описывающая упражнение
    """
    type = models.ForeignKey(to=TypeExercise, on_delete=models.PROTECT, default=0)


class Activity(BaseNamedDescriptionModel):
    """
    Модель описывающая тип активности, бег, силовая тренировка и прочее.
    """
    pass
