# Generated by Django 4.1.4 on 2022-12-22 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('discription', models.TextField(verbose_name='Описание')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_time', models.DateTimeField(verbose_name='Дата задачи')),
                ('done', models.BooleanField(default=False, verbose_name='Сделано')),
            ],
        ),
    ]
