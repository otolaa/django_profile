from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to="user/%Y_%m_%d/", blank=True, null=True, verbose_name="Фотография")
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")

    telegram = models.CharField(max_length=100, verbose_name="Телеграм", null=True, blank=True)
    vk = models.CharField(max_length=100, verbose_name="ВКонтакте", null=True, blank=True)
    twitter = models.CharField(max_length=100, verbose_name="Твиттер", null=True, blank=True)