from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxLengthValidator, MinLengthValidator

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True, verbose_name='Аватарка')
    phone = models.CharField(null=True, blank=True, max_length=111, validators=[MinLengthValidator(limit_value=10, message='10 цифр минимум'), MaxLengthValidator(limit_value=10, message='10 цифр максимум')], verbose_name='Телефон')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    age = models.IntegerField(validators=[MinValueValidator(limit_value=1, message='Больше одного')], null=True, verbose_name='Возраст')


    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name= 'Пользователь'