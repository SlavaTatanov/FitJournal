from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone


class UserProfile(models.Model):
    """
    Модель профиля пользователя связанная со стандартной для пользователя
    """

    class Gender(models.TextChoices):
        no_data = ("-", "Выберите")
        male = ("М", "Муж.")
        female = ("Ж", "Жен.")

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    height = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1,
                              choices=Gender.choices,
                              default=Gender.no_data)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()


class UserWeight(models.Model):
    """
    Модель описывающая вес пользователя в определенный промежуток времени
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=False)
    weight_date = models.DateTimeField(default=timezone.now)

    class Meta:
        """
        Индексы для модели
        """
        indexes = [
            models.Index(fields=['user', '-weight_date'])
        ]
