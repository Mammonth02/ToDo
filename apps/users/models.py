from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True, verbose_name='Аватарка')


    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name= 'Пользователь'