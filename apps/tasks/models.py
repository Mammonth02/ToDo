from django.db import models

from apps.users.models import User

class Task(models.Model):
        title = models.CharField(max_length=100, verbose_name='Заголовок')
        discription = models.TextField(verbose_name='Описание')
        create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
        date_time = models.DateField(verbose_name='Дата задачи')
        done = models.BooleanField(default=False, verbose_name='Сделано')
        owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')
        image = models.ImageField(upload_to='tasks_images/', null=True, blank=True, verbose_name='Фото')