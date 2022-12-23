# Generated by Django 4.1.4 on 2022-12-23 08:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(limit_value=9, message='9 цифр минимум'), django.core.validators.MaxValueValidator(limit_value=11, message='11 цифр максимум')], verbose_name='Телефон'),
        ),
    ]
