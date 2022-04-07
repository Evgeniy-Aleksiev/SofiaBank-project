# Generated by Django 4.0.3 on 2022-04-05 20:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_atmandbranches_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='username',
            field=models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]