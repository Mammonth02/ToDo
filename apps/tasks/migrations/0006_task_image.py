# Generated by Django 4.1.4 on 2022-12-23 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tasks_images/', verbose_name='Фото'),
        ),
    ]
