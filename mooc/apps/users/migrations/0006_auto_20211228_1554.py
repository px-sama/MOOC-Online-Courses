# Generated by Django 2.2 on 2021-12-28 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20211227_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6, verbose_name='gender'),
        ),
    ]
