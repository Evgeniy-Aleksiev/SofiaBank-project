# Generated by Django 4.0.3 on 2022-04-05 12:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_atmandbranches'),
    ]

    operations = [
        migrations.AddField(
            model_name='atmandbranches',
            name='bank_or_atm_number',
            field=models.IntegerField(default=111, unique=True, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1000)]),
            preserve_default=False,
        ),
    ]
