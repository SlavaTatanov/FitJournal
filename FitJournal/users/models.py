from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    """
    Модель профиля пользователя связанная со стандартной для пользователя
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()
