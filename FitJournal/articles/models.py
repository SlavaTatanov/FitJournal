from django.db import models
from django.contrib.auth.models import User


class BaseArticle(models.Model):
    """
    Базовая модель для сервисных статей, о нас, политика приватности и прочее
    """
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()


class Article(BaseArticle):
    """
    Модель описывающая статьи для сайта
    """

    class Status(models.TextChoices):
        PUBLISHED = 'PB', 'Published'
        DRAFT = 'DF', 'Draft'

    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)


