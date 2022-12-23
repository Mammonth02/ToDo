# Generated by Django 4.1.4 on 2022-12-23 09:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=111, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=10, message='10 цифр минимум'), django.core.validators.MaxLengthValidator(limit_value=10, message='10 цифр максимум')], verbose_name='Телефон'),
        ),
    ]
