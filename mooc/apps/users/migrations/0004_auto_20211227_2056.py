# Generated by Django 2.2 on 2021-12-28 01:56

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211227_2056'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]