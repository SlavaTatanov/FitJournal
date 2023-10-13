from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Manager
from django.shortcuts import reverse


class PublishedArticleManager(Manager):
    """
    Определяем модельный менеджер, который извлекает только опуликованные
    """

    def get_queryset(self):
        return super().get_queryset().filter(status=Article.Status.PUBLISHED)


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
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    objects = Manager()


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
    summary = models.CharField(max_length=500, blank=True, default="")
    title_image = models.ImageField(upload_to="articles/uploads/article_title_image/", null=True)
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    # Модельные менеджеры
    objects = Manager()
    published = PublishedArticleManager()

    class Meta:
        indexes = [
            models.Index(fields=['-created', 'category']),
        ]

    def get_absolute_url(self):
        return reverse("articles:article", kwargs={'article_slug': self.slug})

