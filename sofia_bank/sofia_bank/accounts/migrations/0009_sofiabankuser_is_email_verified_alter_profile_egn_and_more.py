# Generated by Django 4.0.3 on 2022-04-20 06:57

import django.core.validators
from django.db import migrations, models
import sofia_bank.common_files.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_profile_egn_alter_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='sofiabankuser',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='egn',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10), sofia_bank.common_files.validators.validate_only_numbers], verbose_name='EGN'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
