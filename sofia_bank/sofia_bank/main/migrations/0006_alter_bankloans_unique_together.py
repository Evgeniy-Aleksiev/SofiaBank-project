# Generated by Django 4.0.3 on 2022-03-31 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_bankloans_amount_alter_banksavings_amount'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bankloans',
            unique_together=set(),
        ),
    ]