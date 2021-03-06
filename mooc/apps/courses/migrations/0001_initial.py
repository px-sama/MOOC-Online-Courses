# Generated by Django 2.2 on 2021-12-26 23:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add Time ')),
                ('name', models.CharField(max_length=50, verbose_name='Course Name')),
                ('desc', models.CharField(max_length=300, verbose_name='Course Description')),
                ('learn_time', models.IntegerField(default=0, verbose_name='Learn Time')),
                ('degree_level', models.CharField(choices=[('beg', 'beginner'), ('intm', 'intermediate'), ('exp', 'expert')], max_length=100, verbose_name='Difficulty Level')),
                ('students', models.IntegerField(default=0, verbose_name='number of students')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='favorite number')),
                ('click_nums', models.IntegerField(default=0, verbose_name='click numbers')),
                ('category', models.CharField(default='Backend Dev', max_length=20, verbose_name='course category')),
                ('tag', models.CharField(default='', max_length=10, verbose_name='course tag')),
                ('course_info', models.CharField(default='', max_length=300, verbose_name='course info')),
                ('teacher_tell', models.CharField(default='', max_length=300, verbose_name='teach tell')),
                ('detail', models.TextField(verbose_name='Course Detail Information')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='Profile Picture')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.Teacher', verbose_name='teacher')),
            ],
            options={
                'verbose_name': 'Course Information',
                'verbose_name_plural': 'Course Information',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add Time ')),
                ('name', models.CharField(max_length=100, verbose_name='chapter name')),
                ('learn_time', models.IntegerField(default=0, verbose_name='learning time (mins)')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
            options={
                'verbose_name': 'Course Chapters',
                'verbose_name_plural': 'Course Chapters',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add Time ')),
                ('name', models.CharField(max_length=100, verbose_name='video name')),
                ('learn_time', models.IntegerField(default=0, verbose_name='learning time (mins)')),
                ('url', models.CharField(max_length=200, verbose_name='learning time (mins)')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Video',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add Time ')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('file', models.FileField(max_length=200, upload_to='course/resources/%Y%m', verbose_name='download address')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='course')),
            ],
            options={
                'verbose_name': 'Course Resources',
                'verbose_name_plural': 'Course Resources',
            },
        ),
    ]
