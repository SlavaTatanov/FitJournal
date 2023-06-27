from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Categories(models.Model):
    """
    Модель описывающая категории статей
    """
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class AbstractBaseArticle(models.Model):
    class Meta:
        abstract = True

    """
    Базовая модель для сервисных статей, о нас, политика приватности и прочее
    """
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()

    def __str__(self):
        return self.title


class BaseArticle(AbstractBaseArticle):
    pass


class Article(AbstractBaseArticle):
    """
    Модель описывающая статьи для сайта
    """

    class Status(models.TextChoices):
        PUBLISHED = 'PB', 'Published'
        DRAFT = 'DF', 'Draft'

    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, default=0)
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    class Meta:
        indexes = [
            models.Index(fields=['-created', 'category']),
        ]

