# Generated by Django 4.1.4 on 2022-12-22 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_time',
            field=models.DateTimeField(verbose_name='Дата задачи'),
        ),
    ]
