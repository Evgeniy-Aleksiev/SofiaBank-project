# Generated by Django 4.0.3 on 2022-04-08 07:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_exchangerates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerates',
            name='currency',
            field=models.CharField(max_length=3, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator('[A-Z]', message='The currency must be capitalized')]),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='happy',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=10),
        ),
    ]