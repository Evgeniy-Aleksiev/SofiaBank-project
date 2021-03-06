# Generated by Django 4.0.3 on 2022-04-07 06:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_feedback_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('currency', models.CharField(max_length=3, unique=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('fixing', models.FloatField()),
                ('buy', models.FloatField()),
                ('sell', models.FloatField()),
                ('currency_units', models.IntegerField()),
            ],
        ),
    ]
